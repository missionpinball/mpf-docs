---
title: OPP Switches
---

# OPP Switches


Related Config File Sections:

* [switches:](../../config/switches.md)

For switches, you can use most of the settings as outlined in the
`switches:` section of the config file reference. There are only a few
things that are OPP-specific:

## Number:

OPP switches are numbered sequentially depending on which wing board is
the switch input. Wing position 0 contains switch numbers 0 to 7. Wing
position 1 contains switch numbers 8 to 15. Wing position 2 contains
switch numbers 16 to 23. Wing position 3 contains switch numbers 24 to
31. The switch is numbered using the position of the OPP card (starting
at 0), then a '-', and finally the switch number on the card.

Enter them as a combination of board-switch, like `0-12`.

``` mpf-config
switches:
  some_switch:
    number: 0-15
```

The above example configures a switch input as the first OPP card, and
the second wing board, last input. On the microprocessor card, the input
is marked as 1.7 (wing port 1, position 7).

Switch inputs for solenoids follow the same number convention. Since
only four inputs are available for each wing card, it uses the first
four switch numbers. Solenoid wing 0 uses switch numbers 0 to 3.
Solenoid wing 1 uses switch numbers 8 to 11. Solenoid wing 2 uses switch
numbers 16 to 19. Solenoid wing 3 uses switch numbers 24 to 27.

Switch inputs for a switch matrix are number slightly differently. To
configure an 8x8 switch matrix wing 2 is configured as the matrix input
and wing 3 is configured as a matrix output. The OPP hardware strobes
the eight outputs while reading from the eight inputs. This allows 64
inputs to be read using only 16 wires. The matrix switch inputs are
numbered from 32 to 95. Switches 32 - 39 are column 0, switches 40 -47
are column 1, switch 48 - 55 are column 2, switches 56 - 63 are column
3, switches 64 - 71 are column 4, switches 72 to 79 are column 5,
switches 80 to 87 are column 6, and switches 88 to 95 are column 7.

## Fully working Example

Lets bring above informaton together and learn by example. Though the
following example is a fully working minimal set for the Cobra
controller, it is as well helpful to understand the concpet more if you
use a different set of hardware. For this example to work physically,
you only need to power up the micro controllers, no need for any other
power supply on the Cobra board. You need to connect a switch to the
switch inputs. See as well in
[CobraPin Pinball Controller powered by OPP](cobrapin/index.md) how to
connect a switch. In this example I am using `0-0-16` if you use a
different switch input, then you need to change the config file. This
`config.yaml` is the only configuration file you need in your project.
The config file is fully valid for the Cobra board connected to a Linux
PC running mpf. If you have a Cobra board but run Windows or macOS you
have to change the `ports`. If you run a completely different hardware
you have to adapt the `hardware` section.

``` mpf-config
#config_version=5

   hardware:
      platform: opp
      driverboards: gen2

   opp:
      ports: /dev/ttyACM0, /dev/ttyACM1 # change this if you are not using Linux

   switches:
      my_test_switch:
         debug: true
         number: 0-0-16 # change this if you have connected the switch to a different input
         tags: switch_tag1, switch_tag2
         events_when_activated: active_event1, active_event2
         events_when_deactivated: inactive_event1
```

The important part for this example is to understand the events which
are being posted. First of all please obey that we have set
`debug:true`, this is necessary to see the events in the mpf monitor.
Events are only visible in the mpf monitor when they are either consumed
or if the `debug:true` flag is set. Since we don't consume the event in
our example we need to set debug to true. Before you start this mpf
project with `mpf both` please start `mpf monitor` and activate the
window in the monitor to view the events. Now you can press and release
the switch and monitor the events being posted. When pressing the switch
you should be able to see the following events:

* `my_test_switch_active` based on the switch <switch_name>_active
* `sw_switch_tag1` based on the tags [sw](../../index.md)<tag_name>
* `sw_switch_tag1_active` based on the tags [sw](../../index.md)<tag_name>_active
* Same as the last two, just for the second tag `switch_tag2`
* `active_event1` based on the configuration `events_when_activated`
* `active_event2` based on the configuration `events_when_activated`

Once you release the switch again some events are being fired:

* `my_test_switch_inactive` based on the switch
    <switch_name>_active
* `sw_switch_tag1_inactive` based on the tags
    [sw](../../index.md)<tag_name>_active
* `sw_switch_tag2_inactive` based on the tags
    [sw](../../index.md)<tag_name>_active
* `inactive_event1` based on the configuration `events_when_activated`

Please obey the difference in activating and releasing a switch in terms
of what events are being fired. When activating a switch the event
`sw_<tag_name>` is being fired, there is no corresponding event when a
switch goes inactive. See as well the [Events](../../events/index.md) reference.

### What if it did not work?

Have a look at our
[OPP troubleshooting guide](../../troubleshooting/index.md).
