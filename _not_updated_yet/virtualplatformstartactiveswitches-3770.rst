
The `virtual_platform_start_active_switches:` section lets you
configure of switches that will automatically start as "active" when
you launch MPF using the virtual hardware platform. (i.e. when you use
the `-x` command line option). This is used to make testing your
machine easier since you can configure the trough to be "full" without
having to manually hit the keyboard keys to activate each trough
switch before you can start a game. This sectioncan be used in your
machine-wide config files. This section *cannot* be used in mode-
specific config files. The settings are pretty simple—just a list of
switch names. For example:


::

    
    virtual_platform_start_active_switches:
        s_trough1
        s_trough2
        s_trough3
        s_trough4
        s_trough5


This section is ignored when you run MPF while connected to a physical
pinball machine.



