
Logic Blocks are used to configure flowchart-style game logic via the
machine configuration files. Logic Blocks are one of the most powerful
features of MPF. You can use them to implement simple game logic. It's
probably easiest to understand them with some examples:


+ If either banks of drop targets is complete and the ball is shot
  into the center hole, light the special.
+ If the lit special is hit, award a special and then reset the
  special.
+ If the tilt switch is activated more than 3 times within a single
  ball, process a tilt.
+ If the player locks three balls, start multiball
+ If the player shoots three ramp shots within 10 seconds, light a
  hurry-up shot to a specific target
+ etc.


There are currently three different types of logic blocks in MPF:


+ Accrual logic blocks are used when you want to track progress
  towards some goal where the individual steps can be completed in any
  order. (You just have to "accrue" all the steps.)
+ Sequence logic blocks are used when you want to track progress
  towards some goal, but where each step has to be completed in order.
+ HitCounter logic blocks are used when you want to track a certain
  event happening again and again, with optional support for decay,
  counting multiple hits within a certain window as one hit, etc.


The real power of logic blocks is that you can chain together
individual blocks to create fairly sophisticated game logic. Logic
Blocks for your game are configured in the machine configuration file,
and you can read the config file reference for each block type for
detailed implementation instructions and examples.



Do you have to use Logic Blocks?
--------------------------------

We love the concept of Logic Blocks and use them extensively for the
games that we program. Even though we know Python and could implement
game logic in pure Python code, we don't want to reinvent the wheel
each step of the way. We designed the Logic Blocks to meet our needs
as game programmers, and we use them a lot. That said, just about
every aspect of the MPF is optional, so if you don't like the idea of
trying to figure out how logic blocks work and you'd like to write
your game logic in Python, then go right ahead! That's totally fine.
And if you're not that good with Python, or if you want to quickly
build-out your basic game logic, take a look at Logic Blocks. Of
course it's unlikely that you'll be able to build 100% of your game
logic with logic blocks alone, but you can definitely get a lot done.
(If you think about it, pinball game logic really is just a giant
flowchart of "if this then this, then this, this, and this, then that,
or if you do this instead, then that..", etc. Logic Blocks can handle
most of those scenarios for you.



