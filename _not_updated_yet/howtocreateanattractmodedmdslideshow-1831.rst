
This tutorial will show you how to create a display show which plays
during your machine's attract mode, including several types of
`display elements`_, `slides`_, and `transitions`_. Here'sa video of
the finished product. https://www.youtube.com/watch?v=4wo-X8hSwMc



(A) Create your show YAML file
------------------------------

The easiest way to create a series of different slides and transitions
is to create a `show`_. For this example, create a new file called
`attract_display.yaml` and put it in the `shows` folder in your
machine's root folder. This folder should be at the same level as your
`config` file, like this: ` `_



(B) Addthe entries to your show
-------------------------------

You can refer to the "`Creating Shows`_" page for details on how to
actually create a show. In this case we created a show that was
strictly for the display. (We'll do lighting effects in their own show
which will run at the same time.) So each step of the show only has a
`display:` section, and then in there you'll see one or more `display
elements`_(text, image, animation, etc.) along with the specific
settings for each. The show file for the show that's playing in the
video above is here:


::

    
    - tocks: 3
      display:
      - type: Text
        font: small
        v_pos: center
        h_pos: center
        text: DRAWING SHAPES
        layer: 1
      - type: Shape
        shape: box
        x: 0
        y: 0
        width: 128
        height: 32
        thickness: 3
      - type: Shape
        shape: box
        x: 10
        y: 10
        width: 10
        height: 15
        shade: 9
      - type: Shape
        shape: box
        x: 100
        y: 5
        width: 20
        height: 30
        thickness: 0
        shade: 3
    
    - tocks: 3
      display:
        - type: Text
          text: MISSION PINBALL
          transition:
            type: move_out
            duration: 1s
            direction: left
        - type: Shape
          shape: box
          width: 128
          height: 32
          shade: 14
          x: 0
          y: 0
    
    - tocks: 3
      display:
      - type: Image
        image: test
        transition:
          type: move_in
          direction: left
        layer: 2
      - type: Text
        text: TEXT UNDER IMAGE
        layer: 1
        shade: 8
    
    - tocks: 3
      display:
        - type: Text
          text: PRESS START
        - type: Text
          text: FREE PLAY
          v_pos: bottom
          font: small
          transition:
            type: move_in
            duration: 1s
            direction: right
    
    - tocks: 3
      display:
      - type: Animation
        animation: rolling_ball
        fps: 60
        drop_frames: no
        layer: 1
      - type: Text
        text: TEXT OVER ANIMATION
        layer: 2
        shade: 0
        transition:
          type: move_out
          direction: top
    
    - tocks: 3
      display:
      - type: Text
        text: JUDGE DREDD
        transition:
          type: move_in
          duration: 1s
          direction: top
      - type: Shape
        shape: box
        width: 128
        height: 32
        shade: 9
    
    - tocks: 3
      display:
      - type: Image
        image: p_roc
        layer: 1
        transition:
          type: move_in
          direction: left
      - type: Text
        text: UNDER IMAGE
        layer: 0
        shade: 8
    
    - tocks: 3
      display:
      - type: Text
        text: CENTERED SIZE 10
      - type: Text
        font: small
        v_pos: top
        h_pos: left
        text: TOP LEFT SIZE 5
      - type: Text
        text: BOTTOM CENTERED SIZE 7
        v_pos: bottom
        h_pos: center
        font: medium
        transition:
          type: move_out
          direction: bottom
    
    - tocks: 3
      display:
      - type: Text
        font: small
        v_pos: center
        h_pos: center
        text: DRAWING SHAPES
        layer: 1
      - type: Shape
        shape: box
        x: 0
        y: 0
        width: 128
        height: 32
        thickness: 3
      - type: Shape
        shape: box
        x: 10
        y: 10
        width: 10
        height: 15
        shade: 9
      - type: Shape
        shape: box
        x: 100
        y: 5
        width: 20
        height: 30
        thickness: 0
        shade: 3




(C) Configure the show to start and stop by itself
--------------------------------------------------

Once we create our show, it just sits there, existing. We have to tell
it when to play and when to stop. Fortunately we can do that via our
machine config file in the `ShowPlayer: section`_which we entered like
this: (If you already have `machineflow_Attract_start` and
`machineflow_Attract_stop` entries because you created an `attract
mode light show`_, that's fine. Just add your display show to the list
under the existing event entries.


::

    
    show_player:
        attract_start:
          - show: attract_display
            repeat: yes
            tocks_per_sec: 1
        attract_stop:
          - show: attract_display
            action: stop


MPF automatically loads show files from the `shows` folder and gives
them the name that matches their file name. So just having our show
file in the right place means it got loaded. Then we just have to make
two entries into our s `how_player:` section—one which starts the show
when the `attract_start` event is posted, and another which stops the
show when a `ttract_stop` is posted. You'll notice that we're running
this show at 1 tocks_per_sec, and that all of our steps in the YAML
file are 3 tocks each. So every step is the 3 seconds. We could have
just as easily made each step 1 tock and then ran the show at .33
tocks_per_sec, but it seems like 1 tock_per_sec gives us good
flexibility to change the timing of individual steps in our show in
the future. So that's it! Save your config file and run your game, and
you should see your show start to play once the attract mode starts
up.

.. _Creating Shows: https://missionpinball.com/docs/shows/creating-shows/
.. _show: https://missionpinball.com/docs/shows/
.. _attract mode light show: https://missionpinball.com/docs/tutorial/step-15-create-an-attract-mode-light-show/
.. _display elements: https://missionpinball.com/docs/displays/display-elements/
.. _slides: https://missionpinball.com/docs/displays/slides/
.. _ShowPlayer: section: https://missionpinball.com/docs/configuration-file-reference/showplayer/
.. _transitions: https://missionpinball.com/docs/displays/transitions/


