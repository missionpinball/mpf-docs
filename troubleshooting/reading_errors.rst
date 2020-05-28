Reading MPF Errors
==================

MPF errors might be chained.
This means that a more general error is caused by a more specific one.
In general, you need to read those error from the bottom to the top.
On the bottom there will be the most general error and all errors above
will be more specific.

For instance a Switch might be unable to initialize because your hardware
platform cannot connect to the relevant node board:

.. code-block:: console

   INFO : EventManager : Event: ======'shutdown'====== Args={}
   Shutdown because of an exception:
   ERROR : Machine : Runtime Exception
   Traceback (most recent call last):
     File "/mpf/mpf/devices/switch.py", line 135, in _initialize
       self.config['number'], config, self.config['platform_settings'])
     File "/mpf/mpf/platforms/virtual.py", line 94, in configure_switch
       raise AssertionError("Cannot find board for switch {}".format(number))
   AssertionError: Cannot find board for switch 0-7

   The above exception was the direct cause of the following exception:

   Traceback (most recent call last):
     File "/mpf/mpf/core/machine.py", line 741, in _run_loop
       raise self._exception['exception']
     File "uvloop/cbhandles.pyx", line 70, in uvloop.loop.Handle._run
     File "/mpf/mpf/core/events.py", line 114, in _async_handler_done
       future.result()
     File "/mpf/mpf/core/device_manager.py", line 103, in _load_device_modules
       await self.initialize_devices()
     File "/mpf/mpf/core/device_manager.py", line 199, in initialize_devices
       await collection[device_name].device_added_system_wide()
     File "/mpf/mpf/core/system_wide_device.py", line 15, in device_added_system_wide
       await self._initialize()
     File "/mpf/mpf/devices/switch.py", line 137, in _initialize
       raise AssertionError("Failed to configure switch {} in platform. See error above".format(self.name)) from e
   AssertionError: Failed to configure switch s_door_back in platform. See error above

So in this case the door switch could not be configured because the node board
was missing at the hardware.
