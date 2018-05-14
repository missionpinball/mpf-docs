RGB.DMD Controller
==================

It's likely that no one would be using :doc:`RGB LED DMDs </hardware/eli_dmd/index>`
if it wasn't for the efforts of Eli Curtz.

Eli first posted about these types of panels in the P-ROC forum (now defunc) in 2014.
At that time we could only find panels with 3mm spacing between pixels which
was a bit larger than traditional pinball DMDs, but that's what kicked
off the conversation about, "Whoa, maybe we could use these for 'real'
color DMDs some day." Then in September 2015, Eli posted again telling
us that we could now get panels with 2.5mm spacing which is the
perfect size we need. Eli also showed us how to connect them and what
software we needed to make everything work. So really everything here
is because of Eli. All we did is take everything he showed us and
write it down. (Well, that and we also created the interface for MPF,
but that was the easy part.) So thanks Eli!

You can grab the `RGB.DMD source code <https://github.com/ecurtz/RGB_DMD>`_ and
flash it to a Teensy 3.2. Connect your panels and you are good to go.

In MPF, RGB.DMD works just like :doc:`/hardware/smartmatrix/index` (go there for details).
Can copy the following example (and replace ``com12`` with your com port):

.. code-block:: mpf-config

    hardware:
        rgb_dmd: smartmatrix

    smartmatrix:
        smartmatrix_1:
           port: com12
           baud: 3000000
           old_cookie: false
