Creating standalone show files
==============================

You can create a subfolder called *shows* in your machinew config folder or
within a  mode config folder. Then inside that folder, you can create separate
files, where each file is its own show. The files need to have a ``.yaml``
extension, and the name of the file before the extension is the name of the show
as you'd refer to it in your MPF configs.

A few notes for creating show files:

* MPF config files are not case sensitive. You can mix-and-match
  uppercase and lowercase letters in the files, but internally MPF will not
  be able to differentiate between ``YouShow.yaml`` and ``yourshow.yaml``.
* Show names are "machine-wide" within MPF. This means that if you have two
  different shows with the same name in different locations, MPF will get
  confused.
* Valid characters for show names are z-x, 0-9, and the underscore. Python
  objects cannot contain dashes in their names, meaning your show file names
  cannot include dashes.

Here is a sample show file. This file might be called something like
``flash_red.yaml`` and would be located in your machine's ``/shows`` folder:

::

   #show_version=4
   - time: 0
     leds:
       led1: red
   - time: +1
     leds:
       led1: off
   - time: + 1

Notice it's essentially the same show we used as an example in the section on
show config formats. However there's one important change.

Since this is a standalone show file, we need to tell MPF what "version" of the
show format this file is. MPF |version| uses ``show_version=4``. If we ever
change something in the show format, then we'll increment the version. (Don't
worry though, we have and automated migration tool that converts shows to the
new formats. That's actually part of the reason we include the show_version in
the show files)

The bottom line is that when you create a .yaml show file, the first line of
the file must be ``#show_version=4`` so MPF knows it's working with the proper
type of file.

Beyond that, the show file follows the show format covered elsewhere in this
documentation. You can nest show files into subfolders under the ``/shows``
folder if you want to, and in can put ``/shows`` folders in both your machine-wide
and mode-specific folders. (The ``/shows`` folder should be in the root of your
machine config or the root of a mode folder. It does *not* go inside the
``/config`` folder.)
