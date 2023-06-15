---
title: Welcome to the Mission Pinball Framework!
search:
    exclude: true  # exclude's this page from the site search
---

# Hello World! Make your first edit!

This is the Mission Pinball website "welcome wall"! It's a place where
people can experiment and try out editing the site with no fear of
breaking anything.

## How to edit this page

Look, lines that start with a # are top level headings. Two hashes are
level 2 headings, etc.

How do links work?

[This is my text](https://missionpinball.org)

Or a link to [another local page](about/index.md)

## Don't worry, we will approve this first!

If you make a pull request, you won't break anything. Your request will
be reviewed by an MPF maintainer before it's merged. No worries!

!!! note "Do you want to be an MPF maintainer?"

    We could use the help. Jump in!

Change something!

## How to format .md files

These .md files are "markdown" format, which is readable in its source form
but can also be processed and converted to HTML when the website is built.
Here are some formatting things you can do.

Add backticks (upper left key with the ~, not a single quote ') to make things
print `like a computer`. You see? `like` `this`.

### Three hashes is a Heading 3

#### Four hashes is Heading 4

Simple!

https://www.markdownguide.org/basic-syntax

Links are easy. Put the text you want in brackets and put the link in parenthesis
right after it. No spaces. Like this:

[Writing with Markdown](https://www.mkdocs.org/user-guide/writing-your-docs/#writing-with-markdown)

Bullet lists are

* Done like
* This
  * You can even add sub bullets
  * Like this

Italics?

*You can have ChatGPT help you with MD formatting. It's really good at it!*

What about **bold**?

### Embedding snippets from other pages

Check out the [`/includes`](https://github.com/missionpinball/mpf-docs/tree/main/includes) folder for a
list of little snippets you can include in any page. Such as the TODO box as seen below. To include a snippet, you just put this on its own line: `--8<--` plus the file name in quotes. (It's little scissors,
get it?)

--8<-- "todo.md"

Hey that rendered all the contents of that todo.md into this page. Cool!
