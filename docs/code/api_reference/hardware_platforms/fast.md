
# self.machine.hardware_platforms[‘fast’]

`class mpf.platforms.fast.fast.FastHardwarePlatform(machine)`

Bases: mpf.core.platform.ServoPlatform, mpf.core.platform.LightsPlatform, mpf.core.platform.DmdPlatform, mpf.core.platform.SwitchPlatform, mpf.core.platform.DriverPlatform

Platform class for the FAST hardware controller.

## Accessing the fast platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the fast platform is available via `self.machine.hardware_platforms['fast']`.

## Methods & Attributes

The fast platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`clear_hw_rule(switch, coil)`

Clear a hardware rule.

This is used if you want to remove the linkage between a switch and some driver activity. For example, if you wanted to disable your flippers (so that a player pushing the flipper buttons wouldn’t cause the flippers to flip), you’d call this method with your flipper button as the sw_num.

Parameters:

* **switch** – The switch whose rule you want to clear.
* **coil** – The coil whose rule you want to clear.

`configure_dmd()`

Configure a hardware DMD connected to a FAST controller.

`configure_driver(config: mpf.core.platform.DriverConfig, number: str, platform_settings: dict) → mpf.platforms.fast.fast_driver.FASTDriver`

Configure a driver.

Parameters:

* **config** – Driver config.
* **number** – Number of this driver.
* **platform_settings** – Platform specific settings.

Returns: Driver object

`configure_light(number, subtype, platform_settings) → mpf.platforms.interfaces.light_platform_interface.LightPlatformInterface`

Configure light in platform.

`configure_servo(number: str) → mpf.platforms.fast.fast_servo.FastServo`

Configure a servo.

Parameters:

* **number** – Number of servo

Returns: Servo object.

`configure_switch(number: str, config: mpf.core.platform.SwitchConfig, platform_config: dict) → mpf.platforms.fast.fast_switch.FASTSwitch`

Configure the switch object for a FAST Pinball controller.

FAST Controllers support two types of switches: local and network. Local switches are switches that are connected to the FAST controller board itself, and network switches are those connected to a FAST I/O board.

MPF needs to know which type of switch is this is. You can specify the switch’s connection type in the config file via the connection: setting (either local or network).

If a connection type is not specified, this method will use some intelligence to try to figure out which default should be used.

If the DriverBoard type is fast, then it assumes the default is network. If it’s anything else (wpc, system11, bally, etc.) then it assumes the connection type is local. Connection types can be mixed and matched in the same machine.

Parameters:

* **number** – Number of this switch.
* **config** – Switch config.
* **platform_config** – Platform specific settings.

Returns: Switch object.

`static convert_number_from_config(number)`

Convert a number from config format to hex.

`classmethod get_coil_config_section()`

Return coil config section.

`get_hw_switch_states()`

Return hardware states.

`get_info_string()`

Dump infos about boards.

`classmethod get_switch_config_section()`

Return switch config section.

`initialize()`

Initialise platform.

`parse_light_number_to_channels(number: str, subtype: str)`

Parse light channels from number string.

`process_received_message(msg: str, remote_processor: str)`

Send an incoming message from the FAST controller to the proper method for servicing.

Parameters:

* **msg** – messaged which was received
* **remote_processor** – Processor which sent the message.

`receive_bootloader(msg, remote_processor)`

Process bootloader message.

`receive_local_closed(msg, remote_processor)`

Process local switch closed.
Parameters:

* **msg** – switch number
* **remote_processor** – Processor which sent the message.

`receive_local_open(msg, remote_processor)`

Process local switch open.

Parameters:

* **msg** – switch number
* **remote_processor** – Processor which sent the message.

`receive_nw_closed(msg, remote_processor)`

Process network switch closed.

Parameters:

* **msg** – switch number
* **remote_processor** – Processor which sent the message.

`receive_nw_open(msg, remote_processor)`

Process network switch open.

Parameters:

* **msg** – switch number
* **remote_processor** – Processor which sent the message.

`receive_sa(msg, remote_processor)`

Receive all switch states.

Parameters:

* **msg** – switch states as bytearray
* **remote_processor** – Processor which sent the message.

`register_io_board(board)`

Register an IO board.

Parameters:

* **board** – ‘mpf.platform.fast.fast_io_board.FastIoBoard’ to register

`register_processor_connection(name: str, communicator)`

Register processor.

Once a communication link has been established with one of the processors on the FAST board, this method lets the communicator let MPF know which processor it’s talking to.

This is a separate method since we don’t know which processor is on which serial port ahead of time.

Parameters:

* **communicator** – communicator object
* **name** – name of processor

`set_pulse_on_hit_and_enable_and_release_and_disable_rule(enable_switch: mpf.core.platform.SwitchSettings, eos_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings, repulse_settings: Optional[mpf.core.platform.RepulseSettings])`

Set pulse on hit and enable and release and disable rule on driver.

`set_pulse_on_hit_and_enable_and_release_rule(enable_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings)`

Set pulse on hit and enable and relase rule on driver.

`set_pulse_on_hit_and_release_and_disable_rule(enable_switch: mpf.core.platform.SwitchSettings, eos_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings, repulse_settings: Optional[mpf.core.platform.RepulseSettings])`

Set pulse on hit and release and disable rule on driver.

`set_pulse_on_hit_and_release_rule(enable_switch, coil)`

Set pulse on hit and release rule to driver.

`set_pulse_on_hit_rule(enable_switch: mpf.core.platform.SwitchSettings, coil: mpf.core.platform.DriverSettings)`

Set pulse on hit rule on driver.

`start()`

Start listening for commands and schedule watchdog.

`stop()`

Stop platform and close connections.

`update_firmware() → str`

Upgrade the firmware of the CPUs.

`update_leds()`

Update all the LEDs connected to a FAST controller.

This is done once per game loop for efficiency (i.e. all LEDs are sent as a single update rather than lots of individual ones).

Also, every LED is updated every loop, even if it doesn’t change. This is in case some interference causes a LED to change color. Since we update every loop, it will only be the wrong color for one tick.

