---
title: Understanding the #config_version setting
---

# Understanding the #config_version setting


Since MPF is mainly "programmed" with YAML-based config files, we need
a way for MPF to know that the config file(s) it's loading are
compatible with the version of MPF that's running.

This is specified in the very first line of a config file (in both the
machine-wide configs and mode config files). You specify the config
version with a list that starts with a hash sign, like this:

``` yaml
#config_version=5
```

In YAML, lines that start with \# are ignored, which means the YAML
processor skips this line, but MPF uses it to make sure the config file
it's trying to load will work with that version of MPF.

Not every new version of MPF changes the config_version number. If we
release a new version of MPF that does not have a new config_version
number, then you can use the new version of MPF without needing to make
any changes to your config files.

## Updating your config files to the latest version

MPF includes a config file migration tool that can automatically migrate
your config files to the latest version.

## Which versions of MPF require which config_versions?

* MPF 0.50+: `#config_version=5`
* MPF 0.30-0.33: `#config_version=4`
* MPF 0.20-0.21: `#config_version=3`
* MPF 0.19: `#config_version=2`
* MPF 0.17-0.18: `#config_version=1`
* MPF 0.1-0.16: config_version not used (a.k.a. config version 0)
