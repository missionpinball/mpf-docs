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

.. code-block:: mpf-config

    twitch_client:
        user: TwitchBotAccount
        password: oauth:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        channel: ChatChannel

DO NOT CHECK YOUR PASSWORD INTO SOURCE CONTROL. If you use a service like
Github you should not check in your password. If this is stored publicly then
someone could log in as you on Twitch.


Required settings
-----------------

The following sections are required in the ``twitch_client:`` section of your config:

user:
~~~~~~~
Single value, type: ``string``.

This is the user that will connect to Twitch. You may want to create a separate
bot account on Twitch to use for this purpose.

password:
~~~~~~~
Single value, type: ``string``.

This is a Twitch OAuth token, not the actual password of the user. You can
generate this token at https://twitchapps.com/tmi/

channel:
~~~~~~~
Single value, type: ``string``.

The channel on Twitch which will be monitored for messages.
