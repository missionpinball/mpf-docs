
# self.machine.show_controller

``` python
class mpf.core.show_controller.ShowController(machine)
```

Bases: `mpf.core.mpf_controller.MpfController`

Manages all the shows in a pinball machine. The ShowController handles priorities, restores, running and stopping shows, etc.

## Accessing the show_controller in code

There is only one instance of the show_controller in MPF, and it’s accessible via `self.machine.show_controller`.

## Methods & Attributes

The show_controller has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`create_show_config(name, priority=0, speed=1.0, loops=-1, sync_ms=None, manual_advance=False, show_tokens=None, events_when_played=None, events_when_stopped=None, events_when_looped=None, events_when_paused=None, events_when_resumed=None, events_when_advanced=None, events_when_stepped_back=None, events_when_updated=None, events_when_completed=None)`

Create a show config.

`get_next_show_id()`

Return the next show id.

`play_show_with_config(config, mode=None, start_time=None)`

Play and return a show from config. Will add the mode priority if a mode is passed.

`register_show(name)`

Register a named show.

`replace_or_advance_show(old_instance, config: mpf.assets.show.ShowConfig, start_step, start_time=None, start_running=True, stop_callback=None)`

Replace or advance show. Compare a given show (may be empty) to a show config and ensure that the new config becomes effective. If the old show runs a config which is equal to the new config nothing will be done. If the old_instance is set to manual_advance and one step behind the target step it will advance the show. Otherwise, the old show is stopped and the new show is stopped in sync.
