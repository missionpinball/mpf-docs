Camera Widget
=============

The camera widget is used to show live video from an attached camera a :doc:`slide </displays/slides/index>`.

Here's an example:

.. code-block:: yaml

   #config_version=4

   slide_player:
     mc_ready:
        camera_example:
         - type: camera
           width: 800
           height: 600

Settings
--------

.. code-block:: yaml

   type: camera
   width:
   height:
   camera_index:

TODO
