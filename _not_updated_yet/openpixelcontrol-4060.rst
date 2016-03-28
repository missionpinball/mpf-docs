
You can use the `open_pixel_control:` section of your machine config
file to control settings for MPF LED hardware connections that use the
Open Pixel Control (OPC) protocol (such as the `FadeCandy`_). This
sectioncan be used in your machine-wide config files. This section
*cannot* be used in mode-specific config files. Here's the
`open_pixel_control:` section of the `mpfdefault.yaml` configuration
file. You don't need to add these to your own config files unless you
want to override any of these defaults.


::

    
    open_pixel_control:
      host: localhost
      port: 7890
      connection_required: no
      connection_attempts: -1
      number_format: int




host:
~~~~~

The host name of the OPC server MPF will connect to. This is almost
always *localhost* since in most cases, the OPC server is running as a
separate process on the computer running MPF.



port:
~~~~~

The TCP port the OPC server is listening on.



connection_required:
~~~~~~~~~~~~~~~~~~~~

Boolean yes/no true/false which controls whether MPF needs a
connection to the OPC server to run. If you enable this, then if MPF
boots and can't connect to the OPC server, MPF will exit. Also if it's
enabled and MPF does connect but then it looses its connection, MPF
will exit.



connection_attempts:
~~~~~~~~~~~~~~~~~~~~

The number of attempts MPF will make to try to connect to the OPC
server. A value of 0 or less (such as the -1 default) means
"unlimited" and MPF will continuously try to connect in the
background. (The OPC client built into MPF runs as a separate thread,
so it's able to keep trying toreconnect in the background without
affecting performance.)



number_format:
~~~~~~~~~~~~~~

Specifies whether the numbers for your Open Pixel LEDsin your config
file are hex or integer format. (Use the values `hex` or `int`.)

.. _FadeCandy: http://www.adafruit.com/products/1689


