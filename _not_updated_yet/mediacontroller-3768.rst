
The `media_controller:` section of the config file controls the
overall behavior of the MPF media controller process. It's analogous
to the `mpf:` section which is used by the MPF core engine. This
config section is included in the `mcconfig.yaml` file which is the
default that's always read in first whenever the media controller
starts up. You shouldn't have to change anything here, though you can
override specific settings if you want. This sectioncan be used in
your machine-wide config files. This section *cannot* be used in mode-
specific config files. Here's the default `media_controller:` section
from `mcconfig.yaml`:


::

    
    media_controller:
        modules:
            modes.ModeController
            language.Language
            display.DisplayController
            show_controller.ShowController
            keyboard.Keyboard
            sound.SoundController
        
        port: 5050
        exit_on_disconnect: yes
        display_modules:
            elements:
                - text
                - virtualdmd
                - image
                - animation
                - shape
                - movie
            modules:
                dmd.DMD
            transitions:
                move_out: move_out.MoveOut
                move_in: move_in.MoveIn
            decorators:
                blink: blink.Blink
        paths:
            shows: shows
            sounds: sounds
            machine_files: machine_files
            config: config
            fonts: fonts
            images: images
            animations: animations
            movies: movies
            modes: modes




modules:
~~~~~~~~

Lists the core modules that will be loaded with the media controller
boots.



port:
~~~~~

The TCP port number the media controller will listen on for an
incoming BCP connection from a pinball controller.



exit_on_disconnect:
~~~~~~~~~~~~~~~~~~~

Whether you want the media controller to automatically shut down and
exit when the connected pinball controller disconnects. Default is
yes.



display_modules:
~~~~~~~~~~~~~~~~

Lists the various display modules that will be available to the media
controller, including display elements, types of displays supported,
transitions, and decorators.



paths:
~~~~~~

Specifies the default folder names which will be used in a machine's
folder to hold different types of media aseets.



