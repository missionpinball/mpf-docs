---
title: Troubleshooting LISY
---

# Troubleshooting LISY


If you got problems with your hardware platform we first recommend to
read our
[troubleshooting guide](../../troubleshooting/index.md). Here are some hardware platform specific steps:

## Run Hardware Scan

Using `mpf hardware scan` you can find out if your LISY based platform
is talking properly to MPF. Additionally, it will show you details about
the hardware:

``` console
$ mpf hardware scan

LISY connected via network at localhost:1234
Hardware: LISY1 Lisy Version: 4.01 API Version: 0.8
Input count: 88 Input map: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87']
Coil count: 9
Modern lights count: 0
Traditional lights count: 40
Display count: 5
```

See [mpf hardware (command-line utility)](../../running/commands/hardware.md) for
details about the command.

## Enable Debugging

If you got problems with your platform try to enable `debug` first. As
described in the
[general debugging section](../../troubleshooting/general_debugging.md) of our
[troubleshooting guide](../../troubleshooting/index.md) this is done by adding `debug: true` to your `lisy` config
section:

``` mpf-config
lisy:
  debug: true
```

This will add a lot more debugging and might slow down MPF a bit. We
recommend to disable/remove it after finishing debugging.

## Coils Are Not Firing

What to do if your coils are not working?

--8<-- "troubleshooting_coils.md"

--8<-- "troubleshooting_lights.md"

--8<-- "troubleshooting.md"
