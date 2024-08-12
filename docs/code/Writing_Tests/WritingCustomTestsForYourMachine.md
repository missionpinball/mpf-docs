
# Writing Custom Tests for your Machine

As we already mentioned, the creators of MPF are HUGE believers in the value of automated testing. To that end, MPF includes everything you need to write automated tests that test the logical functionality of your machine. These tests are extremely valuable even if your game is just based on config files.

For example, you can write a test that simulates starting a game, launching a ball, hitting a sequence of switches, and then verifying that a certain mode is running, or a light is the right color, or an achievement group is in the proper state, etc. Then you can advance the time to timeout a mode and verify that the mode as stopped, etc, etc.

When you first start building your MPF config, you might think, “What’s the point?”… especially with some of the more simple tests. However your MPF config files will get complex pretty quickly, and often times you’ll think you have some mode done and working perfectly, but then a month later you change something that seems unrelated which ends up breaking it. Unfortunately this usually happens without you knowing it, and by the time you realize that something broke, more times has passed and it’s hard to figure out what broke what.

So this is where unit tests come in! :)

If you write simple unit tests that test each new thing you add to an MPF config file, then over time you’ll end up with a huge library of tests for your game. If you get in the habit of running your tests often, then you’ll know right away if a change that you made broke something. (And you’ll also know when everything is ok when all your tests pass again!)

Tutorial for writing your own tests

We have a complete tutorial which walks you through writing tests for your own machine. This tutorial conveniently follows the general MPF tutorial at docs.missionpinball.org. Each step here matches the step with the same number there. (Just make sure you’ll looking at the same version of the documentation in both places.)

In the general MPF tutorial, each step builds on the previous to add more features to the config files for the tutorial project. In the unit test tutorial (what you’re reading here), each step shows you how to write the unit tests which test the new features you just added to the tutorial machine.

You can follow along and learn here:

## Step by Step Tutorial

At this point of time you should have MPF already installed and have some basic game setup.

### 1. Create a “tests” folder in your machine folder

First, create a folder called tests in your machine folder. This would be alongside the other folders in there, which will be “config” (created in the MPF tutorial), as well as “logs” and “data” which were created automatically by MPF the first time it ran.

### 2. Add an empty `__init__.py` file

Next, inside your new tests folder, create a blank file called `__init__.py`. (That’s two underscores, then the word “init”, then two more underscores, then “.py”.) This file should be totally blank. (It just needs to exist.) This file is needed to let the Python test runner find and load the tests from this folder.

### 3. Add a test file

Next you need to add a Python file which actually holds your tests. You can name this file whatever you want as long as it starts with “test”. (The reason for starting it with “test” is also so that the Python test runner knows that this file contains tests, allowing it to automatically find and run tests from it.)

For now let’s call it test_step_2.py.

Open that file and add the following lines to it: (If you are interested in what all this means, then read on below the file. Otherwise you can skip down to Step 4.)

So what’s this file actually doing?

The import line just imports the base class we use for MPF machine tests. (More details on that is covered in the Testing Class API page).

Our specific class name TestTutorialMachine can be whatever you want. Again just make sure it starts with “Test” in order for the test runner to find out.

Our specific method is called test_step_2_mpf_startup(). (Also it has to start with “test”). When the tests are run each method represents a separate “run” of MPF. The test runner will start up MPF and get it all up and running, and then it will move through the code in the test method, then it will cleanly shut down MPF when it’s done. If there are multiple test methods, then the test running will start and stop MPF multiple times. The key is that each test method is run against a “fresh” MPF copy.

These test methods will also load the machine config files (just like if the command mpf was run the regular way).

Anyway, in our test method, we have the only actual line that does anything:

```
self.assertModeRunning('attract')
```

This just tests (“asserts”) that a mode called “attract” is running. There are all sorts of MPF-specific assertion methods which we’ll cover in later steps of this tutorial.

### 4. Run your test

You can run your tests via the command prompt from your machine folder. (In other words, the same place where you run mpf to run your machine.)

The exact command to run is `python -m unittest`. This should produce output similar to the following:

```
C:\pinball\your_machine>python -m unittest
C:\Python34\lib\imp.py:32: PendingDeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses
  PendingDeprecationWarning)
.
----------------------------------------------------------------------
Ran 1 test in 0.734s

OK

C:\pinball\your_machine>
```

That warning about the deprecation can be ignored (if you even have it.. you might not). The important thing is the message towards the bottom: “Ran 1 test in 0.734s” and the “OK” below it. That means your test passed!

### 5. Check out a failed test

When you’re writing unit tests, you’ll end up dealing with failed tests a lot! So let’s purposefully change the test so it fails. In this case, change the line which asserts a mode called “attract” is running to look for a mode called “foo” instead, like this:

```
self.assertModeRunning('foo')
```

Save the file and rerun the tests and you should see results like this:

```
C:\pinball\your_machine>python -m unittest
C:\Python34\lib\imp.py:32: PendingDeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses
  PendingDeprecationWarning)
F
======================================================================
FAIL: test_mpf_starts (tests.test_step_2.TestTutorialMachine)
Tests Step 2 of the tutorial
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\pinball\your_machine\tests\test_step_2.py", line 18, in test_mpf_starts
    self.assertModeRunning('foo')
  File "C:\Python34\lib\site-packages\mpf\tests\MpfTestCase.py", line 576, in assertModeRunning
    raise AssertionError("Mode {} not known.".format(mode_name))
AssertionError: Mode foo not known.

----------------------------------------------------------------------
Ran 1 test in 0.594s

FAILED (failures=1)

C:\pinball\your_machine>
```

Note that we see the test run failed, with one failure, and that we can scroll up and see the specific name of the test that failed along with the line that failed, and information about the failure. (In this case it tells us that the mode “foo” is not known.)

So to get this test to work, you either need to change your MPF config to start a mode called “foo”, or you need to change the test back to looking for a mode called “attract”. :)

### What if it didn’t work?

If the unit tests don’t work for you, there are a few things you can try.

If you get some kind of loading error or config error, make sure you’re running python -m unittest from your machine folder (not from the “tests” folder).

If you get a message about 0 tests run, make sure you have that empty __init__.py in your tests folder.

And if you get some weird error that you can’t figure out, then post a message to the MPF Google Group.


