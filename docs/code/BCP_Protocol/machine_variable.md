
# machine_variable (BCP command)
This is a generic "catch all" which sends machine variables to the media controller any time they change. Machine variables are like player variables, except they're maintained machine-wide instead of per-player or per-game. Since the pin controller will most likely track hundreds of variables (with many being internal things that the media controller doesn't care about), it's recommended that the pin controller has a way to filter which machine variables are sent to the media controller.

## Origin
Pin controller

## Parameters
If the value is a single variable, the command will have one parameter for the name and another for the value:
```
machine_variable?name=credits_string&value=FREE PLAY
```
If the value is more complex, both the name and the value will be contained in a single json parameter with the name 'json':
```
machine_variable?json={"name": "audits_player_score", "value": {"average": 6000, "top": [8300, 5200, 4500], "total": 3}}
```

### name
Type: `string`

This is the name of the machine variable.

### value
Type: Varies depending on the variable type.

This is the new value of the machine variable.

## Response
None
