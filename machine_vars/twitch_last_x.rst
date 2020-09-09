twitch_last_(x)
===============

*MPF machine variables*

Contains information about the last events triggered from Twitch chat.


twitch_last_bits_amount
~~~~~~~~~~~~~~~~~~~~~~~

Holds the number of bits that were last donated via Twitch.

twitch_last_bits_user
~~~~~~~~~~~~~~~~~~~~~~~

Holds the last user who donated bits via Twitch.

twitch_last_chat_message_line_count
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Holds the number of lines last chat message was split into.

twitch_last_chat_message_line(x)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Holds a split version of the last chat message received from the twitch_client.
The system will divide the message into up to 6 lines. The number of lines
will be stored in twitch_last_chat_message_line_count and the full message is
stored in twitch_last_chat_message.

twitch_last_chat_message
~~~~~~~~~~~~~~~~~~~~~~~~

Holds the last chat message received from Twitch chat. This is the complete and
unsplit message.

twitch_last_chat_user
~~~~~~~~~~~~~~~~~~~~~

Holds the last user to send a message via Twitch chat.

twitch_last_raid_user
~~~~~~~~~~~~~~~~~~~~~

Holds the last user to raid the channel.

twitch_last_raid_count
~~~~~~~~~~~~~~~~~~~~~~

Holds the amount of viewers in the most recent raid.

twitch_last_sub_is_gift
~~~~~~~~~~~~~~~~~~~~~~~

Holds a whether or not the last Twitch sub was a gift sub.

twitch_last_sub_message
~~~~~~~~~~~~~~~~~~~~~~~

Holds the message received when announcing a Twitch subcription.

twitch_last_sub_months
~~~~~~~~~~~~~~~~~~~~~~

Holds the number of months that the last user has been subscribed for. This
is total months not consecutive months.

twitch_last_sub_plan
~~~~~~~~~~~~~~~~~~~~

Holds the subscription tier of the last Twitch subscription. This can be
Prime, 1000, 2000, or 3000.

twitch_last_sub_plan_name
~~~~~~~~~~~~~~~~~~~~~~~~~

Holds the streamer specific subscription tier name of the last Twitch
subscription.

twitch_last_sub_user
~~~~~~~~~~~~~~~~~~~~

Holds the Twitch user name of the person who **PAID** for the subscription.
This will not match the recipient if this is a gifted subscription.

twitch_last_sub_recipient
~~~~~~~~~~~~~~~~~~~~~~~~~

Holds the Twitch user name of the person who **RECEIVED** the subscription.
This will not match the user if this is a gifted subscription.
