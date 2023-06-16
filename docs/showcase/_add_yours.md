---
title: Add your project to this list
---

# Add your project to the MPF showcase page!

These instructions are quick and temporary. You can help by writing
more detailed ones!

--8<-- "todo.md"

To add your project to the list on this page, you need to add a file
into the `mpf-docs` showcase folder. (You need to add it to the showcase
folder in the root of the repo):

https://github.com/missionpinball/mpf-docs/tree/main/showcase

Make a copy of the file `_TEMPLATE.yaml` and name it based on your project. Then
edit the entries in there. You can look at the other projects for examples, such as:

`brooks_and_dunn.yaml`

``` yaml

name: Brooks and Dunn
acronym: BnD
team: Gabe Knuth and Brian Madden
location: Chicago, IL, USA
started: 2016-09-07
finished: 2017-04-02
images:
project_type:
youtube_video_ids: uRJKHMzU5vM
documentation_link: https://pinside.com/pinball/forum/topic/brooks-dunn
code_link: https://github.com/GabeKnuth/BnD
gameplay_link:
controller: FAST
description: >

  This game was entering production just as Gottlieb shut down and ceased operations
  (see [IPDB](https://www.ipdb.org/machine.cgi?id=4008) for more history).
  Gabe got it from Mike and finished it with some input from the original designers.

```

When this change is merged in, it will be included when the site is built.
