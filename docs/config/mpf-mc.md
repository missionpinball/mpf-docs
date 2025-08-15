---
title: "mpf-mc: Config Reference"
---

# mpf-mc: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `mpf-mc:` section of your config is where you configure options for
the MC itself.

## Required Settings

All of these settings are required in the `mpf-mc:` section. However,
MPF-MC includes a default config file called `mcconfig.yaml` which
includes all these settings with their defaults. So you only need to
add/enter these if you want to change something from the default.

### bcp_port:

Single integer value, default is `5050`.

This is the TCP port that the MC listens on for incoming BCP
connections. If you change this from the

### bcp_interface:

String, default is `localhost`.

The interface to bind for the BCP connection.

### fps:

Single integer value, default is `30`.

Limit the frames per second to `fps`. This prevents using excessive CPU
for MPF MC.

### allow_invalid_config_sections:

Single boolean value, default is `True`.

Allow sections which are not known to MPF.
