
The show controllerhas a Playlist class you can use to create
playlists of shows that will play in order. Each step of the playlist
can have one or more shows (that play at the same time), and you can
specify how the playlist will move from one step to the next. To
create a playlist, create an instance of the Playlist class, add shows
to it, and configure the settings for each step. Here's an example:
First, make sure you've imported the Playlist class, like this: `from
mpf.system.show_controller import Playlist` Then write some code like
this:


::

    
    self.my_playlist = Playlist(self.machine)
    self.my_playlist.add_show(step_num=1, show=self.machine.shows['show1'], tocks_per_sec=10)
    self.my_playlist.add_show(step_num=2, show=self.machine.shows['show2'], tocks_per_sec=5)
    self.my_playlist.add_show(step_num=2, show=self.machine.shows['show1'], tocks_per_sec=10)
    self.my_playlist.add_show(step_num=3, show=self.machine.shows['show3'], tocks_per_sec=32, blend=False)
    self.my_playlist.step_settings(step=1, time=5)
    self.my_playlist.step_settings(step=2, time=5)
    self.my_playlist.step_settings(step=3, time=5)


The first line creates an instance of the Playlist class named
"self.my_playlist". The next 4 lines use the playlist's "add_show()"
method to add shows to each step. Note that the show called
"self.show1" has been added to both Step 1 and Step 2, meaning it will
play for both steps. The final three lines configure the settings for
each step. In this case it's just that each step will play for 5
seconds before moving on. This is also where you could specify that
you'd like to move on based on a "trigger show" which has played a
certain number of times before moving on. See the documentation in
show_controller.py for details. Once your playlist is all setup, you
can start via: `self.my_playlist.start(priority=100, repeat=True)` The
priority specified what priority all the shows in that playlist will
play at, and `repeat=True` means that this playlist will loop.
(Forever in this case. You can also specify a number of times to
repeat before exiting.) Stopping the playlist is easy too:
`self.my_playlist.stop()`



