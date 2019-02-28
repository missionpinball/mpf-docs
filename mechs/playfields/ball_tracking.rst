How MPF tracks the number of balls on a playfield
=================================================

In MPF, the "playfield" is technically a ball device, just like anything else
that holds a ball (the trough, the plunger lane, a VUK, etc.). Any balls that
are loose and rolling around the playfield can be considered to be "in" the
playfield ball device.

Most ball devices in MPF have either (1) switches that a ball sitting in the
device activates while sitting there (configured as ``ball_switches:`` in MPF),
or (2) a switch that is momentarily activated when a ball rolls over it on its
way in. (Configured as an ``entrance_switch:`` in MPF.)

But a playfield has none of these.

However, there are many switches in a pinball machine which are only hit by
a ball that's on the playfield, and MPF uses these switches to know whether
there's a ball on the playfield.

playfield_active switch tags
----------------------------

In MPF, you add a tag called ``playfield_active`` to the list of tags for every
switch which is hit by a ball that's active on the playfield.

You do this in the ``switches:`` section of your machine config, like this:

.. code-block:: mpf-config

   switches:

      s_trough1:
        number:
      s_trough2:
        number:
      s_plunger_lane:
        number:
      s_standup_1:
        number:
        tags: playfield_active
      s_upper_right_rollover:
        number:
        tags: playfield_active
      s_ramp_enter:
        number:
        tags: playfield_active
      s_ramp_made:
        number:
        tags: playfield_active

Note that not every switch has the ``playfield_active`` tag, rather, it's just
used for the switches that are hit when a ball is on the playfield.

Note that all switches which can be hit by a ball on the playfield are tagged,
even if they're ramp switches since a ball rolling around a ramp is a ball on
the playfield.

Tracking new balls added to the playfield
-----------------------------------------

MPF also uses the playfield_active tags to know whether a ball has successfully
been ejected from a ball device to the playfield.

If a ball device ejects to a playfield that has no balls on it, then the
first time a switch tagged with ``playfield_active`` is hit, MPF knows the ball
successfully made it out of the device and onto the playfield. Ball devices
also have eject timeouts which will be used to confirm that a ball was ejected
to the playfield if the timeout expires and the ball has not fallen back into
the device that ejected it, which is useful since it's possible for the ball
to make it out of the device but then not to hit a switch right away.

The playfield_active tagged switches are only used to confirm a ball ejects to
the playfield if there are no current balls on the playfield when the device
ejects a ball to it. If there is a ball (or multiple balls) on the playfield
when a device ejects a ball to the playfield, then MPF doesn't know whether a
hit to a playfield_active switch is from one of the current balls or the
new ball, so in that case it always falls back to using the eject timeout to
confirm that the ball successfully made it out.

These switches are used for ball search
---------------------------------------

MPF's :doc:`ball search </game_logic/ball_search/index>` functionality uses
the ``playfield_active`` switches to know whether a ball is stuck. (Basically
every activation of one of these switches resets the ball search timer, and if
that timer runs out and the player is not holding in a flipper button, then
the ball search starts.)

So it's important to add the ``playfield_active`` tag to every switch that can
be hit by a ball on the playfield.

Tagging switches with multiple playfields
-----------------------------------------

If you have more than one playfield, then the "playfield_active" switch tag
name should be adjusted to match the name of your actual playfield. For example,
if you have a playfield called "upper_playfield", then the switches which are
hit by a ball on the upper playfield should be tagged ``upper_playfield_active``.
