
The "Move Out" transition is used to have the currentslide smoothly
move out, revealing the new slide beneath it. You can configure the
direction it movesand how long it takes to fully move out. Here's a
demo of it in action: https://www.youtube.com/watch?v=wojAl93fSW0
Settings:


+ Transition name as it's entered into YAML files: move_out
+ Direction. top, right, left, or bottom. Default is 'top'.
+ Duration: An `MPF time string`_. Default is 1 second.


You can add this transition to your `SlideBuilder:` section in your
machine configuration file and to the `display:` section of show
files.

.. _MPF time string: https://missionpinball.com/docs/configuration-file-reference/entering-time-duration-values/


