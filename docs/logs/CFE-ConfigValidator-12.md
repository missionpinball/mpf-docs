---
title: CFE-ConfigValidator-12: Item is not a dict
---

# CFE-ConfigValidator-12: Item is not a dict


This error occurs when MPF expects a dictionary in a config setting but
found something else.

## Examples

For instance, `show_tokens` in a
[show_player](../config/show_player.md) has to
be a dictionary:

``` mpf-config
show_player:
  some_event:
    your_show_name:
      show_tokens:
        dict_key1: "dict_value1"
        dict_key2: "dict_value2"
```

You can see which settings are dicts in the
[config reference](../config/index.md) of your
device.

## Common Pitfalls

### Using a List instead of a Dict

This is a list in yaml:

``` yaml
your_setting:
  - item1_in_list
  - item2_in_list
```

This is a dictionary:

``` yaml
your_setting:
  key1_in_dict: value1_in_dict
  key2_in_dict: value2_in_dict
```

This is a list of dictionaries (used in shows for example):

``` yaml
your_setting:
  - key1_in_dict_in_list1: value1_in_dict_in_list1
  - key1_in_dict_in_list2: value1_in_dict_in_list2
    key2_in_dict_in_list2: value2_in_dict_in_list2
```

### Incorrect Indent

With nested configs (i.e. show_player, slide_player or widget_player)
you might have used an option which should be indented one level further
or one level less. This can sometimes be a bit tricky. Using an
[IDE with the MPF language server](../tools/language_server/index.md) can help here.

## Need more help troubleshooting?

Have a look at our [Troubleshooting](../troubleshooting/index.md) section. It might give you some hints for certain classes of
problems.

## What if this did not fix your problem?

Please tell us about your error in the [community forum](../community/index.md) and we might
be able to update this page afterwards. Or even better:
[You help us to update it afterwards](../about/help_docs.md).

## Is something missing here? Do you have a helpful hint for others experiencing this error?

Please
[create a Pull Request and add it](../about/help_docs.md). Alternatively, please tell us in the [community forum](../community/index.md).

## Related How To guides

* [config reference](../config/index.md)
