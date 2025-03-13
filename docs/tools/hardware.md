---
title: MPF Hardware Command
---

# MPF Hardware Command


MPF allows has a few command line actions to check and update your
hardware:

## mpf hardware scan

You can run [mpf hardware scan](#) to get an overview over the
connected hardware. MPF will try to enumerate all connected boards and
tell you what it know about your hardware. The output varies per
hardware platform from almost nothing to a lot.

## mpf hardware firmware_update

MPF will try to upgrade the firmware of your hardware if this is
supported for your hardware. There will probably be specific
configuration in your hardware platform section to enable this.

## mpf hardware benchmark

Overview video about mpf hardware benchmark:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/uRT--368J6A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

MPF will benchmark latency and jitter of inputs, outputs and rules for
your hardware setup (i.e. your controller with your OS and hardware).
This needs to be configured:

``` mpf-config
switches:
  s_test1:
    number:
  s_test2:
    number:

coils:
  c_coil1:
    number:
  c_coil2:
    number:
    allow_enable: true

flippers:
  f_flipper:
    activation_switch: s_test1
    main_coil: c_coil2

hardware_benchmark:
  coil1: c_coil1
  coil2: c_coil2
  switch1: s_test1
  switch2: s_test2
  flipper: f_flipper
```

Disconnect or disable high voltage. Then connect `s_test1`
to `c_coil1` and `s_test2` to
`c_coil2`. MPF will enable the flipper
`f_flipper` which will create a hardware rule on
`s_test1` to pulse `c_coil2`. Afterwards, MPF
will pulse `c_coil1` which should then activate
`s_test1`. In turn the hardware rule should pulse
`c_coil2` which then activates `s_test2`.
Hardware benchmark will measure the timings of the two switches. It will
repeat this procedure a few times and run some statistics on the
results.
