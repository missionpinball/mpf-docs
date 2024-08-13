
# self.machine.hardware_platforms[‘spi_bit_bang’]

`class mpf.platforms.spi_bit_bang.SpiBitBangPlatform(machine)`

Bases: mpf.core.platform.SwitchPlatform

Platform which reads switch via SPI using bit banging.

## Accessing the spi_bit_bang platform via code

Hardware platforms are stored in the `self.machine.hardware_platforms` dictionary, so the spi_bit_bang platform is available via `self.machine.hardware_platforms['spi_bit_bang']`.

## Methods & Attributes

The spi_bit_bang platform has the following methods & attributes available. Note that methods & attributes inherited from base classes are not included here.

`configure_switch(number: str, config: mpf.core.platform.SwitchConfig, platform_config: dict) → mpf.platforms.interfaces.switch_platform_interface.SwitchPlatformInterface`

Configure switch.

`get_hw_switch_states()`

Read initial hardware state.

This will always be false for all inputs on those switches.

`initialize()`

Register handler for late init.

`read_spi(bits)`

Read from SPI.

