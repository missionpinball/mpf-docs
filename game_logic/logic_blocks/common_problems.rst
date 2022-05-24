Common Issues
-------------

We try to answer some common questions regarding logic blocks here.
If you question is not answered please ask in the forum.

My block only works once. Why?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the default configuration of all logic blocks.
To change it you first need to set ``reset_on_complete`` to ``True``.
As a result you blocks will reset when they reach the final step.
However, that will not be enough in most cases because ``disable_on_complete``
is ``True`` by default.
Unless you have some enable logic to re-enable the block later,
you probably want to set ``disable_on_complete`` to ``False``.

When should I used logic blocks and when should I use shots/show_groups?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is no definitive answer to this question.
Generally, it depends on your usecase.
Shots and shot_groups serve a very specific usecase.
Basically, they implement a sequences of switch hits which trigger lights along
the way.
If you want to stay within that specific usecase then go with shots because it
will be more convenient.
If you plan to extend your mode to use more advanced features then go with
logic blocks.
For instance if you got conditions in your logic (i.e. on how many balls are
locked).
Another clear indicator for logic blocks would be if your logic is triggered
by other elements such as locks (and not just switches).
