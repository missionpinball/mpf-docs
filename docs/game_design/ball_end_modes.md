---
title: Ball End Modes
---

# Ball End Modes


Certain modes typically run on game end. MPF has a lot of built-in modes
for this purpose. You can omit any of them or replace them with your own
mode.

Ball end modes delay the ball ending process. If you want your own mode
to delay the ball ending process you can start the with the following
config:

``` yaml
##! mode: custom_bonus
#config_version=5
mode:
  start_events: ball_ending     # start on ball ending process
  use_wait_queue: true          # delay ball ending
  priority: 500                 # determines the order of ball end modes
  stop_events: stop_my_mode     # post this event to stop the mode and continue the ball ending process
```

Ball ending will be delayed until your mode stops so make sure that your
mode ends eventually or the game will be stuck. In the example above
your config need to post `stop_my_mode` or, if you are writing code,
stop your mode in code.

## Showing slides on mode end

See [Ball Start and End Behavior](../game_logic/ball_start_end.md).

## Bonus Mode

Score multipliers and evaluate them into a bonus at the end of the ball.
See [End of Ball Bonus](../game_logic/bonus/index.md) for details.
