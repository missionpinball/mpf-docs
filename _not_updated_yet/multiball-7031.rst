
MPF includes a *multiball* abstract device which can be used to
automatically start and stop multiballs.



Configuring multiballs
----------------------

See the `multiballs:` section of the configuration file reference.



Events posted by multiball devices
----------------------------------

The multiballs in MPF will post the following events. Each multiball
you set up has a name, and that name will be used in the *<name>*
section of the event names below:


+ * multiball_<name>_started * - This multiball has just begun. A
  parameter *balls* is the number of balls in this multiball.
+ * multiball_<name>_shoot_again * - A ball has drained while this
  multiball's "shoot again" period is active. A parameter *balls*
  indicates how many balls will be added back into play.
+ * multiball_<name>_ended * - This multiball has ended. This event is
  posted when there is only one live ball left on the playfield.




