---
title: Installing MPF Monitor
---

# Installing MPF Monitor


The current stable version of MPF Monitor is `0.56` which matches the stable versions of MPF and MPF-MC.
You can install it via `pip` (or `pip3`, or however you installed MPF).

``` doscon
pip install mpf-monitor
```

The dev branch of MPF Monitor has been updated for MPF 0.57. You can install it by adding the `--pre` flag:

``` doscon
pip install mpf-monitor --pre
```

There seems to be an issue running MPF Monitor 0.57 on Python 3.11. Details [here](https://github.com/missionpinball/mpf-monitor/issues/41). It works fine on Python 3.9. We haven't tried on 3.10, so who knows? We could use some help understanding what's going on here.
