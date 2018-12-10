Debugging Memory Leaks
======================

Sometimes you might experience out of memory conditions.
This might be due to bugs in MPF, custom code or certain config features.
We found that most leaks are caused either by dangling event handlers or
slide/widget which never get unloaded.
For that reason, we added a feature to MPF and MPF-MC to dump all of those.
To trigger the debug dump start MPF and MPF-MC without the production flag
and post the ``debug_dump_stats`` events.
For example, you can add a keyboard key ``d`` to do that:

.. code-block:: mpf-config

   keyboard:
      d:
         event: debug_dump_stats

The MPF log will contain something like this:

.. code-block:: console

   2018-12-10 21:35:55,682 : INFO : EventManager : Event: ======'debug_dump_stats'====== Args={'_from_bcp': True}
   2018-12-10 21:35:55,683 : INFO : EventManager : --- DEBUG DUMP EVENTS ---
   2018-12-10 21:35:55,683 : INFO : EventManager : Total registered_handlers: 265. Total event_queue: 0. Total callback_queue: 0. Total _queue_tasks: 0
   2018-12-10 21:35:55,683 : INFO : EventManager : Registered Handlers:
   2018-12-10 21:35:55,683 : INFO : EventManager :   Total handlers: 24 (for ball_starting)
   [...]
   2018-12-10 21:35:55,689 : INFO : EventManager :   Total handlers: 1 (for balldevice_bd_scoop_front_ball_eject_failed)
   2018-12-10 21:35:55,689 : INFO : EventManager : Queue events:
   2018-12-10 21:35:55,689 : INFO : EventManager : --- DEBUG DUMP EVENTS END ---

MPF-MC will contain even more information:

.. code-block:: console

   2018-12-10 21:35:55,682 : EventManager : Event: ======'debug_dump_stats'====== Args={}
   2018-12-10 21:35:55,702 : EventManager : --- DEBUG DUMP EVENTS ---
   2018-12-10 21:35:55,703 : EventManager : Total registered_handlers: 42. Total event_queue: 0. Total callback_queue: 0. Total _queue_tasks: 0
   2018-12-10 21:35:55,703 : EventManager : Registered Handlers:
   2018-12-10 21:35:55,703 : EventManager :   Total handlers: 2 (for service_power_off)
   2018-12-10 21:35:55,703 : EventManager :   Total handlers: 2 (for debug_dump_stats)
   2018-12-10 21:35:55,703 : EventManager :   Total handlers: 1 (for service_menu_show)
   2018-12-10 21:35:55,703 : EventManager :   Total handlers: 1 (for assets_to_load)
   2018-12-10 21:35:55,703 : EventManager :   Total handlers: 1 (for sound_loop_sets_clear)
   2018-12-10 21:35:55,703 : EventManager :   Total handlers: 1 (for master_volume_decrease)
   2018-12-10 21:35:55,703 : EventManager :   Total handlers: 1 (for service_menu_selected_switch)
   [...]
   2018-12-10 21:35:55,705 : EventManager :   Total handlers: 1 (for service_coil_test_start)
   2018-12-10 21:35:55,705 : EventManager :   Total handlers: 1 (for service_door_opened)
   2018-12-10 21:35:55,705 : EventManager : Queue events:
   2018-12-10 21:35:55,705 : EventManager : --- DEBUG DUMP EVENTS END ---
   2018-12-10 21:35:55,705 : mpfmc : --- DEBUG DUMP DISPLAYS ---
   2018-12-10 21:35:55,705 : mpfmc : Active slides: {'playfield_blank': <Slide name=playfield_blank, priority=0, id=1>, 'transparent_playfield': <Slide name=transparent_playfield, priority=0, id=5>, 'dmd_back_blank': <Slide name=dmd_back_blank, priority=0, id=2>, 'window_slide_1': <Slide name=window_slide_1, priority=0, id=6>, 'dmd_front': <Slide name=dmd_front, priority=10, id=8>, 'dmd_front_blank': <Slide name=dmd_front_blank, priority=0, id=4>, 'window_blank': <Slide name=window_blank, priority=0, id=3>, 'dmd_back': <Slide name=dmd_back, priority=10, id=7>} (Count: 8). Displays: {'dmd_front': <Display name=dmd_front[128, 32], current slide=dmd_front, total slides=2>, 'dmd_back': <Display name=dmd_back[128, 32], current slide=dmd_back, total slides=2>, 'window': <Display name=window[600, 700], current slide=window_slide_1, total slides=2>, 'playfield': <Display name=playfield[225, 250], current slide=transparent_playfield, total slides=2>} (Count: 4)
   2018-12-10 21:35:55,705 : mpfmc : Listing children for display: <Display name=dmd_front[128, 32], current slide=dmd_front, total slides=2>
   2018-12-10 21:35:55,705 : mpfmc : <Display name=dmd_front[128, 32], current slide=dmd_front, total slides=2>
   2018-12-10 21:35:55,705 : mpfmc : <Slide name=dmd_front, priority=10, id=8>
   2018-12-10 21:35:55,706 : mpfmc : <WidgetContainer id=None z=0 key=None>
   2018-12-10 21:35:55,706 : mpfmc : <Image name=drache, size=[128, 32], pos=[64, 16]>
   2018-12-10 21:35:55,706 : mpfmc : Total children: 4
   [...]
   2018-12-10 21:35:55,708 : mpfmc : <Slide name=transparent_playfield, priority=0, id=5>
   2018-12-10 21:35:55,708 : mpfmc : <WidgetContainer id=None z=2 key=None>
   2018-12-10 21:35:55,708 : mpfmc : <Image name=nyannyan, size=[110, 281], pos=[172.0, 155.70284725004058]>
   2018-12-10 21:35:55,708 : mpfmc : <WidgetContainer id=None z=2 key=None>
   2018-12-10 21:35:55,708 : mpfmc : <Image name=nyannyan, size=[110, 281], pos=[60.0, 100.44406174999192]>
   2018-12-10 21:35:55,708 : mpfmc : Total children: 6
   2018-12-10 21:35:55,708 : mpfmc : --- DEBUG DUMP DISPLAYS END ---
   2018-12-10 21:35:55,732 : mpfmc : --- DEBUG DUMP OBJECTS ---
   2018-12-10 21:35:55,732 : mpfmc : Elements in list (may be dead): 152
   2018-12-10 21:35:55,732 : mpfmc : <Display name=playfield[225, 250], current slide=transparent_playfield, total slides=2>
   2018-12-10 21:35:55,732 : mpfmc : <Display name=dmd_back[128, 32], current slide=dmd_back, total slides=2>
   2018-12-10 21:35:55,732 : mpfmc : <Display name=window[600, 700], current slide=window_slide_1, total slides=2>
   2018-12-10 21:35:55,732 : mpfmc : <Display name=dmd_front[128, 32], current slide=dmd_front, total slides=2>
   2018-12-10 21:35:55,732 : mpfmc : <DisplayWidget size=[600, 700], pos=[0, 0], source=window>
   2018-12-10 21:35:55,733 : mpfmc : <Slide name=playfield_blank, priority=0, id=1>
   [...]
   2018-12-10 21:35:55,737 : mpfmc : <Image name=drache, size=[128, 32], pos=[64, 16]>
   2018-12-10 21:35:55,737 : mpfmc : <Image name=nyannyan, size=[110, 281], pos=[60.0, 100.44406174999192]>
   2018-12-10 21:35:55,737 : mpfmc : <Image name=nyannyan, size=[110, 281], pos=[172.0, 155.70284725004058]>
   2018-12-10 21:35:55,737 : mpfmc : --- DEBUG DUMP OBJECTS END ---
   2018-12-10 21:35:55,737 : mpfmc : --- DEBUG DUMP CLOCK ---
   2018-12-10 21:35:55,737 : mpfmc : <ClockEvent (1.0) callback=<function Cache._purge_by_timeout at 0x7fe7c73eeae8>>
   2018-12-10 21:35:55,737 : mpfmc : <ClockEvent (0.0) callback=<bound method SoundSystem.tick of <mpfmc.core.audio.SoundSystem object at 0x7fe7b89c0080>>>
   2018-12-10 21:35:55,737 : mpfmc : <ClockEvent (0.0) callback=<bound method BcpProcessor._get_from_queue of <mpfmc.core.bcp_processor.BcpProcessor object at 0x7fe7b89457f0>>>
   2018-12-10 21:35:55,737 : mpfmc : <ClockEvent (1.0) callback=<bound method MpfMc._check_crash_queue of <mpfmc.core.mc.MpfMc object at 0x7fe7c8ab91e8>>>
   2018-12-10 21:35:55,737 : mpfmc : <ClockEvent (0.0) callback=<bound method MpfMc.tick of <mpfmc.core.mc.MpfMc object at 0x7fe7c8ab91e8>>>
   2018-12-10 21:35:55,737 : mpfmc : <ClockEvent (0.2) callback=<bound method WindowSDL._check_keyboard_shown of <kivy.core.window.window_sdl2.WindowSDL object at 0x7fe7b833a180>>>
   2018-12-10 21:35:55,738 : mpfmc : <ClockEvent (0.0) callback=<bound method EffectWidget._update_glsl of <kivy.uix.effectwidget.EffectWidget object at 0x7fe7b79c1e80>>>
   2018-12-10 21:35:55,738 : mpfmc : <ClockEvent (0.0) callback=<bound method EffectWidget._update_glsl of <kivy.uix.effectwidget.EffectWidget object at 0x7fe7b79f0180>>>
   2018-12-10 21:35:55,738 : mpfmc : <ClockEvent (0.0) callback=<bound method EffectWidget._update_glsl of <kivy.uix.effectwidget.EffectWidget object at 0x7fe79edc9c78>>>
   2018-12-10 21:35:55,738 : mpfmc : <ClockEvent (0.0) callback=<bound method DmdBase.tick of <mpfmc.core.dmd.RgbDmd object at 0x7fe7b89ee198>>>
   2018-12-10 21:35:55,738 : mpfmc : <ClockEvent (0.0) callback=<bound method EffectWidget._update_glsl of <kivy.uix.effectwidget.EffectWidget object at 0x7fe79edc9f50>>>
   2018-12-10 21:35:55,738 : mpfmc : <ClockEvent (0.0) callback=<bound method DmdBase.tick of <mpfmc.core.dmd.RgbDmd object at 0x7fe7b88b36a0>>>
   2018-12-10 21:35:55,738 : mpfmc : <ClockEvent (0.1) callback=<bound method Image._anim of <kivy.core.image.Image object at 0x7fe7b7c0a800>>>
   2018-12-10 21:35:55,738 : mpfmc : <ClockEvent (0.0) callback=<bound method McDisplayLightPlayer._tick of BcpConfigPlayer.display_lights>>
   2018-12-10 21:35:55,738 : mpfmc : <ClockEvent (9.0) callback=<bound method Widget.remove of <Image name=nyannyan, size=[110, 281], pos=[60.0, 100.44406174999192]>>>
   2018-12-10 21:35:55,738 : mpfmc : <ClockEvent (0.0) callback=<bound method Animation._update of <mpfmc.uix.relative_animation.RelativeAnimation object at 0x7fe79d1f18d0>>>
   2018-12-10 21:35:55,738 : mpfmc : <ClockEvent (9.0) callback=<bound method Widget.remove of <Image name=nyannyan, size=[110, 281], pos=[172.0, 155.70284725004058]>>>
   2018-12-10 21:35:55,739 : mpfmc : <ClockEvent (0.0) callback=<bound method Animation._update of <mpfmc.uix.relative_animation.RelativeAnimation object at 0x7fe79d1f1e80>>>
   2018-12-10 21:35:55,739 : mpfmc : --- DEBUG DUMP CLOCK END ---

Leaks usually occur over time so dump all objects on start of your machine.
Leave it running for a few minutes and dump all objects again.
Then compare the output of those two.
Look for events with a very high number of handlers (or a number which is constantly increasing).
Check for widgets or slides which are existing more than once.
If you got questions ask in the forum.
