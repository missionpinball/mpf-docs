Contributing to MPF
===================

Want to add a feature? A missing event somewhere? Wrote a new device which
might be useful for other users? Fixed a bug? Added some small missing piece?

We'd love to take your contribution upstream!

Found a bug which you can reproduce? Fill an issue:

* `MPF Issues on github <https://github.com/missionpinball/mpf/issues>`_. Use
  this for game and platform related bugs
* `MPF-MC Issues on github <https://github.com/missionpinball/mpf-mc/issues>`_. Use
  this for media controller bugs such as problems with slides, widgets or
  audio.

If you want to discuss a feature or bug (or if you are unsure). Visit our
forum: https://groups.google.com/forum/#!forum/mpf-users


Install MPF in development mode
-------------------------------

To work on MPF you need to install it in developer/editable mode:

#. Fork the `mpf repo <https://github.com/missionpinball/mpf/>`_ on GitHub.  Do this by clicking on the Fork button in the top right corner.
#. Fork the `mpf-mc repo <https://github.com/missionpinball/mpf-mc/>`_ on GitHub
   (only needed for media controller changes - skip otherwise).  Do this by clicking on the Fork button in the top right corner.
#. Clone your fork of the mpf repo to your local machine.  Determine the folder where you want this to reside.  Consider using a different
   folder than where your personal MPF code resides. Then run the following command:
   (``git clone https://github.com/YOUR_GITHUB_HANDLE/mpf/``)
#. Install MPF dependencies if you did not install mpf before. On linux you can
   run our installer `https://raw.githubusercontent.com/missionpinball/mpf-debian-installer/dev/install-mpf-dependencies`.
   On other platforms check the :doc:`installation instructions </install/index>` instructions.
#. Navigate to your folder where you ran the command in the earlier step to clone git to your local machine.  From that folder run:
   ``pip3 install -e .`` to install MPF in editable mode.
#. Clone your fork of the mpf-mc repo to your local machine (``git clone https://github.com/YOUR_GITHUB_HANDLE/mpf-mc/``;
   only needed for media controller changes - skip otherwise).  This should be located in the same folder as where you ran this function for
   MPF earlier
#. Install MPF-MC dependencies if you did not install mpf-mc before. On linux
   you can run our installer `https://raw.githubusercontent.com/missionpinball/mpf-debian-installer/dev/install-mc-dependencies`.
   On other platforms check the :doc:`installation instructions </install/index>` instructions.
#. Navigate to your folder where you ran the command in the earlier step to clone git to your local machine.  From that folder run:
   ``pip3 install -e .`` from within the mpf-mc folder to install MPF MC in editable mode (only needed for media controller changes
   - skip otherwise and just run ``pip3 install mpf-mc --pre``).
#. Switch both repositories to the branch corresponding to the version you want
   to work with. This should be ``dev`` in most cases or the current release
   for smaller bug fixed. Do what works best for you. We can help to forward or
   backport your changes.
#. From your MPF folder that is connected with git, create a local branch to work on (``git checkout -b your_feature_name``).
#. Make your changes.
#. Add your name to the ``AUTHORS`` file.
#. If possible add an unit test. We can help with that and a first Pull Request
   without a test is definitely fine.
#. Run ``python3 -m unittest discover -s mpf.tests`` and check that all tests
   still pass. You achieve the same for mpf-mc with ``python3 -m unittest discover -s mpfmc.tests``.
   If you get an error message that Python was not found, try running the following command: ``python -m unittest discover -s mpfmc.tests``.
   This is the same basic command, but runs on python instead of python3.
#. Commit your changes (``git commit -a``)
#. In the git commit screen type your title on line 1.  Leave a blank line, and then type out the description of what is included in this
   commit.  Once you are done typing your commit notes, press escape.  This will bring your cursor to the bottom of this panel.  From there
   type ('':wq'') and press Enter.  This will complete your commit notes.
#. Push your changes to your github (``git push origin your_feature_name``).
#. Open up your Fork on github and create and submit your pull request to merge from your local back to MPF.

We recommend you to use a decent IDE because it makes life easier.
Most of the MPF developers use PyCharm but other IDEs will work as well.


Getting started with an open issue
----------------------------------

We maintain a list of issues which are self-contained and good to solve on
their own without too much interaction with core code. We label those as 
`help wanted <https://github.com/missionpinball/mpf/labels/help%20wanted>`_
(although they do not have to be easy, just self-containted). If you want
to work on one of them (or any other issue) comment on the issue or write
in the forum and we will assist you along the way.
