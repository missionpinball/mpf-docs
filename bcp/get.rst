get (BCP command)
=================

**Parameters:** names=variable1,variable2,…,variableN **Origin:** Pin
controller or media controller **Response:** set Asks the other side
to send the value of one or more variables. Variable names are to be
stripped of leading and trailing spaces and lower-cased. The other
side responds with a “set” command. If an unknown variable is
requested, its value is returned as an empty string. For sanity
reasons, all variable are to be lower case, must start with a letter,
and may contain only lowercase letters, numbers, and underscores.
Variable names should be lowercased on arrival. Variable names can be
no more than 32 characters. See “set” for a list of common variables.