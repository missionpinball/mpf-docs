# Variables in Code

## Player Variables in Code

Player variables are only accessible when a game is running. Be prepared that the current player may change in a multiplayer game.

Inside a (game) mode you can access the current player using self.player. Alternatively, you can use self.machine.game.player but be aware that both self.machine.game and self.machine.game.player may be None.

You can use player variables like this:

```
player = self.machine.game.player    # do not persist the player because it may change
                                     # alternatively use self.player in modes

if not player:
   return    # do something reasonable here but do not crash in the next line

# read player variable
print(player["my_variable"])

# set a variable
player["my_variable"] = 17
```



## Machine Variables in Code

You can use machine variables by calling into the MPF machine.

```
# read machine variable
print(self.machine.variables.get_machine_var("my_variable"))

# configure variable to persist to disk and expire after 1 day (optional)
# alternatively you can also use "machine_vars" in config to achieve the same
self.machine.variables.configure_machine_var("my_variable", persist=True, expire_secs=86400)

# set a variable
self.machine.variables.set_machine_var("my_variable", 17)
```

