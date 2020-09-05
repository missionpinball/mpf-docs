hardware:
=========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``hardware:`` section of your machine config file is where you configure
the options for the :doc:`physical hardware controller boards </hardware/index>`
that MPF will use.

If you intend to use MPF with physical hardware, at a minimum you'll have a
``platform:`` and ``driverboards:`` section in your machine config, like this:

.. code-block:: mpf-config

   hardware:
     platform: fast
     driverboards: fast


Device-specific defaults
------------------------

The following optional settings can be used to set default platforms for a
specific class of devices. Note that ``virtual`` and ``smart_virtual`` are
valid options for all of these, though they are not included in the lists
below. Also note that those lists are not exhaustive.

.. note::

  The list of platforms is incomplete here.
  See the :doc:`/hardware/index` for details which platforms are supported
  by MPF.

.. config


Optional settings
-----------------

The following sections are optional in the ``hardware:`` section of your config. (If you don't include them, the default will be used).

accelerometers:
~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``default``

See :doc:`/hardware/dmd_platforms` for supported platforms.

coils:
~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``default``

For instance:

+ ``p_roc``
+ ``p3_roc``
+ ``fast``
+ ``opp``
+ ``apc``
+ ``snux``

Almost all platforms in :doc:`/hardware/index` are supported here.

dmd:
~~~~
List of one (or more) values, each is a type: ``string``. Default: ``default``

See :doc:`/hardware/dmd_platforms` for supported platforms.

driverboards:
~~~~~~~~~~~~~
Single value, type: ``string``. Defaults to empty.

Specifies the default type of driver boards you're using. If you have a home
brew machine, this will probably match your platform. If you're using an
existing machine, then this will be whatever type of driverboard is installed
in the machine.

+ ``pdb`` P-ROC Driver Boards, PD-16, PD-8x8, etc.)
+ ``fast`` FAST IO boards (0804, 1616, 3208, etc.)
+ ``opp`` OPP wing boards
+ ``wpc95`` Williams WPC-95
+ ``wpc`` Williams WPC
+ ``wpcAlphaNumeric`` Williams WPC with alphanumeric 14-pin connected segmented
  display
+ ``sternSAM`` Stern SAM
+ ``sternWhitestar`` Stern Whitestar

hardware_sound_system:
~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``default``

See :doc:`/hardware/index` for supported platforms.

i2c:
~~~~
List of one (or more) values, each is a type: ``string``. Default: ``default``

See :doc:`/hardware/i2c_platforms` for supported platforms.

lights:
~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``default``

Almost all platforms in :doc:`/hardware/index` are supported here.

platform:
~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``virtual``

Specifies the default platform that will be used by all devices in the config.
We say this is the "default" platform, because it's possible to use more than
one platform at time. (Maybe you use a P-ROC for coils and switches and a
FadeCandy for RGB LEDs, etc.) See the :doc:`/hardware/platform` for more
details on this.

See :doc:`/hardware/index` for a complete list.

rgb_dmd:
~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``default``

See :doc:`/hardware/dmd_platforms` for supported platforms.

segment_displays:
~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``default``

See :doc:`/hardware/segment_display_platforms` for supported platforms.

servo_controllers:
~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``default``

See :doc:`/hardware/servo_platforms` for supported platforms.

stepper_controllers:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``default``

See :doc:`/hardware/stepper_platforms` for supported platforms.

switches:
~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``default``

Almost all platforms in :doc:`/hardware/index` are supported here.


Related How To guides
---------------------

* :doc:`/hardware/index`
