#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sphinx-doc config file
import time
import os
import sys
import tempfile
import git
import sphinx_rtd_theme
from pygments.lexers.data import YamlLexer
from sphinx.highlighting import lexers

# for some reason sphinx needs this
sys.setrecursionlimit(2000)

sys.path.append(os.getcwd())
from _doc_tools.mpf_lexer import MpfLexer, ExampleSliderVisitor
from _doc_tools.build_examples import ExampleBuilder
from _doc_tools.mpf_config_test import CodeBlockVisitor, ConfigSnippetTester

extensions = ['sphinx.ext.todo',
              'sphinx.ext.ifconfig',
              'notfound.extension']

source_suffix = '.rst'

master_doc = 'index'

version = '0.54+'  # all versions these docs cover
release = '0.54.x'  # latest release

project = 'Mission Pinball Framework v{} User Documentation'.format(version)
copyright = '2013-%s, The Mission Pinball Framework Team' % time.strftime('%Y')
author = 'The Mission Pinball Framework Team'

# dev warning box will be shown in HTML builds for the following GitHub branch
# names:
branches_for_dev_warning = ['dev']

language = None

exclude_patterns = ['_build',
                    '_not_updated_yet',
                    '_doc_tools',
                    '_src',
                    '_mpf',
                    '_mpf_mc',
                    '_mpf_installer',
                    'mpf_examples',
                    'mpfmc_examples']

pygments_style = 'none'
highlight_language = 'yaml'

todo_include_todos = True

# Tests Links -------------------------------------------------------

mpf_examples = 'mpf_examples'
mpfmc_examples = 'mpfmc_examples'

# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# html_logo = None
html_favicon = '_static/images/icons/favicon.ico'
html_static_path = ['_static']

# html_extra_path = []  # will be copied to root

html_last_updated_fmt = '%b %d, %Y'
htmlhelp_basename = 'MissionPinballFrameworkdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    'preamble': r'''
        \setcounter{secnumdepth}{0}
        \usepackage{bera}
        \usepackage[defaultsans]{lato}
        \usepackage{inconsolata}
        \usepackage{ragged2e}
        \AtBeginDocument{\raggedright}
        \setcounter{tocdepth}{1}
        \pagenumbering{arabic}
        \renewcommand{\labelitemi}{$\bullet$}
        \renewcommand{\labelitemii}{$\bullet$}
        \renewcommand{\labelitemiii}{$\bullet$}
        \renewcommand{\labelitemiv}{$\bullet$}

        \usepackage{fancyhdr}
        \pagestyle{fancy}
        \fancyhf{}
        \rhead{\thepage}
        \lhead{{\leftmark} ({\nouppercase{\rightmark}})}
        \renewcommand{\headrulewidth}{.4pt}

        ''',

    'figure_align': 'H',

    'releasename': 'Version',

    }

# Added "True" at the end to make Layex only use the TOC from index.rst
# and not the other text content
latex_documents = [
    (master_doc, 'MissionPinballFramework.tex',
     'Mission Pinball Framework Documentation',
     'The Mission Pinball Framework Team', 'report', True),
]

# latex_logo = '_static/images/mpf-logo-200.png'  # doesn't work with report class
# latex_use_parts = False
# latex_show_pagerefs = True
# latex_show_urls = 'inline'
# latex_appendices = []
# latex_domain_indices = True

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'missionpinballframework',
     'Mission Pinball Framework Documentation',
     [author], 1)
    ]

man_show_urls = True

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'MissionPinballFramework',
     'Mission Pinball Framework Documentation',
     author, 'MissionPinballFramework', 'Awesome Pinball Software.',
     'Miscellaneous'),
]

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_exclude_files = ['search.html']
epub_tocdepth = 2

# -- Show warnings for dev branches in HTML docs --------------------------

# If this is running on ReadTheDocs.org, the context dict will be overwritten
# by theirs which will contain the propoer branch name (since the git command
# doesn't work there.

context = dict()

try:
    context['github_version'] = git.Repo().active_branch.name
except TypeError:
    context['github_version'] = None


# Test all configs in case the dummy builder is used
unit_test = ConfigSnippetTester()

def process_source(app, doctree, fromdocname):
    # only run on dummy builder
    if app.builder.name != "dummy":
        return

    visitor = CodeBlockVisitor(doctree, app)
    doctree.walk(visitor)
    unit_test.add_tests(visitor.unit_tests)

def run_tests(app, exception):
    # only run on dummy builder
    if exception:
        print(exception)
    if app.builder.name != "dummy":
        return

    result = unit_test.run_tests()
    sys.exit(result)


def annotate_html(app, doctree, fromdocname):
    # only run on html builder
    if app.builder.name not in ("html", "readthedocs"):
        return

    visitor = ExampleSliderVisitor(doctree, app)
    doctree.walk(visitor)


def setup(app):
    app.add_css_file('mpf.css')
    app.add_config_value('use_mc', False, False, [bool])
    app.add_js_file('mpf.js')

    app.connect('doctree-resolved', process_source)
    app.connect('doctree-resolved', annotate_html)
    app.connect('build-finished', run_tests)

    # We need to do this in the setup() function since ReadTheDocs will append
    # the context dict to the end of conf.py which means we don't have the
    # populated value at the global context yet, so we need to do it here.

    if globals()['context']['github_version'] and globals()['context']['github_version'].startswith("origin/"):
        # no idea why there is an origin/ in there. breaks our edit on github links
        globals()['context']['github_version'] = globals()['context']['github_version'][7:]

    if globals()['context']['github_version'] in branches_for_dev_warning:

        globals()['rst_prolog'] = '''
        
        .. only:: html
        
           .. warning::
           
              **This is the dev documentation for an unreleased version of MPF!**
        
              This is the documentation for MPF |version|, which is the "dev" (next)
              release of MPF that is a work-in-progress. Unless you're specifically
              looking for this version, you probably want to use the version of
              documentation called "latest" which is for the latest released version of
              MPF. That documentation is at
              `docs.missionpinball.org/en/latest <http://docs.missionpinball.org/en/latest>`_.
        
        '''

def get_repo_path(repo_name):
    if os.path.isdir(os.path.join(os.getcwd(), os.pardir, repo_name)):
        return os.path.join(os.getcwd(), os.pardir, repo_name)

    elif os.path.isdir(os.path.join(tempfile.gettempdir(), '_src', repo_name)):
        return os.path.join(tempfile.gettempdir(), '_src', repo_name)

    else:
        # clone repo
        print("Cloning {}".format(repo_name))
        current_branch = "dev"
        repo = git.Repo.clone_from("https://github.com/missionpinball/" + repo_name + ".git", os.path.join(tempfile.gettempdir(), '_src', repo_name), branch=current_branch)
        return os.path.join(tempfile.gettempdir(), '_src', repo_name)

def setup_tests_link(link_name, repo_name, package_name):
    try:
        os.unlink(link_name)
    except FileNotFoundError:
        pass

    tests_root = os.path.join(get_repo_path(repo_name), package_name, 'tests', 'machine_files')

    print("Creating '{}' link to {}".format(link_name, tests_root))
    os.symlink(tests_root, link_name)

def build_event_references():
    sys.path.append(get_repo_path("mpf"))
    from _doc_tools.build_events_reference_docs import run
    run(os.path.join(os.getcwd(), "events"), get_repo_path("mpf"), get_repo_path("mpf-mc"))

setup_tests_link(mpf_examples, 'mpf', 'mpf')
setup_tests_link(mpfmc_examples, 'mpf-mc', 'mpfmc')

build_event_references()
source_dirs = {os.path.join(os.getcwd(), "mpf_examples"): "/mpf_examples",
               os.path.join(os.getcwd(), "mpfmc_examples"): "/mpfmc_examples"}
examples_root = os.path.join(os.getcwd(), 'examples')

b = ExampleBuilder(source_dirs, examples_root)
b.build()

lexers['mpf-config'] = MpfLexer(startinline=True)
lexers['mpf-mc-config'] = MpfLexer(startinline=True)
lexers['test'] = YamlLexer(startinline=True)
