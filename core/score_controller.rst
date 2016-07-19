Score Controller
================

MPF's score controller is used to add or subtract value to or from player variables based on MPF events. (Even though
it's called the "score" controller, it can be used to change the value of any player variable--score, aliens zapped,
extra balls, modes completed, etc.).

The score controller also has intelligence to know which modes various configurations were in, and it ties into the
mode controller and mode priority to allow cascading scores, blocking, etc.