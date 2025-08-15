# Introduction

This introduction chapter should give you a quick start into extending MPF.

!!! note "Mode custom code vs. machine custom code"

    Note that MPF also has the ability to run custom mode code which is code that is associated with a certain game mode and is generally only active when the mode it's in is active. So if you just want to write your own custom game logic, you'll probably use mode code. MPF has well the ability to run machine wide code, which is active as long as MPF is running regardless of the mode you are in. You need to decide what code extension you need.

Follow either the examples for the [machine wide](machine_code.md) extension or the [mode wide](mode_code.md) extension. In the next step most extensions probably have to deal in one or the other way with variables, follow this [variable guide](variables_in_code.md) to learn how to deal with MPF variables in your own code.

As long as you only write smaller extensions you don't have to setup a full Python development environment. Of course you can and the more complex your development gets the more handy it might be. The [setup guide](setup.md) you only have to follow if you really want to develop MPF itself and not only to write an extension for your game.

Last but not least of course the [API Reference](../api_reference/index.md) is very important for you.
