
The *driver_enabled:* section of the config files is used to create
`driver-enabled devices`_. This sectioncan be used in your machine-
wide config files. ` `_Some of the settings inthis section can beused
in mode-specific config files. Here's a sample config from Pin*Bot:


::

    
    driver_enabled:
        playfield_devices:
            number: c23


The options are as follows:



<name>:
~~~~~~~

Each subsection of *driver_enabled:* is the name of the device-enabled
device as you’d like to refer to it in your game code. This can really
be anything you want, but it’s obviously best to pick something that
makes sense.



number (and all other settings):
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Driver-enabled devices in MPF are based on the regular driver (coil)
devices, so all other settings for coils also apply here. So number,
tags, etc. are all the same as coils, so you can refer to the
`configuration file reference settings for`_ *coils:* to see how to
configure them.

.. _configuration file reference settings for: https://missionpinball.com/docs/configuration-file-reference/coils/
.. _driver-enabled devices: https://missionpinball.com/docs/mpf-core-architecture/devices/logical-devices/driver-enabled-device/


