# RGBColor API Reference

``` python
class mpf.core.rgb_color.RGBColor(color: Union[RGBColor, str, List[int], Tuple[int, int, int]] = None)
```

Bases: `object`

One RGB Color.

## Methods & Attributes

The RGBColor has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`static add_color(name: str, color: Union[RGBColor, str, List[int], Tuple[int, int, int]])`

Add (or updates if it already exists) a color.

Note that this is not permanent, the list is reset when MPF restarts (though you can define your own custom colors in your config file’s colors: section). You can use this function to dynamically change the values of colors in shows (they take place the next time an LED switches to that color).

Parameters:

* **name** – String name of the color you want to add/update
* **color** – The color you want to set. You can pass the same types as the RGBColor class constructor, including a tuple or list of RGB ints (0-255 each), a hex string, an RGBColor instance, or a dictionart of red, green, blue key/value pairs.

`static blend(start_color, end_color, fraction)`

Blend two colors.

Parameters:

* **start_color** – The start color
* **end_color** – The end color
* **fraction** – The fraction between 0 and 1 that is used to set the blend point between the two colors.

Returns: An RGBColor object that is a blend between the start and end.


`red`

Return the red component of the RGB color representation.

`blue`

Return the blue component of the RGB color representation.

`green`

Return the green component of the RGB color representation.

`hex`

Return a 6-char HEX representation of the color.

`static hex_to_rgb(hex_string: str, default=None) → Tuple[int, int, int]`

Convert a HEX color representation to an RGB color representation.

Parameters:

* **hex_string** – The 3- or 6-char hexadecimal string representing the color value.
* **default** – The default value to return if \_hex is invalid.

Returns: RGB representation of the input HEX value as a 3-item tuple
with each item being an integer 0-255.

`name`

Return the color name or None.

Returns a string containing a standard color name or None if the current RGB color does not have a standard name.

`static name_to_rgb(name: str, default=(0, 0, 0)) → Tuple[int, int, int]`

Convert a standard color name to an RGB value (tuple).

If the name is not found, the default value is returned. :param name: A standard color name. :param default: The default value to return if the color name is not found. :return: RGB representation of the named color. :rtype: tuple

`static random_rgb() → Tuple[int, int, int]`

Generate a uniformly random RGB value.
Returns:	A tuple of three integers with values between 0 and 255 inclusive

`rgb`

Return an RGB representation of the color.

`static rgb_to_hex(rgb: Tuple[int, int, int]) → str`

Convert an RGB color representation to a HEX color representation.

``` python
(r, g, b) :: r -> [0, 255]
g -> [0, 255] b -> [0, 255]
```

Parameters:

* **rgb** – A tuple of three numeric values corresponding to the red, green, and blue value.

Returns:	HEX representation of the input RGB value.
Return type:	str

`static string_to_rgb(value: str, default=(0, 0, 0)) → Tuple[int, int, int]`

Convert a string which could be either a standard color name or a hex value to an RGB value (tuple).

If the name is not found and the supplied value is not a valid hex string it raises an error. :param value: A standard color name or hex value. :param default: The default value to return if the color name is not found and the supplied value is not a valid hex color string. :return: RGB representation of the named color. :rtype: tuple
