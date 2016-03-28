
An "asset" is an external file that's used in your MPF game. Examples
of assets include sound files, images, animations, etc. MPF includes a
generic asset manager which is responsible for finding, loading,
processing, and unloading assets. Multiple instances of this asset
manager are setup (automatically, in the background) depending on what
type of assets and modules you use in MPF. Currently MPF sets up asset
managers to manage the following types of assets:


+ Images
+ Animations
+ Movies
+ Sounds
+ Shows


Theasset managers are tightly integrated withthe game modes, meaning
you can specify assets on a per-mode basis. For each asset (or type of
assets), you can configure options that control when that asset is
loaded. For example, some assets that are used throughout the game
might be pre-loaded when MPF boots. Other mode-specific assets might
be loaded when a mode starts and then unloaded when a mode ends. You
can also configure assets so that they're loaded "on demand" (i.e.
they're only loaded when they're needed and then unloaded as soon as
they're done.) Each asset manager runs in a background thread, meaning
that your game still runs while the asset managers are loading assets
in the background. (For example, you might choose to pre-load a mode's
intro animations, sounds, and light shows so they're instantly
available when a mode starts, and then while the intro animation is
playing for that mode, the asset managers could load the remaining
assets that mode needs in the background while the intro animation is
playing.) MPF gives you complete control over how assets are loaded.
If your machine has plenty of memory and you don't want to monkey
around with all this dynamic loading and unloading of assets, that's
fine. You can configure your defaults so that every asset in the game
is pre-loaded as the machine boots. Or if you're on a memory-
constrained system (like a BeagleBone Black), you can get fancy with
dynamic loading and unloading.



Asset file locations
--------------------

Each type of asset is stored in a subfolder which matches the name of
the asset type. (The folder names can be overridden if you like.) For
example, sound files are stored in a "sounds" folder, animations are
in an "animations" folder, etc. These asset folders can exist in two
locations, either in a mode's specific subfolder (for mode-specific
assets), or in the root of your machine folder (for game-wide assets).
For example, if you're game is called "Demonstration Man," you
wouldstore machine-wide sounds in the `machine_files/demo_man/sounds/`
folder, and then you would store sounds for the multiball mode in the
`machine_files/demo_man/modes/multiball/sounds/`folder. Here's an
example from within a machine's folder: ` `_



Configuring default asset settings
----------------------------------

Each different type of asset in MPF has settings specific to that type
of assets. For example, animations have settings like how many frames
per second they play, whether they should loop, whether they should be
converted to 16-shade mono to show on a DMD, etc. Sound assets have
settings like what track they should play on (e.g. voice versus sfx
versus music). Othersettings, like whether an asset should be pre-
loaded when MPF boots, whether it should load when a mode starts, or
whether it should load on demand apply to all types of assets. You can
create an `AssetDefaults:` section in your config file to control
which default settings apply to specific types of assets. Further, you
can apply default settings on a per-folder basis within each asset
type's folder. For example, you could configure sound assets in a
"voice" folder so they play on the voice track, and sound files in an
"sfx" folder so they play on the sound effects track. This means you
can control the settings of assets simply by putting the assets in the
proper subfolder! You can also further customize the settings for a
specific asset by creating an entry for that asset in your config
file. This is completely optional, and in general you probably won't
have to do that for every single asset. But maybe you have a few
sounds here and there that are at a different volume than the rest, so
in that case you can create configuration entries in your config file
to set those specific sounds to play at a lower volume. The rest of
their settings will be controlled based on what folder they're in and
what `AssetDefaults:` settings you have applied to those folders. In
other words, *you do not have to create configuration entries for
every single asset file in your game*, because there will probably be
hundreds of them and that would suck. You can specify the settings for
your assets on a folder-by-folder basis, and then just override the
defaults here and there as you need.



Asset loading versus registration
---------------------------------

When MPF boots, it will scan through your asset folders (both in the
root of your game and in all your modes folders) to find and register
all the asset files so they're available for use. Then it will look at
the AssetDefaults: settings for that folder and any asset-specific
settings to figure out whether it should actually load the asset into
memory on boot, whether it should wait until a mode starts, or whether
it should just load the asset on demand as its needed. MPF
differentiates between the process of "registering" and asset versus
"loading" and asset. The registration process is how MPF knows that an
asset exists. It says "there is a file called 'slingshot.ogg' in the
/sounds folder, and it should be played on the track called "sfx."
Registration happens when MPF boots for every asset in your game. The
registration process doesn't take up much memory, so it's ok to have
hundreds or thousands of assets registered at all times. The actual
"loading" process is when MPF reads the asset file from disk into
memory. The exact way this works (and how much memory it consumes)
varies depending on the type of asset. For example, an audio file that
is 44.1KHz, 16-bit, stereo, will require 44100 x 16 x 2 = 1,411,200
bits = 176 kb of memory per second of audio. If you have an hour of
sound in your game, it could require over 600MB of memory to hold all
those sound files in a state where they're ready to play instantly. So
that's why MPF has the ability to dynamically load and unload assets,
and why the loading process is separate from the registration process.



Asset loading times versus asset availability
---------------------------------------------

Because all assets in MPF are registered when MPF boots, any asset is
available to be called at any time. However the registered asset must
have it's file loaded into memory before it can be used. As we
mentioned already, you can control when assets load their files into
memory. But what happens if an asset is called when it's related file
has not been loaded into memory? In that case the asset manager for
that type of asset will fetch the asset file from disk (via a
background thread) and load it into memory right away. (If there's a
queue of assets loading, it will jump to the front of the queue.) Then
once it's loaded, the asset manager will notify whatever called for
that asset to let it know the asset is ready to be used. So how long
does this loading process take? It depends on a several things,
including:


+ How big is the asset file?
+ How much processing has to happen to get the asset file ready to
  use? (Decompressing, decoding, etc.)
+ How fast is the disk? (Magnetic hard drive versus SSD, etc.)
+ How fast is the computer? (BeagleBone Black versus 2GHz x86, etc.)


You also have to take into consideration that most types of assets
aren't critical at the single-digit millisecond level. For example,
when a ball hits a pop bumper and you want to play a sound, you
probably want that sound asset preloaded so it can play instantly. But
if the player gets an extra ball and you need 100ms to load the extra
ball animation, voice callout, and light show, no one will ever
notice. You'll have to do some experimentationto figure out the right
balance of preloading, loading per mode, and on-demand loading of your
assets. You may find that you have plenty of memory to just preload
everything, or you may find that your assets load fast enough that you
can just set them to all be on-demand. It will really depend on your
exact situation.



