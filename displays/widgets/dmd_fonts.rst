How to use DMD fonts
====================

MPF includes three built-in fonts which are pre-configured as widget styles
which look good on DMDs. These fonts are included in the MPF-MC package. They
can be used with any widget that uses fonts, including the Text and Text Input
widgets.

If you don't use one of these fonts on your DMD and just show some text, here's
what the results look like:

.. code-block:: mpf-config

   slides:
       my_slide:
       - type: text
         text: MISSION

.. image:: /displays/images/dmd_default.png

Sure, it works, but it doesn't look good because the default font is a
regular font that's made for a high-res display.

Instead you can use these three styles. (Of course you can use your own fonts
too, but sometimes it's hard to find ones that look good on a low-res DMD.)

style: dmd_big
--------------

dmd_big is 10 pixels tall.

.. code-block:: mpf-config

   slides:
       my_slide:
       - type: text
         style: dmd_big
         text: MISSION

.. image:: /displays/images/dmd_big.png

style: dmd_med
--------------

dmd_med is 7 pixels tall.

.. code-block:: mpf-config

   slides:
       my_slide:
       - type: text
         style: dmd_med
         text: MISSION

.. image:: /displays/images/dmd_med.png

style: dmd_small
----------------

dmd_small is 5 pixels tall.

Notice that this font has a color set and we're using it with a Color DMD. All
three of these fonts (like any font) can be used on a mono or color DMD.

.. code-block:: mpf-config

   slides:
       my_slide:
       - type: text
         style: dmd_small
         text: MISSION
         color: 00ffcc

.. image:: /displays/images/dmd_small.png
