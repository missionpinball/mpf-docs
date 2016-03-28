
Starting with MPF 0.17, MPF expects that the first line of a YAML
configuration file specifies what version of the MPF config it uses.
For example:


::

    
    #config_version=3


This line needs to be the very first line in an MPF config file. This
section *must*be includedin your machine-wide config files. This
section *must*be includedin your mode-specificconfig files. This
section does not need to be included in "show" .yaml files. Each
version of MPF knows what version of the config files it will look
for. If it tries to load a config file with the wrong version, it will
post an error and exit. The important thing to know about this is that
not every new version of MPF will require a new version of the config
files.So that's why MPF 0.17 and 0.18 both use config file version 1,
MPF 0.19 uses version 2, etc. We did this so that game programmers
don't have to go through all their config files and update their
versions if MPF doesn't actually require any version changes.



Updating your config files to the latest version
------------------------------------------------

MPF includes a config file migration tool that can automatically
migrate your config files to the latest version. Details on the tool
and how to use it are `here`_.



Which versions of MPF require which config_versions?
----------------------------------------------------


+ MPF 0.30: `config_version=4`
+ MPF 0.20-0.21: `config_version=3`
+ MPF 0.19: `config_version=2`
+ MPF 0.17-0.18: `config_version=1`
+ MPF 0.1-0.16: config_version not used (a.k.a. config version 0)


.. _here: https://missionpinball.com/docs/tools/config-file-migrator/


