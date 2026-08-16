---
title: How to find MPF example config files
---

# The MPF repo is full of "real" config file examples. Here's how to find them.

Are you looking for example config files you can use to see how certain settings
should be used? There's a great resource built right into the MPF and MPF-MC repos!

## Look at MPF / MPF-MC test config files

Both MPF and MPF-MC contain thousands of tests which ensure that every part of MPF
works as expected. These tests are run automatically on GitHub every time a change is made
to the repo. Since these tests check everything, there are lots of machine and
mode config files used by the tests themselves.

So if you need to see an example of how to use a certain setting, you can look at
the test config files to see how they're used in real life. (And, since these tests
are run automatically, you can be sure that the examples really work and are up to date,
because if a test fails, the change to MPF would not be accepted.)

## Where are the test config files?

Both the MPF and MPF-MC repo have tests which use config files. If you need a example of something from
MPF, (coils, lights, game logic, etc.), look in the MPF repo tests. And if you need something from the MC (displays,
slides, widgets, sounds, etc.), then look in the MPF-MC repo tests. Here are the folder paths to where you'd find the
test machine config files:

* [MPF Repo Root: /mpf/tests/machine_files](https://github.com/missionpinball/mpf/tree/dev/mpf/tests/machine_files)
* [MPF-MC Repo Root: /mpfmc/tests/machine_files](https://github.com/missionpinball/mpf-mc/tree/dev/mpfmc/tests/machine_files)

We'll show you how to find config file examples from your locally downloaded copy of the MPF repo, and then after that, how to
find them on the web.

## Finding config examples from your local downloaded MPF repo

If you've downloaded the MPF or MPF-MC repo to your local machine, you can find the test config files locally. (Note the MPF repo
is often in a folder called `mpf`, and then inside there is another folder called `mpf` which is where the MPF code is. So it might be
`/mpf/mpf/tests...` for you.)

But look here, `mpf` :octicons-arrow-right-24: `tests` :octicons-arrow-right-24: `machine_files`. Now look at all the subfolders for each test type, and further the machine and mode config files in there.

![Alt text](<images/tests in file system.png>)

Here's an example looking at the achievement group tests, in a mode config file:

![Alt text](<images/vscode 2.jpg>)

Of course it's also possible (and easier) to use whatever tool you're developing your game in to search for the config files. Here's an example using [Visual Studio Code](https://code.visualstudio.com). (This is what we recommend you use to develop your game. It's free!)

Here's an example of using VS Code to search for an example `ball_saves:` config file setting. Note that we include the colon so we just get config file examples. You can further set the search to just look in the `tests/machine_files` folder and/or to only include .yaml files. (Remember to use the MPF repo if you're looking for MPF examples, and the MPF-MC repo if you're looking for MC examples.)

![Alt text](<images/vscode 1.jpg>)

## Finding config file examples on the web

If you want to find config file examples on the web, you can do that by searching through the MPF/MPF-MC repos on GitHub.com.
To do that, visit the Mission Pinball homepage at [GitHub.com/missionpinball](https://github.com/missionpinball):

![Mission Pinball homepage on GitHub.com](<images/github 9.jpg>)

Click in the search box at the top of the page. That will automatically set a search file to only search through files from the
Mission Pinball organization (versus searching every file from every repo on GitHub.com!)

![Alt text](<images/github 12.jpg>)

Type what you're looking for, in this case, example configs for `ball_search:` so we'll search for ball_search: including the colon since we want an example from a config file.

![Alt text](<images/github 13.jpg>)

Boom! Lots of results, but notice the first one is an .md file which is a documentation text file, not a config example.

![Alt text](<images/github 11.jpg>)

Click on the YAML option in the languages sidebar to limit the search results to only YAML files:

![Alt text](<images/github yaml.jpg>)

And now see just real config file examples in YAML files. Note that these files are from various locations in MPF.

![Alt text](<images/github 14.jpg>)

You can scroll down to see the ones from the tests/machine_files folder:

![Alt text](<images/github 8.jpg>)
