Build Command Line
==================

The build command line ``mpf build`` can compile configs for production.

Commands
--------

production_bundle
~~~~~~~~~~~~~~~~~

Call this inside your machine folder.
It will create ``mpf_config.bundle`` and ``mpf_mc_config.bundle`` inside your
machine folder.
Those two files contain the complete configuration including all shows for your
machine.
If you change any configs, modes or shows rerun this command.
Make sure that your final machine runs exactly the same version of MPF or bad
things will happen.
Regenerate those files when upgrading MPF (even when not changing configs).

See :doc:`/finalization/software` for details about production machines.
