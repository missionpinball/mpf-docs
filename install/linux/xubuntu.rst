Installing MPF on Xubuntu/Lubuntu
=================================

Xubuntu is a Ubuntu-based linux distribution using the minimalist, yet still feature-packed, XFCE desktop manager.
The focus of this guide will be for getting MPF up and running directly from power (unattended) for use in a production
scenario.

1. Create Xubuntu/Lubuntu Installation Media
--------------------------------------------

You will need:

* 4GB USB Flash Drive or larger

Write the ISO (Win/Mac/Linux)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use `UNetbootin <https://unetbootin.github.io/>`_

* Select LUbuntu or XUbuntu
* Select your USB Stick

2. Install Xubuntu/Lubuntu
--------------------------

Boot from the installation media (you may need to change something in your BIOS to enable booting from USB).
It should be a fairly straight-forward linux installation. When it asks about partioning, choose the
"Guided - entire hard disk" option (unless you have a specific reason not to). You will be asked to create a
user account. When doing so, it's important that you: **DO NOT ELECT TO ENCRYPT THE HOME FOLDER**. If you encrypt
the home folder, the auto login will not work and will have to reinstall to fix.

3. Configure Xubuntu/Lubuntu
----------------------------

The system will reboot after installation. Login with your username and password then follow these steps:

* Launch a Terminal emulator
* Update the sources: ``sudo apt-get update``
* Upgrade all the things: ``sudo apt-get upgrade``
* Setup auto-login to the XFCE desktop
   * Create the file ``/etc/lightdm/lightdm.conf.d/12-autologin.conf`` and edit it to contain:

.. code-block:: console

  [Seat:*]
  autologin-user=your_username
  autologin-user-timeout=0

* Be sure to change ``your_username`` to the username you created during installation.

* Optional: Reduce the Network Timeout
   * You should do this if the system will not always be connected to the internet
   * Edit the file ``/etc/systemd/system/network-online.targets.wants/networking.service``
   * Find the line ``TimeoutStartSec=5min`` and change to ``TimeoutStartSec=10sec``

4. Install MPF
--------------

The existing Debian install script works perfectly on Ubuntu. The following commands will install
the current versions of MPF and MPF-MC as well as each of their dependencies.

.. code-block:: console

  cd ~
  wget https://github.com/missionpinball/mpf-debian-installer/archive/0.54.x.zip
  unzip 0.54.x.zip
  cd mpf-debian-installer-0.54.x
  sudo -H ./install
  rm ~/0.54.x.zip && rm -Rf ~/mpf-debian-installer-0.54.x

If you want to make sure that MPF was installed, you can run:

.. code-block:: console

   mpf --version

This command can be run from anywhere and should produce output something like
this:

.. code-block:: console

   username@host:~$ mpf --version
   MPF v0.33.13

(Note that the actual version number of your MPF installation will be whatever
version is the latest.)

5. Setup your Machine Config
----------------------------

* Copy your machine config root folder to ``~/`` which is the same as ``/home/your_username/``.
* Create a new file named ``run.sh`` in ``/home/your_username/your_machine_folder/``
   * Edit the file to contain:

.. code-block:: console

  #!/bin/bash
  xterm -e "cd /home/your_username/your_machine_folder && mpf both -c config"

* Change ``your_username`` to the username you created during installation.
* Change ``your_machine_folder`` to the name of your specific machine folder.
* Change ``config`` part to reflect the name of your top-level config file in ``~/your_machine_folder/config/``.


6. Setup your Machine Config to Auto-execute
--------------------------------------------

When XFCE is executed, it runs all the *Desktop Entries* found within ``~/.config/autostart``.
We'll create one of our own to run the script we just added to our machine config.

* Create the file ``~/.config/autostart/mpf.desktop`` and edit it to contain:

.. code-block:: console

  [Desktop Entry]
  Version=1.0
  Name=MPF
  Comment=Mission Pinball
  Exec=/home/your_username/your_machine_folder/run.sh
  Path=/home/your_username/your_machine_folder/
  Terminal=false
  Type=Application

* Change ``your_username`` to the username you created during installation.
* Change ``your_machine_folder`` to the name of your specific machine folder.

That's it. At this point, you should be able to reboot and watch the system auto-login to XFCE and then launch MPF
using the script we added to your machine config.

Other Considerations
--------------------

If using the SmartMatrix RGB DMD with this setup, you need to add the system
user running your game to the ``dialout`` group.

.. code-block:: console

   sudo usermod -a -G dialout your_username

.. include:: /install/common_problems_and_solutions.rst
