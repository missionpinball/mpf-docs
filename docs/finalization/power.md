---
title: Controlling your machine & computer power on / power off
---

# Controlling your machine & computer power on / power off


Unlike computers pinball machines are not expected to have a shutdown
procedure. Users tend to just turn off the power which might cause
problems with your operating system and filesystems.

Two general approaches exist here:

## Computer Start-up and Shutdown Controller

Scott Danesi sells a board called [Computer Start-up and Shutdown
Controller (CSSC)](http://www.danesidesigns.com/products/cssc/) which
will trigger a shutdown of your PC when the main power supply of your
machine is turned of (part number: #600-0322-00). However, you need to
make sure that the PC still has power until shutdown is complete. You
can either use a separate outlet (and make sure not to disconnect it
early) or add an Uninterruptible power supply (UPS) to your machine.

This solution is very useful during development and early prototypes.
Especially if you are using (older) Windows which very much dislikes
unclean shutdowns. However, with modern operating systems and
journalling filesystems (such as ext4 or ReFS) this became less of an
issue.

### Make it work on Linux

If you use a Linux distribution with systemd set `HandlePowerKey=ignore`
in `/etc/systemd/logind.conf`.

To handle power button events install `acpid`. Add
`/etc/acpi/events/powerbtn` with the following content (or change it if
if already exists):

``` bash
event=button[ /]power
action=/sbin/poweroff
```

Restart `acpid` (or your computer) and you should be good to go.

## Read-only Filsystems

When you finished your machine you will usually run in on Linux on an
embedded PC. Multiple solutions exist here such as OpenEmbedded/Yocto.
At that point you will usually have a build process which builds an
image which is then deployed to your target PC (via a SD card or flash
process). This image will be mounted read-only and cannot get damaged by
a crash.

Furthermore, you often add one partition to store audits/highscores and
sometimes logs. It is recommended to use a journaling filesystem for
this partition and expect it to break. Usually, there is some kind of
reset mechanism to wipe this partition in case it gets corrupted
(sometimes automatic in case it can no longer be mounted).

We are happy to discuss those topics in our forum (and extend this
section as a result of that).

## Using MPF to Shutdown a Computer

While the above two methods are the best ways to power your computer on
or off, there may be times when you want to use MPF to shutdown your
computer.

For example, if you're developing a DMD-based game and don't have a
computer monitor attached, you can use MPF to safely shutdown your
computer.

Create a mode called `shutdown_computer` and create a `/code` subfolder
and a `/config` subfolder.

Create a `shutdown_computer.py` file in the `/code` folder with the
following code:

``` python
from mpf.core.mode import Mode
import os
import platform
class shutdown_computer(Mode):
    def mode_init(self):
        self.log.info('shutdown_computer mode_init')
        self.OS_type = platform.system().lower()
    def mode_start(self, **kwargs):
        self.log.info('shutdown_computer mode_start')
        self.add_mode_event_handler('shutdown_host_computer', self.shutdown_host)
    def shutdown_host(self, **kwargs):
        #shutdown the mpf game if it's running
        #shutdown the computer
        if self.OS_type == 'linux':
            shutdown_str = 'shutdown -t 0'
        elif self.OS_type == 'windows':
            shutdown_str == 'shutdown -s -t 0'
        else:
            self.log.warning(f'Sorry this feature is not available in {self.os_type}')
            return
        os.system(shutdown_str)
    def mode_stop(self, **kwargs):
        self.machine.events.post('shutdown_computer mode_ended')
        self.log.info('shutdown_computer mode_stop')
```

Create a `shutdown_computer.yaml` file in the `/config` folder with the
following code:

``` yaml
#! switches:
#!   s_left_flipper:
#!     number:
#!   s_start:
#!     number:
##! code: modes/shutdown_computer/code/shutdown_computer.py
#! from mpf.core.mode import Mode
#! import os
#! import platform
#! class shutdown_computer(Mode):
#!     def mode_init(self):
#!         self.log.info('shutdown_computer mode_init')
#!         self.OS_type = platform.system().lower()
#!     def mode_start(self, **kwargs):
#!         self.log.info('shutdown_computer mode_start')
#!         self.add_mode_event_handler('shutdown_host_computer', self.shutdown_host)
#!     def shutdown_host(self, **kwargs):
#!         #shutdown the mpf game if it's running
#!         #shutdown the computer
#!         if self.OS_type == 'linux':
#!             shutdown_str = 'shutdown -t 0'
#!         elif self.OS_type == 'windows':
#!             shutdown_str == 'shutdown -s -t 0'
#!         else:
#!             self.log.warning(f'Sorry this feature is not available in {self.os_type}')
#!             return
#!         os.system(shutdown_str)
#!     def mode_stop(self, **kwargs):
#!         self.machine.events.post('shutdown_computer mode_ended')
#!         self.log.info('shutdown_computer mode_stop')
##! mode: shutdown_computer
#config_version=5
mode:
  start_events: mode_base_started
  stop_events: shutdown_mode_cancel
  priority: 400
  code: shutdown_computer.shutdown_computer

combo_switches:
  shutdown_hold:
    switches_1: s_left_flipper
    switches_2: s_start
    hold_time: 5s
    events_when_both: shutdown_host_computer
```

Enable the mode in your machine config file.

The above config is an example on how you could shutdown the computer.
This example requires you to hold down the left flipper and start button
together for five seconds, then the computer will shutdown.

You can change this and use the shutdown_host_computer event to shutdown
your computer as you like.
