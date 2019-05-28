Auditor
=======

.. todo:: :doc:`/about/help_us_to_write_it`

The Mission Pinball Framework contains an auditor that can be used to
create audit logs of switch events, game events, shots made, and
player variables. The exact behavior of what is (and isn't) included
in the audit log is controlled in the Auditor section of your machine
configuration files. Here's a sample audit file:

::

    Events:
     ball_search_begin: 0
     ball_started: 1
     game_ended: 31
     game_started: 41
     machine_init_phase_1: 0
     machine_reset: 29
    Player:
     score:
     average: 15634
     top:
     - 71130
     - 59840
     - 50190
     - 47490
     - 39350
     - 33350
     - 25700
     - 24890
     - 21980
     - 21670
     total: 31
    Shots:
     AirRaidRamp: 3
     DropTarget: 99
     FullRightOrbit: 5
     Inlane: 54
     LeftOrbit: 13
     LeftRamp: 4
     OrangeStandups: 11
     Outlane: 14
     RightRamp: 7
     Slingshot: 105
     WeakRightOrbit: 6
    Switches:
     ShooterLaneL: 20
     alwaysClosed: 0
     buyIn: 0
     captiveBall1: 22
     captiveBall2: 10
     captiveBall3: 2
     centerRampExit: 16
     coin1: 0
     coin2: 0
     coin3: 0
     coin4: 0
     coinDoor: 0
     craneRelease: 0
     down: 0
     dropTargetD: 9
     dropTargetE: 51
     dropTargetG: 45
     dropTargetJ: 38
     dropTargetU: 47
     enter: 98
     esc: 80
     fireL: 0
     fireR: 122
     flipperLwL: 400
     flipperLwL_EOS: 388
     flipperLwR: 440
     flipperLwR_EOS: 434
     flipperUpL: 364
     flipperUpL_EOS: 360
     flipperUpR: 440
     flipperUpR_EOS: 436
     globePosition1: 108
     globePosition2: 108
     inlaneL: 40
     inlaneR: 38
     leftRampEnter: 24
     leftRampExit: 8
     leftRampToLock: 4
     leftRollover: 136
     leftScorePost: 42
     magnetOverRing: 0
     mystery: 8
     outerInlaneR: 30
     outlaneL: 22
     outlaneR: 6
     plumbBob: 0
     popperL: 36
     popperR: 20
     rightRampExit: 14
     rightTopPost: 28
     shooterR: 106
     slamTilt: 0
     slingL: 134
     slingR: 76
     start: 47
     subwayEnter1: 16
     subwayEnter2: 16
     superGame: 0
     threeBankTargets: 22
     ticketDispenser: 0
     topCenterRollover: 24
     topRampExit: 6
     topRightOpto: 36
     trough1: 120
     trough2: 96
     trough3: 96
     trough4: 96
     trough5: 96
     trough6: 74
     troughJam: 76
     up: 0

Note that in the 'Player' section, the auditor will track the average,
the Top 10, and the total numbers of each item. You can configure all
this (including how many of each item it records) in the ``auditor:``
section of the configuration file`.
