import os
from collections import namedtuple

import re
import sys

import mpf

import ruamel.yaml as yaml
from mpf.core.utility_functions import Util
from typing import Dict, Tuple

rst_path = '../config'


RstSection = namedtuple("RstSection", ["header", "body", "full_body", "level", "parent"])


class ConfigDocParser(object):

    def __init__(self):
        self.file = None
        self.file_list = list()
        self.config_spec = dict()
        self.config_specs = dict()

        self.existing_rsts = list()

        self._load_config_spec()
        self.config_specs, self.all_specs = self._create_config_specs(self.config_spec)
        self._load_existing_rsts()

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
            self.config_spec = yaml.safe_load(f)

    def _load_existing_rsts(self):
        self.existing_rsts = [x[:-4] for x in os.listdir(rst_path)
                              if (x.endswith('.rst') and
                                  not x.startswith('_'))]

    def _create_config_specs(self, source_dict):
        final_dict = dict()
        all_specs = dict()

        for section, settings in source_dict.items():
            all_specs[section] =  (self._create_subsection_config_spec(settings))
            if '__valid_in__' in settings and settings['__valid_in__'].lower() != 'none':
                final_dict[section] = (
                    self._create_subsection_config_spec(settings))

        return final_dict, all_specs

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
            if setting_name == '__type__':
                final_dict['__type__'] = setting_spec

            if isinstance(setting_spec, dict):

                final_dict['sub_sections'][setting_name] = (
                    self._create_subsection_config_spec(setting_spec))

            elif isinstance(setting_spec, str):
                if setting_spec == "ignore":
                    final_dict['optional'].append((setting_name, "ignored", "ignored", "None"))
                else:
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

    def create_rsts(self, dangerous_changes):
        for k, v in self.config_specs.items():
            # skip config players for now as they cause havoc
            if v.get("type", None) == "config_player":
                continue
            if not v["required"] and not v["optional"]:
                # no specs at all
                continue

            try:
                self.create_rst(k, dangerous_changes)
            except AssertionError as e:
                print("FAILED TO UPDATE {}. Skipping. ({})".format(k, e))

    def _prepare_default_texts(self, existing_settings):
        texts = {
            "label": "Name of this device in service mode.",
            "debug": "Set this to true to see additional debug output. This might impact the performance of MPF.",
            "console_log": "Log level for the console log for this device.",
            "file_log": "Log level for the file log for this device.",
        }

        # add the remaining
        for section, text in texts.items():
            if section not in existing_settings:
                existing_settings[section] = RstSection("", text, text, 2, "Optional settings")

    def create_rst(self, name, dangerous_changes):
        type = self.all_specs[name].get("__type__")

        if type == "device":
            spec = self.config_specs[name]
            device_spec = self.all_specs["device"]
            spec = Util.dict_merge(spec, device_spec)

            self._create_rst(name, spec, True, dangerous_changes)
        else:
            spec = self.all_specs[name]
            if "valid_in" not in spec:
                spec["valid_in"] = ""
            self._create_rst(name, spec, False, dangerous_changes)

    def _create_rst(self, name, spec, device=False, dangerous_changes=False):

        if name in self.existing_rsts:
            existing_intro, existing_settings = (
                self.tokenize_existing_rst(os.path.join(rst_path,
                                                        name + '.rst')))

        else:
            existing_intro = ''
            existing_settings = dict()      # type: Dict[str, RstSection]

        if device:
            self._prepare_default_texts(existing_settings)

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
                          name.split('_player')[0])

        final_text += '.. overview\n\n'

        if existing_intro:
            final_text += existing_intro
        else:
            final_text += 'The ``{}:`` section of your config is where ' \
                          'you...\n\n'.format(name)
            final_text += '.. todo:: :doc:`/about/help_us_to_write_it`'

        final_text += '\n\n.. config\n\n\n'

        final_text += self.build_sections(name, spec, existing_settings)

        howtos = ""
        if "Related How To guides" in existing_settings:
            howtos = existing_settings["Related How To guides"].full_body
            del existing_settings["Related How To guides"]

        final_text += self.build_howtos(howtos)

        would_remove_sections = False
        for setting, content in existing_settings.items():
            if content.full_body.strip():
                would_remove_sections = True
                print('WARNING: Removing setting "{}" from {}:\n{}\n\n-----------\n'.format(
                    setting, name, content.full_body))

        if would_remove_sections and not dangerous_changes:
            print('WILL NOT WRITE {} because we would remove text. Add "--yes" to your commandline to process.'.format(
                name
            ))
        else:
            self.create_file(name, final_text)

    def build_howtos(self, howtos):
        final_text = "Related How To guides\n"
        final_text += "---------------------\n\n"

        if not howtos:
            final_text += '.. todo:: :doc:`/about/help_us_to_write_it`'
        else:
            final_text += howtos

        final_text += '\n'

        return final_text

    def build_sections(self, name, spec, existing_settings: Dict[str, RstSection], level=1):
        final_text = ''

        existing_settings.pop("Required settings", None)
        existing_settings.pop("Optional settings", None)

        if spec['required']:
            final_text += self.add_required_section(spec['required'], name,
                                                    existing_settings, level)
            final_text += '\n'

        if spec['optional']:
            final_text += self.add_optional_section(spec['optional'], name,
                                                    existing_settings, level)
            final_text += '\n'

        if 'sub_sections' in spec and spec['sub_sections']:
            final_text += self.add_subsection_section(spec['sub_sections'],
                                                      name, existing_settings, level)
            final_text += '\n'

        return final_text

    def add_required_section(self, required_list, name, existing_settings: Dict[str, RstSection], level):
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

            if setting[0] in existing_settings:
                if existing_settings[setting[0]].level == level + 1:
                    found = True
                    final_text += existing_settings[setting[0]].body
                    del existing_settings[setting[0]]
                else:
                    print("WARNING: Setting {} is at the wrong level".format(setting[0]))

            if not found:
                final_text += '.. todo:: :doc:`/about/help_us_to_write_it`'

            final_text += '\n\n'

        return final_text

    def add_optional_section(self, optional_list, name, existing_settings, level):

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

            if setting[0] in existing_settings:
                if existing_settings[setting[0]].level == level + 1:
                    found = True
                    final_text += existing_settings[setting[0]].body
                    del existing_settings[setting[0]]
                else:
                    print("WARNING: Setting {} is at the wrong level".format(setting[0]))

            if not found:
                final_text += '.. todo:: :doc:`/about/help_us_to_write_it`'

            final_text += '\n\n'

        return final_text

    def add_subsection_section(self, subsection_dict, name, existing_settings, level):
        if level == 1:
            sep = '-'
            sep2 = '~'
        elif level == 2:
            sep = '~'
            sep2 = '^'
        else:
            sep = '^'
            sep2 = '"'

        final_text = ''

        for k, v in subsection_dict.items():

            final_text += '{}:\n'.format(k)
            final_text += sep * (len(k) + 1)
            final_text += '\n\n'

            found = False

            for k1, v1 in existing_settings.items():
                if k1[0] == k and k1[2] == level + 1:
                    final_text += v1
                    found = True
                    del existing_settings[k1]
                    break

            if not found:
                final_text += "The ``{}:`` section contains " \
                              "the following nested sub-settings".format(k)

            final_text += '\n\n'
            final_text += self.build_sections(k, v, existing_settings, level+1)

        return final_text

    @staticmethod
    def tokenize_existing_rst(filename) -> Tuple[str, Dict[str, RstSection]]:
        with open(filename, 'r') as f:
            doc = f.read()

        settings_dict = dict()

        # trim off the header info
        parts = doc.split('.. overview\n\n', 1)
        if len(parts) == 2:
            doc = parts[1]
        else:
            doc = parts[0]

        parts = doc.split('.. config\n\n', 1)
        if len(parts) == 2:
            doc = parts[1]
            beginning = parts[0]
        else:
            doc = parts[0]
            beginning = None

        levels = ['=', '-', '~', '^']
        last_parents = [None, None, None, None]
        sections = list()  # tuple (name, level, parent)
        first_section_start = None

        for x in re.finditer('([^\n]+)\n([~\-^]+)', doc):
            if not first_section_start:
                first_section_start = x.start(1)
            level = levels.index(x.group(2)[0])
            name = x.group(1).strip(':')
            heading = x.group(1)
            last_parents[level] = name

            if level:
                parent = last_parents[level - 1]
            else:
                parent = None

            sections.append((name, heading, level, parent, x.start(1), x.end(2)))

        if not beginning:
            if not first_section_start:
                beginning = doc
            else:
                beginning = doc[:first_section_start]

        beginning = beginning.strip('\n')

        for i, (name, heading, level, parent, start, start_body) in enumerate(sections):
            start = '\n' + heading + '\n' + (levels[level] * (len(heading)))

            try:
                end = sections[i+1][4]
            except IndexError:
                end = None

            if end:
                try:
                    full_body = doc[start_body:end]
                except ValueError:
                    raise AssertionError("Could not process section: {}".format(name))
            else:
                full_body = doc[start_body:]

            full_body = full_body.strip('\n')

            # strip out the old spec string so the latest replaces it
            if level:
                try:
                    header, body = full_body.split('\n\n', 1)
                    header = header.strip('\n')
                    body = body.strip('\n')
                except ValueError:
                    body = full_body
                    header = ""
            else:
                header = ""
                body = full_body

            if name in settings_dict and name not in ("Optional settings", "Required settings"):
                raise AssertionError("Duplicate section {} in {}".format(name, filename))
            settings_dict[name] = RstSection(header, body, full_body, level, parent)

        return beginning, settings_dict

    def _get_index_of_next_heading(self, doc_lines):

        heading_chars = set(('-', '~', '^'))

        for i in range(len(doc_lines)):
            if set(doc_lines[i]).issubset(heading_chars):
                # we have a heading sep
                return i - 1

    def _get_type_desc(self, stype):
        if stype == 'str':
            ftype = '``string``'

        elif stype == 'lstr':
            ftype = '``string`` (case-insensitive)'

        elif stype == 'float':
            ftype = '``number`` (will be converted to floating point)'

        elif stype == 'template_float':
            ftype = '``number`` or ``template`` (will be converted to floating point; ' \
                    ':doc:`Instructions for entering templates ' \
                    '</config/instructions/dynamic_values>`)'

        elif stype == 'int':
            ftype = '``integer``'

        elif stype == 'template_int':
            ftype = '``integer`` or ``template`` (:doc:`Instructions for entering templates ' \
                    '</config/instructions/dynamic_values>`)'

        elif stype == 'num':
            ftype = '``number`` (can be integer or floating point)'

        elif stype == 'bool' or stype == 'boolean' or stype == 'bool_int':
            ftype = '``boolean`` (``true``/``false``)'

        elif stype == 'template_bool':
            ftype = '``boolean`` or ``template`` (``true/false``; :doc:`Instructions for entering templates ' \
                    '</config/instructions/dynamic_values>`)'

        elif stype == 'secs':
            ftype = '``time string (secs)`` (:doc:`Instructions for entering '\
                    'time strings </config/instructions/time_strings>`)'

        elif stype == 'template_secs':
            ftype = '``time string (secs) or template`` (:doc:`Instructions for entering '\
                    'time strings </config/instructions/time_strings>` and :doc:`Instructions for entering templates ' \
                    '</config/instructions/dynamic_values>`)'

        elif stype == 'ms':
            ftype = '``time string (ms)`` (:doc:`Instructions for entering '\
                    'time strings </config/instructions/time_strings>`)'

        elif stype == 'template_ms':
            ftype = '``time string (ms) or template`` (:doc:`Instructions for entering '\
                    'time strings </config/instructions/time_strings>` and :doc:`Instructions for entering templates ' \
                    '</config/instructions/dynamic_values>`)'

        elif stype == 'list':
            ftype = '``list`` (:doc:`Instructions ' \
                      '</config/instructions/lists>` for entering lists)'

        elif stype == 'int_from_hex':
            ftype = '2-byte hex value (``00`` to ``ff``)'

        elif stype == 'kivycolor' or stype == 'color':
            ftype = '``color`` (*color name*, *hex*, or list of values ' \
                    '*0*-*255*)'

        elif stype == 'pow2':
            ftype = '``integer`` (must be a power of 2)'

        elif stype == 'gain':
            ftype = '``gain setting`` (-inf, db, or float between 0.0 and 1.0)'

        elif stype.startswith('subconfig'):
            configs = stype.replace('subconfig(', '')[:-1].split(",")
            try:
                configs.remove("device")
            except ValueError:
                pass
            ftype = "".join(':doc:`{} <{}>`, '.format(config, config) for config in configs)[:-2]

        elif stype.startswith('enum'):
            ftype = 'one of the following options: {}'.format(
                stype.replace('enum(', '').replace(',', ', ')[:-1])

        elif stype.startswith('machine('):
            device_name = stype.replace('machine(', '')[:-1]
            ftype = "string name of a :doc:`{} <{}>` device".format(
                    device_name, device_name)

        elif stype.startswith('dict('):
            stype = stype.replace('dict(', '')[:-1]
            stype = stype.split(':')
            ftype = 'dictionary consisting of {} : {}'.format(
                self._get_type_desc(stype[0]), self._get_type_desc(stype[1]))

        elif ':' in stype:
            raise AssertionError("Should be catched earlier: {}.".format(stype))

        else:
            ftype = stype

        return ftype

    def _layout_attribute_defaults(self, default_settings):
        if default_settings == "None" or default_settings is None:
            return "Defaults to empty."
        elif default_settings == "":
            return "Required attribute."
        else:
            return "Default: ``{}``".format(default_settings)

    def _get_spec_string(self, num, stype, default=None):
        if num == 'single':
            if stype == 'event_posted':
                return 'Single event. This device will be posted by the device. {}\n'.format(
                    self._layout_attribute_defaults(default))
            elif stype == 'event_handler':
                return 'Single event. The device will add an handler for this event. {}\n'.format(
                    self._layout_attribute_defaults(default))

            return_string = 'Single value, '
        elif num == 'list' or num == 'set':
            if stype == 'event_posted':
                return 'List of one (or more) events. Those will be posted by the device. {}\n'.format(
                    self._layout_attribute_defaults(default))
            elif stype == 'event_handler':
                return 'List of one (or more) events. The device will add handlers for those events. {}\n'.format(
                    self._layout_attribute_defaults(default))

            return_string = 'List of one (or more) values, each is a '
        elif num == 'dict':
            stype = stype.split(':')
            return_string = 'One or more sub-entries. Each in the format of {} : {}\n'.format(
                self._get_type_desc(stype[0]), self._get_type_desc(stype[1]))
            return return_string
        elif num == 'omap':
            stype = stype.split(':')
            return_string = 'Ordered list for one (or more) sub-settings. Each in the format of {} : {}\n'.format(
                self._get_type_desc(stype[0]), self._get_type_desc(stype[1]))
            return return_string
        elif num == 'event_handler':
            return 'List of one (or more) device control events (:doc:`Instructions for entering '\
                    'device control events </config/instructions/device_control_events>`). {}\n'.format(
                self._layout_attribute_defaults(default))

        elif num == "ignored":
            return "Unknown type. See description below.\n"
        else:
            raise AssertionError("Invalid config spec num: {}".format(num))

        ftype = self._get_type_desc(stype)

        return_string += 'type: {}. {}\n'.format(ftype, self._layout_attribute_defaults(default))

        return return_string


if __name__ == '__main__':
    parser = ConfigDocParser()

    if len(sys.argv) <= 1:
        print("Usage: {} config_section_name/all".format(sys.argv[0]))

    dangerous_changes = sys.argv[2] == "--yes" if len(sys.argv) > 2 else False

    if sys.argv[1] == "all":
        parser.create_rsts(dangerous_changes)
    else:
        parser.create_rst(sys.argv[1], dangerous_changes)
    #parser.create_rsts()
    #parser.write_index()
