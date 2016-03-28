
Throughout the Mission Pinball Framework config files, there are
several places where the configuration items need to be a "list" or a
"list of lists." The MPF config files are in a YAML format, so you add
list items by following the YAML spec, but it can be a kind of
confusing. So this page is our "how to" guide for the various ways you
can add list items to MPF config files. First of all, there are
several different places we need lists. For example, device tags,
logic block events, switches that make up shots, etc. For our
explanation, we'll use a generic list item with generic
configurations. Some examples:


::

    
    flipperLeft:
        number: SD18
        tags: flipper, player  # this is a list



::

    
    Shots:
        outlane:
            Switch: leftOutlane, rightOutlane  #this is a list



::

    
    Auditor:
        save_events:  # This config wants a list
            game_started  # This is the first list item
            ball_ended  # This is the second list item
            game_ended  # This is the third list item



::

    
    light_special:
        events:
            - sw_eightball  # this is the first list item
            - drop_targets_Solids_lit_complete, drop_targets_Stripes_lit_complete  # 2nd list item, which itself has two items




Valid options for lists
-----------------------

Ok, so let's say you have a config item that needs a list. We'll use a
made-up config called "config" with three list items: item1, item2,
and item3. You can enter this into your config file in one of several
ways. First, you can enter all the items on one line separated by
commas:


::

    
    config: item1, item2, item3


Second, you can enter all the items on one line separated by spaces:
(Obviously you can't do this if your individual items have spaces in
their names. In that case, just use commas.)


::

    
    config: item1 item2 item3


Third, you can enter each item on its own line, like this: (Be sure
that you indent your list items, and that they are all indented the
same amount.


::

    
    config:
        item1
        item2
        item3


Fourth, you can enter each item on its own line, indented, with each
line starting with a dash, like this: (Be sure to include the space
after the dash before the list item. It's a YAML thing.)


::

    
    config:
        - item1
        - item2
        - item3


So you have four options. Which one should you pick? It really doesn't
matter. You can use whichever one has the style you prefer and
whichever one makes your config files easiest to read. (We tend to
just use commas, but if it's a long list then we'll put each item on
its own line so the line doesn't wrap.)



Valid options for "lists of lists"
----------------------------------

Some config items require "lists of lists" where there is a list with
multiple items, and then each of those items is itself another list
which may have multiple items. (This is seen a lot in MPF's Logic
Blocks where we have multiple steps that can each be made up of one or
more events.) The easiest way to enter these into your configuration
files is to combine the method using commas and dashes, like this:


::

    
    config:
        - item1, item2
        - item3, item4, item5
        - item6


So in the example above, the configuration item has a list with three
items. The first list item contains item1 and item 2, the second list
item contains item3, item4, and item5, and the third list item
contains item6. You can also enter each item on it's own line and then
use dashes to signify where a new list item starts, like this:


::

    
    config:
        - item1
          item2
        - item3
          item4
          item5
        - item6


Note that the indentation of all your items is the same, but that the
dash is "outdented".



