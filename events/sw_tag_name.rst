sw_(tag_name) (MPF event)
=========================

A switch tagged with *tag_name* was just activated.

For example, if in the ``switches:`` section of your config, you
have a switch with ``tags: start, hello``, then the events
*sw_start* and *sw_hello* will be posted when that switch is hit.

Note that you can change the format of these events in your
machine config file, but *sw_(tag_name)* is the default.


Keyword arguments: None
