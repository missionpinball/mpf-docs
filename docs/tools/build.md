---
title: Build Command Line
---

# Build Command Line


The build command line `mpf build` can compile configs for production.

## Commands

### production_bundle

Call this inside your machine folder. It will create `mpf_config.bundle`
and `mpf_mc_config.bundle` inside your machine folder. Those two files
contain the complete configuration including all shows for your machine.
If you change any configs, modes or shows rerun this command. Make sure
that your final machine runs exactly the same version of MPF or bad
things will happen. Regenerate those files when upgrading MPF (even when
not changing configs).

See [Tuning Software for Production](../finalization/software.md) for details
about production machines.

## Command line options

There are several command-line options you can use when running build.

### -b (lowercase)

Builds a production config for MPF only, without MC. For builds on MPF `0.80` and later,
you should not be using mpf-mc at all, and should thus include the `-b` option.

### -c (lowercase)

Specifies the name of the config file (or files) to load. Default
`config.yaml` is used if this option is omitted. You do not have to
specify the .yaml extension.

### --dest-path

The path to set as machine_path on the production bundle.
This may be different than the machine_path on the current machine.
