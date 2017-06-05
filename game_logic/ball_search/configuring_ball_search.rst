How to configure Ball Search
============================

To enable ball search set `enable_ball_search` to True for your playfield(s). In most cases, this is as simple as this:

::

   playfields:
     playfield:
       enable_ball_search: True

You can further configure ball search per :doc:`playfield </config/playfields>`. Most devices allow you to configure
their order in ball search using the `ball_search_order` attribute (see the
:doc:`example ball_search </examples/ball_search/index>`). By default flippers are not included in ball search.
However, you might want to enable it for upper playfield flippers:

::

   flippers:
     f_upper_flipper_left:
       ball_search_order: 15
       include_in_ball_search: True
       [...]

Make sure to include the tag `playfield_active` in all playfield switches which are not bound to devices. For instance
do not put that tag into your plunger switch but put it to target, inlane and outlane switches.
