---
title: Installing MPF on a Raspberry Pi
---

# Installing MPF on a Raspberry Pi

These instructions are based on those created by [Gilles Bouthenot](https://github.com/orgs/missionpinball/discussions/115). They use a Python virtual environment without system-wide Python packages, and you can have multiple versions Python if you need.

A few other notes:

* These instructions are specifically made for a Raspberry Pi 5 running Raspberry Pi OS "Bookworm," which appears to have the power to run both MPF and MPF-MC. Older models strugged with video and sounds, but may work in certain scenarios. These instructions should work for them as well.
* It's assumed that you've already installed Raspberry Pi OS, expanded your filesystem, configured wifi, and so on. If you need help getting to that point, check out the [Raspberry Pi documentation](https://www.raspberrypi.com/documentation/computers/getting-started.html).
* The Pi 5 does not have a dedicated Audio Out jack like prior models. You will need a USB audio interface. [This one has been tested](https://www.amazon.com/Adapter-External-Converter-Compatible-Desktops/dp/B099FLWJD3) and is known to work. 
* We're assuming you're not developing your game from the Pi, so these instructions omit mpf-monitor and the MPF Language Server. It may or may not be possible to run those. If you need one or both and get them working, feel free to edit this doc with instructions.
* The versions of MPF and MPF-MC available via pip are not able to run on Raspberry Pi. We will need to install in "editable" mode for the time being, but this page will be updated if and when installation via pip is possible.

## Prerequisites and dependencies

To get started, log in to the terminal (locally or via SSH) and update your device and install some dependencies:

``` shell
sudo apt update
sudo apt upgrade

# Dependencies:
sudo apt-get install libssl-dev libncurses-dev libffi-dev libreadline-dev libbz2-dev libsqlite3-dev liblzma-dev tk-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libsdl2-mixer-dev libavfilter-dev libsdl2-dev libsdl2-image-dev libavcodec-dev libavformat-dev libswscale-dev libavdevice-dev

# These are for mpf-monitor and are not necessarily needed
sudo apt-get install libjpeg-dev libxcb-cursor0 libxkbcommon-x11-0 libxcb-icccm4 libxcb-keysyms1 libxcb-shape0 xsel
```

## Installing pyenv

Now we need to install pyenv, which will both install a specific version of Python and create a virtual environment. To do this, follow these steps:

``` shell
# download the pyenv installer
wget https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer

# execute the installer
bash pyenv-installer

# clean up
rm pyenv-installer

# Update your bash profile to customise the shell at login
cat <<'EOF'>>.bashrc
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
EOF
exec $SHELL

# Check to ensure pyenv is available (A list of pyenv commands is the expected output)
pyenv
```

## Installing Python

Next step is to install Python itself and set up the virtual environment. We'll use Python 3.9.18 since it's compatible with both MPF 0.56 and 0.57, and is the most recent version of Python 3.9.

``` shell
# python3.9 compilation. Note this can take a while since Python is being downloaded and compiled from source
pyenv install 3.9.18

# Create virtual environment
pyenv virtualenv 3.9.18 mpf

# Activate virtual environment
pyenv activate 3.9.18/envs/mpf

# Assuming that works, let's add that command to .bashrc so that the virtual environment activates at each login
cat <<'EOF'>>.bashrc
pyenv activate 3.9.18/envs/mpf
EOF
exec $SHELL
```

## Installing MPF

Now it's time to install MPF. As mentioned, installing automatically via pip isn't possible right now, but that's not a show stopper. With a few extra steps, we can get things up and running in "editable" mode (which still uses pip, but in a different way).

Note: Ensure you're doiong this with the Python pyenv environment activated! You'll see the terminal prompt change to something like this `(3.9.18/envs/mpf) pi@raspberrypi:~ $ `

``` shell
# Upgrade pip
pip install --upgrade pip

# clone mpf repository (note 0.56.x branch has been specified)
git clone -b 0.56.x https://github.com/missionpinball/mpf-mc.git ~/mpf-git/mpf

# install MPF
cd ~/mpf-git/mpf
pip install –e .


# clone mpf-mc repository (note 0.56.x branch has been specified)
git clone -b 0.56.x https://github.com/missionpinball/mpf.git ~/mpf-git/mpf-mc

# install MPF-MC
cd ~/mpf-git/mpf-mc
pip install –e .
```

That's it! Now it's time to test. 

## Tests
You'll need to get mpf-examples first, then make a few tweaks to the demo_man config before you can test.

``` shell
# clone mpf-examples repo
git clone -b 0.56.x https://github.com/missionpinball/mpf-examples.git ~/mpf-git/mpf-examples

# switch to the demo_man configs folder
cd ~/mpf-git/mpf-examples/demo-man/config
```

From here, you'll need to edit two files. How you do this is up to you, but if you're relatively new the easiest way is probably to use `nano` from the command line. Simply run `nano filename.yaml` to open the file. 

First, open hardware.yaml and page down towards the bottom. In the `sound_system:` section towards the bottom, change the `enabled: false` line to `enabled: true`

If using nano, push Control-X to exit, Y to save. Then open the config.yaml file to turn on BCP. At the top of the file, you'll see the `bcp:` section. Simply comment out the `connections: None` line by placing a # in front of it, like this: `# connections: None`

To run the test, ensure your virtual environment is activated (it should be since you added it to your bash profile) and that you have a display connected. 

Note: If you're connected via SSH, you'll need to specify which display should be used. The default is 0, but your configuration might be different. To do this, simply run the following command (remember - you only need to do this if you're not using the local console, either directly or via VNC):

``` shell
# set default display for windowed apps
export DISPLAY=:0
```
To test MPF with the demo-man game, follow these steps:

``` shell
# Switch to demo-man directory
cd ~/mpf-git/mpf-examples/demo-man

# start MPF
mpf both -X
```

You should see MPF run, and the demo-man DMD animations running. If you do, you're in good shape!

To test the media controller to ensure it works, you can switch to the mc_demo folder and run MPF.

``` shell
# switch to mc_demo directory
cd ../mc_demo

# start MPF
mpf both -X
```

You can step left and right through the slides to see animations and videos. You can also test audio here by listening for sounds during slide transitions.

Now that MPF is working on the Raspberry Pi, there are steps to take to tweak the device itself and harden it for use in the machine. Those are A) not fully known and B) outside the scope of this page, but as information becomes available, it can be added. 



