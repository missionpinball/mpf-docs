---
title: twitch_subscription
---

# twitch_subscription


--8<-- "event.md"

A chat user has subscribed or resubscribed on Twitch

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

`gift`

:   True if this sub was gifted by another user

`message`

:   Chat message text

`months`

:   The number of months that the user has been a subscriber

`sub_plan`

:   The subscription tier (Prime, 1000, 2000, 3000)

`sub_plan_name`

:   The streamer specific name for the sub tier

`sub_recipient`

:   The user who is subscribing

`subscriber_message`

:   The message the user typed when subscribing

`user`

:   The chat user name who paid for the subscription
