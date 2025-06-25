# MockBcpClient

``` python
class mpf.tests.MpfBcpTestCase.MockBcpClient(machine, name, bcp)
```

Bases: `mpf.core.bcp.bcp_client.BaseBcpClient`

A Mock BCP Client.

This is used in tests require BCP for testing but where you don’t actually create a real BCP connection.

## Methods & Attributes

The MockBcpClient has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`accept_connection(receiver, sender)`

Handle incoming connection from remote client.

`connect(config)`

Actively connect client.

`format_log_line(msg, context, error_no) → str`

Return a formatted log line with log link and context.

`ignorable_runtime_exception(msg: str) → None`

Handle ignorable runtime exception.

During development or tests raise an exception for easier debugging. Log an error during production.

`raise_config_error(msg, error_no, *, context=None) → NoReturn`

Raise a ConfigFileError exception.

`read_message()`

Read one message from client.

`send(bcp_command, bcp_command_args)`

Send data to client.

`stop()`

Stop client connection.

`warning_log(msg: str, *args, context=None, error_no=None, **kwargs) → None`

Log a message at the warning level.

These messages will always be shown in the console and the log file.
