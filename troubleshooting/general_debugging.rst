How to Turn On Debug and How to Increase Log Verbosity?
=======================================================

You got some kind of issue in MPF?
A crash, weird behaviour or it won't start?
Then this guide is for you.
You will learn how to turn up logging and how to selectively
enable debugging.

1. Run MPF without text ui
--------------------------

The text ui which is shown by default may hide some errors and make
troubleshooting more difficult.
To disable text ui run mpf using:

.. code-block:: console

  $ mpf both -t

This will just show the log on the console.
If some crashes occur this might reveal them as the text ui sometimes hides
them.


2. Start MPF and MPF-MC separately
----------------------------------

If MPF and MPF-MC logs mix up too much you can start them separately:

.. code-block:: console

  $ mpf game -t

And in another console:

.. code-block:: console

  $ mpf mc

This might help you to find out where a crash or error is originating from.


3. Increase Log Verbosity
-------------------------

If you experience problems you should increase verbosity:

.. code-block:: console

  $ mpf game -t -v -V

Start MPF-MC in a separate console:

.. code-block:: console

  $ mpf mc -v -V

(This will also work with ``mpf both -t -v -V``).

Scroll up in the console to find the error which was emitted.

This will increase the size of your logs and slow down MPF a bit.
It should not be used in production but it should be fine to always use
otherwise especially during development.

4. Checkout the Log Folder
--------------------------

MPF will generate separate logs for MPF and MPF-MC in the ``logs`` folder in
your machine.
Those will also contain a bit more information than the console.
Find the issue in your log.
Keep this ready for later in case you want to report an issue.

5. Enable Debugging
-------------------

If you are having an issue with a specific device or platform you should try to
enable debugging.
Almost all devices and platforms in MPF support a ``debug`` option.
If in doubt check the :doc:`config reference </config/index>`.
For instance if you suspect an issue with a switch add ``debug: true`` to it's
config:

.. code-block:: mpf-config

   switches:
     my_switch:
       number: 42
       debug: true

Same works with all devices.
It will generate more log lines but should not affect performance much.

Most platforms support the same.
For instance with a P-Roc:

.. code-block:: mpf-config

   p_roc:
     debug: true

For most platforms this will generate a lot of log lines and might also affect
performance a lot.
We recommend to disable it after you finished debugging.
See :doc:`/hardware/troubleshooting_hardware` for details.

After enable debug check the log again to understand what your device or
platform is actually doing at the time of your issue.
