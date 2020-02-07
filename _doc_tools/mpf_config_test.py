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
    from mpf.tests.MpfDocTestCase import MpfDocTestCase
except ImportError:
    MpfDocTestCase = None

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

    def test_config(self, config_text, source, use_mc):
        if not MpfDocTestCase:
            raise AssertionError("mpf not loaded")

        if not self.app.config.use_mc and use_mc:
            return

        if use_mc and not MpfIntegrationDocTestCase:
            raise AssertionError("mpf-mc not loaded")

        if use_mc:
            testcase = MpfIntegrationDocTestCase(config_text)
        else:
            if "slides:" in config_text or "widgets:" in config_text or "window:" in config_text or \
                    "displays:" in config_text:
                print("{} should use mpf-mc-config instead of mpf-config because it contains MC elements".format(source))
            testcase = MpfDocTestCase(config_text)
        testcase._testMethodDoc = source
        self.unit_tests.append(testcase)

    def visit_literal_block(self, node):
        if node.attributes.get("language") == "mpf-config":
            self.test_config(node.rawsource, "File: {} Line: {}".format(node.source, node.line), False)
        elif node.attributes.get("language") == "mpf-mc-config":
            self.test_config(node.rawsource, "File: {} Line: {}".format(node.source, node.line), True)

    def unknown_visit(self, node: docutils.nodes.Node) -> None:
        """Called for all other node types."""
        pass



