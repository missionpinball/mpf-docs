Run Single File Tests
=====================

The command line ``mpf test`` can run single file tests or doc pages.

You can create a text file which contains the main config, shows and modes of
your test machine.
Then at the bottom you can create some test assertions.

The structure look like this:

.. code-block:: yaml

   # your machine-wide config here. That is what is normally in config/config.yaml.

   # you can have a few modes
   ##! mode: some_mode
   # mode config here

   # you can have a few modes
   ##! mode: another_mode
   # mode config here

   # additionally you can have separate shows
   ##! show: some_show
   # show here

   # now you can add a test
   ##! test
   #! start_game
   # run the machine for 1 virtual second
   #! advance_time_and_run 1
   # post an event
   #! post some_event


All test assertions are defined in
`MpfDocTestCase <https://github.com/missionpinball/mpf/blob/dev/mpf/tests/MpfDocTestCase.py>`_.
Just remove the ``command_`` prefix and you are good to go.
