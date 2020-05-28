import ast
import os
import re
from collections import defaultdict

from mpf.parsers.event_reference_parser import EventReferenceParser, EventReference
from typing import List, Dict


class EventDocCreator(object):

    def __init__(self, rst_path):
        self.file = None
        self.file_list = list()
        self.rst_path = rst_path
        self.device_labels = {}
        self.device_events = defaultdict(list)

    def _format_event_name(self, event: EventReference):
        if event.class_label:
            return event.event_name.replace("(name)", "({})".format(event.class_label))

        return event.event_name

    def create_files(self, events: List[EventReference], event_type):
        """Create files for events and return a list of the file names."""
        file_list = []
        for event in events:
            rst = self.build_rst_entry(event, event_type)
            event_name = self._format_event_name(event)
            filename = self.create_file_if_changed(event_name, rst)
            file_list.append((event, filename))

        return file_list

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
                            filename = self.create_file_if_changed(event, rst)
                            self.file_list.append((event, filename))

                        if config_section and rst:
                            self.device_events[config_section].append(event)
                            self.device_labels[config_section] = class_label

    def write_index(self, file_list, events: List[EventReference]):

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

For example, the switch event called :doc:`(name)_active <switch_active>`
will replace the "(name)" part of the event text with the actual switch name.
So the when a switch called ``s_left_slingshot`` is activated, it will posted
an event called *switch_s_left_slingshot_active*.

.. toctree::
   :maxdepth: 1

'''
        # sort based on the file name, rather than the event name, since that
        # has the special chars stripped.
        file_list.sort(key=lambda x: x[1])

        for file_name in file_list:
            index += '   {} <{}>\n'.format(file_name[0].event_name, file_name[1][:-4])

        index += '''
Device Indexes
--------------
        
.. toctree::
   :maxdepth: 1

'''
        devices = {}
        for event in events:
            if event.class_label and event.config_section:
                if event.config_section not in devices:
                    devices[event.config_section] = []
                devices[event.config_section].append(event)

        for config_section, events in sorted(devices.items()):
            index += '   {} <index_{}>\n'.format(events[0].class_label, config_section)

            rst = events[0].class_label + "\n"
            rst += "=" * (len(events[0].class_label)) + "\n\n"
            rst += "See: :doc:`/config/{}`".format(config_section) + "\n\n"

            for event in events:
                event_name = self._format_event_name(event)
                rst += '* :doc:`{}`'.format(event_name.replace('(', '').replace(')', '')) + "\n"

            self.create_file_if_changed('index_{}'.format(config_section), rst)

            rst = ""

            for event in events:
                event_name = self._format_event_name(event)
                rst += '* :doc:`/events/{}`'.format(event_name.replace('(', '').replace(')', '')) + "\n"

            rst += "\n"

            self.create_file_if_changed('include_{}'.format(config_section), rst)

        self.create_file_if_changed('index', index)

    def create_file_if_changed(self, event, rst):
        filename = event.replace('(', '').replace(')', '') + '.rst'
        file_path = os.path.join(self.rst_path, filename)

        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                content = f.read()

            if content == rst:
                # file did not change
                return filename

        with open(file_path, 'w') as f:
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

    def build_rst_entry(self, event: EventReference, event_type):
        rst_output = str()

        # write the title
        rst_output += event.event_name + '\n'

        rst_output += ('=' * len(event.event_name)) + '\n\n'
        rst_output += '*{}*\n\n'.format(event_type)

        # add the description
        rst_output += event.desc + '\n\n'

        if event.args:

            rst_output += 'Keyword arguments\n'
            rst_output += '-----------------\n'

            rst_output += '''
(See the :doc:`/events/overview/conditional` guide for details for how to
create entries in your config file that only respond to certain combinations of
the arguments below.)\n\n'''
            rst_output += self.build_args(event.args)
        else:
            rst_output += '*This event does not have any keyword arguments*\n'


        rst_output += "\n"

        if event.config_section and event.class_label:
            rst_output += 'Event is posted by the :doc:`{} device </config/{}>`\n\n'.format(
                event.class_label, event.config_section)

            if event.config_attribute:
                rst_output += "The event name can be changed by using the \"{}:\" attribute.\n\n".format(
                    event.config_attribute)

        return rst_output

    def build_args(self, args_dict: Dict[str, str]):
        output = ""

        for k, v in sorted(args_dict.items()):

            v = v.replace('\n', ' ')
            v = re.sub(' +', ' ', v)

            output += '``' + k + '``\n'
            output += '  ' + v + '\n\n'

        return output

def run(rst_path, mpf_path, mc_path):
    dont_delete_files = []

    parser = EventReferenceParser()
    mpf_events = parser.get_events_from_path([mpf_path])
    mpfmc_events = parser.get_events_from_path([mc_path])

    # delete existing files
    for path, _, files in os.walk(rst_path):
        for file in files:
            # only delete files in the rst_path, not subfolders
            if path == rst_path and file not in dont_delete_files:
                os.remove(os.path.join(path, file))

    creator = EventDocCreator(rst_path)
    file_list = []
    file_list.extend(creator.create_files(mpf_events, "MPF Event"))
    file_list.extend(creator.create_files(mpfmc_events, "MPF-MC Event"))
    creator.write_index(file_list, mpf_events + mpfmc_events)

if __name__ == '__main__':
    rst_path = '../events'
    run(rst_path, "../../mpf/mpf", "../../mpf-mc/mpfmc")
