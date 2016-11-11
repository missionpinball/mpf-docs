Understanding MPF versions
==========================

MPF is a work-in-progress and under constant development. The core developers spend about 40 hours a week working on
MPF with multiple fixes and enhancements made every day.

We release a new version of MPF about every 8 weeks. (See the full release history :doc:`here <history>`).

We are also constantly adding and improving documentation which is available via docs.missionpinball.org. When you
visit the docs website, you can see the version of MPF in the URL, like this:

::

   docs.missionpinball.org/en/<version>

The problem with this is that since the version changes so often, that means that links to certain pages will be
quickly out-of-date since the version number is embedded in the URL.

To combat this, we have a special version link called **stable** which always points to the latest released (e.g.
"stable") version of MPF.

The current release of MPF is **0.31** which means that the "stable" URLs point to 0.31. In other words, the following
two URLs actually point to the same page:

::

   docs.missionpinball.org/en/stable
   docs.missionpinball.org/en/0.31

All of the daily changes that we make to MPF get added to the "dev" version of MPF, which is essentially the codename
for the next version.

Since the current stable (released) version of MPF is 0.31, the current dev (next release) of MPF is 0.32. When we
release 0.32, then the "stable" links will point to the 0.32 version of MPF, and the "dev" links will then point to 0.33.

You can access other versions (including prior versions, the current stable version, and the next dev version) of the
documentation by clicking on the "Read The Docs" menu in the lower left corner of any page in the documentation website.

If you view the MPF project on GitHub, you'll notice that there are branches which follow the same naming scheme. (e.g.
there's a 0.30 branch, a 0.31 branch, and a "dev" branch which is the next version we're working on.)

Sometimes we find bugs that are major enough that we fix them in the current (stable) version of MPF (instead of just
adding them to the dev version to be released in the future. When we do that, we increment the "patch" number of MPF.
For example, when 0.31 is released, it's actually released as version 0.31.0. Then if we fix a bug, we increment the
version to 0.31.1, etc.

We do not maintain separate versions of the documentation for the patch levels. In other words, the documentation for
MPF 0.31 applies to 0.31.0 or 0.31.1 or 0.31.9.

You can see which versions are the latest stable versions at any time by visiting the
`MPF Users Google Group <https://groups.google.com/forum/#!forum/mpf-users>` where we list the latest stable versions
in the header of the page.
