
The *score_reels:* section in the machine configuration files holds
settings for mechanical score reels forEM-style pinball machines.
Details about how we support mechanical score reels can be found in
the `Score Reel device section`_ of this documentation. This
sectioncan be used in your machine-wide config files. This
sectioncanbe used in mode-specific config files. Here's an example of
two score reel configurations from the config file:


::

    
            score_1p_10k:
                coil_inc: player1_10k
                switch_0: score_1p_10k_0
                switch_9: score_1p_10k_9
                rollover: True
                limit_hi: 9
                limit_lo: 0
                repeat_pulse_time: 200ms
                hw_confirm_time: 300ms
            score_1p_1k:
                coil_inc: player1_1k
                switch_0: score_1p_1k_0
                switch_9: score_1p_1k_9
                rollover: True
                limit_hi: 9
                limit_lo: 0
                repeat_pulse_time: 200ms
                hw_confirm_time: 300ms


Each section is headed with the name you'd like to refer to this score
reel as in your game code. In the above example, the score reels are
named *score_1p_10k*and *score_1p_1k*. It's helpful if you name each
reel in some way that makes sense to you. In this example, you can
infer that these reels are the 10,000s digit and the 1,000s digit from
the Player 1 score reel group. (Note that the names here are
arbitrary.) What's important tounderstand is that these entries make
up the individual movable reels themselves. Then you use the `Score
Reel Group section`_to group multiple individual reels into logical
groups. Specific configuration options for score reels include:



coil_inc:
~~~~~~~~~

The name of the coil that's pulsedto increment the reel. The actual
coil pulse time is specified in the ` *coils:* section`_ of the config
files.



coil_dec:
~~~~~~~~~

The name of the coil that's pulsed to decrement the reel.The actual
coil pulse time is specified in the` *coils:* section`_of the config
files.



switch_ *x*:
~~~~~~~~~~~~

The name of the switch that is active when the reel is in the value of
the "x" in the name. In the example configuration above, *switch_0*is
active when the reel is showing 0, and *switch_9*is active when the
reel is showing 9. All EM reels have switches in the zero position.
Most have switches for 9 also, and some reels have switches for all
the positions to handle replay scores and match features. You must
specify at least one switch, though it doesn't have to be at the zero
position. When the Mission Pinball Framework sets the initial position
of the reels, it will pulse them continuously until it learns of their
positions via the activation of one of these switches. Then it "knows"
(well, "assumes") the position of the reel based on how many pulses it
did since the last position that was confirmed via a switch. It's not
really necessary to have more than one position switch per reel,
though if you do then they provide a certain redundancy since the
machine could still function if one of the switches breaks. It is
definitely not necessary to wire up all ten switches for each reel.
That would be overkill which doesn't really buy you anything, and it
would take forever and waste a lot of switch inputs on your hardware
controller. Note that whether this switch is normally open or normally
closed is specified in that `switch's settings in the machine
configuration files`_. The reel itself only looks for "active" or
"inactive," so if you have a switch that is open when the reel is
inone position and closed for all others, be sure to configure your
switch as "NC" (normally closed).



rollover:
~~~~~~~~~

A value of True or False that indicates whether this reel is capable
of rolling over, that is, whether it can hit its limit and then take
another pulse to roll back over to zero. In typical EM games, the
scoring reels would have their rollover set to True, but the credit
wheel would have a rollover of False.



limit_hi:
~~~~~~~~~

This is the numeric value of highest position on the reel. For scoring
reels it would be 9. For credit reels it's whatever the highest number
is on the reel.



limit_lo:
~~~~~~~~~

This is the lowest number on the reel, in most cases zero.



repeat_pulse_time:
~~~~~~~~~~~~~~~~~~

This is time that the machine will wait between each "pulse" of the
reel. For example, if you set this to *200ms*, and the machine needs
to pulse the reel from 1 to 6, it will fire off 5 pulses all 200ms
apart. Note that this is *not* the same value as the `coil's *pulse
ms*`_. The coil's pulse ms is how many milliseconds that coil is
pulsed for. This *repeat_pulse_ms* is how many milliseconds the
machine waits between pulses. It's important that your
*repeat_pulse_time* is significantly longer (perhaps 2-to-1) than your
coil pulse time so that the coil has enough time to de-energize,
allowingthe reel toratchet into its next position. You can enter
values here in seconds or milliseconds.See the full explanation of the
time duration formats`here`_.



hw_confirm_time:
~~~~~~~~~~~~~~~~

This is the time, in ms, that the machine will wait after a reel coil
pulse before readingthe switches to see what position the reel is in.
The default is 300ms, though you might have to test your machine to
dial-in the exact values. Many reels advance in two steps, with the
initial coil stroke releasing a lever that advances the reel half-way,
and then a ratchet spring that locks the reel in the rest of the way
after the coil de-energizes. This means that if you have a coil pulse
time of 100ms, you have to wait at least 100ms before the reel starts
ratcheting into its new position. Then you have 20-30ms for that
movement to occur, followed by another 100ms or so of "jitter" on the
switch as it bounces around before locking into its final position.
Our experimentation with mid-70s Gottlieb Decagon reels yielded the
best performance with coil pulse times of around 100ms, but in most
cases the position switches didn't settle down until 240-260ms after
that initial pulse. So in our machine we set this *hw_config_ms* to
300ms just to be safe. (You definitely want to err on the side of
caution, since this is the delay before the machine reads the switches
after a reel is fired. If that switch is still jittering and your
machine just happens to read it as its"open" when in fact the reel has
moved, the machine will think the reel didn't advance correctly and
will try to correct it.) You can enter values here in seconds or
milliseconds.See the full explanation of the time duration
formats`here`_.



confirm:
~~~~~~~~

This option lets you specify how you'd like the machine to confirm
that the score reels are in their proper positions. This is necessary
because most individual reels do not switches in every position, so
it's possible that a reel advance could misfire and the reel could be
physically out of sync with where the machine thinks it should be.
This option lets you control what happens in those cases. There are
three options you can choose from:


+ lazy - The default setting of "lazy" means that the machine does not
  check the value of the reelas it's advancing them, but after the reel
  group stops advancing, the machine will check to make sure the
  hardware switches make sense with where it thinks the reel should be,
  and it will reset them if they're not right. It's important to
  understand that the machine doesn't always know every position each
  reel is in. For example, if your score reels only have switches in the
  9 and 0 positions and your player's score is 782, then all the machine
  can do is make sure that each reel is *not* in the 9 or 0 position.
  But really it doesn't know if the score reel group is showing 782 or
  682 or 222—all it knows is that a 9 or 0 is either showing or not.
  However, if the machine thinks the score reel group should be
  displaying 782, but it sees that the onesdigit reel has the 0 position
  switch active, then it will advance the ones reel twice to move it to
  what it assumes is the 2 position. The same will happen if the machine
  wants the score to be 780 but it does not see an active 0 switch for
  the ones. In that case it will advance the ones reel until the zero
  switch is active.
+ strict - In "strict" mode the machine will check to make sure the
  switches are in the proper positions after *every single pulse*. The
  upside to this is that your score reels have a better chance of always
  being right, but the downside is that you slow down the speed your
  reels operate at. (In strictmode, the fastest a reel can be advanced
  is based on the value of the reel's *hw_confirm_ms*setting which might
  be something like 300ms, whereas in *lazy* or *none* mode it can
  advance the reels at their *repeat_pulse_ms* time which might be
  around 200ms.
+ none - In "none" mode, the machine will never check the status of
  the reels (after the initial positioning to find an active switch when
  the machine is reset). At first you might think this is a horrible
  idea, but really it's how classic EMs have worked all these years.
  (When "none"is used, the machine will still use each reels' switches
  when it resets them to a new position, such as when the game
  restarts.) Also keep in mind that even if "none" is used, the machine
  still knows what each players actual correct score is—regardless of
  what's displayed on the reels.




Device Control Events
---------------------

None.



Settings that apply to all device types
---------------------------------------

There are some settings that apply to all types of devices that also
apply here.



tags:
~~~~~

A list of one or more tags that apply to this device. Tags allow you
to access groups of devices by tag name.



label:
~~~~~~

The plain-English name for this device that will show up in operator
menus and trouble reports.



debug:
~~~~~~

Set this to *true* to add lots of logging information about this shot
to the debug log. This is helpful when you’re trying to troubleshoot
problems with this shot. Default is *False*.

.. _pulse ms: /docs/configuration-file-reference/coils/
.. _switch's settings in the machine configuration files: /docs/configuration-file-reference/switches/
.. _Score Reel Group section: /docs/configuration-file-reference/mechs/score-reel-groups/
.. _Score Reel device section: https://missionpinball.com/docs/mpf-core-architecture/mechs/logical-mechs/score-reel/
.. _here: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/entering-time-duration-values/


