import unittest

import docutils.nodes
import docutils.parsers.rst
import docutils.utils
import logging
from mpf.tests.MpfDocTestCase import MpfDocTestCase


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

    def __init__(self, document):
        super().__init__(document)
        self.unit_tests = []

    def test_config(self, config_text, source):
        testcase = MpfDocTestCase(config_text)
        testcase._testMethodDoc = source
        self.unit_tests.append(testcase)

    def visit_literal_block(self, node):
        if node.attributes.get("language") == "mpf-config":
            self.test_config(node.rawsource, "File: {} Line: {}".format(node.source, node.line))

    def unknown_visit(self, node: docutils.nodes.Node) -> None:
        """Called for all other node types."""
        pass



