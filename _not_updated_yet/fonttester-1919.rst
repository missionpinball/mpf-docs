
The MPF Font Tester (`/tools/font_tester.py`) is a graphical tool that
lets you view how TrueType fonts will be rendered on your DMD. You run
the tool by specifying the path to a folder which contains TrueType
fonts. Anything you type shows up in the on screen DMD preview box.
You can use the left and right arrow keys to flip between fonts, and
you can use the up and down arrow keys to increase or decrease the
font size. There are also shortcuts to enable and disable
antialiasing, to vertically shift the font, to highlight the font's
bounding box, and to save snapshots of the screen for later use.
There's a `how to guide covering adding TrueType fonts to your game`_
which makes extensive use of this Font Tester tool. Here's what the
Font Tester looks like in action: ` `_ We also recorded a ten-minute
YouTube video which demonstrates how the font tester is used:
https://www.youtube.com/watch?v=xKuR80tUJhA



Running the Font Tester
-----------------------

Run the font testertool from the command line by specifying the path
to a folder which has TrueType font files(.ttf) you want to test. You
can optionally specify a file name too which is thefirst font it will
load. Otherwise it just starts at the beginning of thealphabet. For
example:


::

    
    python font_tester.py c:\Windows\Fonts


or


::

    
    python font_tester.py ../mpf.fonts/pixelmix.ttf




Instructions
------------

Once the window pops up, it will show a virtual DMD in the center with
your initial text and the initial font.


+ To change the text that's rendered, just start typing. You can do
  uppercase and lowercase letters, and numbers.
+ Use the `Left` & `Right` arrow keys to cycle through the different
  fonts in the folder.
+ Use the `Up` & `Down` arrow keys to increase & decrease the size of
  the font.
+ Use `SHIFT + Up` and `SHIFT + Down` to vertically adjust the text
  placement in the DMD window.
+ `CTRL+A` (or `CMD+A` on a Mac) toggles Antialias mode
+ `CTRL+B` (or` CMD+B`) toggles showing the green Bounding Box.
+ `CTRL+S` (or `CMD+S`) takes a snapshot of the screen and saves it to
  the'font_snapshots' folder.




Limitations
-----------


+ Only works with TrueType fonts with .ttf extensions.
+ Doesn't work with shift symbols. (i.e. SHIFT+1 shows "1" and not
  "!")




Configuration Options
---------------------

There are lots of configuration options available for the Font Tester
which you can easily access by editing `font_tester.py`. All these
settings entries are in the beginning of the file and easy to find.


+ window_size = (800, 600) -The size (inpixels) of the main window.
+ dmd_size = (128, 32) - Thepixel size of the native DMD.
+ dmd_screen_size = (640, 160) -The pixel size of the on screen DMD.
+ pixel_color = (255, 85, 0) -R, G, B colors of the font pixels.
+ dark_color = (34, 17, 0) -R, G, B colors of the 'off' pixels.
+ pixel_spacing = 2 - Pixel spacing between dots.
+ loop_ms = 100 - How many ms it waits per cycle.
+ font_bg_color = (0, 200, 0) -R, G, B color of the CTRL+B box.
+ max_chars = 10 -How many characters are displayed.
+ snapshot_folder = "font_snapshots" -Path of the CTRL+S screenshots.
+ prefer_uncompressed_snapshots = False -Do you want uncompressed
  BMPs?.
+ snapshot_flash_brightness = 255 -Color of the snapshot flash.
+ snapshot_flash_steps = 5 -Steps for the flash to be done.
+ text_string = "HELLO" -Initial text.
+ font_size = 10 -Initial font size.
+ antialias = False -Initial antialias setting.
+ bounding_box = False -Initial bounding box settings.


.. _how to guide covering adding TrueType fonts to your game: https://missionpinball.com/docs/tutorial/how-to-adding-truetype-fonts/


