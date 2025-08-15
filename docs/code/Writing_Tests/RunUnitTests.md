# How to run MPF unittests

Once MPF is installed, you can run some automated tests to make sure that everything is working.
Let's assume your mpf virtual folder is `mpfenv` and stored here

Windows:
``` console
C:\Users\myname\mpfenv
```
Linux:
``` console
/home/myname/mpfenv
```
Note that you need to activate your virtual environment to run tests the same way you do to run your game. Assuming you are in your users home directory, run:

Windows:
``` console
mpfenv\Scripts\activate.bat
```
Linux:
``` console
mpfenv/bin/activate
```
Now change into the directory where the tests are stored in your console, which is:

Windows:
``` console
C:\Users\myname\mpfenv\Lib\site-packages\mpf\tests
```
Linux:
``` console
/home/myname/mpfenv/lib/python3.11/site-packages/mpf/tests
```
You might have a different version of python and your path might differ slightly.
Now you have different options on how to run the tests. You can either run all tests at once, or only all tests in one test file or only one single test. Which option is best for you depends on your needs.

## Running all tests at once

To do this, open a command prompt, and then type the following command and then press `<enter>`:

``` console
python3 -m unittest discover <path to test directory>
```
Where `<path to test directory>` is the path to the directory where you tests are stored. If you have followed the steps above you are already in that directory and you just omit this value.

You should see a bunch of dots on the screen (one for each test that's run), and then when it's done, you should see a message showing how many tests were run and that they were successful. The whole process should take less a minute or so.

(If you see any messages about some tests taking more than 0.5s, that's ok.)

The important thing is that when the tests are done, you should have a message like this:

``` console
Ran 587 tests in 27.121s

OK

C:\>
```

Note that the number of tests is changing all the time, so it probably won't be exactly 587. And also the time they took to run will be different depending on how fast your computer is.

These tests are the actual tests that the developers of MPF use to test MPF itself. We wrote all these tests to make sure that updates and changes we add to MPF don't break things. :) So if these tests pass, you know your MPF installation is solid.

## Running all test of a single test file
If you have the need only to test all tests in a single test file you can specify the test file in your directory
``` console
python -m unittest test_SegmentDisplay.py
```
That obviously runs all tests in the file called `test_SegmentDisplay.py`, which makes sense to save time if your code changes only took place in that part of the code.

## Running a single test
If only one test fails and you need to execute it more often you can even specify only that one single test
``` console
python -m unittest test_SegmentDisplay.TestSegmentDisplay.test_transitions_with_player
```
where the syntax has the following format
``` console
python -m unittest <file name without py extension>.<Class name within file>.<name of test>
```

## Testing the MPF media controller
Remember though that MPF is actually two separate parts, the MPF game engine and the MPF media controller. The command you run just tested the game engine, so now let's test the media controller. To do this, run the following command (basically the same thing as last time but with an “mc” added to the end, like this):

``` console
python3 -m unittest discover mpfmc/tests
```

(Note that mpfmc does not have a dash in it, like it did when you installed it via pip.)

When you run the MPF-MC tests, you should see a graphical window pop up on the screen, and many of the tests will put graphics and words in that window. Also, some of the tests include audio, so if your speakers are on you should hear some sounds at some point.

These tests take significantly longer (maybe 8x) than the MPF tests, but when they're done, that graphical window should close, and you'll see all the dots in your command window and a note that all the tests were successful.

Notes about the MPF-MC tests:

* These tests create a window on the screen and then just re-use the same window for all tests (to save time). So don't worry if it looks like the window content is scaled weird or blurry or doesn't fill the entire window.
* Many of these tests are used to test internal workings of the media controller itself, so there will be lots of time when the pop up window is blank or appears frozen since the tests are testing non-visual things.
* The animation and transition tests include testing functionality to stop, restart, pause, and skip frames. So if things look “jerky” in the tests, don't worry, that doesn't mean your computer is slow, it's just how the tests work! :)
