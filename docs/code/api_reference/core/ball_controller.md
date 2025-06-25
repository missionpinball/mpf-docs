
# self.machine.ball_controller

``` python
class mpf.core.ball_controller.BallController(machine: mpf.core.machine.MachineController)
```

Bases: `mpf.core.mpf_controller.MpfController`

Tracks and manages all the balls in a pinball machine.

## Accessing the ball_controller in code

    There is only one instance of the ball_controller in MPF, and it’s accessible via self.machine.ball_controller.

## Methods & Attributes

The ball_controller has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`add_captured_ball(source: mpf.devices.ball_device.ball_device.BallDevice) → None`

Inform ball controller about a capured ball (which might be new).

`are_balls_collected(target: Union[str, Iterable[str]]) → bool`

Check to see if all the balls are contained in devices tagged with the parameter that was passed.
Note if you pass a target that’s not used in any ball devices, this method will return True. (Because you’re asking if all balls are nowhere, and they always are. :)

Parameters:

* **target** – String or list of strings of the tags you’d like to collect the balls to. Default of None will be replaced with ‘home’ and ‘trough’.

`collect_balls(target='home, trough') → None`

Ensure that all balls are in contained in ball devices with the tag or list of tags you pass.
Typically this would be used after a game ends, or when the machine is reset or first starts up, to ensure that all balls are in devices tagged with ‘home’ and/or ‘trough’.

Parameters:

* **target** – A string of the tag name or a list of tags names of the ball devices you want all the balls to end up in. Default is [‘home’, ‘trough’].

`dump_ball_counts() → None`

Dump ball count of all devices.

`request_to_start_game(**kwargs) → bool`

Handle result of the request_to_start_game event.
Checks to make sure that the balls are in all the right places and returns. If too many balls are missing (based on the config files ‘Min Balls’ setting), it will return False to reject the game start request.
