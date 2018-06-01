import os
import re
import sys

from mpf._version import __version__
import mpf

import ruamel.yaml as yaml

rst_path = '../config'


class ConfigDocParser(object):

    def __init__(self):
        self.file = None
        self.file_list = list()
        self.config_spec = dict()
        self.config_specs = dict()

        self.existing_rsts = list()
        self.existing_settings = dict()

        self._load_config_spec()
        self.config_specs = self._create_config_specs(self.config_spec)
        self._load_existing_rsts()

    def create_file(self, config_section, rst):
        filename = config_section + '.rst'
        print(config_section, rst)
        with open(os.path.join(rst_path, filename), 'w') as f:
            f.write(rst)

        return filename

    def write_index(self):
        index = '''Config file reference
=====================

This section contains details about every possible entry you can use in your
YAML config files. Each entry also has information about whether it's valid in
your machine-wide config, a mode-specific config, or both.

.. toctree ::
   :maxdepth: 1

   Instructions: <instructions/index>
'''
        self._load_existing_rsts()
        self.existing_rsts.sort()

        for file_name in self.existing_rsts:
            if file_name != 'index':
                index += '   {}: <{}>\n'.format(file_name, file_name)

        with open(os.path.join(rst_path, 'index.rst'), 'w') as f:
            f.write(index)

    def _load_config_spec(self):
        with open(os.path.join(os.path.dirname(mpf.__file__), "config_spec.yaml")) as f:
            self.config_spec = yaml.load(f)

    def _load_existing_rsts(self):
        self.existing_rsts = [x[:-4] for x in os.listdir(rst_path)
                              if (x.endswith('.rst') and
                                  not x.startswith('_'))]

    def _create_config_specs(self, source_dict):
        final_dict = dict()

        for section, settings in source_dict.items():
            if '__valid_in__' in settings and settings['__valid_in__'].lower() != 'none':
                final_dict[section] = (
                    self._create_subsection_config_spec(settings))

        return final_dict

    def _create_subsection_config_spec(self, settings):
        final_dict = dict()
        final_dict['required'] = list()
        final_dict['optional'] = list()
        final_dict['ignored'] = list()
        final_dict['sub_sections'] = dict()
        final_dict['allow_others'] = False

        for setting_name, setting_spec in settings.items():

            if setting_name == '__valid_in__':
                final_dict['valid_in'] = setting_spec

            if isinstance(setting_spec, dict):

                final_dict['sub_sections'][setting_name] = (
                    self._create_subsection_config_spec(setting_spec))

            elif isinstance(setting_spec, str):

                try:
                    num, stype, default = setting_spec.split('|')

                    if default:
                        final_dict['optional'].append((setting_name, num,
                                                       stype, default))
                    else:
                        final_dict['required'].append((setting_name, num, stype))
                except ValueError:
                    final_dict['ignored'].append((setting_name, setting_spec))

            elif setting_name == '__allow_others__':
                final_dict['allow_others'] = True

        final_dict['required'].sort()
        final_dict['optional'].sort()
        final_dict['ignored'].sort()

        return final_dict

    def create_rsts(self):
        for k, v in self.config_specs.items():
            self._create_rst(k, v)

    def create_rst(self, name):
        self._create_rst(name, self.config_specs[name])


    def _create_rst(self, name, spec):

        if name in self.existing_rsts:
            existing_intro, self.existing_settings = (
                self.tokenize_existing_rst(os.path.join(rst_path,
                                                        name + '.rst')))

        else:
            existing_intro = ''
            self.existing_settings = dict()

        final_text = ''
        final_text += '{}:\n'.format(name)
        final_text += '=' * (len(name) + 1)
        final_text += '\n\n*Config file section*\n\n'

        final_text += '+----------------------------------------------------------------------------+---------+\n'
        if 'machine' in spec['valid_in']:
            final_text += '| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |\n'
        else:
            final_text += '| Valid in :doc:`machine config files </config/instructions/machine_config>` | **NO**  |\n'

        final_text += '+----------------------------------------------------------------------------+---------+\n'
        if 'mode' in spec['valid_in']:
            final_text += '| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |\n'
        else:
            final_text += '| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |\n'

        final_text += '+----------------------------------------------------------------------------+---------+\n\n'

        if 'show' in spec['valid_in']:
            final_text += '.. note:: This section can also be used in a show '
            final_text += 'file in the ``{}s:`` section of a step.\n\n'.format(
                          name.split('_')[0])

        final_text += '.. overview\n\n'

        if existing_intro:
            final_text += existing_intro
        else:
            final_text += 'The ``{}:`` section of your config is where ' \
                          'you...\n\n'.format(name)
            final_text += '.. todo:: :doc:`/about/help_us_to_write_it`'

        final_text += '\n\n\n'

        final_text += self.build_sections(name, spec)

        self.create_file(name, final_text)

    def build_sections(self, name, spec, level=1):
        final_text = ''

        if spec['required']:
            final_text += self.add_required_section(spec['required'], name,
                                                    level)
            final_text += '\n'

        if spec['optional']:
            final_text += self.add_optional_section(spec['optional'], name,
                                                    level)
            final_text += '\n'

        if 'sub_sections' in spec and spec['sub_sections']:
            final_text += self.add_subsection_section(spec['sub_sections'],
                                                      name, level)
            final_text += '\n'

        return final_text

    def add_required_section(self, required_list, name, level):

        if level == 1:
            sep = '-'
            sep2 = '~'
        elif level == 2:
            sep = '~'
            sep2 = '^'
        else:
            sep = '^'
            sep2 = '"'

        final_text = 'Required settings\n'
        final_text += sep * 17
        final_text += '\n\nThe following sections are required in the ``{}:`` ' \
                      'section of your config:\n\n'.format(name)

        for setting in required_list:
            final_text += setting[0] + ':\n'
            final_text += sep2 * (len(setting[0]) + 1)
            final_text += '\n'
            final_text += self._get_spec_string(setting[1], setting[2])
            final_text += '\n'

            found = False

            for k1, v1 in self.existing_settings.items():
                if k1[0] == setting[0] and k1[2] == level + 1:
                    final_text += v1
                    found = True
                    break

            if not found:
                final_text += '.. todo:: :doc:`/about/help_us_to_write_it`'

            final_text += '\n\n'

        return final_text

    def add_optional_section(self, optional_list, name, level):

        if level == 1:
            sep = '-'
            sep2 = '~'
        elif level == 2:
            sep = '~'
            sep2 = '^'
        else:
            sep = '^'
            sep2 = '"'

        final_text = 'Optional settings\n'
        final_text += sep * 17
        final_text += '\n\nThe following sections are optional in the ``{}:`` ' \
                      "section of your config. (If you don't include them, " \
                      "the default will be used).\n\n".format(name)

        for setting in optional_list:
            final_text += setting[0] + ':\n'
            final_text += sep2 * (len(setting[0]) + 1)
            final_text += '\n'
            final_text += self._get_spec_string(setting[1], setting[2],
                                                setting[3])
            final_text += '\n'

            found = False

            for k1, v1 in self.existing_settings.items():
                if k1[0] == setting[0] and k1[2] == level + 1:
                    final_text += v1
                    found = True
                    break

            if not found:
                final_text += '.. todo:: :doc:`/about/help_us_to_write_it`'

            final_text += '\n\n'

        return final_text

    def add_subsection_section(self, subsection_dict, name, level):
        if level == 1:
            sep = '-'
            sep2 = '~'
        elif level == 2:
            sep = '~'
            sep2 = '^'
        elif level == 3:
            sep = '^'

        final_text = ''

        for k, v in subsection_dict.items():

            final_text += '{}:\n'.format(k)
            final_text += sep * (len(k) + 1)
            final_text += '\n\n'

            found = False

            for k1, v1 in self.existing_settings.items():
                if k1[0] == k and k1[2] == level + 1:
                    final_text += v1
                    found = True
                    break

            if not found:
                final_text += "The ``{}:`` section contains " \
                              "the following nested sub-settings".format(k)

            final_text += '\n\n'
            final_text += self.build_sections(k, v, level+1)

        return final_text

    def tokenize_existing_rst(self, filename):
        with open(filename, 'r') as f:
            doc = f.read()

        settings_dict = dict()

        # trim off the header info
        parts = doc.split('.. overview\n\n')
        if len(parts) == 2:
            doc = parts[1]
        else:
            doc = parts[0]

        # split the doc into a list of lines
        # doc = doc.split['\n']

        levels = ['=', '-', '~', '^']
        last_parents = [None, None, None, None]
        sections = list()  # tuple (name, level, parent)

        for x in re.findall('([^\n]+)\n([~\-\^]+)', doc):

            level = levels.index(x[1][0])
            name = x[0].strip(':')
            heading = x[0]
            last_parents[level] = name

            if level:
                parent = last_parents[level - 1]
            else:
                parent = None

            sections.append((name, heading, level, parent))

        try:
            beginning = doc[:doc.index(sections[0][1] + '\n' + ('-' * len(sections[0][1])))]
        except (IndexError, ValueError):
            beginning = ''

        beginning = beginning.strip('\n')

        for i, (name, heading, level, parent) in enumerate(sections):
            start = '\n' + heading + '\n' + (levels[level] * (len(heading)))

            try:
                end = '\n' + sections[i+1][1] + '\n' + (levels[sections[i+1][2]] * (len(sections[i+1][1])))
            except IndexError:
                end = None

            try:
                body = doc[doc.index(start):doc.index(end)].replace(start, '').strip('\n')
            except TypeError:
                body = doc[doc.index(start):].replace(start, '').strip('\n')
            except ValueError:
                print("Could not process {}. Skipping...".format(filename))
                body = ''

            # strip out the old spec string so the latest replaces it
            if level:
                body = body.strip('\n')
                body = '\n'.join(body.split('\n')[1:])
                body = body.strip('\n')

            settings_dict[(name, heading, level, parent)] = body

        return beginning, settings_dict

    def _get_index_of_next_heading(self, doc_lines):

        heading_chars = set(('-', '~', '^'))

        for i in range(len(doc_lines)):
            if set(doc_lines[i]).issubset(heading_chars):
                # we have a heading sep
                return i - 1

    def _get_spec_string(self, num, stype, default=None):
        if num == 'single':
            return_string = 'Single value, '
        elif num == 'list' or num == 'set':
            return_string = 'List of one (or more) values, each is a '
        elif num == 'dict':
            return_string = ('Parent setting for one (or more) sub-settings. '
                             'Each sub-setting is a ')
        elif num == 'omap':
            return_string = ('Ordered list for one (or more) sub-settings. '
                             'Each sub-setting is a ')

        else:
            raise AssertionError("Invalid config spec num: {}".format(num))

        if stype == 'str':
            ftype = '``string``'

        elif stype == 'lstr':
            ftype = '``string`` (case-insensitive)'

        elif stype == 'float':
            ftype = '``number`` (will be converted to floating point)'

        elif stype == 'int':
            ftype = '``integer``'

        elif stype == 'num':
            ftype = '``number`` (can be integer or floating point)'

        elif stype == 'bool' or stype == 'boolean' or stype == 'bool_int':
            ftype = '``boolean`` (Yes/No or True/False)'

        elif stype == 'secs':
            ftype = '``time string (secs)`` (:doc:`Instructions for entering '\
                    'time strings) </config/instructions/time_strings>` '

        elif stype == 'ms':
            ftype = '``time string (ms)`` (:doc:`Instructions for entering '\
                    'time strings) </config/instructions/time_strings>` '

        elif stype == 'list':
            ftype = '``list`` (:doc:`Instructions ' \
                      '</config/instructions/lists>` for entering lists)'

        elif stype == 'int_from_hex':
            ftype = '2-byte hex value (``00`` to ``ff``)'

        elif stype == 'kivycolor' or stype == 'color':
            ftype = '``color`` (*color name*, *hex*, or list of values ' \
                    '*0*-*255*)'

        elif stype == 'pow2':
            ftype = '``integer`` (must be a power of 2'

        elif stype == 'gain':
            ftype = '``gain setting`` (-inf, db, or float between 0.0 and 1.0'

        elif stype.startswith('subconfig'):
            ftype = 'sub-configurating containing {} settings'.format(
                stype.replace('subconfig(', '')[:-1])

        elif stype.startswith('enum'):
            ftype = 'one of the following options: {}'.format(
                stype.replace('enum(', '').replace(',', ', ')[:-1])

        elif stype.startswith('machine'):
            ftype = "string name of a ``{}:`` device".format(
                stype.replace('machine(', '')[:-1])

        elif ':' in stype:
            stype = tuple(stype.split(':'))
            return_string = 'One or more sub-entries, each in the format of '
            ftype = '``{}``:``{}``'.format(stype[0], stype[1])

        else:
            ftype = stype

        return_string += 'type: {}.'.format(ftype)

        if default:
            return_string += ' Default: ``{}``'.format(default)

        return_string += '\n'

        return return_string


if __name__ == '__main__':
    parser = ConfigDocParser()
    parser.create_rst(sys.argv[1])
    #parser.create_rsts()
    #parser.write_index()

    #pass # disabling because this doesn't work anymore but I might want to use
    # it in the future
