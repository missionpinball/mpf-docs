---
title: Basic Guide
---

# Basic Guide


## Prerequisites

* Comfort with running Linux commands
* Basic knowledge of SSH
* Host OS with VirtualBox 5+ installed and 10 GB+ of free space
* Internet Connection (Only required for Debian install)

## Setting up new VirtualBox machine

1.  In VirtualBox Manager, start a new machine.
    * Name: Choose a name for your VM. This is the name that will be
        used in VirtualBox.
    * Machine Folder: Choose a path
    * Type: `Linux`
    * Version: `Debian-64`
2.  Allocate at least 1 GB (1024 MB) of RAM
3.  Hard Disk:
    * `Create a Virtual Hard Disk Now`
4.  Hard Disk File type:
    * `VDI (VirtualBox Disk Image)`
5.  Storage on physical hard disk
    * `Dynamically Allocated`
6.  Select how much storage you want for the virtual machine. (At least
    8GB, I used 16GB.)
7.  Click `Create`

Tip: Check out the available options in the ⚙️ `Settings` tab of
VirtualBox. The more accustomed you become to these options, the better
you will understand the powerful tools of VirtualBox.

## Downloading Debian

1.  Navigate to [the official Debian download
    site](https://www.debian.org/distrib/netinst).

2.  Under the `Small CDs or USB sticks` header, click on `amd64` to
    download the latest version of Debian.

    (Latest Debian was 10.4.0 at time of writing)

3.  An `.iso` file of approximately 350 MB will be downloaded.

## Installing Debian

1.  Select your Mission Pinball VM from the VirtualBox GUI
2.  Click the green ➡️ `Start` icon
3.  If you have not yet attached the Debian ISO file to your VM, you
    will be prompted to select it now
    * Click the 📂 Folder icon and find your downloaded Debian.iso
        file:

        `debian-10.4.0-amd64-netinst.iso`
4.  Click `Start`
5.  In the virtual machine window, highlight `Graphical Install` and
    click enter
6.  Follow the prompts to install Debian. You may need to navigate using
    the keyboard (using `Tab` and `Enter`) because the VirtualBox Guest
    Additions are not yet installed. That will be done in the next few
    steps.
7.  Make sure to set a root password and setup a new user of your
    choice.

## Setting up `sudo`

The `sudo` command is required for many of the following steps of this
guide. It is likely the user that was created during the Debian install
was not granted sudo access and you will be met with this error if you
try to use sudo:

`[your-user] is not in the sudoers file. This incident will be reported.`

To fix this:

1.  Open a new terminal window
2.  First change into the root user:
    * ``` console
        su -
        ```

    * The `-` is required to reset \$PATH (`usermod` may not work
        without it)
3.  As root, add your username to the sudo group
    * ``` console
        usermod -aG sudo [your-user]
        ```
4.  Exit the root user shell
    * ``` console
        exit
        ```
5.  Verify your username was granted sudo access
    * ``` console
        sudo echo
        ```

    * A reboot may be required for sudo access to take effect

## Setting up the VirtualBox Guest Additions CD

The VirtualBox Guest Additions provide many benefits including [but not
limited to](https://www.virtualbox.org/manual/ch04.html#guestadd-intro):

* Shared folders
* Shared clipboard
* Ability to resize the guest OS window

Full instructions for setting up the VirtualBox Guest Additions CD [can
be found
here](https://linuxize.com/post/how-to-install-virtualbox-guest-additions-on-debian-10/).
An abbreviated version is listed below:

1.  ``` console
    sudo apt update
    sudo apt install build-essential dkms linux-headers-$(uname -r)
    ```

2.  (Host Window) Devices -> "Insert Guest Additions CD Image"

3.  ``` console
    sudo mkdir -p /mnt/cdrom
    sudo mount /dev/cdrom /mnt/cdrom
    ```

4.  ``` console
    cd /mnt/cdrom
    sudo sh ./VBoxLinuxAdditions.run --nox11
    ```

5.  Reboot

6.  If necessary, confirm module is running after reboot:

    ``` console
    lsmod | grep vboxguest
    ```

## Configuring network for SSH

Now is a good time to configure the network cards so we can SSH into the
virtual machine.

1.  Create a new virtual network adapter
    1.  Focus the main VirtualBox Manager window
    2.  File > Host Network Manager
    3.  ➕ `Create`
    4.  Default name is ok (`vboxnet0` in my case)
    5.  Verify subnet mask is `255.255.255.0`
2.  In VirtualBox Manager, open the settings tab for the MPF VM.
    1.  Navigate to the network settings tab
    2.  Click on the `Adapter 2` tab
    3.  Enable the adapter
    4.  Select `Host Only Adapter` as "Attached to"
    5.  Name is the Virtual Network we created earlier (`vboxnet0` in my
        case)
3.  In the *host* OS, verify the VirtualBox virtual network adapter is
    connected
    * The following is for macOS. Your command and output may look
        different

    * ``` console
        ifconfig vboxnet0
        ```

    * ``` console
        vboxnet0: flags=8943<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
               ether 0a:00:27:00:00:00
               inet 192.168.56.1 netmask 0xffffff00 broadcast 192.168.56.255
        ```
4.  In the *guest* OS (Debian), verify the VirtualBox virtual network
    adapter is connected
    * The following is for my installation. Your command and output
        may look different

    * ``` console
        ip addr
        ```

    * ``` console
        [...]
        3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
            link/ether 08:00:27:d8:b5:e6 brd ff:ff:ff:ff:ff:ff
            inet 192.168.56.101/24 brd 192.168.56.255 scope global dynamic noprefixroute enp0s8
               valid_lft 805sec preferred_lft 805sec
            inet6 fe80::e970:3c21:bf92:1f16/64 scope link noprefixroute
               valid_lft forever preferred_lft forever
        [...]
        ```

    * Verify the IP address (`192.168.56.101` in this case) is located
        in the same subnet as the host's IP address found earlier
        (`192.168.56.1`)
5.  Verify you can SSH into the VM:
    * ``` console
        ssh [your-user]@192.168.56.101
        ```

## Installing environment tools

Now is a good time to install tools such as `git` and any other
environment tools you are accustomed with.

Verify that python is installed and using a version you expect:

``` console
python3 -V
```

`Python 3.7.3`

Install pip3 and pkg-config (which MPF needs for mpf-mc):

``` console
sudo apt-get install python3-pip pkg-config
```

## Installing Mission Pinball Framework

Follow the [installation
guide](/install/linux) for MPF on
Linux.

Basic installation:

``` console
pip3 install pip setuptools --upgrade
```

1.  Clone the Debian installer
    * ``` console
        cd ~
        git clone https://github.com/missionpinball/mpf-debian-installer/
        cd mpf-debian-installer/
        chmod +x install && sudo ./install
        ```
2.  Setup the mpf directory and clone examples
    * ``` console
        cd ~
        mkdir mpf
        cd mpf
        git clone https://github.com/missionpinball/mpf-examples
        ```
3.  Run the Demo Man example. In the VBox Desktop, open terminal and
    execute:
    * ``` console
        cd ~/mpf/mpf-examples/demo_man
        mpf both -X
        ```

    * Verify mpf opens in terminal and mpf-mc opens in a new window.

    * Control Keys:
        * `S` - Start game
        * `L` - Launch ball
        * `X` - Fire slingshot
        * `1` - Drain ball
        * `ESC` - Close mpf-mc and quit

    * Follow the rest of the Demo Man [example
        guide](/examples/demo_man).

!!! warning

    Some users have reported having trouble with OpenGL on a macOS host.

    If mpf-mc shows only a blank screen inside your VM, please [open an
    issue](https://github.com/missionpinball/mpf-mc/issues/new).

## Installing and Running MPF-Monitor

The full installation guide for setting up MPF-Monitor [can be found
here](/tools/monitor/installation).

1.  Install PyQt6 (may already be installed):
    * ``` console
        sudo apt-get install python3-pyqt6
        ```
2.  Install mpf-monitor:
    * ``` console
        pip install mpf-monitor
        ```
3.  Start mpf (with mc) and mpf monitor (in separate terminal tabs):
    * ``` console
        mpf both -X
        ```

    * ``` console
        mpf monitor
        ```
4.  Adjust the size of switches and lights by adding the following to
    the first line of your `monitor.yaml` file:
    * ``` yaml
        device_size: 0.1
        ```

    * More info at [MPF Monitor
        docs](/tools/monitor/running).
