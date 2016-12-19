import ast
import os
import re

paths = ['../../mpf/mpf', '../../mpf-mc/mpfmc']
rst_path = '../machine_vars'
dont_delete_files = []


class MachineVarDocParser(object):

    def __init__(self):
        self.file = None
        self.file_list = list()

    def parse_file(self, file_name):

        self.file = file_name

        with open(file_name) as f:
            my_ast = ast.parse(f.read())

        for x in ast.walk(my_ast):
            if isinstance(x, ast.Str) and (x.s.strip().lower().startswith(
                    'machine_var:')):
                machine_var, rst = self.parse_string(x)

                if rst:
                    filename = self.create_file(machine_var, rst)
                    self.file_list.append((machine_var, filename))

    def write_index(self):

        index = '''Machine Variables
=================

Machine variables are similar to
:doc:`player variables </game_logic/players/index>`, except that
machine variables are machine-wide and persist between games. (In fact,
machine variables can be configured to be saved to disk so they also persist
between reboots of MPF.)

Like player variables, you can use machine variables in your config files,
particularly in text display widgets, to show things on your display.

You can create your own machine variables in your configs. There are also
several machine variables that are automatically created. Here's a list of
the machine variables that are "built in" and available for use in your
configs:

.. toctree::
   :maxdepth: 1

'''

        # sort based on the file name, rather than the event name, since that
        # has the special chars stripped.
        self.file_list.sort(key=lambda x: x[1])

        for file_name in self.file_list:
            index += '   {} <{}>\n'.format(file_name[0], file_name[1][:-4])

        with open(os.path.join(rst_path, 'index.rst'),
                  'w') as f:
            f.write(index)

    def create_file(self, machine_var, rst):
        filename = machine_var.replace('(', '').replace(')', '') + '.rst'

        with open(os.path.join(rst_path, filename), 'w') as f:
            f.write(rst)

        return filename

    def parse_string(self, string):
        # string = string.s.replace('\n', ' ')  # strip newlines
        # string = ' '.join(string.s.split(' '))  # strip extra spaces
        string = '\n'.join(' '.join(line.split())
                           for line in string.s.split('\n'))

        string = string.replace('Machine_var:', 'machine_var:')
        string = string.replace('Desc:', 'desc:')

        try:
            string = string.replace('Args:', 'args:')
        except ValueError:
            pass

        final_dict = self.string_to_args_dict(string, ['machine_var', 'desc',
                                                       'args'])

        if 'desc' not in final_dict:
            # not an machine_vars docstring
            return (None, None)

        return self.build_rst_entry(final_dict)

    def string_to_args_dict(self, string, args):
        index_starts = list()

        for arg in args:
            try:
                index_starts.append(string.index(arg + ':'))
            except ValueError:
                pass

        index_starts.sort()
        sliced_list = list()
        for x in range(len(index_starts)):
            try:
                sliced_list.append(string[index_starts[x]:index_starts[
                    x + 1]])
            except IndexError:
                sliced_list.append(string[index_starts[x]:])

        final_dict = dict()

        for entry in sliced_list:
            split_entry = entry.split(':', 1)
            final_dict[split_entry[0].strip()] = split_entry[1].strip()

        return final_dict

    def build_rst_entry(self, final_dict):
        rst_output = str()

        # write the title
        try:
            rst_output += final_dict['machine_var']+ '\n'
        except KeyError:
            print("machine_vars entry missing from: {}".format(self.file))

        rst_output += ('=' * len(final_dict['machine_var'])) + '\n\n'
        rst_output += '*MPF machine variable*\n\n'

        # add the description
        rst_output += final_dict['desc'] + '\n\n'

        # add the keyword arguments section

        # rst_output += 'Keyword arguments\n'
        # rst_output += '-----------------\n\n'
        #
        # if 'args' in final_dict:
        #     rst_output += self.parse_args(final_dict['args'])
        # else:
        #     rst_output += '*None*\n'

        return final_dict['machine_var'], rst_output

    def parse_args(self, args_string):

        args = list()
        output = str()

        for x in re.findall('\\b(\w*)\\b(?=\:)', args_string):
            if x:
                args.append(x)

        args_dict = self.string_to_args_dict(args_string, args)

        for k, v in sorted(args_dict.items()):
            output += k + '\n'
            output += ('~' * len(k)) + '\n'
            output += v + '\n\n'

        return output

if __name__ == '__main__':
    a = MachineVarDocParser()

    # delete existing files
    for path, _, files in os.walk(rst_path):
        for file in files:
            if file not in dont_delete_files:
                os.remove(os.path.join(path, file))

    # walk through the folders to scan
    for path in paths:
        for root, _, files in os.walk(path):
            for file in [x for x in files if x.endswith('.py')]:
                a.parse_file(os.path.join(root, file))

    # create the index.rst based on everything that was found
    a.write_index()
