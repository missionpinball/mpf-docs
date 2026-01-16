---
title: API Reference - Utility Functions
---

# Utility Functions API Reference

``` python
class mpf.core.utility_functions.Util`
```

Bases: `object`

Utility functions for MPF.

## Methods & Attributes

The Utility Functions has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`static any(futures: Iterable[_asyncio.Future], loop, timeout=None)`

Return first future.

`static bin_str_to_hex_str(source_int_str: str, num_chars: int) → str`

Convert binary string to hex string.

`static cancel_futures(futures: Iterable[_asyncio.Future])`

Cancel futures.

`static chunker(l, n)`

Yield successive n-sized chunks from l.

`static convert_to_simply_type(value)`

Convert value to a simple type.

`static convert_to_type(value, type_name)`

Convert value to type.

`static db_to_gain(db: float) → float`

Convert a value in decibels (-inf to 0.0) to a gain (0.0 to 1.0).

Parameters:

* **db** – The decibel value (float) to convert to a gain

Returns float.

`static dict_merge(a, b, combine_lists=True) → dict`

Recursively merge dictionaries.

Used to merge dictionaries of dictionaries, like when we're merging together the machine configuration files. This method is called recursively as it finds sub-dictionaries.

For example, in the traditional python dictionary update() methods, if a dictionary key exists in the original and merging-in dictionary, the new value will overwrite the old value.

Consider the following example:

Original dictionary: `config['foo']['bar'] = 1`

New dictionary we're merging in: `config['foo']['other_bar'] = 2`

Default python dictionary update() method would have the updated dictionary as this:

``` python
{'foo': {'other_bar': 2}}
```

This happens because the original dictionary which had the single key bar was overwritten by a new dictionary which has a single key other_bar.)

But really we want this:

``` python
{'foo': {'bar': 1, 'other_bar': 2}}
```

This code was based on this: https://www.xormedia.com/recursively-merge-dictionaries-in-python/

Parameters:

* **a (dict)** – The first dictionary
* **b (dict)** – The second dictionary
* **combine_lists (bool)** – Controls whether lists should be combined (extended) or overwritten. Default is True which combines them.

Returns the merged dictionaries.

`static event_config_to_dict(config) → dict`

Convert event config to a dict.

`static first(futures: Iterable[_asyncio.Future], loop, timeout=None, cancel_others=True)`

Return first future and cancel others.

`static get_from_dict(dic, key_path)`

Get a value from a nested dict (or dict-like object) from an iterable of key paths.

Parameters:

* **dic** – Nested dict of dicts to get the value from.
* **key_path** – iterable of key paths

Returns the value from the dict.

This code came from here: http://stackoverflow.com/questions/14692690/access-python-nested-dictionary-items-via-a-list-of-keys

`static get_named_list_from_objects(switches) → List[str]`

Return a list of names from a list of switch objects.

`static hex_string_to_int(inputstring: str, maxvalue: int = 255) → int`

Take a string input of hex numbers and an integer.

Parameters:

* **inputstring** – A string of incoming hex colors, like ffff00.
* **maxvalue** – Integer of the max value you'd like to return. Default is 255. (This is the real value of why this method exists.)

Returns integer representation of the hex string.

`static hex_string_to_list(input_string, output_length=3) → List[int]`

Take a string input of hex numbers and return a list of integers.

This always groups the hex string in twos, so an input of ffff00 will be returned as [255, 255, 0].

Parameters:

* **input_string** – A string of incoming hex colors, like ffff00.
* **output_length** – Integer value of the number of items you'd like in your returned list. Default is 3. This method will ignore extra characters if the input_string is too long, and it will pad the left with zeros if the input string is too short.

Returns list of integers, like [255, 255, 0].

Raises ValueError if the input string contains non-hex chars.

`static int_to_hex_string(source_int: int) → str`

Convert an int from 0-255 to a one-byte (2 chars) hex string, with uppercase characters.

`static is_hex_string(string: str) → bool`

Return true if string is hex.

`static is_power2(num: int) → bool`

Check a number to see if it's a power of two.

Parameters:

* **num** – The number to check

Returns True or False.

`static keys_to_lower(source_dict) → Union[dict, list]`

Convert the keys of a dictionary to lowercase.

Parameters:

* **source_dict** – The dictionary you want to convert.

Returns a dictionary with lowercase keys.

`static list_of_lists(incoming_string)`

Convert an incoming string or list into a list of lists.

`static normalize_hex_string(source_hex: str, num_chars: int = 2) → str`

Take an incoming hex value and convert it to uppercase and fills in leading zeros.

Parameters:

* **source_hex** – Incoming source number. Can be any format.
* **num_chars** – Total number of characters that will be returned. Default is two.

Returns string, uppercase, zero padded to the num_chars.

Example usage: Send “c” as source_hex, returns “0C”.

`static power_to_on_off(power: float, max_period: int = 20) → Tuple[int, int]`

Convert a float value to on/off times.

`static pwm32_to_hex_string(source_int: int) → str`

Convert a PWM32 value to hex.

`static pwm32_to_int(source_int: int) → int`

Convert a PWM32 value to int.

`static pwm8_to_hex_string(source_int: int) → str`

Convert an int to a PWM8 string.

`static pwm8_to_int(source_int: int) → int`

Convert a PWM8 value to int.

`static race(futures: Dict[_asyncio.Future, str], loop)`

Return key of first future and cancel others.

`static raise_exceptions(future: _asyncio.Future) → None`

Re-raise any error except CancelledError on this exception.

Use this with add_done_callback on any future which is not awaited directly to prevent swallowed exceptions.

`static set_in_dict(dic, key_path, value)`

Set a value in a nested dict-like object based on an iterable of nested keys.

Parameters:

* **dic** – Nested dict of dicts to set the value in.
* **key_path** – Iterable of the path to the key of the value to set.
* **value** – Value to set.

`static string_to_class(class_string: str) → Callable[[...], Any]`

Convert a string like mpf.core.events.EventManager into a Python class.

Parameters:

* **class_string (str)** – The input string

Returns a reference to the python class object.

This function came from here: http://stackoverflow.com/questions/452969/does-python-have-an-equivalent-to-java-class-forname

`static string_to_event_list(string: Union[str, List[str], None]) → List[Any]`

Convert a comma-separated and/or space-separated event string into a Python list if not already a list.

This version honors placeholders/templates for events.

Parameters:

* **string** – The string you'd like to convert.

Returns a python list object containing whatever was between commas in the string.

`static string_to_gain(gain_string: str) → float`

Convert string to gain.

Decode a string containing either a gain value (0.0 to 1.0) or a decibel value (-inf to 0.0) into a gain value (0.0 to 1.0).

Parameters:

* **gain_string** – The string to convert to a gain value

Returns float containing a gain value (0.0 to 1.0).

`static string_to_list(string: Union[str, List[str], None]) → List[Any]`

Convert a comma-separated string into a Python list if not already a list.

Parameters:

* **string** – The string you'd like to convert.

Returns a python list object containing whatever was between commas in the string.

`static string_to_ms(time_string: str) → int`

Decode a string of real-world time into an int of milliseconds.

Example inputs:

200ms 2s None

If no “s” or “ms” is provided, this method assumes “milliseconds.”

If time is 'None' or a string of 'None', this method returns 0.

Returns an integer. The examples listed above return 200, 2000 and 0, respectively.

`static string_to_secs(time_string: str) → float`

Decode a string of real-world time into an float of seconds.

See `string_to_ms` for a description of the time string.
