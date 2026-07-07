---
title: machine_abort_shutdown
---

# machine_abort_shutdown


--8<-- "event.md"

!!! info ""

    Event available in MPF 0.81

Posted when soft shutdown request has been made and
was blocked by a handler. This means the machine
will NOT proceed with shutdown. Further requests may be made,
in case the blockage is temporary and shutdown should be reattempted.

--8<-- "event_no_keywords_notice.md"
