Understanding MPF version numbering
===================================

This document explains how version numbering works in MPF.

MPF is a work-in-progress and under constant development. The core developers spend about 40 hours a week working on
MPF with multiple fixes and enhancements made every day.

We release a new version of MPF about every 8 weeks. (See the full release history :doc:`here <history>`).

MPF versions follow a standard called `semantic versioning <http://semver.org/>`_ which uses a MAJOR.MINOR.PATCH version
number format. For example, the version number ``0.31.8`` is major version 0, minor version 31, and patch number 8.

.. note::

   Version numbers in MPF are numeric, not mathematical decimals. In other words, MPF 0.30.0 is "zero point thirty",
   which is not the same as "0.3.0" which is "zero point three". Also, 0.30.0 is 27 versions newer than 0.3.0.

All the MAJOR versions of MPF start with "0" because we have not yet released a "1." version.

MPF features and configuration files can change between MINOR versions, meaning there could be changed between (for
example) MPF 0.30.x and 0.31.x.

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
`MPF Users Google Group <https://groups.google.com/forum/#!forum/mpf-users>` where we list the latest versions
in the header of the page.
