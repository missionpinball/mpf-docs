Contributing to MPF's Documentation
===================================

Want to help make these docs better! Great! We'd love any help, whether it's as
small as correcting a typo, adding to a section that isn't clear, adding your
own How To guide, or whatever else you want to change.

How does the layout work?
-------------------------

The documentation uses reStructuredText (rst).
You can read about possible elements in the `rst documentation <http://www.sphinx-doc.org/en/stable/rest.html>`_.

Some excempts from the documentation above:

A list of item:

    * element 1
    * element 2

Looks like:

* element 1
* element 2

Highlighted yaml:

    .. code-block:: yaml

      element:
        subelement: value

Looks like:

.. code-block:: yaml

  element:
    subelement: value


To make a quick change to an existing page
------------------------------------------

Quick changes to existing pages can be done right on the web!

To do that:

#. Browse to the page you want to update, and click the "Edit on
   GitHub" link in the upper right corner of the page.
#. Click the pencil icon in the upper-right corner of the page's text. (If
   this is grayed out, that means you need to create a GitHub account and/or
   login.) This will create a fork of mpf-docs in your GitHub account.
#. Make your change, and click the "Propose file change". This will create a
   pull request. Type a name describing your change, and click "Create pull
   request".
#.  Details and screen shots of this entire process are `here <https://help.github.com/articles/editing-files-in-another-user-s-repository/>`_.

To make a suggestion for a new doc (or to point out an error)
-------------------------------------------------------------

Even if you don't feel comfortable actually changing or editing docs, you can
still tell us about an error in the documentation or suggest new
documentation that we should add. To do this:

#. Go to the `"Issues" page of the mpf-docs repository on GitHub <https://github.com/missionpinball/mpf-docs/issues>`_.
#. Create a GitHub account if you don't have one, and/or login.
#. Click the "New Issue" button and describe what you'd like us to fix or add!

To clone the mpf-docs repo locally to make bigger changes
---------------------------------------------------------

If you want to make bigger changes to the docs, or if you want to download the
mpf-docs repo so you can work on it offline, do the following:

#. Clone the `mpf-docs repo <https://github.com/missionpinball/mpf-docs/>`_
   from GitHub.
#. Switch to the branch corresponding to the version of the docs you want to
   work with (usually *dev* or *latest*).
#. Makes your changes.
#. Add your name to the ``/authors/index.rst`` doc.
#. To test the docs locally, you'll need *sphinx* and *sphinx_bootstrap_theme*,
   both of which you can install via *pip*.
#. Run ``make html`` to ensure everything builds properly without any
   additional warnings from whatever docs you added or changed. (The built docs
   will be in the ``_build/html`` folder. You can open *index.html* in your
   local browser to preview your changes.
#. Submit your pull request.
