---
title: GMC Window Filters
---

# GMC Window Filters

GMC includes a handful of shaders for applying filter effects to your displays. They are outlined here for you to enjoy, or you can create your own using the powerful [Godot Shader Language](https://docs.godotengine.org/en/stable/tutorials/shaders/index.html)

!!! note

    These shaders have been tested but not tried out in the wild, so you may encounter unexpected behavior or weirdness. Please let us know if you see anything strange!

## Configuring Filters

You can enable and configure the default filters in your *gmc.cfg* file by creating a `[filter]` section. You then specify the filter name and any relevant parameters in that section.

An example configuration might look like this:

``` yaml
[filter]
filter="virtual_dmd"
columns=120
rows=45
hardness=5
spacing=2
```

## Filter Config Reference

The following reference documents the filters included in GMC and their configuration parameters.

### Virtual DMD

``` ini
[filter]
filter="virtual_dmd"
```

The most popular shader filter creates the effect of a color DMD by pixelating the screen and adding an overlay of dots.

#### `color`

Single value, type `Color(R,G,B,A)`. Default `1.0, 1.0, 1.0, 1.0`

The color of the dot overlay. Must be specified as four (RGBA) floats between `0.0` and `1.0`. All four values (including opacity) are required.

``` ini
color=Color(1.0, 0.5, 0.2, 1.0)
```

#### `columns`

Single value, type `int`. Default `128`

The number of columns (horizontal pixels) to render.

#### `hardness`

Single value, type `float`. Default `5.0`

The hardness of the edge of the dot circles (or, the distance from center at which the edge of the circle starts). Higher numbers are harder (i.e. sharper dots) and lower numbers are softer (i.e. fuzzier).

A value of `0.0` will be entirely black, so `1.5` is probably the lowest you'll want to try. The upper bound will depend on the size of the dots, so play around until you like it!

#### `rows`

Single value, type `int`. Default `32`

The number of rows (vertical pixels) to render.

#### `spacing`

Single value, type `float`. Default `2.0`

The distance from the edge of the "pixel" to the outer edge of the circle. A value of `1.0` means no spacing, and dots will not appear. Higher values put more space between the dots (i.e. smaller dots).


### DMD Dots


``` ini
[filter]
filter="dmd_dots"
```

This filter renders the dots of the Virtual DMD filter, but without pixelating the underlying content. You may want this if you are already using pixel art or a different method of pixelation, but still want the DMD look.

The configuration options for `dmd_dots` are the same as `virtual_dmd`,


### Pixelate


``` ini
[filter]
filter="pixelate"
```

This filter pixelates the display into blocks with a fixed number of rows and columns. It's similar to what's done in `virtual_dmd` but without the dot overlay.

You may want this if you're making a pixel-art style game, or if you are rendering to an *actual* DMD.

#### `columns`

Single value, type `int`. Default `128`

The number of columns (horizontal pixels) to render.

#### `rows`

Single value, type `int`. Default `32`

The number of rows (vertical pixels) to render.


## Custom Filters

You can also create your own custom filters by making a shader yourself. There are plenty of great examples in the [Godot Shaders Library](https://godotshaders.com/shader-type/canvas_item/) for you to experiment with (note that only *Canvas Item* shaders will work).

!!! example  "Try this one!"

    A great example shader to try is the [VCR Analog Distortions](https://godotshaders.com/shader/vcr-analog-distortions/) that creates curvature and scan lines like an old VHS tape!

To use a custom shader, you must first create a Shader Material file and save it in your project. In the Godot Editor *FileSystem* panel, choose where you want your shader to live and right click to *Create New > Resource...*.  Select `Shader` as the resource type (just `Shader`, not any other shader-related type) and choose a good name for it.

Back in the *FileSystem* panel, find your new shader file (with the *.gdshader* extension) and double-click it to bring up the *Shader Editor* panel. Put in your shader code and save.

Once again in the *FileSystem* panel, right click on your shader file and select *Copy Path*. Open your *gmc.cfg* config file and paste that path as the `filter=` value in the `filter` section. Make sure to add quotes around the path!

``` ini
[filter]
filter="res://shaders/my_awesome_shader.gdshader"
awesomeness=9000
frequency=0.5
```

If your shader requires any parameters (using `uniform` variables) that you want to configure in *gmc.cfg* instead of hard-coding in the shader, you can add those parameters as key/value pairs in the filter config section as well.