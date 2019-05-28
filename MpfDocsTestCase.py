"""Contains the MpfDocsTestCase class"""

import os
import shutil
import tempfile
import uuid

from mpf.tests.MpfTestCase import MpfTestCase

class MpfDocsTestCase(MpfTestCase):

    """Allows unittests to extract configs from .rst files in mpf-docs and
       load them and run tests against them.

    To use it, add comments in the rst file which specific the begin/end of
    the indended code block in the RST file which will be the config. The
    begin also has the path and filename to the config file.

    For example, from an .rst file:

    ---------------------------------------------------

    blah blah blah some text blah blah blah

    .. begin_mpfdoctest:config/config.yaml

    ::

        #config_version=5

        switches:
            s_left_flipper:
                number: 1

    .. end_mpfdoctest

    blah blah blah some text blah blah blah

    ---------------------------------------------------

    """

    rst_target = ''

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._temp_machine_folder = None

    def setUp(self):
        self._temp_machine_folder = os.path.join(tempfile.gettempdir(),
                                                 str(uuid.uuid4()))
        self.create_temp_config_files()
        super().setUp()

    def getOptions(self):
        options = super().getOptions()
        options['no_load_cache'] = True
        options['create_config_cache'] = False

        return options

    def tearDown(self):
        super().tearDown()
        shutil.rmtree(self.getMachinePath())
        self._temp_machine_folder = None

    def getConfigFile(self):
        return 'config.yaml'

    def getMachinePath(self):
        return self._temp_machine_folder

    def create_temp_config_files(self):
        if not self.rst_target.endswith('.rst'):
            self.rst_target += '.rst'

        if self.rst_target[0] == '/':
            self.rst_target = self.rst_target[1:]

        with open(os.path.abspath(self.rst_target), 'r') as f:

            in_config = False
            config = ''
            file_path = None

            for line in f:

                if '.. begin_mpfdoctest' in line:
                    in_config = True
                    file_path = line.split(':')[1]
                    file_path = file_path[:-1]  # strip off the \n
                    file_path = os.path.join(self._temp_machine_folder,
                                             file_path)

                elif in_config and '::' not in line and line != '\n':

                    if '.. end_mpfdoctest' in line:
                        os.makedirs(os.path.dirname(file_path), exist_ok=True)

                        with open(os.path.abspath(file_path), 'w') as f:
                            f.write(config)

                        in_config = False

                    else:
                        config += line

