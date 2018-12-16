Tutorial step 2a: Testing your machine
======================================

Before we continue to Step 3, we want to take a moment to let you know about MPF's automated testing features.

One of the cool things about MPF is that you can write "tests" which actually launch and run MPF and your
machine config and then check to make sure everything is alright. These tests can hit switches and check to
make sure that coils fired, or that lights are the right color, or that a certain mode is running, or that certain
text is on the display, etc.

What's great about these tests is that they're easy to write, so you can write them bit-by-bit as you're creating
your MPF config files. Eventually you'll have tests that cover hundreds of little things, and you can run them
every time you change something in your config. Then down the road when your config is very advanced, you might
be changing something in one area that accidentally breaks something else. (Maybe a mode doesn't stop properly so
an unrelated playfield light is the wrong color.) Without tests, you might only find the bug after hours of play,
but with the tests, you'll know immediately that something isn't right.

The only "catch" with the tests is that they're written in Python, so you have to learn a little Python to be able
to use them. If you don't want to worry about tests right now because you're just learning MPF or just getting
started, that's fine. No problem! But we wanted to make sure that you knew that these automated tests were available.

We have a tutorial which explains how to write tests on our developer site which follows this general tutorial (that
you're reading now) 1-to-1. In other words, Step 2 in the MPF tutorial created an empty config file and got MPF up
and running with the attract mode active, and Step 2 in the test writing tutorial shows how to write a test that
verifies everything is ok.

In fact we have tests for every step in the tutorial in the MPF Examples repository. (That's what's in the "tests"
folder in each step's machine folder.) You can even run the tests yourself (even if you don't know Python or don't
know how to write tests) to verify that the config files you typed in are entered correctly.

More information about writing unit tests for your machine, as well as the test writing tutorial, is available
here: `<http://developer.missionpinball.org/en/dev/testing/writing_machine_tests.html>`_.
