Sequence Shots
==============

+------------------------------------------------------------------------------+
| Related Config File Sections                                                 |
+==============================================================================+
| :doc:`/config/sequence_shots`                                                |
+------------------------------------------------------------------------------+

A sequence of switches which need to be hit in order with a timeout.

This is an example:

.. code-block:: mpf-config

   switches:
     s_ramp_entry:
       number: 1
     s_ramp_success:
       number: 2

   sequence_shots:
        ramp:
            switch_sequence: s_ramp_entry, s_ramp_success
            sequence_timeout: 3s


Related How To guides
---------------------

* :doc:`/mechs/loops/index`

Related Events
--------------

.. include:: /events/include_sequence_shots.rst
