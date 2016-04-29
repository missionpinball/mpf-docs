credits:
========

*Config file section*

.. include:: _machine_config_yes.rst
.. include:: _mode_config_no.rst

.. overview

The ``credits:`` section of your config is where you...

.. todo::
   Add description.


Optional settings
-----------------

The following sections are optional in the ``credits:`` section of your config. (If you don't include them, the default will be used).

credit_expiration_time:
~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). Default: ``0``

.. todo::
   Add description.

credits_string:
~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``CREDITS``

.. todo::
   Add description.

fractional_credit_expiration_time:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). Default: ``0``

.. todo::
   Add description.

free_play:
~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``yes``

.. todo::
   Add description.

free_play_string:
~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``FREE PLAY``

.. todo::
   Add description.

max_credits:
~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

.. todo::
   Add description.

persist_credits_while_off_time:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string`` (:doc:`Instructions </config/instructions/lists>` for entering time strings). Default: ``1h``

.. todo::
   Add description.

service_credits_switch:
~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``switches:`` device. Default: ``None``

.. todo::
   Add description.


pricing_tiers:
--------------

The ``pricing_tiers:`` section contains the following nested sub-settings

Optional settings
~~~~~~~~~~~~~~~~~

The following sections are optional in the ``pricing_tiers:`` section of your config. (If you don't include them, the default will be used).

credits:
^^^^^^^^
Single value, type: ``integer``. Default: ``1``

.. todo::
   Add description.

price:
^^^^^^
Single value, type: ``number`` (will be converted to floating point). Default: ``.50``

.. todo::
   Add description.


switches:
---------

The ``switches:`` section contains the following nested sub-settings

Optional settings
~~~~~~~~~~~~~~~~~

The following sections are optional in the ``switches:`` section of your config. (If you don't include them, the default will be used).

switch:
^^^^^^^
Single value, type: string name of a ``switches:`` device. Default: ``None``

.. todo::
   Add description.

type:
^^^^^
Single value, type: ``string``. Default: ``money``

.. todo::
   Add description.

value:
^^^^^^
Single value, type: ``number`` (will be converted to floating point). Default: ``0.25``

.. todo::
   Add description.



