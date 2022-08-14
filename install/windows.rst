Installing MPF on Windows (Aug 12, 2022 update)
===============================================

This process is the new step-by-step process we are actively working out to get MPF 0.56 (current dev branch) installed on a Windows machine.

Current version these instructions are for: v0.56.0.dev30


Overview of MPF on Windows
--------------------------

We test MPF on Windows 10 and Windows 11. Older versions of Windows might (probably?) work too, we just don't test them. MPF requires 64-bit (x86) Windows running on Intel-compatible processors. It does not run on 32-bit systems and does not run on ARM processors on Windows.

MPF 0.56 requires Python 3.7, 3.8, or 3.9.

Here are the steps:

Install Python from python.org. Pick the latest version of Python 3.9 (which is 3.9.13 at the time of this writing).

Then open a command prompt (you can just run "cmd"), and type each of these commands one at a time (and hit enter after each one):

.. code-block:: doscon

  pip install --user pipx
  python -m pipx ensurepath

After this, restart the cmd window. (Just close it and then open a new one.) Then type this commands and push enter:

.. code-block:: doscon

    pipx install mpf-mc --pip-args '\--pre' --verbose --include-deps
