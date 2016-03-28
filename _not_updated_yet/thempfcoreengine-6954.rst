
As we've mentioned elsewhere in this documentation, the MPF core
engine is a separate running process on your computer from the code
that controls your display and sounds. When you run MPF, you'll
typically have two processes running—the core game engine and a media
controller, and the two processes talk to each other via a protocol we
created called the Backbox Display Protocol (BCP). ` `_ The MPF core
engine is written in Python 2.7. It lives in the `/mpf` folder in your
MPF download package. (If your MPF download package is in a folder on
your computer called *mpf*, then the MPF game engine is in a folder
called `/mpf/mpf`.) The MPF core engineis the process responsible for
running the pinball machine and communicating with its hardware,
including:


+ All communication with physical hardware.
+ Managing, tracking, and controlling all devices, including switches,
  coils, lights, LEDs, motors, steppers, servos, and flashers.
+ All game logic, including game starting and stopping game modes,
  rules, players, scores, etc.


You run the MPF core engine from the command prompt like this: `python
mpf.py *your_machine_folder*`.



