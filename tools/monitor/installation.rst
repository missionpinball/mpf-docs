Installing the MPF Monitor (Aug 29, 2022 update)
==========================

The MPF installers have been rewritten and updated in August 2022. See the new instructions :doc:`here </install/index>`.

The instructions for installing MPF Monitor have been updated too. If you installed MPF 0.56 (the current dev version) via the new instructions
using ``pipx`` from August 2022, then you can use the following process to install MPF Monitor.

Note that MPF Monitor ``0.56.0.dev4``, released on September 5, 2022, is the first version to change from PyQt5 to PyQt6.

To install MPF Monitor, you also need to inject it into the ``mpf`` environment via pipx. You can do that with the following two commands:

.. code-block:: doscon

    pipx inject mpf PyQt6 --verbose --include-deps --include-apps
    pipx inject mpf mpf-monitor --pip-args="--pre" --verbose --include-deps --include-apps
