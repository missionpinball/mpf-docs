Contributing code to MPF
========================

If you want to work on the core MPF or MPF-MC code, you have to install MPF and
MPF-MC a bit differently than the normal process.

Why? Because normally when you install MPF and MPF-MC via *pip*, they get
installed as Python packages into your ``Python/Lib/site-packages`` folder, and
that location is not too conducive to editing MPF source code since it's in a
deep random location.

1. Install a git client
-----------------------

2. Clone the MPF and/or MPF-MC repo(s)
--------------------------------------

3. Install MPF / MPF-MC in "developer" mode
-------------------------------------------

4. Make your changes
--------------------

Be sure to add your name to the AUTHORS file in the root of the MPF or MPF-MC
repo!

5. Submit a pull request
------------------------
If your change fixes an open issue, reference that issue number in the comments,
like "fixes #123".
