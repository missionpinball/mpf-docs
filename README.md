Mission Pinball Framework Documentation (mpf-docs)
==================================================

<img align="right" height="146" src="_static/images/mpf-logo-200.png"/>

This repo is the documentation for the
[Mission Pinball Framework](http://missionpinball.org).

Docs are hosted by Read the Docs at <http://docs.missionpinball.org>.
You can download PDF, HTML, and Epub versions.

The "latest" branch of these docs corresponds to the latest released branch
recent version of MPF. (We note which features have been added, changed,
and removed as needed.)


Building Docs Locally
---------------------

You can build the docs using **Sphinx**. You will first need to install
`Python 3.x` and `pip`. Then add these libraries:

    pip install sphinx
    pip install gitpython
    pip install sphinx_rtd_theme
    pip install sphinx-notfound-page
    pip install ruamel.yaml==0.15.100

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
