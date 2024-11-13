
# MpfBcpTestCase

`class mpf.tests.MpfBcpTestCase.MpfBcpTestCase(methodName='runTest')`

Bases: `mpf.tests.MpfTestCase.MpfTestCase`

An MpfTestCase instance which uses the MockBcpClient.

## Methods & Attributes

The MpfBcpTestCase has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`static add_to_config_validator(machine, key, new_dict)`

Add config dict to validator.

`advance_time_and_run(delta=1.0)`

Advance the test clock and run anything that should run during that time.

Parameters:

* **delta** – How much time to advance the test clock by (in seconds)

This method will cause anything scheduled during the time to run, including things like delays, timers, etc.

Advancing the clock will happen in multiple small steps if things are scheduled to happen during this advance. For example, you can advance the clock 10 seconds like this:

```
self.advance_time_and_run(10)
```

If there is a delay callback that is scheduled to happen in 2 seconds, then this method will advance the clock 2 seconds, process that delay, and then advance the remaining 8 seconds.

`assertAlmostEqual(first, second, places=None, msg=None, delta=None)`

Fail if the two objects are unequal as determined by their difference rounded to the given number of decimal places (default 7) and comparing to zero, or by comparing that the difference between the two objects is more than the given delta.

Note that decimal places (from zero) are usually not the same as significant digits (measured from the most significant digit).

If the two objects compare equal then they will automatically compare almost equal.

`assertAvailableBallsOnPlayfield(balls, playfield='playfield')`

Assert that a certain number of ball is available on a playfield.

`assertBallsOnPlayfield(balls, playfield='playfield')`

Assert that a certain number of ball is on a playfield.

`assertColorAlmostEqual(color1, color2, delta=6)`

Assert that two color are almost equal.

Parameters:

* **color1** – The first color, as an RGBColor instance or 3-item iterable.
* **color2** – The second color, as an RGBColor instance or 3-item iterable.
* **delta** – How close the colors have to be. The deltas between red, green, and blue are added together and must be less or equal to this value for this assertion to succeed.

`assertCountEqual(first, second, msg=None)`

An unordered sequence comparison asserting that the same elements, regardless of order. If the same element occurs more than once, it verifies that the elements occur the same number of times.

```
self.assertEqual(Counter(list(first)),
  Counter(list(second)))
```

Example:
```
[0, 1, 1] and [1, 0, 1] compare equal.
[0, 0, 1] and [0, 1] compare unequal.
```

`assertDictContainsSubset(subset, dictionary, msg=None)`

Checks whether dictionary is a superset of subset.

`assertEqual(first, second, msg=None)`

Fail if the two objects are unequal as determined by the ‘==’ operator.

`assertEventCalled(event_name, times=None)`

Assert that event was called.

Parameters:

* **event_name** – String name of the event to check.
* **times** – An optional value to confirm the number of times the event was called. Default of None means this method will pass as long as the event has been called at least once.

If you want to reset the times count, you can mock the event again.

Note that the event must be mocked via self.mock_event() first in order to use this method.

For example:

```
self.mock_event('my_event')
self.assertEventNotCalled('my_event')  # This will pass

self.post_event('my_event')
self.assertEventCalled('my_event') # This will pass
self.assertEventCalled('my_event', 1)  # This will pass

self.post_event('my_event')
self.assertEventCalled('my_event') # This will pass
self.assertEventCalled('my_event', 2)  # This will pass
```

`assertEventCalledWith(event_name, **kwargs)`

Assert an event was called with certain kwargs.

Parameters:

* **event_name** – String name of the event to check.
* ****kwargs** – Name/value parameters to check.

For example:

```
self.mock_event('jackpot')

self.post_event('jackpot', count=1, first_time=True)
self.assertEventCalled('jackpot')  # This will pass
self.assertEventCalledWith('jackpot', count=1, first_time=True)  # This will also pass
self.assertEventCalledWith('jackpot', count=1, first_time=False)  # This will fail
```

`assertEventNotCalled(event_name)`

Assert that event was not called.

Parameters:

* **event_name** – String name of the event to check.

Note that the event must be mocked via self.mock_event() first in order to use this method.

`assertFalse(expr, msg=None)`

Check that the expression is false.

`assertGreater(a, b, msg=None)`

Just like self.assertTrue(a > b), but with a nicer default message.

`assertGreaterEqual(a, b, msg=None)`

Just like self.assertTrue(a >= b), but with a nicer default message.

`assertIn(member, container, msg=None)`

Just like self.assertTrue(a in b), but with a nicer default message.

`assertIs(expr1, expr2, msg=None)`

Just like self.assertTrue(a is b), but with a nicer default message.

`assertIsInstance(obj, cls, msg=None)`

Same as self.assertTrue(isinstance(obj, cls)), with a nicer default message.

`assertIsNone(obj, msg=None)`

Same as self.assertTrue(obj is None), with a nicer default message.

`assertIsNot(expr1, expr2, msg=None)`

Just like self.assertTrue(a is not b), but with a nicer default message.

`assertIsNotNone(obj, msg=None)`

Included for symmetry with assertIsNone.

`assertLess(a, b, msg=None)`

Just like self.assertTrue(a < b), but with a nicer default message.

`assertLessEqual(a, b, msg=None)`

Just like self.assertTrue(a <= b), but with a nicer default message.

`assertLightChannel(light_name, brightness, channel='white')`

Assert that a light channel has a certain brightness.

`assertLightColor(light_name, color)`

Assert that a light exists and shows one color.

`assertLightColors(light_name, color_list, secs=1, check_delta=0.1)`

Assert that a light exists and shows all colors in a list over a period.

`assertLightFlashing(light_name, color=None, secs=1, check_delta=0.1)`

Assert that a light exists and is flashing.

`assertLightOff(light_name)`

Assert that a light exists and is off.

`assertLightOn(light_name)`

Assert that a light exists and is on.

`assertListEqual(list1, list2, msg=None)`

A list-specific equality assertion.

Parameters:

* **list1** – The first list to compare.
* **list2** – The second list to compare.
* **msg** – Optional message to use on failure instead of a list of differences.

`assertLogs(logger=None, level=None)`

Fail unless a log message of level level or higher is emitted on logger_name or its children. If omitted, level defaults to INFO and logger defaults to the root logger.

This method must be used as a context manager, and will yield a recording object with two attributes: output and records. At the end of the context manager, the output attribute will be a list of the matching formatted log messages and the records attribute will be a list of the corresponding LogRecord objects.

Example:

```
with self.assertLogs('foo', level='INFO') as cm:
  logging.getLogger('foo').info('first message')
  logging.getLogger('foo.bar').error('second message')
self.assertEqual(cm.output, ['INFO:foo:first message',
  'ERROR:foo.bar:second message'])
```

`assertMachineVarEqual(value, machine_var)`

Assert that a machine variable exists and has a certain value.

`assertModeNotRunning(mode_name)`

Assert that a mode exists and is not running.

`assertModeRunning(mode_name)`

Assert that a mode exists and is running.

`assertMultiLineEqual(first, second, msg=None)`

Assert that two multi-line strings are equal.

`assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)`

Fail if the two objects are equal as determined by their difference rounded to the given number of decimal places (default 7) and comparing to zero, or by comparing that the difference between the two objects is less than the given delta.

Note that decimal places (from zero) are usually not the same as significant digits (measured from the most significant digit).

Objects that are equal automatically fail.

`assertNotEqual(first, second, msg=None)`

Fail if the two objects are equal as determined by the ‘!=’ operator.

`assertNotIn(member, container, msg=None)`

Just like self.assertTrue(a not in b), but with a nicer default message.

`assertNotIsInstance(obj, cls, msg=None)`

Included for symmetry with assertIsInstance.

`assertNotLightChannel(light_name, brightness, channel='white')`

Assert that a light channel does not have a certain brightness.

`assertNotLightColor(light_name, color)`

Assert that a light exists and does not show a certain color.

`assertNotRegex(text, unexpected_regex, msg=None)`

Fail the test if the text matches the regular expression.

`assertNumBallsKnown(balls)`

Assert that a certain number of balls are known in the machine.

`assertPlaceholderEvaluates(expected, condition)`

Assert that a placeholder evaluates to a certain value.

`assertPlayerVarEqual(value, player_var)`

Assert that a player variable exists and has a certain value.

`assertRaises(expected_exception, *args, **kwargs)`

Fail unless an exception of class expected_exception is raised by the callable when invoked with specified positional and keyword arguments. If a different type of exception is raised, it will not be caught, and the test case will be deemed to have suffered an error, exactly as for an unexpected exception.

If called with the callable and arguments omitted, will return a context object used like this:

```
with self.assertRaises(SomeException):
  do_something()
```
An optional keyword argument ‘msg’ can be provided when assertRaises is used as a context object.

The context manager keeps a reference to the exception as the ‘exception’ attribute. This allows you to inspect the exception after the assertion:

```
with self.assertRaises(SomeException) as cm:
  do_something()
the_exception = cm.exception
self.assertEqual(the_exception.error_code, 3)
```

`assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)`

Asserts that the message in a raised exception matches a regex.

Parameters:

* **expected_exception** – Exception class expected to be raised.
* **expected_regex** – Regex (re.Pattern object or string) expected to be found in error message.
* **args** – Function to be called and extra positional args.
* **kwargs** – Extra kwargs.
* **msg** – Optional message used in case of failure. Can only be used when assertRaisesRegex is used as a context manager.

`assertRegex(text, expected_regex, msg=None)`

Fail the test unless the text matches the regular expression.

`assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)`

An equality assertion for ordered sequences (like lists and tuples).

For the purposes of this function, a valid ordered sequence type is one which can be indexed, has a length, and has an equality operator.

Parameters:

* **seq1** – The first sequence to compare.
* **seq2** – The second sequence to compare.
* **seq_type** – The expected datatype of the sequences, or None if no datatype should be enforced.
* **msg** – Optional message to use on failure instead of a list of differences.

`assertSetEqual(set1, set2, msg=None)`

A set-specific equality assertion.

Parameters:

* **set1** – The first set to compare.
* **set2** – The second set to compare.
* **msg** – Optional message to use on failure instead of a list of differences.

assertSetEqual uses ducktyping to support different types of sets, and is optimized for sets specifically (parameters must support a difference method).

`assertSwitchState(name, state)`

Assert that a switch exists and has a certain state.

`assertTrue(expr, msg=None)`

Check that the expression is true.

`assertTupleEqual(tuple1, tuple2, msg=None)`

A tuple-specific equality assertion.

Parameters:

* **tuple1** – The first tuple to compare.
* **tuple2** – The second tuple to compare.
* **msg** – Optional message to use on failure instead of a list of differences.

`assertWarns(expected_warning, *args, **kwargs)`

Fail unless a warning of class warnClass is triggered by the callable when invoked with specified positional and keyword arguments. If a different type of warning is triggered, it will not be handled: depending on the other warning filtering rules in effect, it might be silenced, printed out, or raised as an exception.

If called with the callable and arguments omitted, will return a context object used like this:

```
with self.assertWarns(SomeWarning):
  do_something()
```

An optional keyword argument ‘msg’ can be provided when assertWarns is used as a context object.

The context manager keeps a reference to the first matching warning as the ‘warning’ attribute; similarly, the ‘filename’ and ‘lineno’ attributes give you information about the line of Python code from which the warning was triggered. This allows you to inspect the warning after the assertion:

```
with self.assertWarns(SomeWarning) as cm:
  do_something()
the_warning = cm.warning
self.assertEqual(the_warning.some_attribute, 147)
```

`assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)`

Asserts that the message in a triggered warning matches a regexp. Basic functioning is similar to assertWarns() with the addition that only warnings whose messages also match the regular expression are considered successful matches.

Parameters:

* **expected_warning** – Warning class expected to be triggered.
* **expected_regex** – Regex (re.Pattern object or string) expected to be found in error message.
* **args** – Function to be called and extra positional args.
* **kwargs** – Extra kwargs.
* **msg** – Optional message used in case of failure. Can only be used when assertWarnsRegex is used as a context manager.

`fail(msg=None)`

Fail immediately, with the given message.

`static get_abs_path(path)`

Get absolute path relative to current directory.

`get_absolute_machine_path()`

Return absolute machine path.

`get_config_file()`

Return a string name of the machine config file to use for the tests in this class.

You should override this method in your own test class to point to the config file you need for your tests.
Returns:	A string name of the machine config file to use, complete with the .yaml file extension.

For example:

```
def get_config_file(self):
  return 'my_config.yaml'
```

`get_enable_plugins()`

Control whether tests in this class should load MPF plugins.

Returns: True or False

The default is False. To load plugins in your test class, add the following:

```
def get_enable_plugins(self):
  return True
`

`get_machine_path()`

Return a string name of the path to the machine folder to use for the tests in this class.

You should override this method in your own test class to point to the machine folder root you need for your tests.
Returns:	A string name of the machine path to use

For example:

```
def get_machine_path(self):
  return 'tests/machine_files/my_test/'
```

Note that this path is relative to the MPF package root

`get_options()`

Return options for the machine controller.

`get_platform()`

Force this test class to use a certain platform.
Returns:	String name of the platform this test class will use.

If you don’t include this method in your test class, the platform will be set to virtual. If you want to use the smart virtual platform, you would add the following to your test class:

```
def get_platform(self):
  return 'smart_virtual`
```

`get_use_bcp()

Control whether tests in this class should use BCP.

Returns: True or False

The default is False. To use BCP in your test class, add the following:

```
def get_use_bcp(self):
  return True
```

`hit_and_release_switch(name)`

Momentarily activates and then deactivates a switch.

Parameters:

* **name** – The name of the switch to hit.

This method immediately activates and deactivates a switch with no time in between.

`hit_and_release_switches_simultaneously(names)`

Momentarily activates and then deactivates multiple switches.

Switches are hit sequentially and then released sequentially. Events are only processed at the end of the sequence which is useful to reproduce race conditions when processing nearly simultaneous hits.

Parameters:

* **names** – The names of the switches to hit and release.

`hit_switch_and_run(name, delta)`

Activates a switch and advances the time.

Parameters:

* **name** – The name of the switch to activate.
* **delta** – The time (in seconds) to advance the clock.

Note that this method does not deactivate the switch once the time has been advanced, meaning the switch stays active. To make the switch inactive, use the release_switch_and_run().

`machine_run()`

Process any delays, timers, or anything else scheduled.

Note this is the same as:

self.advance_time_and_run(0)

`mock_event(event_name)`

Configure an event to be mocked.

Parameters:

* **event_name** – String name of the event to mock.

Mocking an event is an easy way to check if an event was called without configuring some kind of callback action in your tests.

Note that an event must be mocked here before it’s posted in order for assertEventNotCalled() and assertEventCalled() to work.

Mocking an event will not “break” it. In other words, any other registered handlers for this event will also be called even if the event has been mocked.

For example:

```
self.mock_event('my_event')
self.assertEventNotCalled('my_event')  # This will be True
self.post_event('my_event')
self.assertEventCalled('my_event')  # This will also be True
```

`post_event(event_name, run_time=0)`

Post an MPF event and optionally advance the time.

Parameters:

* **event_name** – String name of the event to post
* **run_time** – How much time (in seconds) the test should advance after this event has been posted.

For example, to post an event called “shot1_hit”:

```
self.post_event('shot1_hit')
```

To post an event called “tilt” and then advance the time 1.5 seconds:

```
self.post_event('tilt', 1.5)
```

`post_event_with_params(event_name, **params)`

Post an MPF event with kwarg parameters.

Parameters:

* **event_name** – String name of the event to post
* ****params** – One or more kwarg key/value pairs to post with the event.

For example, to post an event called “jackpot” with the parameters count=1 and first_time=True, you would use:

```
self.post_event('jackpot', count=1, first_time=True)
```

`post_relay_event_with_params(event_name, **params)`

Post a relay event synchronously and return the result.

`release_switch_and_run(name, delta)`

Deactivates a switch and advances the time.

Parameters:

* **name** – The name of the switch to activate.
* **delta** – The time (in seconds) to advance the clock.

`reset_mock_events()`

Reset all mocked events.

This will reset the count of number of times called every mocked event is.

`restore_sys_path()`

Restore sys path after test.

`save_and_prepare_sys_path()`

Save sys path and prepare it for the test.

`setUp()`

Setup test.

`set_num_balls_known(balls)`

Set the ball controller’s num_balls_known attribute.

This is needed for tests where you don’t have any ball devices and other situations where you need the ball controller to think the machine has a certain amount of balls to run a test.

Example:

self.set_num_balls_known(3)

`shortDescription()`

Returns a one-line description of the test, or None if no description has been provided.

The default implementation of this method returns the first line of the specified test method’s docstring.

`skipTest(reason)`

Skip this test.

`start_mode(mode)`

Start mode.

`stop_mode(mode)`

Stop mode.

`tearDown()`

Tear down test.

`static unittest_verbosity()`

Return the verbosity setting of the currently running unittest program, or 0 if none is running.

Returns: An integer value of the current verbosity setting.


