## Playfield Devices

In the context of MPF Monitor, a **device** refers to a switch,
light, or diverter.

### Adding devices to playfield

1.  Locate the *Devices* window.
2.  Locate the light or switch you want to add to the playfield.
3.  Drag device to image of playfield.

!!! note

    You can use the search box to filter to the name you are looking for.

### Changing the default size of all devices

1.  Ensure Device Inspector is disabled.
2.  Change the size slider or spinbox.

!!! note

    Any devices that have manually been resized will not be affected by the
    default size changes. You can reset this for a device by selecting the
    device and clicking "Reset to Defaults".

### Sorting and filtering devices

* To filter devices, type your keyword in the device search box.
* Sorting devices:
    1.  Latest received **Default**
        * Should match order of MPF config file
    2.  First received
    3.  Alphabetical, increasing:
        * Useful when placing ordered targets, ie: "*ltarget1*",
            "*ltarget2*", "*ltarget3*"...
    4.  Alphabetical, decreasing

------------------------------------------------------------------------

## Using Device Inspector

Use Device Inspector to modify your playfield devices without sending
switch hits to MPF

### Enabling Device Inspector

1.  Locate *Inspector* window.
2.  Enable Device Inspector by clicking the button labeled "Toggle
    Device Inspector".
3.  Device inspector is enabled. The button will stay "clicked" as an
    indicator. The *Playfield* window title will change to "Inspector
    Enabled - Playfield".
4.  Changes are saved automatically.
5.  Disable Device Inspector by clicking again on "Toggle Device
    Inspector".

!!! note

    While device is inspector is enabled, clicks on switches will not be
    sent to MPF.

### Viewing the name of a device

1.  Enable Device Inspector.
2.  On the playfield, select the device you want to view.
3.  The name of the device will be shown below the "Toggle Device
    Inspector" button.

### Changing display properties of device

Depending on your image dimensions switches and lights might be a little
small or too large. You may also want your device to display as a
different shape, or rotated to match an insert. You can change the size,
rotation, and shape of a device.

1.  Enable Device Inspector.
2.  Click on the device you want to change.
3.  Change size, shape or rotation by changing options in the inspector.

!!! note

    While device is inspector is enabled, clicks on switches will not be
    sent to MPF.

### Deleting devices from the playlist

1.  Enable Device Inspector.
2.  Click on the device you want to delete.
3.  Click the delete button in inspector.

### Resetting a device to its defaults

If you would like to clear your changes to a device's parameters, you
can reset all of them by selecting the device and clicking "Reset to
Defaults".

1.  Enable Device Inspector.
2.  Click on the device you want to reset.
3.  Click the "Reset to Defaults" button in inspector.

!!! warning

    It is not possible to undo resetting a device to its defaults.
