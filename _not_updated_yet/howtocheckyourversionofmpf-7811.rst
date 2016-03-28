
Since MPF is a work-in-progress, things can change from version-to-
version. You can check which version of MPF you have from the command
line. To do this, run the following command from your MPF folder:


::

    
    python mpf.py --version


It should print something like this:


::

    
    Z:\mpf>python mpf.py --version
    MPF v0.21.3 (config_version=3, BCP v1.0)
    
    Z:\mpf>


The main thing you're looking for is what's after the "MPF" in the
results it prints. (The example above is MPF version 0.21.3.) The
first two sections of that number are the major & minor release
numbers. (0.21 in this example.) Those are the important numbers. The
last section is the patch number which we update if we find major bugs
that can't wait until the next release. The patch version doesn't
really matter, so if we say you need MPF version 0.21 then it doesn't
matter if you have 0.21.0 or 0.21.1 or 0.21.7 or whatever. You can
also see (and download) the most recent version
here:`https://github.com/missionpinball/mpf/releases/latest`_

.. _https://github.com/missionpinball/mpf/releases/latest: https://github.com/missionpinball/mpf/releases/latest


