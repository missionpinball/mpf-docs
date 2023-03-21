Mission Pinball Framework Documentation (mpf-docs)
==================================================

<img align="right" height="146" src="_static/images/mpf-logo-200.png"/>

This repo is the user documentation for the
[Mission Pinball Framework](http://missionpinball.org).

These docs are static HTML, generated from the files in this repo via the
[Sphinx Python Documentation Generator](https://www.sphinx-doc.org/en/master/) project.

The rendered HTML docs are hosted by [Read the Docs](https://readthedocs.org)
at <http://docs.missionpinball.org>. You can also download PDF and HTML versions from, there.

Building Docs Locally
---------------------

You can build the docs using **Sphinx**. You will first need to install
`Python 3.x`. Then install the packages used by this repo. From the root folder of this repo, run
the following command:

    pip3 install -r requirements.txt

You can view the contents of the [requirements.txt](requirements.txt) file to see which packages will be installed.

### Running Unit Tests

To test that MPF can run all the config snippets in the docs and run the
corresponding unit tests inside the docs (if there is one) type:

    make unit

### Compiling HTML

Compile the docs to `./_build/html/` with the command:

    make html

Licensing
---------

These docs are licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
MPF and all code licensed [MIT](https://opensource.org/licenses/MIT).
