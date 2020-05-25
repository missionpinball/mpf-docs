Your hardware is not working at all
-----------------------------------

If your hardware is not working at all make sure that you removed the
options ``-X``, ``-x`` and ``--vpx`` from your ``mpf both`` or
``mpf game`` command line.
Those options will overwrite the settings in your ``hardware`` section and
MPF will not even try to connect to your hardware.
If you got config errors we suggest you add ``-X`` to figure things out without
interfacing real hardware all the time.
Just keep that option in mind.

Another stupid thing to check:
Is your hardware connected to your PC?
We know it is stupid but a loose USB connector has happened to most of us.

Add debugging to related devices
--------------------------------

If you got problems with some switches also add ``debug: true`` to those as
it will give to more insights into the intentions of those devices.
Same will work for flippers, coils, lights, servos, steppers and more.
See :doc:`general debugging section </troubleshooting/general_debugging>`
for details.

Run MPF with verbose flag
-------------------------

See :doc:`general debugging section </troubleshooting/general_debugging>` for
details.
TLDR: run ``mpf both -t -v -V``.


Report Your Issue and Ask For Help
----------------------------------

If you cannot find the issue yourself please prepare some information about
your issue according to our
:doc:`troubleshooting guide </troubleshooting/index>` and ask in our forum.

Consider Improving the Documentation
------------------------------------

Did you solve your issue but found that some relevant information in the
documentation is missing or should be linked/located elsewhere?
Either tell us in the forum or consider
:doc:`improving the documentation </about/contributing_to_mpf_docs>`
yourself to save future users some troubles the same way others saved you
some troubles by writing this documentation.
