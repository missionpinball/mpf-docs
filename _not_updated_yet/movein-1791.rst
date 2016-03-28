
The "Move In" transition is used to have the new slide smoothly move
in on top of the existing slide. You can configure the direction the
new slide comes in from, as well as how fast it moves. Here's a demo
of it in action: https://www.youtube.com/watch?v=0vpG0NFee-0 Settings:


+ Transition name as it's entered into YAML files: move_in
+ Direction. top, right, left, or bottom. Default is 'top'.
+ Duration: An `MPF time string`_. Default is 1 second.


You can add this transition to your `SlideBuilder:` section in your
machine configuration file and to the `display:` section of show
files.

.. _MPF time string: https://missionpinball.com/docs/configuration-file-reference/entering-time-duration-values/


