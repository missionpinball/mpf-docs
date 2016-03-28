
Often times in pinball programming, you need to set a "delay" for
something to happen in the future. You can't just tell MPF to sleep()
because that would mean that all of MPF would stop running and your
game would stop, so instead MPF contains a Delay Manager which is
responsible for scheduling and servicing delays for actions which need
to happen at some future time. MPF's delay manager lives in the
*mpf/system/tasks.py* module. Delays are used for one-time things you
want to happen at some point in the future. You can create, reset, and
delete as many delays as you want. Example uses of delays in the
framework include:


+ The ball search feature sets a delay to start the ball search
  anytime there's at least one uncontained ball. (The length of the ball
  search delay is specified in the configuration files, typically 10
  seconds.) Then once that delay is set, any time a playfield switch is
  hit, the delay is reset to start that many seconds in the future
  again. When there are no more balls uncontained, the ball search delay
  is removed.
+ Delays are used with ball devices any time a ball switch changes
  state. This allows for the balls to settle so the device can get an
  accurate count. For example, when a ball enters the trough and rolls
  down to the end, all the switches along the way will quickly change
  between "active" and "inactive" as the ball rolls by. Each switch
  change in the trough sets (or resets) a ball count delay for 1/2
  second in the future (also configurable), so the trough device doesn't
  actually count the the switches until the delay expires.
+ You can use delays to display information on the DMD for a short
  duration. For example, when a ball is saved you could write the words
  "Ball Saved!" to the DMD immediately, and then schedule a delay for
  two seconds in the future to remove those words.




