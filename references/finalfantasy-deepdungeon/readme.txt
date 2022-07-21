DEEP DUNGEON
============

Overview
--------

This is a randomizer of sorts for Final Fantasy 1. It essentially erases all
the existing dungeon data and turns Coneria Castle into a procedurally
generated 50-ish floor dungeon. Some have referred to it as an "Ancient Cave"
style randomizer, but whereas Ancient Cave (to my knowledge at least) takes 
existing map layouts and simply randomizes their order, Deep Dungeon discards
the existing maps and generates entirely new ones with random layouts.

Every so many floors there will be a branch to the next town. You can save at
the Inns in the towns, but when you load your game, you will be back on the
overworld outside Coneria Castle. 

There are also no particularly useful places to use shelter items like TENTs,
so you will not find them in the chests very often, and I recommend not
purchasing any. However, I have included a patch which you can optionally
apply to turn them into Ether items which restore MP (ETHR restores a L1 and
L2, DRY restores a L1 through L4, and XETH restores a L1 through L8). Older
versions of this patch had a couple of bugs relating to staying at the inn,
but I believe I have fixed them, at least from the testing I was able to do.

In addition, there is included a patch that will add a clinic to Melmond, a
clinic and an inn to Lefein, and swap Elfland's Silver Sword with Melmond's
Long Sword in the corresponding shops. This is mainly for the sake of
convenience in the case of the inn/clinics, and balancing in the case of
the swords (the Silver Sword obsoletes a fair number of weapons you 
normally would obtain after it).

Somewhere on the final floor will be Chaos. In addition, there is a Bahamut
and a TAIL randomly placed somewhere in the dungeon; they may not be on the
same floor, and they could be encountered in either order. In addition,
there are four Ribbons distributed relatively randomly throughout the
dungeon.

The treasures will on average get "better" the deeper you go into the dungeon,
as do the "difficulty" of the monster encounters. The reason I put those words
in quotes is because they are tricky to measure in any kind of objective way,
so I used item price as a general heuristic for treasure value and Exp/GP
rewards as a general heuristic for monster encounter strength (though the 
algorithm is smart enough to know that there are certain very difficult 
encounters worth almost no Exp and certain very strong items worth almost no 
GP; I did my best to account for that, so don't worry about fighting PHANTOM
on the first floor).

The treasure "density" is completely random, so it's entirely possible that
you might go a long stretch without seeing any treasure and then come across a
floor or even a single room packed with dozens of chests.

Stairs leading to previous floors always look like "down" staircases for the
particular tileset of the floor, and stairs leading to subsequent floors or to
towns look like "up" staircases. Sometimes one or both will look like a ladder
or teleporter, and stairs can appear either in rooms or out of rooms, but 
there will never be any that look like pillars or otherwise secretly disguised
as normal tiles.

Sometimes traversing a certain staircase will light an orb. It doesn't play
the "orb lighting" animation you would see at an altar or anything; in fact
you would never even know it happened unless you thought to look up at your
orbs in the status screen display. This effect is not intentional, but it
appears to be benign with no real effect on the game that I can tell.


Compatibility
-------------

Deep Dungeon seems to be mostly compatible with the standard FF1 randomizer at
finalfantasyrandomizer.com but I would recommend foregoing the "randomization"
type flags, since Deep Dungeon obsoletes most of them. However, the
"convenience" (quality of life), speed, and bug-fix patches I highly recommend.
Note that a rom randomized with both FFR and Deep Dungeon seems to occasionally
not display when you get gold from a chest ("In the chest you found..." and 
then a blank, even though it successfully added gold). This bug is cosmetic
only and has no effect on gameplay.

If you scale Gold and Exp rewards from monsters using the FFR randomizer, make 
sure your settings do not result in an early game item having a price of 
exactly 2 GP. It will cause those items to be found in end game chests. This 
is because FFR does not actually scale the rewards but rather the prices, and 
Deep Dungeon thinks anything worth exactly 2 Gold is an end game item.

If you apply the Ethers patch included with Deep Dungeon, do not apply any FFR
flags that affect shelter items, including the "House MP bug fix". Likewise,
if you apply the Shops patch included with Deep Dungeon, do not apply FFR's
Lefeinish Hospitality flag.

It should in theory work on most FF hacks, as long as they didn't move the
location of the map data within the rom. (Changing map data is fine as long as
it's in the same general memory range in the rom.) Moving the location in
memory of the treasure data would also cause incompatibility with Deep 
Dungeon. Though admittedly, I haven't tested this aspect very thoroughly. If 
you use it on a hack with expanded Job selection such as Final Fantasy -1 or 
Final Fantasy Ultra, I would recommend not talking to Bahamut, as who knows 
what it might do to your party. If anyone does test Deep Dungeon with any rom 
hacks, I would certainly  be curious as to the results. Feel free to contact 
me on RHDN (Pinkpuff).


Usage
-----

To install: 

 * Unzip into a folder of your choice.

To use: (The order matters for these steps)

 * (OPTIONAL) apply the "ethers.ips" patch to a Final Fantasy NES rom file.
 * (OPTIONAL) apply the "shops.ips" patch to the same rom file.
 * (OPTIONAL) apply convenience/bugfix flags to the rom via FFR randomizer.
 * Drag and drop the Final Fantasy NES rom onto the "deepdungeon.exe" file.
 * A black text box will appear.
 * It will ask you for a "seed"; this allows you to reproduce the same random
   result as a previously generated rom. If you have a certain seed you want
   to use, type it here and press enter; otherwise, just press enter.
 * A bunch of text will come up displaying the progress of the randomization.
 * It should eventually say "SUCCESS!" and report the filename of the newly
   randomized rom (it creates a new file without modifying the original). The
   filename of the new file is a bunch of numbers which represent the "seed"
   used to generate the rom in case you wish to reproduce it.
 * Press any key and the black box should go away and the new rom should 
   appear in the folder.
   

Notes
-----

I did my best to test and debug the program but it is possible a few bugs may
have persisted. The ones I know of are:

Occasionally the randomizer will crash (it will say something like "exit with
code" followed by a large negative number); don't worry, it doesn't damage 
anything. Just run the program again with a different seed and you should be
fine. I don't yet know what the cause of that is. It's some kind of broken
pointer or something but it will take some digging to pin down what's
triggering that. (I haven't experienced this issue in a long time so if it
does happen with the current version, I would love to know about it.)

It's also possible you might get a message like "couldn't place Bahamut" or
"couldn't place boss" or something; again, this is a known bug that I don't
have a good solution for yet but from my testing it is fairly rare. Again,
simply run the program again with a different seed and it should work.
(Likewise, I haven't seen this error in my own testing in a very long time
and I would be curious to know about it if you do see it.)

Occasionally it puts a room tile at (0, 0) even when this is in the middle of
the abyss. Again, I'm not sure yet why it does that but it shouldn't affect
gameplay.

If you find anything else, feel free to message me on Romhacking.net


Version History
---------------

1.7
 - Fixed (I think) issue where a staircase could be generated inaccessible
   (at least it hasn't happened again during my testing; let me know if it
   happens to you!)
 - Added four ribbons distributed evenly-ish throughout dungeon
 - Fixed ether patch inn bugs
 - Reduced frequency of "grid of rooms" style floors (the Marsh Basement
   looking ones) and made them a bit smaller on average
 - Added shops patch that swaps Long Sword with Silver Sword and adds inn
   and clinic to Lefein and clinic to Melmond

1.6
 - Fixed bug related to "meandering path" style paths not branching correctly
 - Fixed the rest of the glitch with towns entered from inside rooms
 - Fixed Garland being invisible when spawned outside of a room

1.5
 - Added "meandering path" style and "grid of rooms" style dungeon layouts

1.4
 - Warp (backward) tiles all look like they go "down" while teleport (forward)
   tiles all look like they go "up"

1.3
 - Fixed problem with ether item decrement
 - Fixed minor audiovisual glitch with towns entered from inside rooms

1.2
 - Fixed (I think) problem that could potentially block an exit with a chest
   (no way to know for sure whether it worked unless it happens again)

1.1
 - Added ether patch
 - Changed monster evaluation to look for PHANTOM by monster ID instead of by
   formation ID

1.0
 - Initial release
