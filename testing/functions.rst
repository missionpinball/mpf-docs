MPF Test Functions
==================

Here's a list of test functions you can use for your own machine.

:doc:`/about/help_us_to_write_it`

MpfGameTestCase

assertBallNumber(number)
assertPlayerNumber(number)
assertGameIsRunning()
assertGameInNotRunning()

MpfTestCase

assertColorAlmostEqual(color1, color2, delta=6)
assertPlayerVarEqual(value, player_var)
assertSwitchState(name, state)
assertLedColor(led_name, color)
assertLedColors(led_name, color_list, secs, check_delta=.1)
assertModeRunning(mode_name)
assertModeNotRunning(mode_name)
assertEventNotCalled(event_name)
assertEventCalled(event_name, times=None)
assertEventCalledWith(event_name, kwargs)
assertShotShow(shot_name, show_name)
assertShowRunning(show_name)
assertShowNotRunning(show_name)
assertBallsOnPlayfield
assertAvailableBallsOnPlayfield
assertShotProfile
assertShotState
assertShotEnabled

add utility functions

MpfMcTestCase

assertEventNotCalled(event_name)
assertEventCalled(event_name, times=None)
assertEventCalledWith(event_name, kwargs)

MpfSlideTestCase

assertSlideOnTop(slide_name, target='default')
assertTextOnTopSlide(text, target='default')
assertTextNotOnTopSlide(text, target='default')
assertSlideActive(slide_name)
assertSlideNotActive(slide_name)
assertTextInSlide(text, slide_name)
assertTextNotInSlide(text, slide_name)

