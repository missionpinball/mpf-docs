achievement_(name)_state_(state)
================================

*MPF Event*

Achievement (name) changed to state (state).

Valid states are: disabled, enabled, started, completed

This is only posted once per state. Its also posted on restart on the next ball to restore state.

Keyword arguments
-----------------

(See the :doc:`/events/overview/conditional` guide for details for how to
create entries in your config file that only respond to certain combinations of
the arguments below.)

``restore``
  true if this is reposted to restore state

