import filecmp
import os
import shutil

source_paths = ['../../mpf/mpf/tests/machine_files',
                '../../mpf-mc/mpfmc/tests/machine_files']

existing_paths = ['../example_configs/mpf_configs',
                  '../example_configs/mpfmc_configs']

file_types = ['.yaml', '.py']

paths_to_ignore = ['data']

examples_root = '../examples'
examples_index = '../examples/index.rst'


class ExampleBuilder(object):

    def __init__(self):
        # all of these are tuples of (full_path, partial_path)
        self.source_files = list()  # all files in the source folders
        self.existing_files = list()  # all files in the docs folders
        self.removed_files = list()  # files in docs but not source
        self.files_in_both = list()  # files in both (based on name)

        # all of these are tuples of (full source path & file, full dest path)
        self.changed_files = list()  # files that are in both but have changed content
        self.new_files = list()  # files in source but not docs

        self.examples_sections = dict()

        self.create_source_file_list()
        self.create_existing_file_list()
        self.find_duplicates()
        self.update_existing_files()

        # the following build the examples folder structure
        self.create_examples_sections()
        self.empty_existing_examples_folder()
        self.write_files()
        self.write_index()

    def create_source_file_list(self):
        for source_path in source_paths:
            for path, _, files in os.walk(source_path):
                for file in files:

                    if os.path.splitext(file)[1] not in file_types:
                        continue

                    full_path = os.path.join(path, file)

                    if self._check_ignored(full_path):
                        continue

                    partial_path = full_path.replace(source_path, '')

                    self.source_files.append((full_path, partial_path))

    def create_existing_file_list(self):
        for existing_path in existing_paths:
            for path, _, files in os.walk(existing_path):
                for file in files:

                    if os.path.splitext(file)[1] not in file_types:
                        continue

                    full_path = os.path.join(path, file)

                    if self._check_ignored(full_path):
                        continue

                    partial_path = full_path.replace(existing_path, '')
                    self.existing_files.append((full_path, partial_path))

    def _check_ignored(self, path):
        for ignore_path in paths_to_ignore:
            if '/{}/'.format(ignore_path) in path:
                return True

        return False

    def find_duplicates(self):
        for full_path, file in self.source_files:
            if file in [x[1] for x in self.existing_files]:
                self.files_in_both.append((full_path, file))

                for index, path in enumerate(source_paths):
                    if full_path.startswith(path):

                        if not filecmp.cmp(
                                source_paths[index] + file,
                                existing_paths[index] + file):

                            self.changed_files.append(
                                (source_paths[index] + file,
                                 os.path.split(existing_paths[index] + file)[0]))

            else:

                for index, path in enumerate(source_paths):
                    if full_path.startswith(path):

                        self.new_files.append(
                            (source_paths[index] + file,
                             os.path.split(existing_paths[index] + file)[0]))

        for full_path, file in self.existing_files:
            if file not in [x[1] for x in self.source_files]:
                self.removed_files.append((full_path, file))

    def update_existing_files(self):

        # copy new files
        for source, target in self.new_files:
            os.makedirs(target, exist_ok=True)
            print("+++++", source, target)
            shutil.copy(source, target)

        # copy changed files
        for source, target in self.changed_files:
            os.makedirs(target, exist_ok=True)
            print(">>>>>", source, target)
            shutil.copy(source, target)

        # delete removed files
        for file, _ in self.removed_files:
            print("-----", file)
            os.remove(file)

        if self.removed_files:
            self.remove_empty_dirs()

    def remove_empty_dirs(self):
        for path in existing_paths:
            empty_count = 0
            used_count = 0

            for curdir, subdirs, files in os.walk(path):
                if len(subdirs) == 0 and len(files) == 0:
                    empty_count += 1
                    os.rmdir(curdir)
                elif len(subdirs) > 0 and len(files) > 0:
                    used_count += 1

    def empty_existing_examples_folder(self):
        shutil.rmtree(examples_root)
        os.makedirs(examples_root)

    def create_examples_sections(self):
        for path in existing_paths:
            for dir in os.listdir(path):
                self.examples_sections[dir] = dict()
                self.examples_sections[dir]['config'] = list()
                self.examples_sections[dir]['modes'] = list()
                self.examples_sections[dir]['shows'] = list()

            for full_path, dirs, files in os.walk(path):
                rel_path = full_path.replace(path, '')

                if files:
                    folders = rel_path.lstrip('/').split('/')
                    section = folders[0]
                    folder = folders[1]

                    if (section in self.examples_sections and
                            folder in self.examples_sections[section]):
                        for file in files:
                            self.examples_sections[section][folder] = (
                                os.path.join(rel_path, file))

        import pprint
        pprint.pprint(self.examples_sections)

    def write_files(self):
        for section, folders in self.examples_sections.items():
            content = section + '\n' + '*' * len(section) + '\n\n'

            if folders['config']:
                content += 'Machine config sections\n=======================\n'

            for file in folders['config']:
                content += '''
Machine config sections
=======================

.. literalinclude::

'''


    def write_index(self):
        index = '''Example Configuration Files
===========================

MPF contains lots of tests with sample configs. Here's a list of them.

.. toctree::
'''
        for folder in sorted(self.examples_sections.keys()):
            index += '   {}\n'.format(folder)

        with open(examples_root + '/index.rst', 'w') as f:
            f.write(index)



if __name__ == '__main__':
    a = ExampleBuilder()
