---
title: "assets: Config Reference"
---

# assets: Config Reference

--8<-- "config_section.md"

| Valid in | |
|-----|:----:|
|[machine](instructions/machine_config.md) config files |**YES** :white_check_mark:|
|[mode](instructions/mode_config.md) config files|**YES** :white_check_mark:|

The `assets:` section of a config file lets you configure the default
settings for different types of assets based on what folder those assets
are in. Any settings you specify here are just the defaults, though, and
you can still override the defaults for an individual asset by adding an
entry for it to your machine or mode config file.

Let's take a look at an example:

``` yaml
assets:
  images:
    default:
      load: preload
    preload:
      load: preload
    on_demand:
      load: on_demand
    potato:
      some_key: some_value
      something_else: whatever
```

The above config contains the asset settings for *image* assets. Notice
there are 4 entries under `images:`: `default`, `preload`, `on_demand`,
and `potato`. Those names represent sub-folders that could contain image
assets.

Then under each of those, there are one or more key/value pairs. These
key/value pairs are applied to assets located in the sub-folders above.

!!! note

    Although you can create sub-folders nested as many levels deep as you
    wish, only the top-level sub-folder can be listed in the assets section.
    Any assets in sub-folders below the top level will inherit the settings
    from their top-level sub-folder parent.

The `default` entry is special, as it applies to the root folder as well
as any assets that are in folders that are not specified here.

Consider the following files & folders in a machine folder with the
`assets:` section from above:

![image](images/image_asset_folder_structure.png)

In this case, `/your_machine/images/hello.jpg` would have the `default:`
settings applied, `/your_machine/images/preload/special.jpg` would have
the `load: preload` key/value pair applied to it,
`/your_machine/images/potato/toppings/cheese.jpg` would have the
`some_key: some_value` and `something_else: whatever` key/value pairs
applied to it, etc.

The `assets:` section of the config file doesn't really care what the
key/value pairs are. They're just the defaults for the assets in those
folders, and if they're not valid settings then MPF will give you an
error. (Note that different types of assets have different settings
options and different keys & values that are correct.)

Currently MPF supports four kinds of assets. Click on each to go to that
asset type's description in the config file reference which will
explain what settings and be used and what the options are.

Asset types include:

* [shows:](shows.md) (use file_shows entry)
* [images:](images.md)
* [sounds:](sounds.md)
* [videos:](videos.md)
