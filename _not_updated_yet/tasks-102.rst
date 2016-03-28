
The Mission Pinball Framework includes a Tasks module (
`mpf/system/tasks.py`) that lets you create, start, sleep, and kill
tasks. This module uses the coroutines design pattern. If you're not
familiar with this, check out David Beazley's excellent tutorial "`A
Curious Course on Coroutines and Concurrency`_." (Actually if you want
to take your Python skills to the next level, `his book is awesome
too`_.) MPF makes heavy use of tasks for the stuff it does internally.
You can use tasks for modes and features you write.

.. _A Curious Course on Coroutines and Concurrency: http://www.dabeaz.com/coroutines/
.. _his book is awesome too: http://www.amazon.com/Python-Essential-Reference-4th-Edition/dp/0672329786/


