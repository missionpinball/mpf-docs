Debugging Segfaults
===================

If you experience a crash/segfault or hang (especially in MC) you can run
`gdb on python <https://wiki.python.org/moin/DebuggingWithGdb>`_ to find the
crash or hang.
You can attach a debugger to the running mc process like this:

.. code-block:: console

  $ ps aux | grep mpf
  jan       9678 12.4  0.3 1082068 127304 pts/2  SNl+ 23:17   0:06 /usr/bin/python3 /usr/local/bin/mpf mc
  jan       9760 37.0  0.1 571368 56660 pts/3    Sl+  23:17   0:01 /usr/bin/python3 /usr/local/bin/mpf game -X

In this example ``9678`` is the pid of MC and ``9760`` is the pid of MPF.
You can then attach gdb:

.. code-block:: console

  $ sudo gdb python3 9678
  [...]
  (gdb) thread apply all bt
  [...]
  (gdb) thread apply all py-bt
  [...]

Please send us the complete output of gdb.
That will help us to figure out the problem.
