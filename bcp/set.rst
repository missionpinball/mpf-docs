set (BCP command)
=================

**Parameters:** variable1=value1&variable2=value2&etc=etc **Origin:**
Pin controller or media controller **Response:** None Tells the other
side to set the value of one or more variables. For sanity reasons,
all variable are to be lower case, must start with a letter, and may
contain only lower case letters, numbers, and underscores. Variable
names should be lowercased on arrival. Variable names can be no more
than 32 characters. Variable values are of unbounded length. A value
can be blank. Setting a variable should have an immediate effect. For
example if the system audio volume is set, it is expected that audio
will immediate take on that volume value. Or if the high score is
currently being displayed and its variable it set, it should
immediately update the display.