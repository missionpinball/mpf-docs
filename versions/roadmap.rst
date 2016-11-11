MPF Road Map, Vision & Future
=============================

If you sum up our vision, we’d say that we like “traditional” pinball. We love mid-90s
Williams games and the new Stern stuff, and we’re excited about new games which have a
traditional format (like Predator, The Big Lebowski, Wrath of Olympus, etc.). A lot of
people have been talking about all these cool things like Pinball 2000, LCD screens for
backglasses, and even the `entire playfield being replaced by an LCD <http://www.multimorphic.com/index.php/p3-pinball-platform>`_!
We think these are really, really awesome, but quite honestly we’re most excited about
playing traditional pinball machines.

That said, we believe there is quite a bit of room for innovation even within the boundaries
of classic pinball. For example:

Internet-connected pinball machines that report their own outages & problems
----------------------------------------------------------------------------

One of the problems with pinball on location today is that the machines often break.
Unfortunately since most of these machines are owned by route operators, if a pinball
machine in a bar breaks then the bartender just turns it off and the route operator has
no idea that it’s not earning. So if the operator is stopping by once a week to check on a
machine, it might break an hour after he leaves and then be dark (and not earning) for the
next 6 1/2 days until he comes back again.

We believe that pinball machines should be able to use the internet to report their current
status. The operator should be able to log into a web portal to see all his machines and
to view the current status. He should get text messages or iOS alerts with details of the
“credit dot.”

Furthermore, the ultimate indicator of whether a machine is working or not is whether it’s
earning. If a pinball machine only earns $20 a week, it’s literally not worth an operator’s
time to drive to the location to check on it. So if he can see a report that the machine is
earning as expected, he wouldn't have to waste his time and gas driving around to all his
locations to check on his machines.

We can also be proactive when machines are turned off. The operator ought to be able to
configure a schedule which basically says, “This machine should be powered on from noon
until 2am every day,” so if the cloud service ever loses connectivity with a machine
during those hours, it can notify the operator (and maybe the location owner) that the
machine is offline when it should be on, and the operator can make a phone call to see
if the machine is ok before heading out. (And, if the machine is not ok, the operator
can know that he’s going out to the location for a reason.)

Of course their are plenty of times when a machine is powered on with no credit dot, but
where the machine might still not be playable. (Maybe there’s a stuck ball or a broken
rubber.) In those cases we can go back to the earnings reports. If a machine is typically
earning 5 dollars per day but half a day goes by without any money inserted, the machine
can alert the operator that there’s a problem.

Dynamic Pricing
---------------

Another cool thing about an internet-connected pinball machine is that operator settings
can be centrally “pushed” to the machine. If a bar is rented out for a private party, the
bar tender ought to be able to fire up an app on his or her smart phone to instantly set
all the machines to free play. Or maybe there’s an automatic schedule. “Wednesday night
is free pinball,” or “All pinball is free from 4-7pm.” The operator ought to be able to
set up a schedule and the machines should be able to change their pricing automatically
based on the time of day.

We could even imagine “demand pricing,” where the price is automatically adjusted up or
down based on demand for a particular machine.

Player “Log in” for notification of high scores being beat
----------------------------------------------------------

We love the idea of players being able to “log in” to a machine, most likely by “tapping
in” to the machine with their Bluetooth or NFC-enabled smart phone. (This idea is not new
of course. Pyprocgame creator Adam Preble `blogged about this in 2014 <http://adampreble.net/blog/2014/02/ibeacon-at-the-arcade/>`_,
and Dutch Pinball's Bride of Pin*Bot 2.0 and Big Lebowski have "Player Profiles" features.)

Regardless of how it’s implemented, we love the idea of a particular player being able to
login to a machine, since there are several cool things this could enable, including:

* Notification of high scores being beat. How cool would it be if you could get a text
  message or iOS notification when you lost your high score spot on your favorite machine?
* Accomplishments tracking. I would love to know what my high score was on different
  machines, or for a mobile app to tell me, “That’s the most combos you’ve ever completed
  in Attack from Mars.”
* Player preference settings. Most pinball machine settings are geared towards operators
  (number of balls per game, difficulty, etc.), but modern machines have plenty of options
  that don’t matter to operators that hard core players are very passionate about. A
  pinball machine’s app should allow players to set their own white balance for RGB
  LEDs (cool versus warm white), or the overall brightness of the LEDs, or even whether
  the LEDs “pop” on-and-off instantly or gently fade up and down like traditional
  incandescent bulbs. Players should be able set these preferences on their own or
  save their to their profile which they can have applied to whatever machine they walk
  up to.

All of this could be done on a per-player basis, with the machine taking on a different
look and feel as each player steps up. Players could even set their color preferences with
RGB LEDs in the apron lighting to indicate which player is up.

Mobile phone companion apps
---------------------------

We’ve already `demonstrated a feature <https://www.youtube.com/watch?v=0HouBZHx2uQ>`_ of
the Mission Pinball Framework where we use an iPhone app as a “second screen” for a pinball
machine. We can imagine players being able to customize their iOS app to show whatever
data they want—score, ball, shots lit, etc.—which they can then set on the
glass near the flippers. The machine could also send all DMD information and animations
to that device and the player wouldn't have to take their eyes off the flipper area.

The mobile app could have a "helper" mode where it knows exactly what's going on in the game
and can tell you want to shoot for—kind of like if you had a world-class player
standing over your shoulder and telling you want to do.

The mobile app could also let you know when it's your turn (in case you walked away from
the machine), or when a certain machine you're waiting in line for is free. (Maybe you
even pay for and "reserve" your place in line from your phone?)

It could also let you see all sorts of statistics for your game when while another
player is playing (balls locks, goals remaining, etc.).

You'd also be able to collect very detailed metrics and analytics about your games. (Average
time to hit a hurry-up, average ball time, number of shots, etc.) That could also be
shared in a web-based dashboard and player ranking system.

Mobile phone audio integration
------------------------------

One of the things that stinks about playing pinball in a loud bar is that you can't hear
the machines. Some machines have headphone jacks, but that's a separate piece of hardware.

What if you could pair your phone to the machine, and then the machine could stream its
audio to your phone which you could listen to via headphones? You could even allow
multiple people standing around to connect their audio to the same machine?

Another option is if you pair your phone with a machine, you could play a playlist from
your phone instead of the machine's music. The pinball machine could still add the
voice call outs and sound effects, but just with your music. (This could be done via
headphones or even through the pinball machine's speakers.)

The machine could even have a mobile app which lists all the various music cues
(waiting to plunge, base mode background, wizard mode background, etc.) and you could
map those to individual tracks from your phone. Then whenever you walk up to a machine,
you get your own custom music! (This could integrate with a cloud-based music service
like Spotify or Apple Music and be configurable via the web so you get your own music
any time you play that machine.)

Mobile phone "waiting player" actions
-------------------------------------

Traditional multi-player pinball machines alternate between players, with the non-playing
players just watching the current player that's up. The games themselves are very much
about the "player versus the machine" more so than the "player versus player."

But what if the waiting player could use their phone to mess with the current player
who's up? Maybe they have buttons that could temporarily shut off the flippers, or pop
up drop targets which block shots, or release extra balls into play, or turn off all the
lights...

These could be things that are granted to each player (you get one of each per game), or
they could be earned by players for accomplishing certain achievements during the game.

Social media integration
------------------------

Like it or not, people love posting random stupid things to social media, and their
latest accomplishments on some pinball machine in a bar fit nicely into that. We can
imagine a pinball machine tweeting high scores and jackpots made, perhaps even with a
tiny camera in the top of the backbox which sends photos winning (and losing) moments
to the players.

Most locations that have pinball machines also have social media accounts, and they
struggle with ways to get their customers to “connect” with them. An internet-connected
pinball machine could be part of that. Maybe they give players a free game (which they
can redeem by tapping in with their phone) if the player lets the pinball machine tweet
a photo of them winning.

“Offline” goals
---------------

An internet and social media connected pinball machine can also keep the relationship
with the player going even when they’re not at the machine. Maybe a player has to play a
Facebook game or engage with a brand to “unlock” certain features of the game. Or maybe
that’s reversed, where people who play massive online games have to seek out a real world
pinball machine to unlock certain goals in their online game.

Promos & advertising
--------------------

We briefly mentioned the concept that locations could change their machines’ pricing
around special events and for happy hours. But why stop there? What if an advertiser,
desperate to reach the 18-to-35 year old male, could buy their potential customers a
free round of pinball? Imagine that tied to location services with the pinball players’
app. You walk by a bar and your phone buzzes and it says “Lexus would like to buy you a
free pinball game if you walk into this bar in the next 10 minutes.” (Of course this is
something that the bar could do too. Come in now and get a free game of pinball with
every pint you buy.)

We could also imagine in-game advertising, maybe between balls or even integrated within
the game. (Maybe a game has multiple pricing tiers, with the 25-cent game add supported
while the 75-cent game remains “pure.”)

Pinball only costs 75 cents or a dollar to play, and there are many types of advertising
today where the advertisers pay far more than a dollar per impression. A pinball ad
network could charge the advertiser one dollar per game, and the location and operator
would make the same money they always did, the ad network could take their cut, and
there would still be enough left over to increase the revenue a pinball machine could
generate overall.

In-app purchases for game credits and power-ups
-----------------------------------------------

Even in 2014, we notice a lot of our friends saying, “I don’t have any quarters,” as an
excuse not to play pinball. What if you could buy credits via an in-app purchase? There
could be options for credits that expire, credits that are only good for one machine or
one bar, bulk pricing discounts, and even credits that never expire. You could even
structure it like a public transit card where a player’s credits are automatically topped
up when the balance gets low.

This could be used for much more than just credits. Players could buy options like extra
balls, longer ball saves, tilt forgiveness, and other in-game goals all from their phones.
The machines could keep track of which games used which options (important for keeping
fair high scores), and the additional revenue could be shared with the location and
operators.

Buh-bye four-button service menus!
----------------------------------

It probably goes without saying that the four-button
tap-tap-tap-tap-tap-tap-enter-tap-tap-tap service menu is going to be history. Every
pinball machine moving forward should have a mobile app for operators that lets them
configure settings and few reports and audits in an easy-to-use interface on the mobile
device.

Even if they’re not sitting at their machine, operators should be able to connect to a
website to see all their machines, view Google Analytics-style earnings reports, remotely
update software, push out configuration settings, and manage all aspects of the machine.
Leaning down behind a coin door to configure things is almost laughable for a new machine
in today’s world!

Advanced tournament options
---------------------------

One of the problems with tournaments today is that if a machine malfunctions, it can break
the current game in progress which isn't really fair to the current players.

What if the machine could maintain a sort of "transaction log" of everything that happened,
so if a machine malfunctions, the tournament operator could hit a button to pause the
machine, reset the ball or fix the problem, roll back the errant entries, and resume the
game?

You'd also be able to integrate the actual machine scores and players with the
tournament system. Super Selfie Leagues could automatically post scores and notify players
when their scores have been beat or when they move down on the leaderboard.

Accelerometer integration
-------------------------

Modern machines with accelerometers can use them to track g-forces as well as to know
the precise angle (in 3 axes) of the machine.

This means that the machine could notify the operator if the machine was not level. And
when you were leveling the machine, it should show you that level on the display, or even
read it out with text-to-speech as you were underneath the machine adjusting the legs.

The machine could also record the playfield angle for high scores (especially those posted
online, maybe along with tilt sensitivity and outlane settings) to start to get a more
universal baseline to high scores. (Though it still wouldn't be perfect due to wear,
playfield wax, etc.)

The machine would also know if someone was lifting up the front of the machine (even
slightly), which could make for some funny callouts. Maybe the points start draining
until the player sets the machine down again.

You could even have a machine that can apply scoring multipliers based on the angle. (And
maybe even have a machine where you can set the angle and scoring on your own?) Imagine
"My high score on Ghostbusters is 200M at 6.5 degrees, but only 25M at 7 degrees."

The future is bright!
---------------------

One of the things we love most about pinball is that it’s a real, physical thing.
Traditional arcade games have lost much of their earnings power because everyone has a
PS4 and 60″ tv at home. But most people don’t have pinball machines at home. And even
though there are pinball apps for every device out there (which we LOVE, by the way), it
just doesn't compare to actually banging a metal ball around with some mechanical levers.

Maybe it goes without saying, but we consider everything on this page to be our “to do”
list for the Mission Pinball Framework.

The best part is that the Mission Pinball Framework is highly modular, so if you think
some (or all) of these ideas are stupid, that’s fine with us! You can pick-and-choose the
parts of MPF that you like and throw out the rest.

Finally, we understand that a lot (ok, everything) we talked about here only applies to
new pinball machines moving forward. But what about the hundreds of thousands of existing
machines which are already in the world based on 20-year old technology? We have some
ideas for them too... stay tuned!

Happy pinballing!

Late 2016 Update
----------------

We originally wrote this vision when we started MPF back in 2014 (though it's been updated
since then). In late 2016, Jersey Jack Pinball announced `Dialed In! <http://www.jerseyjackpinball.com/games/#dice>`_,
a machine that has some of the features we wrote about in our vision. At Expo, someone asked
us if we were upset that Jersey Jack "ripped us off". Our answer is quite the opposite.
We're thrilled! We love these ideas and love that they're making their way into pinball.
(And frankly we hope that Stern and everyone else does these too.)

Everything about Mission Pinball is open and available for sharing, use, and ripping off.
Take our ideas. Take our code. Copy our docs. We love it all!
