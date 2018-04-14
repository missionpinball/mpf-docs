import filecmp
import os
import shutil


class ExampleBuilder(object):

    def __init__(self, source_dirs, examples_root):
        self.examples_root = examples_root
        self.file_types = ['.yaml', '.py']
        self.paths_to_ignore = ['data']

        # all of these are tuples of (full_path, partial_path)
        self.examples_sections = dict()
        for source, rst_dir in source_dirs.items():
            self.add_examples_sections(source, rst_dir)

    def build(self):
        # the following build the examples folder structure
        self.empty_existing_examples_folder()
        self.write_files()
        self.write_index()

    def create_source_file_list(self):
        for source_path in source_config_paths:
            for path, _, files in os.walk(source_path):
                for file in files:

                    if os.path.splitext(file)[1] not in self.file_types:
                        continue

                    full_path = os.path.join(path, file)

                    if self._check_ignored(full_path):
                        continue

                    partial_path = full_path.replace(source_path, '')

                    self.source_files.append((full_path, partial_path))

    def create_existing_file_list(self):
        for path, _, files in os.walk(source_config_paths[0]):
            for file in files:

                if os.path.splitext(file)[1] not in self.file_types:
                    continue

                full_path = os.path.join(path, file)

                if self._check_ignored(full_path):
                    continue

                partial_path = full_path.replace(local_config_path, '')
                self.existing_files.append((full_path, partial_path))

    def _check_ignored(self, path):
        for ignore_path in self.paths_to_ignore:
            if '/{}/'.format(ignore_path) in path:
                return True

        return False

    def find_duplicates(self):
        for full_path, file in self.source_files:
            if file in [x[1] for x in self.existing_files]:
                self.files_in_both.append((full_path, file))

                if not filecmp.cmp(full_path, local_config_path + file):

                    self.changed_files.append(
                        (full_path,
                         os.path.split(local_config_path + file)[0]))

            else:
                self.new_files.append(
                    (full_path,
                     os.path.split(local_config_path + file)[0]))

        for full_path, file in self.existing_files:
            if file not in [x[1] for x in self.source_files]:
                self.removed_files.append((full_path, file))

    def update_existing_files(self):

        # copy new files
        for source, target in self.new_files:
            os.makedirs(target, exist_ok=True)
            target_file_with_path = os.path.join(target, os.path.split(source)[1])

            # check if the target file exists:
            # if os.path.isfile(target_file_with_path):
            #     print("WARNING: Duplicate file found:", target_file_with_path)
            #     continue

            print("<NEW> {} -> {}".format(source, target_file_with_path))
            shutil.copy(source, target)

        # copy changed files
        for source, target in self.changed_files:
            os.makedirs(target, exist_ok=True)
            target_file_with_path = os.path.join(target, os.path.split(source)[1])

            print("<UPDATED> {} -> {}".format(source, target_file_with_path))
            shutil.copy(source, target)

        # delete removed files
        for file, _ in self.removed_files:
            print("<REMOVED>", file)
            os.remove(file)

        if self.removed_files:
            self.remove_empty_dirs()

    def remove_empty_dirs(self):
        empty_count = 0
        used_count = 0

        for curdir, subdirs, files in os.walk(local_config_path):
            if len(subdirs) == 0 and len(files) == 0:
                empty_count += 1
                os.rmdir(curdir)
            elif len(subdirs) > 0 and len(files) > 0:
                used_count += 1

    def empty_existing_examples_folder(self):
        try:
            shutil.rmtree(self.examples_root)
        except FileNotFoundError:
            pass
        os.makedirs(self.examples_root)

    def add_examples_sections(self, path, rst_path):
        for dir in os.listdir(path):
            if dir.startswith('.'):
                continue
            if dir not in self.examples_sections:
                self.examples_sections[dir] = dict()
                self.examples_sections[dir]['config'] = list()
                self.examples_sections[dir]['modes'] = list()
                self.examples_sections[dir]['shows'] = list()

        for full_path, dirs, files in os.walk(path):
            rel_path = os.path.abspath(full_path).replace(os.path.abspath(os.path.join(path, "..")), '')
            name_path = os.path.abspath(full_path).replace(os.path.abspath(path), '')

            if files:
                folders = name_path.lstrip('/').split('/')
                section = folders[0]
                if len(folders) > 1:
                    folder = folders[1]

                    if (section in self.examples_sections and
                            folder in self.examples_sections[section]):
                        for file in files:
                            if os.path.splitext(file)[1] not in self.file_types:
                                continue

                            self.examples_sections[section][folder].append((
                                os.path.join(rel_path, file), os.path.join(name_path, file)))

    def write_files(self):
        for section, folders in self.examples_sections.items():
            content = (section + ' (example config files)\n' + '=' *
                       (len(section) + 23) + '\n')

            # Machine-wide configs

            if folders['config']:
                content += '''
Machine config examples
-----------------------

Here are some example machine-wide config files that show
real-world examples of how these configs are used.
'''

            if len(folders['config']) > 1:
                content += '''
Note that there are multiple machine config
examples here. They're just included to show different
options. You wouldn't actually use more than one.
'''

            for file, path_in_config in folders['config']:

                content += '''
.. literalinclude:: {}
   :caption: `your_machine_folder{} <{}>`_
   :language: yaml
'''.format(file, path_in_config, file)
            os.makedirs(self.examples_root + '/' + section, exist_ok=True)
            with open(self.examples_root + '/' + section + '/index.rst', 'w') as f:
                f.write(content)

            # Mode configs

            if folders['modes']:
                content += '''
Mode config examples
--------------------

Here are some example mode config files that go along with the machine-wide
config above.
'''

            if len(folders['modes']) > 1:
                content += '''
Note that there are multiple mode config examples here. You might not
necessarily use more than one in your machine.
'''

            for file, path_in_config in folders['modes']:

                content += '''
.. literalinclude:: {}
   :caption: `your_machine_folder{} <{}>`_
   :language: yaml
'''.format(file, path_in_config, file)
            os.makedirs(self.examples_root + '/' + section, exist_ok=True)
            with open(self.examples_root + '/' + section + '/index.rst', 'w') as f:
                f.write(content)

            # Show files

            if folders['shows']:
                content += '''
Show file examples
------------------

Here are some example show files that go along with the above config(s).
'''

            if len(folders['shows']) > 1:
                content += '''
Note that there are multiple shows here.
'''

            for file, path_in_config in folders['shows']:

                content += '''
.. literalinclude:: {}
   :caption: `your_machine_folder{} <{}>`_
   :language: yaml
'''.format(file, path_in_config, file)
            os.makedirs(self.examples_root + '/' + section, exist_ok=True)
            with open(self.examples_root + '/' + section + '/index.rst', 'w') as f:
                f.write(content)

    def write_index(self):
        index = '''Example Configuration Files
===========================

MPF is very complex with lots of modules and options. In order to make sure
that everything works, we have over 700 automated tests that run every time we
add or change something in MPF in order to make sure we didn't break something.

All of these automated tests include config files (machine configs,
mode configs, and show files). In many ways, these config files are the
"ultimate truth" when it comes to what configs actually work with MPF.

All of the links below show the actual config files (pulled from the MPF and
MPF-MC packages) that are used to test MPF. They're also a valuable resource
for people creating games with MPF since they show many different options and
configurations that are known to work.

You can click on any of the links below to see the actual config files for
each topic. Each link may have multiple separate machine configs, mode configs,
and/or show configs.

.. toctree::
   :titlesonly:

'''
        for folder in sorted(self.examples_sections.keys()):
            index += '   {} </examples/{}/index>\n'.format(folder, folder)

        with open(self.examples_root + '/index.rst', 'w') as f:
            f.write(index)


if __name__ == '__main__':
    source_dirs = {"../mpf_examples": "/mpf_examples", "../mpfmc_examples": "/mpfmc_examples"}
    examples_root = '../examples'

    b = ExampleBuilder(source_dirs, examples_root)
    b.build()
