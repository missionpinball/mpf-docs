import ast
import os
import re
from collections import defaultdict


class EventDocParser(object):

    def __init__(self, rst_path):
        self.file = None
        self.file_list = list()
        self.rst_path = rst_path
        self.device_labels = {}
        self.device_events = defaultdict(list)

    def parse_file(self, file_name):

        self.file = file_name
        class_label = None
        config_section = None

        try:
            with open(file_name) as f:
                my_ast = ast.parse(f.read())
        except:
            raise AssertionError("Error while parsing {}".format(file_name))

        for x in ast.walk(my_ast):
            if isinstance(x, ast.ClassDef):
                class_label = None
                config_section = None
                for statement in x.body:
                    if isinstance(statement, ast.Assign) and len(statement.targets) == 1 and \
                       isinstance(statement.targets[0], ast.Name) and isinstance(statement.value, ast.Str):
                            #print('class: %s, %s=%s' % (str(x.name), str(statement.targets[0].id), str(statement.value)))
                            if statement.targets[0].id == "class_label":
                                class_label = str(statement.value.s)
                            elif statement.targets[0].id == "config_section":
                                config_section = str(statement.value.s)

                for y in ast.walk(x):
                    if isinstance(y, ast.Str) and (y.s.strip().lower().startswith('event:')):
                        event, rst = self.parse_string(y)

                        if event:
                            event = event.strip('.')

                        if rst:
                            filename = self.create_file(event, rst)
                            self.file_list.append((event, filename))

                        if config_section and rst:
                            self.device_events[config_section].append(event)
                            self.device_labels[config_section] = class_label

    def write_index(self):

        index = '''Events
======

The concept of *events* is one of the most important concepts in MPF. MPF is an
event-driven framework, and just about everything is either posting and event
or responding to an event that was posted.

There are several important concepts about events in MPF that you should
understand:

.. toctree::
   :titlesonly:
   :maxdepth: 1

   overview/index
   overview/conditional
   overview/priorities
   overview/event_types

Event Reference
---------------

Here's a list of all the "built in" events that are included in MPF and the
MPF MC. Of course your own machine could include custom events that aren't
on the list here.

Every event in MPF is just a string of text. You'll see that in many cases,
the actual event that's posted has a slight variation of the event text, typically
incorporating something about which mechanism or logic device posted the event.

For example, the event called :doc:`switch_(name)_active <switch_name_active>`
will replace the "(name)" part of the event text with the actual switch name.
So the when a switch called ``s_left_slingshot`` is activated, it will posted
an event called *switch_s_left_slingshot_active*.

.. toctree::
   :maxdepth: 1

'''
        # sort based on the file name, rather than the event name, since that
        # has the special chars stripped.
        self.file_list.sort(key=lambda x: x[1])

        for file_name in self.file_list:
            index += '   {} <{}>\n'.format(file_name[0], file_name[1][:-4])

        index += '''
Device Indexes
--------------
        
.. toctree::
   :maxdepth: 1

'''
        for config_section, events in sorted(self.device_events.items()):
            index += '   {} <index_{}>\n'.format(self.device_labels[config_section], config_section)

            rst = self.device_labels[config_section] + "\n"
            rst += "=" * (len(self.device_labels[config_section])) + "\n\n"
            rst += "See: :doc:`/config/{}`".format(config_section) + "\n\n"

            for event in events:
                rst += '* :doc:`{}`'.format(event.replace('(', '').replace(')', '')) + "\n"

            with open(os.path.join(self.rst_path, 'index_{}.rst'.format(config_section)), 'w') as f:
                f.write(rst)

            rst = ""

            for event in events:
                rst += '* :doc:`/events/{}`'.format(event.replace('(', '').replace(')', '')) + "\n"

            rst += "\n"

            with open(os.path.join(self.rst_path, 'include_{}.rst'.format(config_section)), 'w') as f:
                f.write(rst)


        with open(os.path.join(self.rst_path, 'index.rst'), 'w') as f:
            f.write(index)

    def create_file(self, event, rst):
        filename = event.replace('(', '').replace(')', '') + '.rst'

        with open(os.path.join(self.rst_path, filename), 'w') as f:
            f.write(rst)

        return filename

    def parse_string(self, string):
        # string = string.s.replace('\n', ' ')  # strip newlines
        # string = ' '.join(string.s.split(' '))  # strip extra spaces
        string = '\n'.join(' '.join(line.split())
                           for line in string.s.split('\n'))

        string = string.replace('Event:', 'event:')
        string = string.replace('Desc:', 'desc:')

        try:
            string = string.replace('Args:', 'args:')
        except ValueError:
            pass

        final_dict = self.string_to_args_dict(string, ['event', 'desc',
                                                       'args'])

        if 'desc' not in final_dict:
            # not an events docstring
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
            rst_output += final_dict['event']+ '\n'
        except KeyError:
            print("Events entry missing from: {}".format(self.file))

        rst_output += ('=' * len(final_dict['event'])) + '\n\n'
        rst_output += '*MPF Event*\n\n'

        # add the description
        rst_output += final_dict['desc'] + '\n\n'

        if 'args' in final_dict:

            rst_output += 'Keyword arguments\n'
            rst_output += '-----------------\n'

            rst_output += '''
(See the :doc:`/events/overview/conditional` guide for details for how to
create entries in your config file that only respond to certain combinations of
the arguments below.)\n\n'''
            rst_output += self.parse_args(final_dict['args'])
        else:
            rst_output += '*This event does not have any keyword arguments*\n'

        return final_dict['event'], rst_output

    def parse_args(self, args_string):

        args = list()
        output = str()

        for x in re.findall('\\b(\w*)\\b(?=\:)', args_string):
            if x:
                args.append(x)

        args_dict = self.string_to_args_dict(args_string, args)

        for k, v in sorted(args_dict.items()):

            v = v.replace('\n', ' ')
            v = re.sub(' +', ' ', v)

            output += '``' + k + '``\n'
            output += '  ' + v + '\n\n'

        return output

if __name__ == '__main__':
    paths = ['../../mpf/mpf', '../../mpf-mc/mpfmc']
    rst_path = '../events'
    dont_delete_files = []

    a = EventDocParser(rst_path)

    # delete existing files
    for path, _, files in os.walk(rst_path):
        for file in files:
            # only delete files in the rst_path, not subfolders
            if path == rst_path and file not in dont_delete_files:
                os.remove(os.path.join(path, file))

    # walk through the folders to scan
    for path in paths:
        for root, _, files in os.walk(path):
            for file in [x for x in files if x.endswith('.py')]:
                a.parse_file(os.path.join(root, file))

    # create the index.rst based on everything that was found
    a.write_index()
