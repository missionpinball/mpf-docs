Installing the MPF Monitor (Aug 29, 2022 update)
==========================

The MPF installers have been rewritten and updated in August 2022. See the new instructions :doc:`here <install>`.

The instructions for installing MPF Monitor have been updated too. If you installed MPF 0.56 (the current dev version) via the new instructions
from August 2022, then you can use the following process to install MPF Monitor.

To install MPF Monitor, you also need to inject it into the mpf environment via pipx. You can do that with the following two commands:

.. code-block:: doscon

    pipx inject mpf PyQt5 --verbose --include-deps --include-apps
    pipx inject mpf mpf-monitor --pip-args="--pre" --verbose --include-deps --include-apps
