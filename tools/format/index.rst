Format And Lint Config Files
============================

The command line ``mpf format`` can reformat your MPF configs.

Run it using ``mpf format path/to/your_file.yaml``.
It will show you a preview of the changes it your make:

.. code-block:: console

   $ mpf format config/config.yaml
   Parsing single test config/config.yaml.
   Config is not linted.
   ---
   +++
   @@ -1,13 +1,13 @@
    #config_version=5

    config:
   -- shots.yaml
   -- switches.yaml
   -- coils.yaml
   -- devices.yaml
   -- leds.yaml
   -- slides.yaml
   -- sound.yaml
   +  - shots.yaml
   +  - switches.yaml
   +  - coils.yaml
   +  - devices.yaml
   +  - leds.yaml
   +  - slides.yaml
   +  - sound.yaml

    mpf:
      device_modules:
   @@ -203,7 +203,7 @@
          0.54: servo_pos2
        ball_search_min: 0.35
        ball_search_max: 0.55
   -    debug: True
   +    debug: true
      servo_figure_back:
        number: servo_back-64-0
        reset_events: machine_reset_phase_3
   @@ -217,8 +217,7 @@
          0.31: servo_pos2
        ball_search_min: 0.1
        ball_search_max: 0.3
   -    debug: True
   +    debug: true

   Not writing back changes. Use --yes to do this.

You can add ``--yes`` to the commandline to apply the changes.
