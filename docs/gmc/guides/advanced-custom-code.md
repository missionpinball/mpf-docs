---
title: Advanced Custom Code
---

# Advanced Custom Code

For experienced developers who want complete control over how the GMC behaves, there are advanced options for hooking into, extending, and overriding all GMC behavior.

## Extending Core Script Classes

Each of the core scripts of GMC ([outlined here](../reference/mpf-gmc.md)) has a registered class name that allows the script to be extended or overridden. Many of these classes have virtual methods for code paths that would be common use cases, and *any* method on the class can be extended or overridden.

### Create a Custom Core Script

To insert your own code into the core GMC scripts, create a new GDScript file that `extends` from the core script class you want.

You can then create your own logic for virtual methods, extend existing methods with `super()`, or overwrite them entirely.

``` code
# /custom_code/my_custom_bcp.gd

extends GMCServer

# Override a virtual method
func on_connect():
    print("Connection established, running custom startup flow.")

# Extend an existing method by calling super() and adding custom logic
func set_machine_var(name: String, value) -> void:
    super()
    print("Machine var %s updated to value: %s" % [name, value])
```

### Inject Custom Script into GMC

Now that your script is written, you can instruct GMC to use your script instead of the core script by configuring it in *gmc.cfg*.

In your *gmc.cfg* file, create a new section named `[gmc]` and enter a key of the class name you're overriding and a value of the path to your custom script.

``` ini
[gmc]
GMCServer="custom_code/my_custom_bcp.gd"
```

The available core scripts to override are:

  1.  `GMCUtil` - Utility functions for common scenarios
  1.  `GMCLogger` - Logging handler for MPF-style logging
  1.  `GMCGame` - Game data from MPF (player and machine vars, modes, settings)
  1.  `GMCServer` - The BCP server (sending, receiving, and processing events)
  1.  `GMCMedia` - The media controller for slides, widgets, and sounds

Note that the core scripts are loaded **in the above order** and earlier scripts cannot reference later ones.