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

        self.existing_rsts = list()

        self._load_config_spec()
        self._load_existing_rsts()

        for k, v in self.config_spec.items():
            rst = self.create_spec(k, v)
            self.create_file(k, rst)

        self.write_index()

    def create_file(self, config_section, rst):
        filename = config_section + '.rst'

        with open(os.path.join(rst_path, filename), 'w') as f:
            f.write(rst)

        return filename

    def write_index(self):
        index = '''YAML config file reference
==========================

This section contains details about every possible entry you can use in your
YAML config files. Each entry also has information about whether it's valid in
your machine-wide config, a mode-specific config, or both.

.. toctree ::
   :maxdepth: 1

'''
        self._load_existing_rsts()
        self.existing_rsts.sort()

        for file_name in self.existing_rsts:
            index += '   {}: <{}>\n'.format(file_name, file_name)

        with open(os.path.join(rst_path, 'index.rst'), 'w') as f:
            f.write(index)

    def _load_config_spec(self):
        self.config_spec = yaml.load(mpf_config_spec)

    def _load_existing_rsts(self):
        self.existing_rsts = [x[:-4] for x in os.listdir(rst_path)
                              if (x.endswith('.rst') and
                                  not x.startswith('_'))]

    def create_spec(self, section, spec_settings):

        beginning = '{}: (config_setting)\n'.format(section)
        beginning += '=' * (len(section) + 18)
        beginning += '\n.. todo::\n'
        beginning += '   Add description.'
        settings = dict()

        if section in self.existing_rsts:
            print('found existing RST for', section)
            beginning, settings = self.tokenize_existing_rst(
                '{}/{}.rst'.format(rst_path, section))

        # add spec items not in rst
        for k in spec_settings.keys():
            if k not in settings:
                settings[k] = '.. todo::\n   Add description.'

        # deprecate rst items not in spec
        for k in settings.keys():
            if k not in spec_settings and not k.startswith('<'):
                settings[k] = '.. deprecated:: {}'.format(__version__)

        # put the keys in order
        ordered_settings = sorted(settings.keys())

        # build the final
        final_rst = beginning + '\n\n\n'
        final_rst += 'Settings & options\n------------------\n'

        if '<name>' in ordered_settings:
            final_rst += '<name>:\n~~~~~~~\n'
            final_rst += settings['<name>'] + '\n\n'

        for s in ordered_settings:

            s = s.strip(':')

            if s == '__allow_others__':
                continue
            if s == '<name>':
                continue
            final_rst += '\n' + s + ':\n' + ('~' * (len(s) + 1)) + '\n'

            if isinstance(spec_settings[s], str):
                final_rst += self._get_spec_string(spec_settings[s]) + '\n'
            elif isinstance(spec_settings[s], dict):
                final_rst += '\n'
                for k, v in spec_settings[s].items():
                    final_rst += '* *{}*: {}'.format(k, v)
                final_rst += '\n'

            final_rst += settings[s] + '\n\n'

        if '__allow_others' in s:
            final_rst += ('.. note::\n   Your config may have additional '
                          'settings not included here since the {}: config '
                          'section allows additional settings that are passed '
                          "when it's used.")

        final_rst = final_rst.replace('\n\n\n\n', '\n\n\n')
        print()
        print(final_rst)
        print()
        return final_rst

    def tokenize_existing_rst(self, filename):
        with open(filename, 'r') as f:
            doc = f.read()

        beginning, settings = doc.split(
            'Settings & options\n------------------')

        beginning = beginning.strip('\n')

        setting_names = list()
        settings_dict = dict()

        for x in re.findall('([^\n]+)\n(~+)', settings):
            setting_names.append(x[0].strip(':'))

        for i, setting_name in enumerate(setting_names):
            start = setting_name + ':\n' + ('~' * (len(setting_name) + 1))

            try:
                end = setting_names[i+1] + ':\n' + ('~' * (len(setting_names[i+1]) +1))
            except IndexError:
                end = None

            try:
                settings_dict[setting_name] = settings[settings.index(start):
                    settings.index(end)].replace(start, '').strip('\n')
            except TypeError:
                settings_dict[setting_name] = settings[settings.index(start):].replace(start, '').strip('\n')

        # strip out the old spec string so the latest replaces it
        # for k, v in settings_dict.items():
        #     if not k.startswith('<'):
        #         v = v.strip('\n')
        #         v = '\n'.join(v.split('\n')[1:])

        return beginning, settings_dict

    def _get_spec_string(self, config_spec):
        try:
            num, stype, default = config_spec.split('|')
        except AttributeError:
            return config_spec
        except:
            return('.. todo::\n   Need to add details here.\n')

        if num == 'single':
            return_string = 'Single value, '
        elif num == 'list' or num == 'set':
            return_string = 'List of one (or more) values, each is a '
        elif num == 'dict':
            return_string = ('Parent setting for one (or more) sub-settings. '
                             'Each sub-setting is a ')

        if stype == 'str':
            ftype = 'string'
        elif stype == 'lstr':
            ftype = 'string (case-insensitive)'
        elif stype == 'float':
            ftype = 'number (will be converted to floating point)'
        elif stype == 'int':
            ftype = 'integer'
        elif stype == 'num':
            ftype = 'number (can be integer or floating point'
        elif stype == 'bool' or stype == 'boolean' or stype == 'bool_int':
            ftype = 'boolean (Yes/No or True/False)'
        elif stype == 'ms':
            ftype = 'time string (will be converted to milliseconds)'
        elif stype == 'secs':
            ftype = 'time string (will be converted to seconds)'
        elif stype == 'list':
            ftype = 'list'
        elif stype == 'int_from_hex':
            ftype = '2-byte hex value (00 to ff)'
        elif stype == 'kivycolor' or stype == 'color':
            ftype = 'color (color name, hex, or list'
        elif stype == 'pow2':
            ftype = 'integer (must be a power of 2'
        elif stype == 'gain':
            ftype = 'gain setting (-inf, db, or float between 0.0 and 1.0'
        elif stype.startswith('subconfig'):
            ftype = 'sub-configurating containing {} settings'.format(
                stype.replace('subconfig(', '')[:-1])
        elif stype.startswith('enum'):
            ftype = 'one of the following options: {}'.format(
                stype.replace('enum(', '').replace(',', ', ')[:-1])
        elif stype.startswith('machine'):
            ftype = "string name of a '{}' device".format(
                stype.replace('machine(', '')[:-1])
        else:
            ftype = stype

        return_string += 'type: {}. '.format(ftype)

        if default:
            return_string += 'Default: {}\n'.format(default)
        else:
            return_string += 'Default: n/a (a value is required)\n'

        return return_string


if __name__ == '__main__':
    ConfigDocParser()