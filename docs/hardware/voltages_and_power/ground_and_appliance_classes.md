---
title: Ground and Appliance Classes
---

# Ground and Appliance Classes


Pinball machines commonly are classified as class 1 devices according to
IEC 61140 (US) and EN 61140 (Europe). When building or modifying pinball
machines you should understand which requirements need to be met for
safe operations.

!!! warning

    If you are unsure ask a professional electric engineer. This guide does
    not provide all information needed to design and operate a
    high-voltage/high-current system in a pinball machine. Use this at your
    own risk. Electricity can be dangerous and might kill you or burn down
    your house.

FAST Pinball has wiring guides for machines built on their platforms,
but even if you're not using FAST Pinball hardware, there are some relevant ones here:

* [FAST Pinball guide to pinball ground and grounding](https://fastpinball.com/wiring/grounding/)

Video about ground:

<div class="video-wrapper">
<iframe width="560" height="315" src="https://www.youtube.com/embed/cFdT7YdXGO0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Class 1 appliances

Class 1 appliances typically connect to a 3-prong AC connector which
contains separate ground/electrical earth and neutral. They require that
a single fault (e.g. a disconnected conductor wire touching the lock
down bar of the machine) may not cause an electric shock. For that
reason, all conducting parts need to be connected to the ground. In
pinball machines, those are all metal parts such as:

* Legs
* Backbox connector metal parts
* Speaker grills
* Lockdown bar
* Service door
* Screws on the cabinet side

In a lot of cases braid copper wire is used to connect those parts to
ground. You should test that a low-impedance connection between any
conducting parts and ground exist. See [Application
classes](https://en.wikipedia.org/wiki/Appliance_classes) for details.

## Common Ground

If you operate more than one power supplies in your machine make sure to
connect all their neutral connectors (N; 0V; commonly referred as
ground). Funcionally, this is needed for logic components to maintain a
common reference. Additionally, a floating ground might become dangerous
when working with voltage multiple voltages. See
[Voltages and Power](voltages_and_power.md) for details.
