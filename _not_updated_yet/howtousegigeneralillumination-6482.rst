
(A) Understand GI (B) Add gis: entry to your machine config asdf


::

    
    gis:
        gi_back_panel:
            number: g01
            label:
            tags:
        gi_upper_right:
            number: g02
            label:
            tags:
        gi_upper_left:
            number: g03
            label:
            tags:
        gi_lower_right:
            number: g04
            label:
            tags:
        gi_lower_left:
            number: g05
            label:
            tags:


asdf (C) Turn them on By default, they turn on in
machine_reset_phase_3. You can override this or add to it. You can
also add disable_events.



