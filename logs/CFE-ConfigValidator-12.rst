CFE-ConfigValidator-12: Item is not a dict
==========================================

This error occurs when MPF expects a dictionary in a config setting but found
something else.

Examples
--------

For instance, ``show_tokens`` in a :doc:`show_player </config/show_player>`
has to be a dictionary:

.. code-block:: mpf-config

   show_player:
     some_event:
       your_show_name:
         show_tokens:
           dict_key1: "dict_value1"
           dict_key2: "dict_value2"

You can see which settings are dicts in the
:doc:`config reference </config/index>` of your device.


Common Pitfalls
---------------

Using a List instead of a Dict
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a list in yaml:

.. code-block:: yaml

   your_setting:
     - item1_in_list
     - item2_in_list

This is a dictionary:

.. code-block:: yaml

   your_setting:
     key1_in_dict: value1_in_dict
     key2_in_dict: value2_in_dict

This is a list of dictionaries (used in shows for example):

.. code-block:: yaml

   your_setting:
     - key1_in_dict_in_list1: value1_in_dict_in_list1
     - key1_in_dict_in_list2: value1_in_dict_in_list2
       key2_in_dict_in_list2: value2_in_dict_in_list2

Incorrect Indent
^^^^^^^^^^^^^^^^

With nested configs (i.e. show_player, slide_player or widget_player) you might
have used an option which should be indented one level further or one level
less.
This can sometimes be a bit tricky.
Using an :doc:`IDE with the MPF language server </tools/language_server/index>`
can help here.

.. include:: config_error_footer.rst


Related How To guides
---------------------

* :doc:`config reference </config/index>`

