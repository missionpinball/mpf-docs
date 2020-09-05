Troubleshooting
===============

Your machine is not starting, behaving weird or crashing?
We are sorry to hear that.
This chapter tries to help you to help yourself.
Please try to find the root of your problem.
Maybe the solution will be obvious then.
If not we will help you in the forum.

Please remember that this is a two step process:
First, try to diagnose the problem and collect as much information as possible.
Second, report the issue if you cannot find a solution yourself.
If you skip the first step we will likely send you to this page.

Step 1: Diagnosing Your Issue
------------------------------


Do you already know
:doc:`how to turn on debugging and increase log verbosity <general_debugging>`?


What kind of issue are you having?

.. toctree::
   :maxdepth: 1

   debugging_memory_leaks
   debugging_yaml_parse_errors
   debugging_segfaults
   debugging_mpf_install


If you coils are not firing, switches are not working or hardware is behaving
weirdly in general read our
:doc:`hardware troubleshooting guide </hardware/troubleshooting_hardware>`.

Step 2: Prepare a Report and Ask in the Forum
---------------------------------------------

Please include the following information if available and relevant:

Output of MPF diagnosis
~~~~~~~~~~~~~~~~~~~~~~~

If your game won't run, let's make sure MPF is ok.
This will also tell use which MPF and MPF-MC version you are using.
Run ``mpf diagnosis`` from within your machine folder to see if your installation is fine:

.. code-block:: console

  $ mpf diagnosis


  MPF version: MPF v0.50.0-dev.11
  MPF install location: /data/home/jan/cloud/flipper/src/mpf/mpf
  Machine folder detected: /data/home/jan/cloud/flipper/src/good_vs_evil
  MPF-MC version: MPF-MC v0.50.0-dev.5 (config_version=5, BCP v1.1, Requires MPF v0.50.0-dev.10)

  Serial ports found:
  /dev/ttyUSB3
      desc: Quad RS232-HS
      hwid: USB VID:PID=0403:6011 LOCATION=1-12
  /dev/ttyUSB2
      desc: Quad RS232-HS
      hwid: USB VID:PID=0403:6011 LOCATION=1-12
  /dev/ttyUSB1
      desc: Quad RS232-HS
      hwid: USB VID:PID=0403:6011 LOCATION=1-12
  /dev/ttyUSB0
      desc: Quad RS232-HS
      hwid: USB VID:PID=0403:6011 LOCATION=1-12

Relevant Configuration
----------------------

Please provide the relevant configuration snippets.
Leave out anything which is not related.
For instance if you got problems with lights on your P-Roc or FAST platform
provide the configuration for the relevant lights, the ``p_roc`` or ``fast``
section and any light_players or shows which are used when the problem occurs.

Attach a Log with debug and verbose logging
-------------------------------------------

Please attach the log with verbose logging from MPF or MPF-MC (depending where
your problem occured).
Make sure you enabled ``debug`` on the relevant devices and/or platforms.
See :doc:`how to turn on debugging and increase log verbosity <general_debugging>`
for details.

A link to your machine config also help.
Ideally this would be some git repository which can be checked out and browsed
online.

Prepare the Error Message
--------------------------

Your error message likely is inside your log.
However, please include it inside your message as well.
See :doc:`reading_errors` for how to read the error.

Please check the relevant device or platform documentation for any mentions of
that error.
Often we already documented how to solve it.

Tell Us How to Reproduce Your Problem
-------------------------------------

It might be hard for us to help you if we cannot reproduce your issue.
Is there a way you can provide a minimal config which shows your problem?
Try to remove everything unrelated to your problem and bring it to its bare
minimum.
Sometimes you will find the root of the issue while doing this.
You would be surprised how often issues are caused by seemingly unrelated
devices or configs.

Ideally you can provide a :doc:`single file test </tools/test/index>` which
fails or shows your issue in its log.
This allows us to verify the issue quickly and provide a quick fix.
But don't worry if this not possible.
Just a minimal machine config is also fine.
In that case please tell us how to run your machine to experience the issue.

Ask In the Forum
----------------

With all this information ask in our `support forum <https://groups.google.com/forum/#!forum/mpf-users>`_.
Please keep in mind that MPF is an open source project and we are doing this
for fun in our spare time.
Be kind and patient.
If you provide more relevant information it is likely that somebody can help you.
More is not always better if it is not relevant to your problem.
But missing information will just delay the overall process.

#. If you got a problem with a device (e.g. a ball_lock) or a platform
   (e.g. P-ROC or FAST) add ``debug: True`` to the relevant config section to
   enable extra debug output.
#. Add a log of your game. Therefore, run your game with ``mpf both -v -V`` and
   grab the latest MPF and MC log from the log folder in your machine.
#. Describe how to reproduce your problem.
#. Provide relevant config snippets or, if possible, a link to
   download/checkout your machine config so we can reproduce the issue.


Consider Improving the Documentation
------------------------------------

Did you solve your issue but found that some relevant information in the
documentation is missing or should be linked/located elsewhere?
Either tell us in the forum or consider
:doc:`improving the documentation </about/contributing_to_mpf_docs>`
yourself to save future users some troubles the same way others saved you
some troubles by writing this documentation.


More Howtos
-----------

.. toctree::
   :maxdepth: 1

   General Debugging <general_debugging>
   reading_errors
