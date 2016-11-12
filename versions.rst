Understanding MPF versions
==========================

MPF is a work-in-progress and under constant development. The core developers spend about 40 hours a week working on
MPF with multiple fixes and enhancements made every day.

We release a new version of MPF about every 8 weeks. (See the full release history :doc:`here </version_history/index>`).

We are also constantly adding and improving documentation which is available via docs.missionpinball.org. When you
visit the docs website, you can see the version of MPF in the URL, like this:

::

   docs.missionpinball.org/en/<version>

The problem with this is that since the version changes so often, that means that links to certain pages will be
quickly out-of-date since the version number is embedded in the URL.

To combat this, we have a special version link called **latest** which always points to the latest version of MPF.

For example, if the latest version of MPF is **0.31**, that means the "latest" URLs point to 0.31.

You can access other versions of the documentation by clicking on the "Read The Docs" menu in the lower left corner of
any page in the documentation website.

If you view the MPF project on GitHub, you'll notice that there are branches which follow the same naming scheme.
(The "latest" version of the docs points to the "dev" branch in GitHub.)

Sometimes we find bugs that are major enough that we fix them in the current older versions of MPF (instead of just
adding them to the latest version. When we do that, we increment the "patch" number of MPF. For example, when 0.31 is
released, it's actually released as version 0.31.0. Then if we fix a bug, we increment the version to 0.31.1, etc.

We do not maintain separate versions of the documentation for the patch levels. In other words, the documentation for
MPF 0.31 applies to 0.31.0 or 0.31.1 or 0.31.9.

You can see which versions are the latest stable versions at any time by visiting the
`MPF Users Google Group <https://groups.google.com/forum/#!forum/mpf-users>` where we list the latest stable versions
in the header of the page.
