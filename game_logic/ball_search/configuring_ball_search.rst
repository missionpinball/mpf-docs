How to configure Ball Search
============================

To enable ball search set `enable_ball_search` to True for your playfield(s). In most cases, this is as simple as this:

.. code-block:: mpf-config

   #! switches:
   #!    s_flipper_left:
   #!       number:
   #! coils:
   #!    c_flipper_left:
   #!       number:
   #!       allow_enable: True
   #! flippers:
   #!   f_upper_flipper_left:
   #!     ball_search_order: 15
   #!     include_in_ball_search: True
   #!     main_coil: c_flipper_left
   #!     activation_switch: s_flipper_left
   playfields:
     playfield:
       enable_ball_search: True

Ball search will run in multiple phases with increasing intensity (phase 1 to 3) and give up afterwards.
To change the timeout before ball search starts when no ball was seen by MPF, change `ball-search-timeout`.
Similarly, `ball-search-interval` determines the delay between coil fires during search.
You can further configure ball search per :doc:`playfield </config/playfields>`.

Coils are included indirectly using their devices. Most devices allow you to configure
their order in ball search using the `ball_search_order` attribute (see the
:doc:`example ball_search </examples/ball_search/index>`). By default flippers are not included in ball search.
However, you might want to enable it for upper playfield flippers:

.. code-block:: mpf-config

   #! switches:
   #!    s_flipper_left:
   #!       number:
   #! coils:
   #!    c_flipper_left:
   #!       number:
   #!       allow_enable: True
   flippers:
     f_upper_flipper_left:
       ball_search_order: 15
       include_in_ball_search: True
       main_coil: c_flipper_left
       activation_switch: s_flipper_left

Make sure to include the tag `playfield_active` in all playfield switches which are not bound to devices. For instance
do not put that tag into your plunger switch but put it to target, inlane and outlane switches.

If you want to pulse a standalone coil which is not bound to any device, you can use pulse_events on ball_search_phase_x_searches (replace x with phase 1 to 3).
