hardware:
=========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

The ``hardware:`` section of your machine config file is where you configure
the options for the :doc:`physical hardware controller boards </hardware/index>`
that MPF will use.

If you intend to use MPF with physical hardware, at a minimum you'll have a
``platform:`` and ``driverboards:`` section in your machine config, like this:

.. code-block:: mpf-config

   hardware:
     platform: fast
     driverboards: fast

Primary Platform Settings
-------------------------


platform:
~~~~~~~~~
Single value, type: ``string``. Default: ``smart_virtual``

Specifies the default platform that will be used by all devices in the config.
We say this is the "default" platform, because it's possible to use more than
one platform at time. (Maybe you use a P-ROC for coils and switches and a
FadeCandy for RGB LEDs, etc.) See the :doc:`/hardware/platform` for more
details on this.

Valid platform options include: (Click on them for direct links to the
configuration guide for that platform.)

+ ``p_roc`` :doc:`Multimorphic P-ROC </hardware/multimorphic/index>`
+ ``p3_roc`` :doc:`Multimorphic P3-ROC </hardware/multimorphic/index>`
+ ``fast`` :doc:`FAST Pinball </hardware/fast/index>` (any controller)
+ ``opp`` :doc:`Open Pinball Project </hardware/opp/index>` open source hardware
+ ``spike`` :doc:`Stern SPIKE / SPIKE 2 </hardware/spike/index>`
+ ``smart_virtual`` :doc:`Virtual (software only) </hardware/virtual/smart_virtual>`
  that simulates switch changes based on coil actions.
+ ``virtual`` :doc:`Virtual software-only </hardware/virtual/index>`, with no
  "smart" simulation.

driverboards:
~~~~~~~~~~~~~
Single value, type: ``string``.

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

Device-specific defaults
------------------------

The following optional settings can be used to set default platforms for a
specific class of devices. Note that ``virtual`` and ``smart_virtual`` are
valid options for all of these, though they are not included in the lists
below. Also note that those lists are not exhaustive.

See the :doc:`/hardware/index` section for details of how to use and setup
each of these different types of platforms and hardware.

accelerometers:
~~~~~~~~~~~~~~~
Single value, type: ``string``.

+ ``p3_roc``

coils:
~~~~~~
Single value, type: ``string``. Default: ``default``

+ ``p_roc``
+ ``p3_roc``
+ ``fast``
+ ``opp``
+ ``snux``

dmd:
~~~~
Single value, type: ``string``. Default: ``default``

``p_roc``
``fast``



flashers:
~~~~~~~~~
Single value, type: ``string``. Default: ``default``

+ ``p_roc``
+ ``p3_roc``
+ ``fast``
+ ``opp``
+ ``snux``

gis:
~~~~
Single value, type: ``string``. Default: ``default``

+ ``fast``
+ ``opp``
+ ``p_roc``

i2c:
~~~~
Single value, type: ``string``.

+ ``i2c``

lights:
~~~~~~~
Single value, type: ``string``. Default: ``default``

+ ``p_roc``
+ ``p3_roc``
+ ``fast``
+ ``fadecandy``
+ ``opp``
+ ``openpixel``
+ ``spike``

rgb_dmd:
~~~~~~~~
Single value, type: ``string``. Default: ``default``

+ ``smartmatrix``

servo_controllers:
~~~~~~~~~~~~~~~~~~
Single value, type: ``string``.

+ ``i2c``

switches:
~~~~~~~~~
Single value, type: ``string``. Default: ``default``

+ ``p_roc``
+ ``p3_roc``
+ ``fast``
+ ``opp``
+ ``snux``

