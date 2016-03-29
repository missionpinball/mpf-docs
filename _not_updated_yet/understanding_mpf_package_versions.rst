
Source code for the MPF project is hosted on`GitHub`_. Ifyou look at
the project page, you'll see several branches:


+ The *master* branch is the current up-to-date version of MPF and the
  most stable. It's typically updated every month or two. Versions are
  in the format x.y.z, (such as 0.17.1). The .z number is the latest
  patch / bug fix number and changes there do not introduce any new
  functionality.
+ The * dev * branch is the work-in-progress of the next version of
  MPF. It's typically updated a few times a week. Versions *ahead* of
  master and end in "-dev" plus a revision number. For example, if the
  latest master branch is 0.17.1, the latest dev branch might be
  0.18.0-dev4.
+ The *gh-pages* branch contains the `Sphinx`_-generated `HTML API
  documentation`_ from the `docstrings`_ in the master branch. It
  doesn't contain any MPF code, and the other MPF packages do not
  include any documentation. (Keeping them separate keeps both cleaner.)
+ There might also be other branches at various times which contain
  work-in-progress bug fixes, new features, etc. We work on them there
  in order to keep the master and dev branches somewhat stable.


You can always download the latest stable version of MPF via the
following
link:`https://github.com/missionpinball/mpf/releases/latest`_ You can
think of the MPF package as containing three parts:


+ The MPF game engine.
+ The MPF media controller.
+ Machine-specific configuration files & code.


The * `MPF game engine`_ * contains all the files MPF uses to run,
including the MPF system components, plugins, pinball device drivers,
built-in modes, and a system-wide configuration file. These components
are contained in the */mpf*folder in the MPF package that you
download. The * `MPF media controller`_ * is responsible for all the
display, graphics, video, and audio components of a pinball machine,
including the DMD and LCD display windows. MPF's architecture
separates the game engine from the media controller, so you can
replace the "in-box" MPF media controller with a more advanced one if
you like. (For example, there's a team working on a Unity 3D-based
media controller.) MPF's built-in media controller files live in the
*/mpf/media_controller* folder in the MPF package. The third part of
MPF is your * `machine files`_ *. These are the specific
configurations, code, images, sounds, and videos that make up a single
pinball machine. MPF includes some sample machine configurations in
the */machine_files*folder in the MPF package, with each specific
machine having its own folder under there. (Most likely you'd put your
own machine's files in a folder outside of the MPF folder so you can
download updates of MPF without overwriting your own machine's files.)

.. _https://github.com/missionpinball/mpf/releases/latest: https://github.com/missionpinball/mpf/releases/latest
.. _MPF media controller: https://missionpinball.com/docs/mpf-core-architecture/media-controllers/
.. _Sphinx: http://sphinx-doc.org/
.. _GitHub: https://github.com/missionpinball/mpf
.. _HTML API documentation: /apidocs
.. _machine files: https://missionpinball.com/docs/overview/understanding-the-mpf-package/machine-config-files/
.. _MPF game engine: https://missionpinball.com/docs/mpf-core-architecture/mpf-core-engine/
.. _docstrings: https://www.python.org/dev/peps/pep-0257/


