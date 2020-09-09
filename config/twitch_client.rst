twitch_client:
==============

*Config file section*

+----------------------------------------------------------------------------+---------+
| Valid in :doc:`machine config files </config/instructions/machine_config>` | **YES** |
+----------------------------------------------------------------------------+---------+
| Valid in :doc:`mode config files </config/instructions/mode_config>`       | **NO**  |
+----------------------------------------------------------------------------+---------+

.. overview

The ``twitch_client:`` section of your config is where you configure the built-in
Twitch chat monitor.

Before using this plugin you must install the irc library with ``pip3 install irc``

.. code-block:: mpf-config

    twitch_client:
        user: TwitchBotAccount
        password: oauth:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        channel: ChatChannel

.. code-block:: mpf-config

    machine_vars:
      twitch_user:
        initial_value: 'TwitchBotAccount'
        value_type: str
      twitch_password:
        initial_value: 'oauth:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        value_type: str
      twitch_channel:
        initial_value: 'ChatChannel'
        value_type: str

    twitch_client:
        user_var: twitch_user
        password_var: twitch_password
        channel_var: twitch_channel


DO NOT CHECK YOUR PASSWORD INTO SOURCE CONTROL. If you use a service like
Github you should not check in your password. If this is stored publicly then
someone could log in as you on Twitch.


Required settings
-----------------

One set of credentials are required in the ``twitch_client:`` section of your config.
They may be either hard coded or pulled from machine variables:

user:
~~~~~
Single value, type: ``string``.

This is the user that will connect to Twitch. You may want to create a separate
bot account on Twitch to use for this purpose.

password:
~~~~~~~~~
Single value, type: ``string``.

This is a Twitch OAuth token, not the actual password of the user. You can
generate this token at https://twitchapps.com/tmi/

channel:
~~~~~~~~
Single value, type: ``string``.

The channel on Twitch which will be monitored for messages.

user_var:
~~~~~~~~~
Single value, type: ``string``.

This is the machine variable name that contains the user that will connect to
Twitch. You may want to create a separate bot account on Twitch to use for this
purpose.

password_var:
~~~~~~~~~~~~~
Single value, type: ``string``.

This is the machine variable name that contains the password to use when
connecting to Twitch, This is a Twitch OAuth token, not the actual password of
the user. You can generate this token at https://twitchapps.com/tmi/

When you run ``mpf -b`` it may show your token in the machine variables
portion of the window. Be careful what you share on stream.

channel_var:
~~~~~~~~~~~~
Single value, type: ``string``.

his is the machine variable name that contains the channel on Twitch which will
be monitored for messages.
