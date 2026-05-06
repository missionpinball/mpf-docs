---
title: match_has_match
---

# match_has_match


--8<-- "event.md"

At least one player has a match.

This is a queue event. The match mode match_has_match
will not be complete until the queue is cleared.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

#### `match_number0`:

Match number for player 0

#### `match_number1`:

Match number for player 1

#### `match_number1_won`:

True/False for whether player 1 matched.

#### `match_numberX`:

Match number for player X (up to max players)

#### `match_numberX_won`:

True/False for whether player X matched (up to max players).

#### `winner_number`:

Winner number

#### `winners`:

Number of winners (always more than 0 here)
