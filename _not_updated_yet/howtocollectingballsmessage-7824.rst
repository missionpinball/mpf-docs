
"Ball collection" in MPF is the process where the ball controller
collects all the balls into devices with certain tags. By default,
when MPF boots, it will eject all the balls from all devices *except*
those that are tagged with *home* or *trough*. This process also
happens before a game can start. Previously it was confusing for
players because if they pressed Start when all the balls were not
collected, they'd see balls moving but the game wasn't started. So I
added some events you can use to trigger slides and effects:


+ * collecting_balls * - posted when the ball controller is in the
  process of collecting balls. (This event will only be posted if there
  are balls to be collected, and it may be posted multiple times as ball
  trickle through the system.)
+ * collecting_balls_complete * - posted when all the balls have been
  collected.


Typically you'd use these to post a slide that says something like
"COLLECTING BALLS. PLEASE WAIT"



