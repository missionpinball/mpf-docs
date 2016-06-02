How to install P-ROC / P3-ROC drivers on Windows (64-bit)
=========================================================

This guide explains how to install the USB drivers for the P-ROC or P3-ROC on 64-bit Windows (x64).



1. Download and install the FTDI drivers
----------------------------------------

http://www.ftdichip.com/Drivers/D2XX.htm

At the time of this writing, this is a direct link to the latest: http://www.ftdichip.com/Drivers/CDM/CDM21216_Setup.exe

2. Now download and unzip the other package
-------------------------------------------

http://www.ftdichip.com/Drivers/CDM/CDM%20v2.12.16%20WHQL%20Certified.zip

Find the file ftd2xx64.dll. (Or search your computer for it)

When you find it, copy it to C:\Windows\System32

Rename it from ftd2xx64.dll to ftd2xx.dll

Then hopefully MPF will be able to connect to the P-ROC.

Alternately, if you can’t find that file, you can download it. Here’s the latest driver package:
http://www.ftdichip.com/Drivers/CDM/CDM%20v2.12.16%20WHQL%20Certified.zip

When you unzip that, go to the “amd64” folder and get ftd2xx64.dll from there and then do steps 2 and 3 above.
