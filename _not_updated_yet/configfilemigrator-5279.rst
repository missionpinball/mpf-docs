
MPF includes a config file migration tool that can help you migrate
your MPFconfiguration files to the latest config version. (Read
`here`_ for details on what the config file version is.) To use the
tool, switch to the `tools` folder in your MPF package and run it from
the command line, specifying the location of your machine folder as a
command line argument, like this:


::

    
    >python config_migrator.py c:\brian\machine_files\sttng


You should see results that look something like this:


::

    
    Migrating MPF config files from v1 to v2
    
    Migration Results
    =================
    Backup location for existing files: c:\brian\machine_files\sttng\previous_config_files\2015-07-27-16-45-40
    Files migrated successfully: 9
    Files skipped: 20
    Files that require manual intervention: 2
    
    Open up each of these files to see the details of the sections you 
    need to manually update:
    c:\brian\machine_files\sttng\config\game_logic.yaml
    c:\brian\machine_files\sttng\config\hardware.yaml


The config migrator will automatically scan through the folder
(including subfolders) looking for `.yaml`files. If it finds them, it
will open them up and make sure that they are the previous version,
and, if so, it will make changes to them. In other words, if the
current MPF config file version is 2, then the migrator tool will only
attempt to migrate files that have `#config_version=1` as their first
line. The tool will not touchlight or display show files, and it will
not touchconfig files whose version already matches the latest version
of MPF. The migrationtool automatically creates a backup of each file
it makes changes to in a folder called `previous_config_files` in the
root of the path you specified. In there it creates another folder
based on the date and time the tool was run, and that folder contains
the original versions of the `.yaml` files the migrator tool made
changes to.



Command line options
--------------------

`-f` force the re-migration of already migrated files. (This option
means that the migration tool will also target files that have the
latest config_version, rather than the default of only targeting files
that are the previous version.)



What does the config migrator actually do?
------------------------------------------

The config migrator tool can do three things. First, it does simple
"find and replace" changes to section names that have changed. For
example,many section names changes between config version 1 and
version 2— `Autofire Coils:` was renamed to `autofire_coils:`,
`BallDevices` was renamed to `ball_devices:`, etc. These changes are
pretty easy and safe for the tool to do automatically. (Note that even
though section names in the MPF config files are not case sensitive,
any renamed sections will be changed to lowercase.) Next, the migrator
tool can identify any sections of the config file that have been
deprecated (removed). For example, early versions of MPF included a
section called `plugins:`, but in current versions, plugins are loaded
automatically and do not need to be included in the config file. So if
the migrator tool finds a `plugins:` section in a config file, it adds
a comment into the file letting you know that you can safely remove
that section. Finally, the config migrator searches for sections that
have major changes that will require manual intervention. In these
cases since the changes are major, the tool cannot automatically make
the changes for you. When files containing these sections are found,
the toolwill add some text to the top of the `.yaml` file explaining
what section has changed, and it gives you a URL where you can get
more information about the new way that section works. In these
cases,the warning text that the migration tool adds to the `.yaml`
file will essentially "break" that file (since adding that text means
the first line in the file is no longer `#config_version=x`. This was
done on purpose to ensure that you can't accidentally run MPFwith
outdated sections. As you can see in the example output from running
the migration tool above, it printsa summary of the results on the
screen.Files migrated successfully: 9 means that 9 files are
completely migrated and ready to go. They have the latest
#config_version entry and all the find-and-replace for renamed
sections is done. Files skipped: 20 means that the migration tool
found 20 files that were either light show or display show files, or
they were files that were either too old or too new to migrate
automatically. (In the future we'll add a support to migrate through
multiple versions at a time.) Finally, the Files that require manual
intervention: 2 result means that there were 2 files with sections
that need manual changes. Then you'll see the list of those files. In
this case, they're game_logic.yaml and hardware.yaml. Let's take a
look at hardware.yaml and see what the migration tool did:


::

    
    # ---------------------------------------------------
    # MIGRATION WARNING:
    # This file contains a "targets" section which underwent major changes in config_version=2.
    # You will have to read the docs and re-do this section.
    # New documentation for this section is here:
    # https://missionpinball.com/docs/configuration-file-reference/targets/
    
    # When you're done, delete this message so #config_version=2 is the first line in this file.
    # ---------------------------------------------------
    
    #config_version=2
    
    machine:
      hz: 60
    ...


Notice that the text at the top of the file explains that it's the
"targets" section of this file which needs to be manually updated, and
it also provides a link to the new targets documentation. Next we can
use CTRL+F to search the file for "targets" which will reveal this
section:


::

    
    ...
    Targets:
        t_topLaneLeft:
            switch: s_topLaneLeft
            light: l_topLaneLeft
        t_topLaneCenter:
            switch: s_topLaneCenter
            light: l_topLaneCenter
        t_topLaneRight:
            switch: s_topLaneRight
            light: l_topLaneRight
        t_leftBankTop:
            switch: s_leftBankTop
            light: l_leftBankTop
        t_leftBankMiddle:
            switch: s_leftBankMiddle
            light: l_leftBankMiddle
        t_leftBankBottom:
            switch: s_leftBankBottom
            light: l_leftBankBottom
        t_rightBankTop:
            switch: s_rightBankTop
            light: l_rightBankTop
        t_rightBankMiddle:
            switch: s_rightBankMiddle
            light: l_rightBankMiddle
        t_rightBankBottom:
            switch: s_rightBankBottom
            light: l_rightBankBottom
    ...


From there you can check the link and update that section as needed.
When you're done, be sure to delete the block of warning text at the
top of the config file so that the `#config_version=x` is the top
line.

.. _here: https://missionpinball.com/docs/configuration-file-reference/config_version/


