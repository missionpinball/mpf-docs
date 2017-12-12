fadecandy:
==========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``fadecandy:`` section of your config is where you...

.. todo::
   :doc:`/about/help_us_to_write_it`

Optional settings
-----------------

The following sections are optional in the ``fadecandy:`` section of your config. (If you don't include them, the default will be used).

dithering:
~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

.. todo::
   :doc:`/about/help_us_to_write_it`

gamma:
~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``2.5``

.. todo::
   :doc:`/about/help_us_to_write_it`

keyframe_interpolation:
~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

.. todo::
   :doc:`/about/help_us_to_write_it`

linear_cutoff:
~~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``0.0``

.. todo::
   :doc:`/about/help_us_to_write_it`

linear_slope:
~~~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

.. todo::
   :doc:`/about/help_us_to_write_it`

whitepoint:
~~~~~~~~~~~
List of one (or more) values, each is a type: ``number`` (will be converted to floating point). Default: ``1.0, 1.0, 1.0``

.. todo::
   :doc:`/about/help_us_to_write_it`

