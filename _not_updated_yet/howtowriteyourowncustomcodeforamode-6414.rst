
It's possible to write your own custom code for a mode. (A) Create the
file to hold your code
<your_machine_folder>/modes/<your_mode>/code/<your_mode>.py. For
example, if you have a mode called "mania", you'd add it like this:
<your_machine_folder>/modes/mania/code/mania.py (B) Create the
"skeleton" file (C) Options for things you can do.
self.machine.events.post('some_event')



