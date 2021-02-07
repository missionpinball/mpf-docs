Service Mode
============

**Service Mode** is an important part of a pinball machine that provides an interface that allows the user to perform a number of important operations to their machine.  MPF provides a comprehensive base set of service mode features, that can be extended if required.

The structure of the built-in Service Mode is as follows:
image:: MPF-ServiceMode-Structure.png  

Utilities
---------
MPF provides a **Reset** function that allows you to provide a set of standard functions to the user to reset certain elements of the game, such as High Scores, Audits and Earnings.  This menu option is available from the ``service_menu_selected`` event with the label ``Utilities Menu``.

Utilities has the following sub menus:

Coin Audits
~~~~~~~~~~~
Resets all counters for earnings data.  All counters will be reset to zero in ``earnings.yaml`` in the ``/data`` subfolder of your game. 

Factory Reset
~~~~~~~~~~~~~
Resets the value of all of your machine variables in your ``machine_vars.yaml`` file in the ``/data`` subfolder of your game to the ``initial_value`` if the ``persist: true`` setting is configured for that variable.  

Credits
~~~~~~~
Resets the value of the ``credit_units`` machine variable in your ``machine_vars.yaml`` file in the ``/data`` subfolder of your game to zero.

High Scores (HSTD)
~~~~~~~~~~~~~~~~~~
Resets all values for game scores that are being monitored as configured in the ``categories:`` section of your ``high_score.yaml`` mode configuration.  All scores stored in the ``high_scores.yaml`` file in the ``/data`` subfolder of your game will be reset to teh ``defaults:`` section of your ``high_score.yaml`` mode configuration. 

Game Audits
~~~~~~~~~~~
Resets all counters for game elements that are being audited as configured in the ``auditor:`` section of your game configuration.  All counters will be reset to zero in ``audits.yaml`` in the ``/data`` subfolder of your game. 


Adjustments
-----------
MPF provides an **Adjustments** function that presents all of your configured game variables in the ``Settings`` section to the user to modify certain elements of the game.  This menu option is available from the ``service_menu_selected`` event with the label ``Adjustments Menu``.   

Audits
---------
(To be completed)

Diagnostics
-----------
MPF provides a **Diagnostics** function that allows the user to test hardware elements of the game such as switches, lights and coils.  This menu option is available from the ``service_menu_selected`` event with the label ``Diagnostics Menu``.   


