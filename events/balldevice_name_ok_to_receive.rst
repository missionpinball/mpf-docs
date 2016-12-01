balldevice_(name)_ok_to_receive
===============================

*MPF Event*

The ball device (name) now has capicity to receive a ball (or
balls). This event is posted after a device that was full has
successfully ejected and is now able to receive balls.

Keyword arguments
-----------------

(See the :doc:`/events/overview/conditional` guide for details for how to
create entries in your config file that only respond to certain combinations of
the arguments below.)

``balls``
  The number of balls this device can now receive.

