---
title: API Reference - Randomizer
---

# Randomizer API Reference

``` python
class mpf.core.randomizer.Randomizer(items)
```

Bases: `object`

Generic list randomizer.

## Methods & Attributes

The Randomizer has the following methods & attributes available. Note that methods & attributes inherited from the base class are not included here.

`get_current()`

Return current item.

`get_next()`

Return next item.

`loop`

Return loop property.

`static pick_weighted_random(items)`

Pick a random item.

Parameters:

* **items** – Items to select from
