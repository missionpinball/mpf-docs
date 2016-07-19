Shot Profile Manager
====================

The shot profile manager is responsible for loading, parsing, and
registering shot profiles. It also figures out which profiles should
be applied to which shots. The shot profile manager lives in the
``mpf/core/shot_profile_manager.py`` module. The actual shots (and
shot groups) that the shot profile manager applies profiles to are
implemented as devices and are covered in the devices section of the
documentation.
