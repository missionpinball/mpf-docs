
The MPF game engine contains several core system components which are
included in the `/mpf/system`folder. Some of the components do OS-like
things (system timers, an event manager, task scheduling, etc.), while
others are more pinball-specific (a switch controller, platform
drivers, lighting effectscontrollers, etc.). There's really not too
much you need to know about the core components other than (1) they
are all in the `/mpf/system`folder, and (2) they are all required, so
if you delete or change any of them, bad things will happen. :) We
designed MPF to be flexible and extensible, so anything that is not
absolutely 100% required for every machine is considered a "plugin"
and located in the `/mpf/plugins` folder. The rest of this
documentation section will detail the OS-like core system components.
Then we have separate documentation sections which cover the pinball-
specific stuff as well as the plugins.



