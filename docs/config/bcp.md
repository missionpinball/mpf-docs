---
title: "bcp: Config Reference"
---

# bcp: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**NO** :no_entry_sign:|

The `bcp:` section of your config file controls how the MPF core engine
communicates with the standalone media controller.

There's a default `bcp:` section in the default `mpfconfig.yaml`
system-wide defaults section that should be fine to get started, and
then you can override it if needed for a specific situation:

``` yaml
bcp:
  connections:
    local_display:
      host: localhost
      port: 5050
      type: mpf.core.bcp.bcp_socket_client.BCPClientSocket
      required: true
      exit_on_close: true
  servers:
    url_style:
      ip: 127.0.0.1
      port: 5051
      type: mpf.core.bcp.bcp_socket_client.BCPClientSocket
  debug: false
```

## Optional settings

The following sections are optional in the `bcp:` section of your
config. (If you don't include them, the default will be used).

### connections:

List of one (or more) values, each is a type:
[bcp_connection:](bcp_connection.md).
Defaults to empty.

The `connections:` section is where you can specify the
connections the MPF core engine will make to standalone media
controllers. MPF supports connecting to multiple media controllers
simultaneously which is why you can add multiple entries here.

### debug:

Single value, type: `boolean` (`true`/`false`). Default: `false`

Set this to true to see more debug messages in the log.

### servers:

List of one (or more) values, each is a type:
[bcp_server:](bcp_server.md). Defaults to
empty.

The `servers:` section is where you can specify bcp server
instances which can be connected from other processes. For instance,
this is used for the
[service cli](../running/commands/service.md).
MPF supports connecting to multiple servers simultaneously which is why
you can add multiple entries here.

## Related Pages:

* [The MPF Unity BCP Server](../mc/unity_bcp_server.md)
* [Creating your own Media Controller](../mc/creating_your_own.md)
* [bcp API Reference](../code/api_reference/core/bcp.md)
