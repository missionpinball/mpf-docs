
MPF includes a *file manager* that provides a common interface for
various configuration and data files that MPF uses. The file manager
is in the *mpf/system/file_manager.py* module. Examples of the types
of files and MPF reads from and writes to include config files (MPF
config, your machine-wide configs, and your mode configs) as well as
data files like audits, operator settings, high scores, etc. The file
manager uses file interface plugins to read and write different
formats of files. By default, everything MPF does with files is in a
YAML format, though it's possible to use other formats if you prefer
(XML, JSON, etc.)



