Why use a Virtual Machine
=========================



VM Benefits
-----------

-  Containerization:

   -  Keep Mission Pinball inside it's own container, without having to
      worry about outside packages or configurations causing problems

   -  Ensures dependencies are exactly what you expect them to be

-  Standardization/ease of setup:

   -  Allows users to keep using host OS they are comfortable with,
      without having to dual boot or replace main OS

   -  Only part that might change between host OSes is setting up the
      virtual machine

   -  Making a new VM is easy with VirtualBox

   -  Once Debian is running, less weird OS specific bugs

-  Portability:

   -  Move VM container to a different machine

      -  Host can have more/less resources as needed

      -  Can scale guest resources from VirtualBox Manager

   -  Can port to a real x86_64 machine from virtual machine

      -  Generate real disk image and copy to physical HDD

-  Emulation:

   -  "Pinball Machine in a box" (inside your computer)

   -  Simulates what resources you'll have available on real/physical
      game

   -  Network managed by VirtualBox:

      -  No cables / WiFi drivers

      -  No host or guest configuration

      -  VirtualBox network configuration is easy

      -  "It just works"

-  Development:

   -  Test code in simulated game environment

   -  Can develop on host OS and easily push to guest OS

   -  Test hardware driver code on host OS against real install of MPF
      on simulated pinball machine using virtual serial port pass
      through or ``socat`` remote serial port device.



VM Limitations
--------------

-  Resource intensive on host

   -  Need semi-decent computer to develop

-  Probably cannot port to ARM/RISC platforms (untested)

   -  This includes all Raspberry Pis and most SBCs

   -  Still useful for simulating resource limited environments

-  Not "true" emulation of real hardware (close but not 100%)

-  Takes longer to set up



Why VirtualBox
--------------

-  Open Source and Free

-  Flexible to many guest OSes

-  Powerful network tools

-  Snapshot feature allows returning to last known good configuration

-  Reliable passthrough USB and Serial support (for testing pinball
   hardware)

-  Well supported; new releases available often
