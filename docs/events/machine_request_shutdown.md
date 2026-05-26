---
title: machine_request_shutdown
---

# machine_request_shutdown


--8<-- "event.md"

!!! info ""

    Event available in MPF 0.81

This is a *Boolean Event* posted by the machine when
a soft shutdown request has been made. Components may
register handlers for this event and return True or False,
where False will cause the soft shutdown request to abort.

--8<-- "event_no_keywords_notice.md"
