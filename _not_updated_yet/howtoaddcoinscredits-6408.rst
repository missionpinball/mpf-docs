
This How To guide explains how to setup your machine to take money and
track credits. The MPF package contains a the code for a mode called
*credits*, so all you have to do to use add some configs to your
machine’s *modes* folder and sit back and get rich! Features of the
credits mode include:


+ Configuration of different coin/price values per coin switch.
+ Tracking money and/or tokens.
+ Set price tiers (1 credit for 50 cents, 5 credits for 2 dollars,
  etc.)
+ Specify max credits and credit expiration times
+ Retain credits even when the machine is powered off
+ Get access to a "credits string" machine variable that will show the
  number of credits (or configurable free play text) for use on your
  display.
+ Flexible events you can use to show display items based on credits
  being added, insert coin messages, max credits reached, etc.


Here are some screen shots of the credits mode in action: ` `_ ` `_
Now let's dig in to actually getting this set up:



(A) Create your 'credits' mode folder
-------------------------------------

The credits mode works like any other mode in MPF. You’ll create a
folder called *credits* in your machine’s *modes* folder, and that
folder will contain subfolders config files, images, etc. So to begin,
create a folder called *<your_machine>/modes/credits*. Then inside
there, create another folder called *config*. Then inside there,
create a file called *credits.yaml*. (So that file should be at
*<your_machine>/modes/credits/config/credits.yaml*.) Your folder
structure should look something like this:



(B) Configure options for the credits mode
------------------------------------------

Open up the credits mode's config file that you just copied into your
machine folder. It should be at
*<your_machine>/modes/credits/config/credits.yaml*. Since this file is
totally blank, add the required ` *#config_version=3*`_ to the top
line. Next, add a section called *credits:*, and then under there,
indent a few spaces (it doesn't matter how many, 2 or 4 or whatever
you prefer) and add a section called *categories:*. Your
*credits.yaml* file should now look like this:


::

    
    #config_version=3
    
    credits:


Next you need to add the settings for the credits system. You can use
the following as a starting point:


::

    
    credits:
      max_credits: 12
      free_play: no
      service_credits_switch: s_esc
      switches:
        - switch: s_left_coin
          type: money
          value: .25
        - switch: s_center_coin
          type: money
          value: .25
        - switch: s_right_coin
          type: money
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


Full details of what each of these settings does is outlined in the `
*credits:* section`_ of the configuration file reference, so check
that out for details on anything not covered here. There are a few
sections worth pointing out here though:



switches:
~~~~~~~~~

The *switches* section is how you map out the monetary values of
credit switches in your machine. Notice that the sub-entries under
switches are actually a list with the settings for switch, type, and
value repeated multiple times. The * switch: * entry is the name of
the switch (from your machine-wide *switches:* section) for the credit
switch. Pretty simple. The * value: * entry represents the numeric
value of how much is added whenever this switch is hit. Notice that
there are no currency symbols here or anything. A value of .25 could
be 0.25 dollars or 0.25 Euros or 0.25 Francs—it really doesn't matter.
The key is that it's 0.25 of whatever monetary system you have. The *
type: * entry specifies what type of currency is being deposited when
that switch is hit. This doesn't affect the actual behavior of MPF,
rather it's just used in as the column name and for totaling the
earnings reports (so you can track "money" separate from "tokens").
You can enter whatever you want here: *money*, *dollars*, *dinars*,
etc. You can mix & match these in the same machine if you have a
machine that accepts tokens and quarters, for example. Note that the
sample credits configuration file has three sets of entries for the
credit switches. You just need one for each credit switch. It can be
one or two or five—it doesn't matter.



pricing_tiers:
~~~~~~~~~~~~~~

The *pricing_tiers:* section is where you actually set your pricing by
mapping how many of your monetary units you want to equate to a
certain number of credits. The sample config is fairly common, with
0.50 currency resulting in 1 credit, with a price break at 2 that
gives the player 5 credits instead of 4. (So basically they get one
free credit if they put in enough money for 4 credits.) The most
important thing to know here is that MPF always requires that 1 credit
is used to start a game, and 1 credit is required to add an additional
player to a game. So if you want to change the price of your game, you
don't change the number of credits per game, rather, you change the
number of credits a certain amount of money is worth. The pricing tier
discount processing is reset when Ball 2 starts. So if it costs $0.50
for one credit or $2 for 5 credits, if the player puts $0.50 in the
machine and plays a game, if they wait until that game is over and
deposit another $1.50, they'll only get 3 more credits. You can have
as many *pricing_tiers* as you want. The first one dictates how much a
regular game costs and is required. If you don’t want any price
breaks, then just add the first one.



service_credits_switch:
~~~~~~~~~~~~~~~~~~~~~~~

This is the name of a switch that's used to add so-called "service
credits" to the machine. This switch has a 1-to-1 ratio, meaning that
one credit is added to the machine each time this switch is pressed.
Notice that this line is commented out (with a # sign) by default, so
if you want to use it, change the name of the switch to the name of
the switch in your actual machine and remove the # character at the
beginning of the line. Service credits are tracked separated in your
earnings data file. If you don't have a service credits switch, then
just don't add that setting.



(C) Add the credits mode to your list of modes
----------------------------------------------

Now that you have some basic credits settings configured, you can add
the credits mode to the list of modes that are used in your machine.
To do this, add `- credits` to the modes: section in your machine-wide
config, like this:


::

    
    modes:
      - base
      - some_existing_mode
      - another_mode_you_might_have
      - bonus
      - credits


The order doesn’t matter here since the priority each mode runs at is
configured in its own mode configuration file. All you’re doing now is
configuring the credits mode as a mode that your machine will use. You
might be wondering why your new *credits.yaml* mode configuration file
doesn't have a *mode:* section? That's because the *credits* mode is
built-in to MPF (in the *mpf/modes/credits*) folder, so when you add a
*credits* folder to your own machine's modes folder, MPF merges
together the settings from the MPF modes folder and your modes folder.
(It loads the MPF mode config first with baseline settings, and then
it merges in your machine's mode config which can override them.) If
you look at the built-in *credits* mode's config (at
*mpf/modes/credits/config/credits.yaml*), you'll see it has the
following *mode:* section:


::

    
    mode:
      code: credits.Credits
      priority: 11000
      start_events: machine_reset_phase_3
      stop_on_ball_end: False


First is that the priority of this mode is really high, 11000 by
default. That's because we want this mode to run "on top" of any other
mode so any slides it puts on the display (like the message for new
coins being inserts or the *INSERT COINS* message if the start button
is pressed without enough credits) are displayed on top of the slides
from any other mode that might be running. Also note that the credits
mode starts when the *machine_reset_phase_3* event is posted (which is
done as part of the MPF startup process), and that there are no stop
events. Basically we want the credits mode to start and never stop.
Also note that *stop_on_ball_end:* is set to *false*, again because we
don't want this mode to ever stop. (Without that setting, MPF would
stop the mode when the ball ends.)



(D) Create slides to show the credits when the player deposits money
--------------------------------------------------------------------

There are several credit-related things you need to show the player on
your display. Here are some settings you can use as a starting point:


::

    
    slide_player:
      credits_added:
        type: text
        text: "%machine|credits_string%"
        expire: 2s
      not_enough_credits:
      - type: text
        text: "%machine|credits_string%"
        expire: 2s
        font: small
        v_pos: bottom
      - type: text
        text: INSERT COINS
        decorators:
          type: blink
          repeats: -1
          on_secs: .1
          off_secs: .1
      enabling_free_play:
        type: text
        text: ENABLING FREE PLAY
        expire: 2s
      enabling_credit_play:
      - type: text
        text: ENABLING CREDIT PLAY
        expire: 2s
      - type: text
        text: "%machine|credits_string%"
        expire: 2s
        font: small
        v_pos: bottom


There are several events that the credit module will post which you
can use to trigger slides:


+ * max_credits_reached * – Posted once when the max number of credits
  is reached.
+ * credits_added * – Posted any time a credit or partial credit is
  added. Use it with machine variables (below) to show the values.
+ * not_enough_credits * – Posted when the player pushes start but
  there is not at least one credit to add a player. This could happen in
  attract mode or during the first ball of a game when it’s still
  possible to add players.
+ * enabling_free_play * – Posted when the machine is switched to free
  play mode. (In case you want to have a switch or something which
  changes it. Details below.)
+ *enabling_credit_play* – Posted when the machine is switched to
  credit (pay) mode.




(E) Adding credits information to game slides
---------------------------------------------

Many of the display slides in a pinball machine display information
about the number of credits on the machine. For example, the default
score display slide will usually contain a message about how many
credits are on the machine, like this: ` `_ This can be a challenge
since the exact text you want to display will change based on whether
or not the machine is on free play, and whether there are any
fractions of credits on the machine or only whole credits. To handle
this, MPF includes a machine variable called *credits_string* that is
automatically updated to show the value of credits on the machine. If
the machine is set to free play, or if you don't have the credits mode
enabled, the *credit_string* value is *FREE PLAY*. Otherwise it's the
word CREDIT followed by the number of credits (in fraction, not
decimal, as is tradition with pinball machines). Note that you can
override the text here with the *free_play_string* and
*credits_string* configuration options. Remember that you can include
machine variables in a text display element (in either a slide_player:
or a show YAML file) like this:


::

    
    - type: text
      text: "%machine|credits_string%"


And of course you can customize the font, position, and alignment of
this display element like any display element. There are several other
machine variables created too in case you want to get fancy with how
they're displayed in your particular machine. (We’ll use an example of
`2 1/4` credits here):


+ *credits_string* – This is the fully generated string which is ready
  to use in your slides, including the word *CREDITS* (or *FREE PLAY*)
  from your settings above, as well as the whole number of credits and
  any fraction. In the example this would be `CREDITS 2 1/4`.
+ *credits_value* – This is just the numeric value of the credits,
  including the fraction (if there are any partial credits). For
  example, `2 1/4`.
+ *credits_whole_num* – This is just the whole number of credits.
  Example: `2`.
+ *credits_numerator* – This is just the numerator of the fraction of
  partial credits. Example: `1`.
+ *credits_denominator* – This is just the denominator of the fraction
  of partial credits. Example: `4`.


The denominator of the fraction in the *credit_string* is
automatically calculated based on the smallest value coin switch and
the price of your game. So 0.25 switches with a game price of 0.50
will use “2” as the denominator (for 1/2 credits). 0.25 switches with
0.75 game will use 3, etc. Remember that text elements with machine
variables in slides automatically update themselves when the
underlying variable changes. So you can use these in your attract mode
DMD show, your score display, etc. See the ` `slide_player:` from
*Demo Man*`_ for details. (Also check out ` *Demo Man’s* DMD slide
show`_ for more examples.) You can also change a machine between
credit mode and free play mode by posting events. (This is not common,
but useful if you want to have a switch or something that changes the
mode. The “real” way to set this will come later when we build the
service mode.) These control events are:


+ *enable_free_play* – Puts the machine into free play mode
+ *enable_credit_play* – Puts the machine into credit play mode
+ *toggle_credit_play* – Toggles the machine between modes.




(F) Viewing Earnings
--------------------

A tally of the earnings for your machine is available at
*<your_machine_folder>/data/earnings.yaml*. Here's an example:


::

    
    money:
      count: 50
      total_value: 14.0
    service_credit:
      count: 4
      total_value: 4
    token:
      count: 1
      total_value: 1.0


Notice that there are sections in this file for each "type" of switch
you configured. The sample configuration from the template file
included type values of money and token which is why you see them
here. If you changed those to something like dollars then you would
see a dollars category here. The *count* is the total number of switch
hits that contributed towards that count, and the *total_value* is the
total numeric value based on the value of each switch. If you
configured a *service_credits_switch* then you'll also see a count of
service credits. (The service credits count and *total_value* will
always be the same since a service credit switch is always worth one
credit.)



(G) Check out this complete credits config file
-----------------------------------------------

Here's the complete credits config file from the Demo Man sample game.
( *demo_man/modes/credits/config/credits.yaml*):


::

    
    #config_version=3
    
    credits:
      max_credits: 12
      free_play: no
      service_credits_switch: s_esc
      switches:
        - switch: s_left_coin
          type: money
          value: .25
        - switch: s_center_coin
          type: money
          value: .25
        - switch: s_right_coin
          type: token
          value: 1
        - switch: s_fourth_coin
          value: 1
          type: money
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
    
    slide_player:
      credits_added:
        type: text
        text: "%machine|credits_string%"
        expire: 2s
      not_enough_credits:
      - type: text
        text: "%machine|credits_string%"
        expire: 2s
        font: small
        v_pos: bottom
      - type: text
        text: INSERT COINS
        decorators:
          type: blink
          repeats: -1
          on_secs: .1
          off_secs: .1
      enabling_free_play:
        type: text
        text: ENABLING FREE PLAY
        expire: 2s
      enabling_credit_play:
      - type: text
        text: ENABLING CREDIT PLAY
        expire: 2s
      - type: text
        text: "%machine|credits_string%"
        expire: 2s
        font: small
        v_pos: bottom


.. _Demo Man: https://github.com/missionpinball/mpf/blob/master/machine_files/demo_man/modes/base/config/base.yaml
.. _ section: https://missionpinball.com/docs/configuration-file-reference/credits/
.. _#config_version=3: https://missionpinball.com/docs/configuration-file-reference/important-config-file-concepts/config_version/
.. _ DMD slide show: https://github.com/missionpinball/mpf/blob/master/machine_files/demo_man/shows/attract_dmd_loop.yaml


