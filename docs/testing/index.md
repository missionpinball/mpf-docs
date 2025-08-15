---
title: How to test your game code
---


# How to test your MPF game code

(You mean, other than taking it to a show to see what breaks?)

This is an incomplete placeholder, but here are the things to cover.

--8<-- "todo.md"

You can write automated tests which "play" your game and look for bugs. These tests are pretty fun. They're basically a script that does something, then checks the state of something else. For example:

* Do something: push start
* Check for something: was a ball ejected out of the trough?

Or, to test a lane change feature.

* Confirm that Lane 1 LED is on (or a certain color), and Lanes 2, 3, and 4 are off.
* Hit the right flipper buttton
* Confirm that Lane 2 LED is on (or a certain color), and Lanes 1, 3, and 4 are off.

Every time you add a feature or capability to your game, you should add a test. (Actually, there's a school of thought called
Test Driven Developer / TDD which says you should write your tests *before* you implement a new feature. Obviously the tests will fail, but once they pass that means your feature is done!)

I can 100% guarantee that writing good tests will save you time in the long run AND it will make your game more stable.
2:36

Bonus: there are “fuzz” tests too which are just automated tests that hit all the switches randomly and make sure MPF doesn't crash or hang. Good for beefing up your machine before you're done, and something you should set up EARLY and run OFTEN so you don't have surprises 2 days before a show

Consolidate this content to here:

* https://missionpinball.org/latest/tutorial/19_unit_testing/
* https://developer.missionpinball.org/en/dev/testing/writing_machine_tests.html
* https://developer.missionpinball.org/en/dev/testing/tutorial/2.html

Example tests:

* https://github.com/GabeKnuth/BnD/blob/master/tests/test_bnd.py