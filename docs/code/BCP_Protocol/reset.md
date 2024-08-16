
# reset (BCP command)
This command notifies the media controller that the pin controller is in the process of performing a reset. If necessary, the media controller should perform its own reset process. The media controller must respond with a [reset_complete](reset_complete.md) command when finished.

## Origin
Pin controller

## Parameters
None

## Response
[reset_complete](reset_complete.md) when reset process has finished
