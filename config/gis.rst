gis:
====

.. warning::
   As of MPF 0.50, ``matrix_lights``, ``flashers`` and ``leds`` have been combined into a single
   ``lights`` configuration. See :doc:`/config/lights` for details.

.. overview

You would configure GIs as normal lights with ``subtype: gi`` (see your platform documentation for details about
``subtype``).

Here's an example from *Judge Dredd*:

.. code-block:: mpf-config

    lights:
      gi01:    # lower backglass
        number: G01
        subtype: gi
      gi02:    # mid backglass and rear playfield
        number: G02
        subtype: gi
      gi03:    # upper left backglass and slings, variable
        number: G03
        subtype: gi
      gi04:    # upper right backglass and Deadworld globe, variable
        number: G04
        subtype: gi
      gi05:    # coin slot lights & side cabinet fire buttons
        number: G05
        subtype: gi

See :doc:`/config/lights` for details about the ``lights`` section.
