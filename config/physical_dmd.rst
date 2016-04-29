physical_dmd:
=============

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_no.rst

.. overview

The ``physical_dmd:`` section of your config is where you...

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``physical_dmd:`` section of your config. (If you don't include them, the default will be used).

brightness:
~~~~~~~~~~~
Single value, type: ``number`` (will be converted to floating point). Default: ``1.0``

.. todo::
   Add description.

fps:
~~~~
Single value, type: ``integer``. Default: ``0``

.. todo::
   Add description.

luminosity:
~~~~~~~~~~~
List of one (or more) values, each is a type: ``number`` (will be converted to floating point). Default: ``.299, .587, .114``

.. todo::
   Add description.

only_send_changes:
~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

shades:
~~~~~~~
Single value, type: ``integer`` (must be a power of 2. Default: ``16``

.. todo::
   Add description.

source_display:
~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``dmd``

.. todo::
   Add description.


