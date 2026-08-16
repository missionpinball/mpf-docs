---
title: text_input_(name)_complete
---

# text_input_(name)_complete


--8<-- "event.md"

Event is posted by the BCP integration for a [text input](../gmc/reference/mpf-text-input.md)
(such as in the [high score](../config/high_score.md) built-in mode.

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

#### text:

The text value submitted for the current record. This value will be saved
with the record and transmitted through the event
[high_score_award_display](high_score_award_display.md)
so that any following slides may display the name back to the user.
