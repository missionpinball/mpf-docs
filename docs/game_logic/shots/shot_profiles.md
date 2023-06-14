---
title: Shot Profiles
---

# Shot Profiles


Related Config File Sections:

* [shots:](../../config/shots.md)
* [shot_profiles:](../../config/shot_profiles.md)
* [shot_groups:](../../config/shot_groups.md)

Shot profiles define how shots will behave when hit. This is an example:

``` mpf-config
##! mode: mode1
shot_profiles:
  my_default_profile:
    states:
      - name: unlit
        show: "off"
      - name: lit
        show: "on"
```

Normally, a shot will advance its profile (unless `advance_on_hit` is
set to `False`) and will stay at its last step (unless `loop` is set to
`True`). There can be a show with option for every state.
