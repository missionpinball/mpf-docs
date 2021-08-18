blinkenlight_player:
====================

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **YES** |
+----------------------------------------------------------------------------+---------+

.. note:: This section can also be used in a show file in the ``blinkenlights:`` section of a step.

.. overview

The ``blinkenlight_player:`` section of your config is where you add or remove
colors to or from a blinkenlight based on events. It's also used in shows
(via the ``blinkenlights:`` section) to add or remove colors in that show step.

Example from a config file:

.. code-block:: mpf-config

    blinkenlight_player:
      some_event:
        my_blinkenlight1:
          action: add
          color: red
          label: mykey1
      mode_ended:
        my_blinkenlight1:
          action: remove
          label: mykey1    

In the example above, when the event called ``some_event`` is posted,
the color red will be added to my_blinkenlight1's list of colors (this will
cause the light to immediately start flashing if it wasn't already).  The new
color will have the label ``mykey1``.  The label is used like a name of the color,
so that it can be removed later.
When the event ``mode_ended`` is posted, the red color (label ``mykey1``) will be
removed from the blinkenlight.

Example blinkenlight player from a show:

.. code-block:: mpf-config

    ##! show: test
    - time: 0
      blinkenlights:
        my_blinkenlight1:
          action: add
          color: blue
          label: blue_color
        my_blinkenlight2: purple

The first example shows the full config, while the second shows the
"express" config. (What's an "express config?" Details :doc:`here </config/instructions/express_config>`.

The blinkenlight player's express config is the "add" action.  Note that the
express config uses a random label, so there's no way for you to remove this
color with the ``remove`` action if you use this config. However, all colors added
to a blinkenlight by any mode are removed automatically when the mode ends.

See :doc:`/config_players/blinkenlight_player` for details.

.. config


Optional settings
-----------------

The following sections are optional in the ``blinkenlight_player:`` section of
your config. (If you don't include them, the default will be used).

action:
~~~~~~~
Single value, type: one of the following options: add, remove, remove_mode, remove_all.
Default: ``add``

What action the blinkenlight should perform. The ``add`` and ``remove`` actions
require a ``label`` to know which color to add or remove.  The ``remove_all``
action will remove all the colors from the blinkenlight, effectively turning it
off.  The ``remove_mode`` action will remove all the colors that were added by
the mode that the ``remove_mode`` action is coming from (remember that a
blinkenlight can have colors added from lots of different modes -- that's its
whole purpose!).

color:
~~~~~~
Single value, type: ``string``. Default: ``ffffff``

The only action that requires a color setting is the ``add`` action.  It sets
the color to add to this blinkenlight. Color values may be a hex string
(e.g. ``22FFCC``), a list of RGB values (e.g. ``[50, 128, 206]``), a color name
(e.g. ``turquoise``), or a brightness value (i.e. ``AA`` or ``120``).
MPF knows 140+ standard web color names, and you can define your own custom
colors in the :doc:`/config/named_colors` section of your config.
If you use brightness on an RGB light MPF will use the brightness for every
channel.
For instance brigness ``AA`` will result in color ``AAAAAA``.

label:
~~~~~~
Single valid, type: ``string``. Defaults to empty.

You can think of this value as a name for the color you're adding or removing
from the blinkenlight.  If you add a color, then the label allows you to remove
the color later using the label to specify which color to remove.

Related How To guides
---------------------

* :doc:`/config_players/blinkenlight_player`
