import os
import unittest

try:
    import kivy     # this is needed for the env hack in the next lines
except ImportError:
    pass

os.environ['KIVY_NO_FILELOG'] = '1'
os.environ['KIVY_NO_CONSOLELOG'] = '1'
os.environ["KIVY_NO_ARGS"] = "1"

try:
    del os.environ["KIVY_DOC"]
    del os.environ["KIVY_DOC_INCLUDE"]
except KeyError:
    pass

import docutils.nodes
import docutils.utils
import logging
try:
    from mpf.tests.MpfDocTestCase import MpfDocTestCase, MpfDocTestCaseNoFakeGame
except ImportError:
    MpfDocTestCase = None
    MpfDocTestCaseNoFakeGame = None

try:
    from mpf.tests.MpfIntegrationDocTestCase import MpfIntegrationDocTestCase
except ImportError:
    MpfIntegrationDocTestCase = None


class ConfigSnippetTester(object):

    def __init__(self):
        self.unit_tests = []

    def add_tests(self, unit_tests):
        self.unit_tests.extend(unit_tests)

    def run_tests(self):
        if self.unit_tests:
            old_level = logging.getLogger().getEffectiveLevel()
            logging.getLogger().setLevel(200)
            suite = unittest.TestSuite()
            suite.addTests(self.unit_tests)
            result = unittest.TextTestRunner(verbosity=1).run(suite)
            logging.getLogger().setLevel(old_level)
            return not result.wasSuccessful()
        else:
            return 0


class CodeBlockVisitor(docutils.nodes.NodeVisitor):

    def __init__(self, document, app):
        super().__init__(document)
        self.app = app
        self.unit_tests = []

    def test_config(self, config_text, source, use_mc, source_file):
        if not MpfDocTestCase:
            raise AssertionError("mpf not loaded")

        if not self.app.config.use_mc and use_mc:
            return

        if use_mc and not MpfIntegrationDocTestCase:
            raise AssertionError("mpf-mc not loaded")

        base_dir = os.path.dirname(os.path.abspath(source_file))
        if use_mc:
            testcase = MpfIntegrationDocTestCase(config_text, base_dir=base_dir)
        else:
            if "slides:" in config_text or "widgets:" in config_text or "\nwindow:" in config_text or \
                    "\ndisplays:" in config_text or "slide_player:" in config_text or "widget_player:" in config_text:
                print("{} should use mpf-mc-config instead of mpf-config because it contains MC elements".format(source))
            if "##! no_fake_game" in config_text:
                testcase = MpfDocTestCaseNoFakeGame(config_text, base_dir=base_dir)
            else:
                testcase = MpfDocTestCase(config_text, base_dir=base_dir)
        testcase._testMethodDoc = source
        self.unit_tests.append(testcase)

    def visit_literal_block(self, node):
        if node.attributes.get("language") == "mpf-config":
            self.test_config(node.rawsource, "File: {} Line: {}".format(node.source, node.line), False, node.source)
        elif node.attributes.get("language") == "mpf-mc-config":
            self.test_config(node.rawsource, "File: {} Line: {}".format(node.source, node.line), True, node.source)

    def unknown_visit(self, node: docutils.nodes.Node) -> None:
        """Called for all other node types."""
        pass



