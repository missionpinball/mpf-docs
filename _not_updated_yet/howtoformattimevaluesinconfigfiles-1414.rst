
You machine configuration files are full of settings which require
time values to be entered, such as "10 seconds" or "250 milliseconds."
Rather than arbitrarily decide which values should be entered as
seconds versus milliseconds, we've built MPF so that you can enter
either one whenever a time entry is needed which MPF will internally
convert to the proper value. These time values are used all over the
place. (Ball device count delays, ball save time, ball search
settings, reset delays, etc.) We'll use an example from a ball device
forthe `ball_count_delay` `:` setting. (Again, this is just an
example. You use these same options whenever you need to enter a time
value):



Entering a time duration in seconds
-----------------------------------

To enter a time duration in seconds, simply add an "s" or "sec" after
your number. (This can be uppercase or lowercase and you can put a
space in between your number and the letters if you want.) Some
examples: `ball_count_delay` `: 0.5s` `ball_count_delay` `: 0.5 S`
`ball_count_delay` `: 0.5sec`



Entering a time duration in milliseconds
----------------------------------------

To enter a time duration in seconds, simply add an "ms" or "msec"
after your number. (This can be uppercase or lowercase, and you can
put a space in between your number and the letters if you want.) Note
that if you do not enter and letters, then MPF will read in the time
duration as milliseconds. Some examples: `ball_count_delay` `: 500ms`
`ball_count_delay` `: 500 MS` `ball_count_delay` `: 500msec`
`ball_count_delay` `: 500` It makes no difference whether you enter
your time durations as seconds or milliseconds, as MPF will convert
everything to milliseconds when it reads in your configuration files.



Entering a time duration in minutes, hours, or days
---------------------------------------------------

You can also enter time strings in MPF for time periods longer than
seconds or milliseconds. While this isn't practical for things like
ball device delays, it's used in certain modules (like the credits
module) for some settings. Some examples: `credit_expiration_time: 2m`
(2 minutes) `credit_expiration_time: 2h` (2 hours)
`credit_expiration_time: 2d` (2 days)



