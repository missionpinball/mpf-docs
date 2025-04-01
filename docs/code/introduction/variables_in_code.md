# Variables in Code

## Player Variables in Code

Player variables are only accessible when a game is running. Be prepared that the current player may change in a multiplayer game.

Inside a (game) mode you can access the current player using `self.player`. Alternatively, you can use `self.machine.game.player` but be aware that both `self.machine.game` and `self.machine.game.player` may be None. Using the current player is probably the most common use case, but you can as well access the player variable of a specific player in code.

You can use player variables like this:

``` python
player = self.machine.game.player    # do not persist the player because it may change
                                     # alternatively use self.player in modes

if not player:
   return    # do something reasonable here but do not crash in the next line

# read player variable
self.machine.log.info(player["my_variable"])

# set a variable
player["my_variable"] = 17
```



## Machine Variables in Code

You can use machine variables by calling into the MPF machine.

``` python
# read machine variable
self.machine.log.info(self.machine.variables.get_machine_var("my_variable"))

# configure variable to persist to disk and expire after 1 day (optional)
# alternatively you can also use "machine_vars" in config to achieve the same
self.machine.variables.configure_machine_var("my_variable", persist=True, expire_secs=86400)

# set a variable
self.machine.variables.set_machine_var("my_variable", 17)
```

