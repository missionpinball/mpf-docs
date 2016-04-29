diverter_(name)_disabling
=========================

*MPF Event*

The diverter called (name) is disabling itself. Note that if this
diverter has ``activation_switches:`` configured, it will not
physically deactivate now, instead deactivating based on switch
hits and timing. Otherwise this diverter will deactivate immediately.


Keyword arguments:
------------------

auto
~~~~
Boolean which indicates whether this diverter disabled itself
automatically for the purpose of routing balls to their proper
location(s).

