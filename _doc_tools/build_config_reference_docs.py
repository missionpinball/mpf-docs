import os
import re

from mpf.core.config_validator import mpf_config_spec
from mpf._version import __version__

import ruamel.yaml as yaml

rst_path = '../config'


class ConfigDocParser(object):

    def __init__(self):
        self.file = None
        self.file_list = list()
        self.config_spec = dict()
        self.config_specs = dict()

        self.existing_rsts = list()

        self._load_config_spec()
        self.config_specs = self._create_config_specs(self.config_spec)
        self._load_existing_rsts()
        self.create_rsts()
        self.write_index()

    def create_file(self, config_section, rst):
        filename = config_section + '.rst'

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

'''
        self._load_existing_rsts()
        self.existing_rsts.sort()

        for file_name in self.existing_rsts:
            if file_name != 'index':
                index += '   {}: <{}>\n'.format(file_name, file_name)

        with open(os.path.join(rst_path, 'index.rst'), 'w') as f:
            f.write(index)

    def _load_config_spec(self):
        self.config_spec = yaml.load(mpf_config_spec)

    def _load_existing_rsts(self):
        self.existing_rsts = [x[:-4] for x in os.listdir(rst_path)
                              if (x.endswith('.rst') and
                                  not x.startswith('_'))]

    def _create_config_specs(self, source_dict):
        final_dict = dict()

        for section, settings in source_dict.items():
            if settings['__valid_in__'].lower() != 'none':
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
            self.create_rst(k, v)

    def create_rst(self, name, spec):

        # todo check for existing and tokenize it

        existing_intro = ''
        existing_settings = dict()
        final_text = ''

        final_text += '{}:\n'.format(name)
        final_text += '=' * (len(name) + 1)
        final_text += '\n\n*Config file section*\n\n'

        if 'machine' in spec['valid_in']:
            final_text += '.. include:: _machine_config_yes.rst\n'
        else:
            final_text += '.. include:: _machine_config_no.rst\n'

        if 'mode' in spec['valid_in']:
            final_text += '.. include:: _mode_config_yes.rst\n\n'
        else:
            final_text += '.. include:: _mode_config_no.rst\n\n'

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
            final_text += '.. todo::\n'
            final_text += '   Add description.'

        final_text += '\n\n\n'

        final_text += self.build_sections(name, spec)

        self.create_file(name, final_text)

    def build_sections(self, name, spec, sep='-'):
        final_text = ''

        if spec['required']:
            final_text += self.add_required_section(spec['required'], name,
                                                    sep)
            final_text += '\n'

        if spec['optional']:
            final_text += self.add_optional_section(spec['optional'], name,
                                                    sep)
            final_text += '\n'

        if 'sub_sections' in spec and spec['sub_sections']:
            final_text += self.add_subsection_section(spec['sub_sections'],
                                                      name, sep)
            final_text += '\n'

        if spec['allow_others']:
            final_text += '.. note:: The ``{}:`` section of your config may ' \
                          'contain additional settings not mentioned here. ' \
                          'Read the introductory text for details of what ' \
                          'those might be.\n\n'.format(name)

        return final_text


    def add_required_section(self, required_list, name, sep='-'):

        if sep == '-':
            sep2 = '~'
        elif sep == '~':
            sep2 = '^'

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

            # todo add to pull in existing
            final_text += '.. todo::\n   Add description.'

            final_text += '\n\n'

        return final_text

    def add_optional_section(self, optional_list, name, sep='-'):

        if sep == '-':
            sep2 = '~'
        elif sep == '~':
            sep2 = '^'

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

            # todo add to pull in existing
            final_text += '.. todo::\n   Add description.'

            final_text += '\n\n'

        return final_text

    def add_subsection_section(self, subsection_dict, name, sep='-'):
        if sep == '-':
            sep2 = '~'
        elif sep == '~':
            sep2 = '^'

        final_text = ''

        for k, v in subsection_dict.items():

            final_text += '{}:\n'.format(k)
            final_text += sep * (len(k) + 1)
            final_text += '\n\n'
            final_text += "The ``{}:`` section contains " \
                          "the following nested sub-settings\n\n".format(k)

            final_text += self.build_sections(k, v, sep=sep2)

        return final_text

    def tokenize_existing_rst(self, filename):
        with open(filename, 'r') as f:
            doc = f.read()

        beginning = ''
        required_settings = ''
        optional_settings = ''

        beginning, settings = doc.split(
            'Settings & options\n------------------')

        beginning = beginning.strip('\n')

        setting_names = list()
        settings_dict = dict()

        for x in re.findall('([^\n]+)\n(~+)', settings):
            setting_names.append(x[0].strip(':'))

        for i, setting_name in enumerate(setting_names):
            start = '\n' + setting_name + ':\n' + ('~' * (len(setting_name) + 1))

            try:
                end = '\n' + setting_names[i+1] + ':\n' + ('~' * (len(setting_names[i+1]) +1))
            except IndexError:
                end = None

            try:
                settings_dict[setting_name] = settings[settings.index(start):
                    settings.index(end)].replace(start, '').strip('\n')
            except TypeError:
                settings_dict[setting_name] = settings[settings.index(start):].replace(start, '').strip('\n')

        # strip out the old spec string so the latest replaces it
        for k, v in settings_dict.items():
            if not k.startswith('<'):
                v = v.strip('\n')
                v = '\n'.join(v.split('\n')[1:])
                v = v.strip('\n')
                settings_dict[k] = v

        return beginning, settings_dict

    def _get_spec_string(self, num, stype, default=None):
        if num == 'single':
            return_string = 'Single value, '
        elif num == 'list' or num == 'set':
            return_string = 'List of one (or more) values, each is a '
        elif num == 'dict':
            return_string = ('Parent setting for one (or more) sub-settings. '
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

        elif stype in ('ms', 'secs'):
            ftype = '``time string`` (:doc:`Instructions ' \
                      '</config/instructions/lists>` for entering time ' \
                      'strings)'

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

        return_string += 'type: {}. '.format(ftype)

        if default:
            return_string += 'Default: ``{}``'.format(default)

        return_string += '\n'

        return return_string


if __name__ == '__main__':
    ConfigDocParser()
