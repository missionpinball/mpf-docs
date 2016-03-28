
Now that we have a running game and some basic scoring, let's continue
to make the DMD more useful.



(A) Create an attract mode DMD loop
-----------------------------------

First, let's create a slide show that plays during the attract mode
and cycles through a few different slides. ("GAME OVER", "PRESS
START", ... that sort of thing.)



(1) Create an attract mode folder structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

So far it looks like your game only has one mode. (The *base* mode you
created a few steps ago.) But MPF actually has a few built-in modes
that it uses to do it's thing. For example, there's a mode called
"attract" which runs the attract mode (including watching for the
start button press to start a game), and there's a mode called "game"
which actually runs your games. (You may have noticed these modes in
your logs. *Attract* runs at priority 10 and *game* runs at priority
20.) Even though the attract mode is built-in, you can still create an
attract mode folder and an attract mode config which enable you to
extend the attract mode for your own use. So let's do that now. Go
into your machine's modes folder (which should only have your base
folder in it) and create a new folder called `attract`. Now you should
see two folders in it: ` `_ Now create a config folder in your attract
folder, and then create a new config file called `attract.yaml`: ` `_
Finally, create a folder called shows in your new attract mode folder,
and inside that folder, create a new file called
attract_dmd_loop.yaml: ` `_



(2) Edit your show yaml file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MPF has the ability to run "shows" which are coordinates series of
lights, sounds, slides, flashers, images, videos, gi, etc. These show
files also use the `.yaml` file format, though they're different than
the yaml config files. You can name the show whatever you want. In
this case we called it `attract_dmd_loop.yaml` since that pretty much
describes what it does. Note that we put this show file in a folder
called shows in our `attract` mode folder. Technically you can play
any show from any mode (and you could add a machine-wide `shows`
folder if you want), but we prefer to add shows used by a mode inside
that mode's `shows` folder since it keeps everything together. (In
other words, by doing that we keep everything a mode needs in its own
consolidated folder.) Here's a complete sample `attract_dmd_loop.yaml`
file you can use as a starting point:


::

    
    - tocks: 3
      display:
        - type: text
          text: YOU ARE AWESOME
          transition:
            type: move_out
            duration: 1s
            direction: left
    
    - tocks: 3
      display:
        - type: Text
          text: PRESS START
          decorators:
            type: blink
            repeats: -1
            on_secs: .5
            off_secs: .5
        - type: Text
          text: FREE PLAY
          color: 00ff00
          v_pos: bottom
          font: small
          transition:
            type: move_in
            duration: 1s
            direction: right
    
    - tocks: 3
      display:
        - type: Text
          text: MISSION PINBALL
          color: ff0000
          transition:
            type: move_in
            duration: 1s
            direction: top
        - type: shape
          shape: box
          width: 128
          height: 32


Notice that the show file is broken into steps, each beginning with a
dash and then a tocks: entry. The "tocks" entry controls the ratio of
how long each step plays for. In this case we have three steps, and
they're each three tocks, meaning they will each play for the same
amount of time. (How long is a tock? That's up to you to set when you
play the show. More on that in a moment... Then in each step, you
define what you want it to do. In this case each step of the show is a
"display" step, so we enter display:, and then under that we configure
settings for the display slides. Note that these settings are the
exact same settings you use in the slide_player: section of a config
file. You can define one or more display elements, and you can also
define transitions that will take place. At this point we're only
using text and shape display elements, but you could also use movies
and images.



(3) Configure your show to play automatically
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next we need to configure our new attract mode DMD loop show to start
playing automatically when the attract mode starts. To do this, go
back to the config file for the attract mode (
`modes/attract/config/attract.yaml`) and add the following:


::

    
    #config_version=3
    
    show_player:
      mode_attract_started:
        - show: attract_dmd_loop
          repeat: yes
          tocks_per_sec: 1


Note that we don't need a mode: section here because those settings
are already configured in the default attract mode settings folder
contained inside of MPF. So instead all we need to do is add a
`show_player:` entry. Like the `slide_player:`, the `show_player:`
section contains sub-sections for MPF events, and when that event is
posted the shows underneath it are started. In this case we're going
to start the show when the mode_attract_started event is posted.
Notice that we also add `repeat: yes` which means the show will repeat
(or loop) indefinitely, and we will add `tocks_per_sec: 1` which means
this show will play at a speed of 1 tock per second. (And since each
of the entries in this show file are set for 3 tocks, that means each
slide will be on the DMD for 3 seconds. You can play around with
different settings here. For example, try `tocks_per_sec: 30` and then
don't blink! :) You can configure `show_player:` entries to stop
shows, though in this case that's not necessary because any running
shows that a mode starts are automatically stopped when the mode
stops, and the attract mode stops when the game mode starts, so you
don't have to manually stop the show here.



(4) Remove the PRESS START slide_player entry from your machine-wide
config
~~~~~~

One last thing you should do here while you're at it is go back into
the machine-wide config and remove the `slide_player:` entry for the
`mode_attract_started` with that text that says PRESS START. The
attract mode runs at a priority of 10, and any `slide_player:` entries
in your machine-wide config run at priority 0, so that's why you don't
see that text anymore, but it's still a good idea to remove it just to
keep things clean. Now when you run your game, your attract mode
should look something like this:
https://www.youtube.com/watch?v=fu5EkZELlHQ



