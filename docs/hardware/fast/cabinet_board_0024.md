---
title: Cabinet Board FP-I/O-0024
---

# Cabinet Board FP-I/O-0024

FAST Pinball has full documentation for thier cabinet board on their website:

* [FAST Cabinet I/O Board](https://fastpinball.com/products/ioboards/cabinet/)
* [Wiring the Cabinet I/O Board in a FAST Neuron](https://fastpinball.com/wiring/neuron/cabinet-ioboard/)

## FAST-Recommended MPF configuration

This IO board offers some unique features not seen in other IO boards, and needs some additional configuration to use to its full potential. The key is that this board offers low-voltage driver outputs. These can be used as additional open drains (to simplify wiring) or to control low-voltage devices.

The Start button light and coin reject button lights (or other lights) can be controlled as single-channel units with an additional layer of configuration.

Using all of these tricks, we end up with a FAST-recommended (TODO: get the PDF :) ) configuration as follows:
(Note that `platform: fast` should be specified in your hardware, or you will need to add it to each device config below yourself.)

```yaml
#config_version=6

### in config/cabinet.yaml:

event_player:
  mode_attract_started: enable_always_on_drivers
  game_started: enable_always_on_drivers

switches:

  ### Header J4 - Coin Door

  s_coin_door_service_esc:
    number: cabinet-0
    tags: service_esc

  s_coin_door_service_down:
    number: cabinet-1
    tags: service_down

  s_coin_door_service_up:
    number: cabinet-2
    tags: service_up

  s_coin_door_service_enter:
    number: cabinet-3
    tags: service_enter

  s_coin_door:
    number: cabinet-4
    tags: service_door_open

  s_coin_mech_1:
    number: cabinet-5
  s_coin_mech_2:
    number: cabinet-6

  s_slam_tilt:
    number: cabinet-7
    tags: slam_tilt


  ### Header J1 - Cabinet Left

  s_flipper_left:
    number: cabinet-8
    tags: left_flipper

  s_flipper_left_secondary:
    number: cabinet-9

  s_start:
    number: cabinet-10
    tags: start

  s_tilt_bob:
    number: cabinet-11
    tags: tilt_warning


  ### Header J10 - Cabinet Right

  s_flipper_right:
    number: cabinet-16
    tags: right_flipper

  s_flipper_right_secondary:
    number: cabinet-17

  s_launch:
    number: cabinet-18

coils:
  # Some drivers are always enabled as low current drains for their switches (L0, L1, L3)
  # Low current drivers can also control single-channel lights (L2, L4)

  c_interlock_control:
    number: cabinet-0 # L0
    allow_enable: true
    enable_events: enable_always_on_drivers

  c_coin_mechs:
    number: cabinet-1 # L1
    allow_enable: true
    enable_events: enable_always_on_drivers

  c_start_light_driver:
    number: cabinet-2 # L2
    allow_enable: true
    console_log: none
    file_log: none

  c_tilt_control:
    number: cabinet-3 # L3
    allow_enable: true
    enable_events: enable_always_on_drivers
    console_log: none
    file_log: none

  c_launch_light_driver:
    number: cabinet-4 # L4
    allow_enable: true
    console_log: none
    file_log: none

  c_knocker:
    number: cabinet-7 # D1 - 48v driver

lights:
  # Single-channel cabinet lights using low-current drivers.
  # Note that the platform is drivers itself, not FAST directly

  l_start:
    number: c_start_light_driver
    platform: drivers
    type: w

  l_launch:
    number: c_launch_light_driver
    platform: drivers
    type: w
```

## Harness wiring guide:

The harness to match the above config is described as follows.

Note, the FP-SWI-708X refers to the FAST opto flipper units with different left and right SKUs.

```ruby
### Configuration per board labeling on variant FAST-I/O-0024-5
### Other variants may have different connector numbers or pin orders

# Cabinet A - J1
Left Opto Flipper Orange = Flipper Switch 1         J1-8
Left Opto Flipper Brown = Flipper Switch 2          J1-9
Start Button Switch Gray = Start Button Switch      J1-10
Tilt Bob Switch Green = Tilt Bob Switch             J1-11

Start Button Switch Purple = Ground # from GND on FP-SWI-708X opto flipper board connection
Left Opto Flipper Purple = Ground                   J1-G
Start Button LED Red = 5V                           J1-5V
Start Button LED White = Driver                     J1-L2
Tilt Bob Switch Black = Driver                      J1-L3
Left Opto Flipper Yellow = 12v                      J1-V+

# Coin Door - J4
Coin Mech Yellow = 12v                              J4-V+
Coin Mech Black = Ground (Driver and switch)        J4-L1
Door Interlock Switch White = Ground (Driver)       J4-L0
Service Buttons Purple = Ground                     J4-G

Coin Mech Green = Slam Tilt                         J4-7
Coin Mech Gray = Coin 2                             J4-6
Coin Mech Brown = Coin 1                            J4-5
Door Interlock Switch Orange = Coin Door Interlock  J4-4
Service Buttons Green = Enter                       J4-3
Service Buttons Gray = Up                           J4-2
Service Buttons Brown = Down                        J4-1
Service Buttons Orange = ESC                        J4-0

# Cabinet B - J10
Right Opto Flipper Yellow = 12v                     J10-V+
Reserved for Dollar Bill Acceptor Use               J10-L5
Launch/Lockdown Button LED White = Driver           J10-L4
Launch/Lockdown Button LED Red = 5V                 J10-5V
Right Opto Flipper Purple = Ground                  J10-G
Launch/Lockdown Button Switch Purple = Ground # from GND on FP-SWI-708X opto flipper board connection

Launch/Lockdown Button Switch Gray = Switch         J10-18
Right Opto Flipper Brown = Flipper Switch 2         J10-17
Right Opto Flipper Orange = Flipper Switch 1        J10-16

```
