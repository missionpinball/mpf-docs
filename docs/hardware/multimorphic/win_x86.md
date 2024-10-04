---
title: How to install P-ROC / P3-ROC drivers on Windows (32-bit)
---

# How to install P-ROC / P3-ROC drivers on Windows (32-bit)


This guide explains how to install the USB drivers for the P-ROC or
P3-ROC on 32-bit Windows (x86).

## 1. Download and install the FTDI drivers

The P-ROC and P3-ROC boards use a chip from a company called "FTDI
Chip" to handle the USB communication, so you need to install the FTDI
driver so Windows can properly see the device when you plug it in.

You can download the latest version from here:

<http://www.ftdichip.com/Drivers/D2XX.htm>

Here's a screen shot of the download section of that page. Note that
the actual version number of the driver might be newer that the screen
shot below. That should be ok.

![image](/docs/hardware/images/ftdi_x86.jpg)

Download and run the setup executable from the "1" link in the screen
shot. (We like to use that because it's easier than the manual process
you get from using the "2" link in that screen shot.)

Now MPF will be able to communicate with the P-ROC or P3-ROC.

Continue on with the [How to configure MPF for the P-ROC/P3-ROC platform](platform.md)
documentation to finish your MPF configuration for the P-ROC/P3-ROC.

## 2. Install Visual C++ Redistributable for Visual Studio 2019

You might already have those but in case you do not install [Visual C++
Redistributable for Visual Studio 2019
(32-bit)](https://aka.ms/vs/16/release/vc_redist.x86.exe).

## What if it did not work?

MPF is erroring out on start-up? Cannot connect to your P/P3-Roc? Have a
look at the
[troubleshooting guide for P/P3-Roc](../../troubleshooting/index.md).
