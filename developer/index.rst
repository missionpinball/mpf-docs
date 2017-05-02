Information for Software Developers
===================================

We talk a lot about how you don't have to be an experienced software developer to use MPF. However, if you are an
experienced developer, there are a few ways you can leverage your coding knowledge:

Writing custom Python for your machine
--------------------------------------

It's possible to :doc:`write custom Python code for your machine <custom_code>`. This is really easy to do,
and MPF was designed in a way that your own custom code (from your machine folder) and happily run
alongside core MPF code.

If you know Python, you might be nervous to use MPF and it's "config files". But fear not! You can use as much
or as little of the config files as you want and write everything else in Python (or C++ or whatever other
language you want). That way you can let MPF handle the boring stuff (interfacing with hardware, posting and
processing events, etc.) and you can write everything else yourself if you want.

We have a guide called :doc:`dsl_vs_programming` which explores this topic in detail.

Extending MPF
-------------

IF you are a programmer and you'd like to help us improve MPF, we have a :doc:`guide for that <mpf>` which walks you
through how to setup your dev environment and how to do pull requests against the MPF codebase.

We also explain how you can write your own hardware platform interface (if you've built your own pinball controller
hardware). See the :doc:`mpf` guide for details.

API Reference
-------------

We also have an :doc:`API reference <api>` which details all the internal MPF classes & methods which is useful for
people extending MPF or writing custom code for their machines.

There's also a :doc:`BCP protocol reference </bcp/index>` if you'd like to write your own media controller.
