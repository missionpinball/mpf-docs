---
title: Mixing-and-Matching hardware platforms
---

# Mixing-and-Matching hardware platforms


In MPF it's possible to mix-and-match your hardware platforms. For
example, you could use a P-ROC for your coils and switches while using a
FadeCandy for your LEDs. (Or, if you wanted to be crazy, you could use a
FAST controller for your switches and a P-ROC for your coils and lamps.)

You can specify hardware platforms in three ways:

## 1. Machine-wide default platform

Whatever you set in the `hardware: platform:` section of your
machine-wide config is the default platform for all types of mechanisms
across all of MPF.

For example:

``` yaml
hardware:
  platform: p_roc
  driverboards: pdb
```

In the above config, the P-ROC platform will be the default for
everything. (switches, coils, lights, LEDs, DMDs, servos, etc.)

## 2. Device-specific default platform

If you want to specify a default for a certain class of devices that is
different than the machine-wide default, you can also do that in the
`hardware:` section by adding an entry for the type of device you want
to specify the default for.

For example, if you want to use a P-ROC as the default for everything
except for LEDs, which you want to be FadeCandy, you would do it like
this:

``` yaml
hardware:
  platform: p_roc
  driverboards: pdb
  lights: fadecandy
```

You can enter a device-specific default for the following types of
devices here:

* coils:
* switches:
* matrix_lights:
* lights:
* dmd:
* rgb_dmd:
* gis:
* flashers:
* servo_controllers:
* accelerometers:
* i2c:

## 3. Overriding the platform of individual devices

Finally, you can override the platform of an individual device by adding
a `platform:` setting to that device.

For example, if you're using a FAST Pinball controller which can
control up to 256 LEDs, but you also want to add some more LEDs that
will be attached to a FadeCandy, you could set up your config like this:

``` yaml
hardware:
  platform: fast
lights:
  led00:
    number: 0-0
  led01:
    number: 0
    platform: fadecandy
```

In this example, *led00* will use the FAST platform (and the number 0-0
is a FAST configuration number), and *led01* will use the FadeCandy
platform (and the number 0 is a Fadecandy number).

You could also invert this, like so:

``` yaml
hardware:
  platform: fast
  lights: fadecandy
lights:
  led00:
    number: 0-0
    platform: fast
  led01:
    number: 0
```

In the example above, *led00* is still a FAST LED and *led01* is still a
FadeCandy LED, but the difference is that while the default platform is
FAST, the default platform for LEDs is FadeCandy. That means you don't
have to specify the platform for LEDs attached to the FadeCandy, but you
do need to specify the platform for LEDs attached to the FAST
controller.
