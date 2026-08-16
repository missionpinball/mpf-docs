# mode_list (BCP command)
This message informs the media controller about which modes are currently running. It is sent whenever a mode starts or stops, but only to clients currently [monitoring](monitor_start.md) the `mode` category.

## Origin
Pin controller


## Parameters
### running_modes
Type: JSON Array

Example (Formatted for legibility; the parameter does not contain line-breaks):
``` json
{
    "running_modes": [
        [
            "base",
            100
        ],
        [
            "game",
            20
        ]
    ]
}
```

Each element of the array is another JSON Array with the following elements:

1. The name of the mode (`string`)
2. The priority of the mode (`int`)
