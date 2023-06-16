---
title: How to configure an RGB DMD (FAST Pinball)
---

# How to configure an RGB DMD (FAST Pinball)

Related Config File Sections:

* [rgb_dmds:](../../config/rgb_dmds.md)

If you would like to use the FAST RGB LED DMD, follow the instructions
for the [How to configure a "SmartMatrix" RGB LED DMD](../smartmatrix.md).

You can copy the following example (and replace `com12` with your com
port):

``` mpf-config
hardware:
  rgb_dmd: smartmatrix
smartmatrix:
  smartmatrix_1:
    port: com12
    baud: 4000000
    old_cookie: false
```

## What if it did not work?

Have a look at our
[FAST troubleshooting guide](../../troubleshooting/index.md).
