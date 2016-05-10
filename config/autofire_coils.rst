autofire_coils:
===============

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_no.rst

.. overview

The *autofire_coils:* section of your config file contains all the
settings for the coils which you would like to fire automatically
based on a switch activationin a pinball machine. (See the Autofire
coils device documentation for the full explanation.)

Here’s an example:

::


    autofire_coils:
        left_sling:
            coil: c_left_sling
            switch: s_left_sling
        right_sling:
            coil: c_right_sling
            switch: s_right_sling

Note that autofire coils in MPF are 1-to-1 in terms of coils-to-
switches, so a single entry is for one switch to control one coil. On
some platforms, you can have two switches control a single coil (or
two coils controlled by a single switch), but to do that you would
create two separate *autofire_coils:* entries with one coil and one
switch each. (And again, that's platform-specific. Check your hardware
platform documentation for details.)

If you're wiring your slingshots and you want two switches to control a single coil, on
nearly 100% of pinball machines in the world, those two switches are
wired together and use a single input, so the hardware sees them as a
single switch. (Just be sure to wire them in parallel, not series, so
that either switch closing causes the hardware to see the switch
activation.) The top-level setting is the name you can refer to this
autofire coil as, such as ``left_sling:`` or ``right_sling:`` in the example
above.

Then each entry has the following required and optional settings:


Required settings
-----------------

The following sections are required in the ``autofire_coils:`` section of your config:

coil:
~~~~~
Single value, type: string name of a ``coils:`` device. 

The name of the coil you want to fire. (Actually, perhaps we should
phrase it as the name of the coil you want to change the state on,
because you can also use these autofire coil rules to cause coils to
stop firing based on a switch change.)

switch:
~~~~~~~
Single value, type: string name of a ``switches:`` device. 




Optional settings
-----------------

The following sections are optional in the ``autofire_coils:`` section of your config. (If you don't include them, the default will be used).

coil_overwrite:
~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``str``. Default: ``None``

.. todo::
   Add description.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Set this to *true* to add lots of logging information about this shot
to the debug log. This is helpful when you’re trying to troubleshoot
problems with this shot.

disable_events:
~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``ball_ending``

Disables this autofire coil by clearing the hardware rule from the
pinball controller hardware.. Default is *ball_ending*.

enable_events:
~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``ball_started``

Enables this autofire coil by writing the hardware rule to the pinball
controller hardware.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

The plain-English name for this device that will show up in operator
menus and trouble reports.

reverse_switch:
~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

Boolean which controls whether this autofire device fires when the
switch is active or inactive. The default behavior is that the coil is
fired when the switch goes to an active state. If you want to reverse
that, so the coil fires when the switch goes to inactive, then set
this to False. (This is what you would use if you have an opto.)
Default is *False*.

switch_overwrite:
~~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``str``. Default: ``None``

.. todo::
   Add description.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

A list of one or more tags that apply to this device. Tags allow you
to access groups of devices by tag name.


