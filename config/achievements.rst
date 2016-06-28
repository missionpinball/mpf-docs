achievements:
=============

*Config file section*

.. include:: _machine_config_no.rst
.. include:: _mode_config_yes.rst

.. overview

The ``achievements:`` section of your config is where you configure player-based "achievement"
tracking, which are like progress items that are tracked per player and can automatically
restore states on the next ball.

Like other devices, the top-level entries in the ``achievements:`` section are the achievement
names, and then under each of those, you set specific options for each achievement.

MPF includes defaults for all options, meaning that every achievement setting is optional (though
if you don't set any options, your achievement won't do much.)

Optional settings
-----------------

The following sections are optional in the ``achievements:`` section of your config. (If you don't include them, the default will be used).

complete_events:
~~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

debug:
~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

disable_events:
~~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

enable_events:
~~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

Enables this achievement. (This achievement can only start when it's enabled.)

enable_on_next_ball_when_enabled:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

If a ball ends when this achievement is enabled, should it automatically enable itself again
when the next ball starts?

events_when_completed:
~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

A single event, or a list of events, that should be posted when this achievement is complete.

events_when_disabled:
~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

A single event, or a list of events, that should be posted when this achievement is disabled.

events_when_enabled:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

A single event, or a list of events, that should be posted when this achievement is enabled.

events_when_started:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

A single event, or a list of events, that should be posted when this achievement is started.

events_when_stopped:
~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

A single event, or a list of events, that should be posted when this achievement is stopped.

label:
~~~~~~
Single value, type: ``string``. Default: ``%``

A friendly name for this achievement device.

reset_events:
~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

restart_after_stop_possible:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

Is it possible to restart this achievement after it's been stopped?

restart_on_next_ball_when_started:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``True``

.. todo::
   Add description.

show_tokens:
~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``str``. Default: ``None``

.. todo::
   Add description.

show_when_completed:
~~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Name of the show that will be started when this achievement has been completed.

show_when_disabled:
~~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Name of the show that will be started when this achievement has been disabled.

show_when_enabled:
~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Name of the show that will be started when this achievement has been enabled.

show_when_started:
~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Name of the show that will be started when this achievement has been started.

show_when_stopped:
~~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``None``

Name of the show that will be started when this achievement has been stopped.

start_enabled:
~~~~~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``False``

.. todo::
   Add description.

start_events:
~~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

stop_events:
~~~~~~~~~~~~
One or more sub-entries, each in the format of type: ``str``:``ms``. Default: ``None``

.. todo::
   Add description.

tags:
~~~~~
List of one (or more) values, each is a type: ``string``. Default: ``None``

.. todo::
   Add description.


