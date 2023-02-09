Installing MPF Monitor
======================

The MPF installer was rewritten for this current release (0.56).

Note that MPF Monitor 0.56 now requires PyQt6. (Prior versions of MPF Monitor required PyQt5.)

If you installed MPF 0.56 via ``pipx``, you also need to inject it into the ``mpf`` environment via pipx. You can do that with the following two commands:

.. code-block:: doscon

    pipx inject mpf mpf-monitor --pip-args="--pre" --verbose --include-deps --include-apps

If you installed MPF 0.56 via ``pip``, you can install MPF Monitor 0.56 via ``pip`` as well:

.. code-block:: doscon

    pip install mpf-monitor
