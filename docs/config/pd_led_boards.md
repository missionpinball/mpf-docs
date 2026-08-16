---
title: "pd_led_boards: Config Reference"
---

# pd_led_boards: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**NO** :no_entry_sign:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `pd_led_boards:` section of your config is where you configure your
PD-LED boards connected to your
[P-Roc or P3-Roc](../hardware/multimorphic/index.md). See [Servos on a PD-LED (P-ROC/P3-ROC)](../hardware/multimorphic/servos.md), [Steppers on a PD-LED (P-ROC/P3-ROC)](../hardware/multimorphic/steppers.md) or [How to configure LEDs on the PD-LED (P-ROC/P3-ROC)](../hardware/multimorphic/leds.md) for details.

## Optional settings

The following sections are optional in the `pd_led_boards:` section of
your config. (If you don't include them, the default will be used).

### lpd880x_0_first_address:

Single value, type: `integer`. Default: `100`

First LED address to map to lpd880x_0. This will be the LED number on
the PD-LED for your first LED in the chain. If you set this to 100 it
will be the first LED in your chain. 101 will be the second in chain and
so on.

### lpd880x_0_last_address:

Single value, type: `integer`. Default: `249`

Last LED address to map to lpd880x_0. This will determine how many LEDs
map to your chain. The more LEDs you have in your chain the lower the
update rate will be.

### lpd880x_1_first_address:

Single value, type: `integer`. Default: `250`

First LED address to map to lpd880x_1. This will be the LED number on
the PD-LED for your first LED in the chain. If you set this to 100 it
will be the first LED in your chain. 101 will be the second in chain and
so on.

### lpd880x_1_last_address:

Single value, type: `integer`. Default: `399`

Last LED address to map to lpd880x_1. This will determine how many LEDs
map to your chain. The more LEDs you have in your chain the lower the
update rate will be.

### lpd880x_2_first_address:

Single value, type: `integer`. Default: `400`

First LED address to map to lpd880x_2. This will be the LED number on
the PD-LED for your first LED in the chain. If you set this to 100 it
will be the first LED in your chain. 101 will be the second in chain and
so on.

### lpd880x_2_last_address:

Single value, type: `integer`. Default: `549`

Last LED address to map to lpd880x_2. This will determine how many LEDs
map to your chain. The more LEDs you have in your chain the lower the
update rate will be.

### max_servo_value:

Single value, type: `integer`. Default: `250`

Max clock cycles in a servo duty cycle. 300 will rougly map to 2ms.

### stepper_speed:

Single value, type: `integer`. Default: `13524`

Clock cycles for a stepper half step (at 32MHz). This might need some
tuning depending on your stepper.

### use_lpd880x_0:

Single value, type: `boolean` (Yes/No or True/False). Default: `false`

Enable the first LPD880x serial LED chain on connector J8 pin 13 (clock)
and pin 14 (data). If you enable this you cannot use LEDs 79 and 80 on
the board.

### use_lpd880x_1:

Single value, type: `boolean` (Yes/No or True/False). Default: `false`

Enable the second LPD880x serial LED chain on connector J8 pin 9 (clock)
and pin 12 (data). If you enable this you cannot use LEDs 77 and 78 on
the board.

### use_lpd880x_2:

Single value, type: `boolean` (Yes/No or True/False). Default: `false`

Enable the third LPD880x serial LED chain on connector J8 pin 7 (clock)
and pin 8 (data). If you enable this you cannot use LEDs 75 and 76 on
the board.

### use_servo_0:

Single value, type: `boolean` (Yes/No or True/False). Default: `false`

Set to true to enable servo 0 on connector J8 pin 2. If you enable this
you cannot use LED 72 on the board.

### use_servo_1:

Single value, type: `boolean` (Yes/No or True/False). Default: `false`

Set to true to enable servo 1 on connector J8 pin 3. If you enable this
you cannot use LED 73 on the board.

### use_servo_10:

Single value, type: `boolean` (Yes/No or True/False). Default: `false`

Set to true to enable servo 10 on connector J8 pin 18. If you enable
this you cannot use LED 82 on the board.

### use_servo_11:

Single value, type: `boolean` (Yes/No or True/False). Default: `false`

Set to true to enable servo 11 on connector J8 pin 19. If you enable
this you cannot use LED 83 on the board.

### use_servo_2:

Single value, type: `boolean` (Yes/No or True/False). Default: `false`

Set to true to enable servo 2 on connector J8 pin 4. If you enable this
you cannot use LED 74 on the board.

### use_servo_3:

Single value, type: `boolean` (Yes/No or True/False). Default: `false`

Set to true to enable servo 3 on connector J8 pin 7. If you enable this
you cannot use LED 75 on the board.

### use_servo_4:

Single value, type: `boolean` (Yes/No or True/False). Default: `false`

Set to true to enable servo 4 on connector J8 pin 8. If you enable this
you cannot use LED 76 on the board.

### use_servo_5:

Single value, type: `boolean` (Yes/No or True/False). Default: `false`

Set to true to enable servo 5 on connector J8 pin 9. If you enable this
you cannot use LED 77 on the board.

### use_servo_6:

Single value, type: `boolean` (Yes/No or True/False). Default: `false`

Set to true to enable servo 6 on connector J8 pin 12. If you enable this
you cannot use LED 78 on the board.

### use_servo_7:

Single value, type: `boolean` (Yes/No or True/False). Default: `false`

Set to true to enable servo 7 on connector J8 pin 13. If you enable this
you cannot use LED 79 on the board.

### use_servo_8:

Single value, type: `boolean` (Yes/No or True/False). Default: `false`

Set to true to enable servo 8 on connector J8 pin 14. If you enable this
you cannot use LED 80 on the board.

### use_servo_9:

Single value, type: `boolean` (Yes/No or True/False). Default: `false`

Set to true to enable servo 9 on connector J8 pin 17. If you enable this
you cannot use LED 81 on the board.

### use_stepper_0:

Single value, type: `boolean` (Yes/No or True/False). Default: `false`

Set to true to enable stepper 0 on connector J8 pin 12 (sleep), pin 13
(pulse) and pin 14 (direction). If you enable this you cannot use LEDs
78, 79 and 80 on the board.

### use_stepper_1:

Single value, type: `boolean` (Yes/No or True/False). Default: `false`

Set to true to enable stepper 1 on connector J8 pin 7 (sleep), pin 8
(pulse) and pin 9 (direction). If you enable this you cannot use LEDs
75, 76 and 77 on the board.

### use_ws281x_0:

Single value, type: `boolean` (Yes/No or True/False). Default: `false`

Enable the first WS281x serial LED chain on connector J8 pin 19. If you
enable this you cannot use LED 83 on the board.

### use_ws281x_1:

Single value, type: `boolean` (Yes/No or True/False). Default: `false`

Enable the second WS281x serial LED chain on connector J8 pin 18. If you
enable this you cannot use LED 82 on the board.

### use_ws281x_2:

Single value, type: `boolean` (Yes/No or True/False). Default: `false`

Enable the third WS281x serial LED chain on connector J8 pin 17. If you
enable this you cannot use LED 81 on the board.

### ws281x_0_first_address:

Single value, type: `integer`. Default: `100`

First LED address to map to ws281x_0. This will be the LED number on the
PD-LED for your first LED in the chain. If you set this to 100 it will
be the first LED in your chain. 101 will be the second in chain and so
on.

### ws281x_0_last_address:

Single value, type: `integer`. Default: `249`

Last LED address to map to ws281x_0. This will determine how many LEDs
map to your chain. The more LEDs you have in your chain the lower the
update rate will be.

### ws281x_1_first_address:

Single value, type: `integer`. Default: `250`

First LED address to map to ws281x_1. This will be the LED number on the
PD-LED for your first LED in the chain. If you set this to 100 it will
be the first LED in your chain. 101 will be the second in chain and so
on.

### ws281x_1_last_address:

Single value, type: `integer`. Default: `399`

Last LED address to map to ws281x_1. This will determine how many LEDs
map to your chain. The more LEDs you have in your chain the lower the
update rate will be.

### ws281x_2_first_address:

Single value, type: `integer`. Default: `400`

First LED address to map to ws281x_2. This will be the LED number on the
PD-LED for your first LED in the chain. If you set this to 100 it will
be the first LED in your chain. 101 will be the second in chain and so
on.

### ws281x_2_last_address:

Single value, type: `integer`. Default: `599`

Last LED address to map to ws281x_2. This will determine how many LEDs
map to your chain. The more LEDs you have in your chain the lower the
update rate will be.

### ws281x_end_bit_time:

Single value, type: `integer`. Default: `40`

Clock cycles for the end bit in a WS281x chain (at 32MHz). Usually this
does not have to be changed.

### ws281x_high_bit_time:

Single value, type: `integer`. Default: `24`

Clock cycles for a high bit in a WS281x chain (at 32MHz). Usually this
does not have to be changed.

### ws281x_low_bit_time:

Single value, type: `integer`. Default: `13`

Clock cycles for a low bit in a WS281x chain (at 32MHz). Usually this
does not have to be changed.

### ws281x_reset_bit_time:

Single value, type: `integer`. Default: `1603`

Clock cycles for a reset bit in a WS281x chain (at 32MHz). Usually this
does not have to be changed.

## Related How To guides

* [How to configure LEDs on the PD-LED (P-ROC/P3-ROC)](../hardware/multimorphic/leds.md)
