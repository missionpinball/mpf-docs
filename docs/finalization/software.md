---
title: Tuning Software for Production
---

# Tuning Software for Production


## Run MPF in production mode

YAML is quite slow to parse and reading configs dominates the startup
time of MPF and MPF-MC. This is mostly fine during development and we
can partially mitigate the costs by caching. However, things are
different when running a production machine as caching will not work on
a cold boot with a typical read-only setup. Usually production machine
setups use less beefy computers with slower disks which makes thinks
even worse.

Starting with version 0.54 MPF has a production mode which will use
pre-compiled config bundles for much faster start-up times.
Additionally, this will disable some expensive config and runtime
validations to increase performance. Furthermore this will reduce the
amount of debug output.

First run `mpf build production_bundle` which will create
`mpf_config.bundle` and `mpf_mc_config.bundle`. You have to recreate
those files after every config, mode or show change. Those bundles
include all yaml files but not any other assets (such as videos or
sounds). Second, add the `-P` flag to the commandline to run MPF in
production mode.

MPF will also try to keep running in some cases instead of exiting the
game. This will not be helpful to find bug but a when you ship machines
you won't see the log anyway. Finally, MPF will try to initialize for
`30s` and then exit in case something went wrong. You can use that to
run MPF in a while loop or to reboot your PC in case initialization went
wrong.

## Run MPF without text UI

Text UI costs some performance so disable it in production or on less
powerful hardware in general. You can do this by adding the `-t` flag to
the MPF commandline.

## Install the latest Python version

For instance, MPF runs significantly faster on Python 3.6 than on 3.5.
Similarly, 3.5 is faster than 3.4. We expect the same for the next
releases. You might not need this if you are using PyPy.

## Install uvloop

When running MPF on linux install `uvloop` will reduce latency and
increase throughput for I/O operations. This will keep your game
responsive:

``` console
pip3 install uvloop
```

MPF will use uvloop once it is available.

## Run MPF with PyPy

PyPy is a replacement for standard Python. It uses a Just-in-time
compiler that makes it facter and often use less memory. PyPy does not
support all Python code, and currently works for MPF, but not for MPF-MC
because kivy is not yet compatible with PyPy. Performance and latency
improvements are around 10x in our benchmarks so this might be essential
on low-end hardware. Download PyPy and install it. Since PyPy is a
separate Python environment you need to install pip and reinstall all
pip packages for PyPy.

``` console
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
pypy get-pip.py
pypy -m pip install mpf
```

Afterward, you can start MPF within your game folder using:

``` console
pypy -m mpf game
```

Instead of the `mpf` command just use `pypy -m mpf`. For `pip` use
`pypy -m pip`.

You still need to run MPF-MC using normal Python. This might change in
the future.

## Some random hints

* Optimize assets for your hardware. Audio should have the same
    sampling rate as your hardware is using. Images and videos should be
    at native resolution to prevent scaling up or down.
* Re-encode your videos in a codec which can be efficiently decoded on
    your target hardware.
* Let us know if we missed something here.
