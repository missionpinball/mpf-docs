High score (mode)
=================

MPF includes a built-in high score mode that can be used
to track high scores, including letting players enter their names (or
initials) and tracking different high score awards. (See the How To:
High Scores guide for details).

You can use the config files to completely customize how the high
scores work, including the number of scores to track, what you call
each award ("GRAND CHAMPION", "HIGH SCORE 1", etc.) and what (and how
many) awards you track (score, loops, aliens blasted, etc.).

The high score mode stores its high
scores in *<your_machine_folder>/data/high_scores.yaml* file. It
automatically reads them in when MPF boots to create machine variables
that can be accessed from your game, and it automatically updates the
high scores on disk when they change after a game ends.
