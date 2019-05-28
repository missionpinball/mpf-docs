Understanding MPF version numbering
===================================

This page explains:

* How version numbering works in MPF, and
* How the MPF documentation versions map to the MPF versions.

MPF is under constant development. The core developers typically spend a combined 40 hours a week working on
MPF with multiple fixes and enhancements made every day. You can see the stream of code "commits" on GitHub,
`here for MPF <https://github.com/missionpinball/mpf/commits/dev>`_ and
`here for MPF-MC <https://github.com/missionpinball/mpf-mc/commits/dev>`_. (Actually we work on the docs a lot too,
check out the latest updates `here <https://github.com/missionpinball/mpf-docs/commits/latest>`_.)

Anyway, we release a new version of MPF about every 6 months. (See the full
release history :doc:`here <release_notes>`).

MPF version numbering follows a standard called `semantic versioning <http://semver.org/>`_ which uses a
"MAJOR.MINOR.PATCH" version number format. For example, the version number ``0.31.8`` is major version 0, minor
version 31, and patch number 8.

.. note::

   Version numbers in MPF are numbers separated by dots which are *not* mathematical decimals. In other words,
   MPF 0.30 is "zero point thirty", which is not the same as "0.3" which is "zero point three". Also, 0.30 is
   27 versions newer than 0.3.

All the MAJOR versions of MPF start with "0" because we have not yet released a 1.0 version yet.

MPF features and configuration files can change between MINOR versions. For example, there were significant changes
between versions 0.21 and 0.30.

The PATCH versions are bug fixes only which do not have functional or config file changes. So 0.30.0, 0.30.1, and 0.30.11
are all the same in terms of documentation and features. (Also 0.30.11 is ten patches newer than 0.30.1.)

You can see which version of MPF you have by adding a ``--version`` option to whatever command you use to launch MPF.
For example:

::

   mpf --version

Since MPF is actually two projects (MPF and MPF-MC), all of this version stuff applies to both of them. (Typically you'll
use the same MAJOR.MINOR versions of both, but the PATCH number might be different. For example, the latest MPF version
might be 0.31.11 while the latest MPF-MC version could be 0.31.8. That's fine.)

You can see which versions are the latest released versions at any time by visiting the
`MPF Users Google Group <https://groups.google.com/forum/#!forum/mpf-users>`_ where we list the latest versions
in the header of the page.

Documentation Versions
----------------------

Since MPF versions are constantly changing, we're also constantly adding and
improving the documentation.

Generally speaking, each documentation set covers multiple MPF versions. You
can see the current version(s) of MPF the documentation you're reading is for
by looking for the version numbers in the blue box in the upper left corner
under the Mission Pinball logo of any page on the documentation site.

If you'd like to access documentation for an older version of MPF, you can
click the "Read the Docs" link in the lower left corner of any page.

If you look in the URL for a page, you'll see the version(s) of MPF that
page is for. Note that there's a special version of the docs called "latest"
which always points to the latest version of the docs. (That way you can
safely link to a page and know that in the future it will always be the most
recent version.)
