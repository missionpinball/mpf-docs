---
title: Bonus Mode Settings
---

# Bonus Mode Configuration

With MPF 0.80 the bonus configuration is consolidated and simplified, providing a single *bonus_entry* event for all bonus-related information.

The *bonus.yaml* config spec has changed slightly as well, but is quick to migrate.

#### Summary of Changes from MPF 0.57:

  * Individual bonus events are gone: all bonus events are now the *bonus_entry* event
  * `event:` config is now `entry`
  * `text:` config option (new) for display text

### Creating Bonus Entries

In your *bonus.yaml* config file, create a `mode_settings:` section with a subsection `bonus_entries:`. Each bonus entry will be a list item under `bonus_entries:`, like so:

``` yaml
mode_settings:
    bonus_entries:
        - entry: loops_completed
          text: "Ranger Loops"
          player_score_entry: ranger_loops_count
          score: 10_000
        - entry: songs_completed
          text: "Songs Sung"
          player_score_entry: total_songs
          score: 5_000
```

### `mode_settings` Config Reference

#### `entry:`

Single value, type `String`. Required.

A key for the bonus entry that will be posted as part of the event. Any unique name will do **except for** the reserved values `subtotal`, `multiplier`, and `total`.

#### `reset_player_score_entry:`

Single value, type `boolean`. Default `false`.

If true, the `player_score_entry` player variable will be reset to zero after the bonus is awarded. Useful for awarding bonuses based on per-ball accomplishments.

#### `score:`

Single value, type `integer`. Required. Dynamic values supported.

The number of points scored for this bonus entry. If `player_score_entry` is provided, this number of points will be multiplied by the player score entry to calculate the full score of this bonus entry.

#### `skip_if_zero:`

Single value, type `boolean`. Default `true`

If true, this bonus entry will not be posted if the calculated bonus score is zero.

#### `skip_if_negative:`

Single value, type `boolean`. Default `false`

If true, this bonus entry will not be posted if the calculated bonus score is less than zero.

#### `text:`

Single value, type `string`. Default `None`

A text string to be passed with the *bonus_entry* event that describes the bonus being awarded.

#### `player_score_entry:`

Single value, type `string`. Default `None`

A player variable that will be multiplied by the `score` for this bonus entry's point award. In other words, the player will receive a bonus `score` amount for every `player_score_entry` they have.