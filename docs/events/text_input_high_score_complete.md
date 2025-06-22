---
title: text_input_high_score_complete
---

# text_input_high_score_complete


--8<-- "event.md"

Event is posted by the BCP integration for the [high_score](../config/high_score.md) built-in mode.
When using the high_score built-in behaviors, 

## Keyword arguments

(See the [Conditional Events](overview/conditional.md)
guide for details for how to create entries in your config file that
only respond to certain combinations of the arguments below.)

#### text:

The text value submitted for the current record. This value will be saved
with the record and transmitted through the events
[(award_name)\_award_display](award_name_award_display.md),
[(category_name)\_award_display](category_name_award_display.md),
and [high_score_award_display](high_score_award_display.md)
so that any following slides may display the name back to the user.
