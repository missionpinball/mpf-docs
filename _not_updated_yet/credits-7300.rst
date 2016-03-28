
The *credits:* section of the config file contains settings for the
credits mode. This sectioncan be used in your machine-wide config
files. This sectioncan be used in your mode-specific config files. If
you include this section in both your machine-wide config and the
config for the credits mode, the machine-wide config is loaded first,
and then any new or different settings in the credits mode config are
merged in. There’s a full `How To guide`_ which walks you through
setting up the credits mode, so be sure to read that for the details.
This page just contains the settings which control how the credits
mode behaves. Here’s an example config:


::

    
    credits:
      max_credits: 12
      free_play: no
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
      fractional_credit_expiration_time: 15m
      credit_expiration_time: 2h
      persist_credits_while_off_time: 1h
      free_play_string: FREE PLAY
      credits_string: CREDITS




switches:
~~~~~~~~~

A list of switches that, when triggered, add credits (or fractions of
a credit) to the machine. Notice that the sub-entries under switches
are actually a list with the settings for *switch*, *type*, and
*value*, repeated multiple times.



switch:
```````

The name of the switch (from your machine-wide *switches:* section)
for the credit switch.



value:
``````

How much value is added whenever this switch is hit. Notice that there
are no currency symbols here or anything. A value of .25 could be 0.25
dollars or 0.25 Euros or 0.25 Francs—it really doesn’t matter. The key
is that it’s 0.25 of whatever monetary system you have.



type:
`````

What type of currency is being deposited when that switch is hit. This
doesn’t affect the actual behavior of MPF, rather it’s just used in as
the column name and for totaling the earnings reports (so you can
track “money” separate from “tokens”). You can enter whatever you want
here: *money*, *dollars*, *dinars*, etc.



pricing_tiers:
~~~~~~~~~~~~~~

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



credit_expiration_time:
~~~~~~~~~~~~~~~~~~~~~~~

The amount of time before any credits on the machine are removed
(resetting the number of credits back to 0). This timer only runs
while the machine is in attract mode, and its reset each time a new
credit (or partial credit) is added to the machine. If a game is
played, the timer starts fresh when the game is over and the machine
goes back to attract mode. This value is entered as a `standard MPF
time string`_ and can be minutes, hours, or even days long. Default is
*2 hours*.



credits_string:
~~~~~~~~~~~~~~~

This is the text that will make up the credits_string before the
number of credits. For example, if there are 2 1/2 credits on the
machine, the credits_string will be *CREDITS 2 1/2*. Default is
*CREDITS*.



free_play:
~~~~~~~~~~

Controls whether the machine is in free play mode. Note that if you
want your machine to always be in free play mode, then you can also
choose to not use the credits mode altogether.



free_play_string:
~~~~~~~~~~~~~~~~~

The text string that will be used in the credits_string machine
variable when the machine is in free play. Default is *FREE PLAY*.



fractional_credit_expiration_time:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The amount of time before fractions of credits are removed from the
machine. This doesn't affect whole credits, so if the machine is
sitting there with 2 1/4 credits on it, after this time expires MPF
will clear the 1/4 credit leaving 2 whole credits. This timer only
runs while the machine is in attract mode, and its reset each time a
new credit (or partial credit) is added to the machine. If a game is
played, the timer starts fresh when the game is over and the machine
goes back to attract mode. This value is entered as a `standard MPF
time string`_ and can be minutes, hours, or even days long. Default is
*15 minutes*.



max_credits
~~~~~~~~~~~

The maximum number of credits you want to allow on the machine. Note
that pinball machines can't prevent players from adding money to
machines, so be careful with this.



persist_credits_while_off_time:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The amount of time that credits will remain on the machine even when
MPF is not running. Set to 0 if you do not want to MPF to retain
credits when its powered off. The way this works behind the scenes is
that whenever a new credit (or a fraction of a credit) is added to the
machine, MPF writes that to disk as a persistent machine variable with
an expiration time and date based on the current time plus the delay
time you add here. When MPF boots up, it loads the credits from the
machine variables file and checks their expiration time, and if it's
in the past then it doesn't add them back. This value is entered as a
`standard MPF time string`_ and can be minutes, hours, or even days
long. Default is *1 hour*.



service_credit_switch:
~~~~~~~~~~~~~~~~~~~~~~

This is the name of a switch that’s used to add so-called “service
credits” to the machine. This switch has a 1-to-1 ratio, meaning that
one credit is added to the machine each time this switch is pressed.

.. _How To guide: https://missionpinball.com/docs/howto/how-to-add-coins-credits/
.. _standard MPF time string: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/entering-time-duration-values/


