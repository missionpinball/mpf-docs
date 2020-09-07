twitch_last_chat_message_line(x)
================================

*MPF machine variable*

Holds a split version of the last chat message received from the twitch_client.
The system will divide the message into up to 6 lines. The number of lines
will be stored in twitch_last_chat_message_line_count and the full message is
stored in twitch_last_chat_message.
