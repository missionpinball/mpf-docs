credits:
========

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``credits:`` section of your config contains settings for the
credits mode.

There’s a full How To guide which walks you through
setting up the credits mode, so be sure to read that for the details.
This page just contains the settings which control how the credits
mode behaves. Here’s an example config:

.. code-block:: mpf-config

    credits:
      max_credits: 12
      free_play: no
      price_tier_template: "{{credits}} CREDITS ${{price}}"
      service_credits_switch: s_esc
      switches:
        - switch: s_left_coin
          type: dollars
          value: .25
        - switch: s_right_coin
          type: dollars
          value: 1
      pricing_tiers:
        - price: .50
          credits: 1
        - price: 2
          credits: 5
      events:
        - event: special
          type: special
          credits: 1
        - event: replay
          type: replay
          credits: 1
        - event: high_score_credit
          type: high_score
          credits: 1
        - event: match
          type: match
          credits: 1
      fractional_credit_expiration_time: 15m
      credit_expiration_time: 2h
      persist_credits_while_off_time: 1h
      free_play_string: FREE PLAY
      credits_string: CREDITS

Optional settings
-----------------

The following sections are optional in the ``credits:`` section of your config. (If you don't include them, the default will be used).

credit_expiration_time:
~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``0``

The amount of time before any credits on the machine are removed
(resetting the number of credits back to 0). This timer only runs
while the machine is in attract mode, and its reset each time a new
credit (or partial credit) is added to the machine. If a game is
played, the timer starts fresh when the game is over and the machine
goes back to attract mode. This value is entered as a standard MPF
time string and can be minutes, hours, or even days long. Default is
*2 hours*.

credits_string:
~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``CREDITS``

This is the text that will make up the credits_string before the
number of credits. For example, if there are 2 1/2 credits on the
machine, the credits_string will be *CREDITS 2 1/2*. Default is
*CREDITS*.

fractional_credit_expiration_time:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (ms)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``0``

The amount of time before fractions of credits are removed from the
machine. This doesn't affect whole credits, so if the machine is
sitting there with 2 1/4 credits on it, after this time expires MPF
will clear the 1/4 credit leaving 2 whole credits. This timer only
runs while the machine is in attract mode, and its reset each time a
new credit (or partial credit) is added to the machine. If a game is
played, the timer starts fresh when the game is over and the machine
goes back to attract mode. This value is entered as a standard MPF
time string and can be minutes, hours, or even days long. Default is
*15 minutes*.

free_play:
~~~~~~~~~~
Single value, type: ``boolean`` (Yes/No or True/False). Default: ``yes``

Controls whether the machine is in free play mode. Note that if you
want your machine to always be in free play mode, then you can also
choose to not use the credits mode altogether.

free_play_string:
~~~~~~~~~~~~~~~~~
Single value, type: ``string``. Default: ``FREE PLAY``

The text string that will be used in the credits_string machine
variable when the machine is in free play. Default is *FREE PLAY*.

max_credits:
~~~~~~~~~~~~
Single value, type: ``integer``. Default: ``0``

The maximum number of credits you want to allow on the machine. Note
that pinball machines can't prevent players from adding money to
machines, so be careful with this.

.. include:: template_setting.rst

persist_credits_while_off_time:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single value, type: ``time string (secs)`` (:doc:`Instructions for entering time strings) </config/instructions/time_strings>` . Default: ``1h``

The amount of time that credits will remain on the machine even when
MPF is not running. Set to 0 if you do not want to MPF to retain
credits when its powered off. The way this works behind the scenes is
that whenever a new credit (or a fraction of a credit) is added to the
machine, MPF writes that to disk as a persistent machine variable with
an expiration time and date based on the current time plus the delay
time you add here. When MPF boots up, it loads the credits from the
machine variables file and checks their expiration time, and if it's
in the past then it doesn't add them back. This value is entered as a
standard MPF time string and can be minutes, hours, or even days
long. Default is *1 hour*.

service_credits_switch:
~~~~~~~~~~~~~~~~~~~~~~~
List of one (or more) values, each is a type: string name of a ``switches:`` device. Default: ``None``

This is the name of a switch that’s used to add so-called “service
credits” to the machine. This switch has a 1-to-1 ratio, meaning that
one credit is added to the machine each time this switch is pressed.

switches:
---------

The ``switches:`` section contains the following nested sub-settings.

A list of switches that, when triggered, add credits (or fractions of
a credit) to the machine. Notice that the sub-entries under switches
are actually a list with the settings for *switch*, *type*, and
*value*, repeated multiple times.

Optional settings
~~~~~~~~~~~~~~~~~

The following sections are optional in the ``switches:`` section of your config. (If you don't include them, the default will be used).

switch:
^^^^^^^
Single value, type: string name of a ``switches:`` device. Default: ``None``

The name of the switch (from your machine-wide *switches:* section)
for the credit switch.

type:
^^^^^
Single value, type: ``string``. Default: ``money``

What type of currency is being deposited when that switch is hit. This
doesn't affect the actual behavior of MPF, rather it’s just used in as
the column name and for totaling the earnings reports (so you can
track “money” separate from “tokens”). You can enter whatever you want
here: *money*, *dollars*, *dinars*, etc.

value:
^^^^^^
Single value, type: ``number`` (will be converted to floating point). Default: ``0.25``

How much value is added whenever this switch is hit. Notice that there
are no currency symbols here or anything. A value of .25 could be 0.25
dollars or 0.25 Euros or 0.25 Francs—it really doesn't matter. The key
is that it’s 0.25 of whatever monetary system you have.

.. include:: template_setting.rst

price_tier_template
~~~~~~~~~~~~~~~~~~~

Default "{{credits}} CREDITS ${{price}}"

Placeholder to generate the credits string.

pricing_tiers:
--------------

The ``pricing_tiers:`` section contains the following nested sub-settings.

This is where you actually set your pricing by mapping how many of
your monetary units you want to equate to a certain number of credits.
The default config is fairly common, with 0.50 currency resulting in 1
credit, with a price break at 2 that gives the player 5 credits
instead of 4. (So basically they get one free credit if they put in
enough money for 4 credits.) The most important thing to know here is
that MPF always requires that 1 credit is used to start a game, and 1
credit is required to add an additional player to a game. So if you
want to change the price of your game, you don’t change the number of
credits per game, rather, you change the number of credits a certain
amount of money is worth. The pricing tier discount processing is
reset when Ball 2 starts. So if it costs $0.50 for one credit or $2
for 5 credits, if the player puts $0.50 in the machine and plays a
game, if they wait until that game is over and deposit another $1.50,
they’ll only get 3 more credits. You can have as many *pricing_tiers*
as you want. The first one dictates how much a regular game costs and
is required. If you don’t want any price breaks, then just add the
first one.

Here's an example:

.. code-block:: mpf-config

   credits:
      # ...
      pricing_tiers:
        - price: .50
          credits: 1
        - price: 2
          credits: 5


price:
~~~~~~

Price for number of ``credits``.

.. include:: template_setting.rst

Optional settings
~~~~~~~~~~~~~~~~~

The following sections are optional in the ``pricing_tiers:`` section of your config. (If you don't include them, the default will be used).

credits:
^^^^^^^^
Single value, type: ``integer``. Default: ``1``

The total number of credits that will be added based on this price tier

price:
^^^^^^
Single value, type: ``number`` (will be converted to floating point). Default: ``.50``

The numeric currency value for this pricing tier.

events:
-------

A list of one or more events with settings which add credits based on MPF events. Like the pricing_tiers section, start each entry here
with a minus sign and a space.

.. code-block:: mpf-config

   credits:
      # ...
      events:
        - event: special
          type: special
          credits: 1
        - event: replay
          type: replay
          credits: 1
        - event: high_score_credit
          type: high_score
          credits: 1
        - event: match
          type: match
          credits: 1

event:
~~~~~~
The event that will trigger a credit action.

type:
~~~~~
String which can be whatever you want, used for audits. This lets you track different types of credits, for example, money in versus replays
versus specials versus high score awards, etc.

award:
~~~~~~
Numeric value of the number of credits you'd like to award.
