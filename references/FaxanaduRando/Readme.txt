Faxanadu randomizer

version 0.23

randomizes various aspects of the game.

Requires .net framework 4.8

Tested with a Faxanadu (USA) rom. Does not work with the revised edition.

If you have any interest in the randmizer, consider joining our discord:
https://discord.gg/AyJErR8kyV

Please note that With "Shuffle Towers" and "Include Evil One's Fortress in the tower shuffle" both active, the door that normally leads to the final world will instead be a warp to Eolis.

Features:
    General:
        Fast Text - Makes the text load faster

        Fast Start - You start with Full HP and MP, 1500 golds, and if "randomize keys" is off you also start with the Ring of Elf

        Make equipped Dragon Slayer required - Can't beat the game without the full Battle gear equipped.

        Make Pendant, Magical Rod and Ruby Ring required - Can't beat the game without all of these items

        Move Spring requirement to final requirement - Spring quest must be completed to beat the game, but is not needed to exit Trunk. You still need to push the rock to enter Mist, but only need the ruby ring to do so.

        Move final requirements to final door - Checks for required items at the Evil Ones room instead of at the end of Dartmoor.

        Shuffle Towers - Tower locations are shuffled.

        Update misc text - Update various text related to randomization. One example is that NPCs holding items will tell you what they have if you have not fulfilled their requirement yet.

        Generate Spoiler Log - Generates a .txt file with all item/dungeon locations and other relevant info in it

        Quick seed - The randomizer will try to create a seed that can be beaten more quickly than th3e average seed.

        Allow lowering of respawn value - Make talking to a guru always set your spawn there

        Prevent knockback while on ladders - This will prevent the player from being knocked off ladders when taking damage

        Hints - Changes NPC dialog to add hints for things like item and dungeon locations

        Misc doors - Setting for shuffling some of the non-tower doors, such as outside buildings and possibly town doors.

        World doors - setting for shuffling the location of the tower doors and misc doors in a world, which can result in towers being in different locations than they normally are.

        Allow equipping items indoors - You can equip items inside buildings, but still can't use a sword inside.
        
        Dark towers - The inside of towers will be dark. This tends to make them more challenging.
        
        Include Evil One's Fortress in the tower shuffle - The final dungeon will be shuffled together with other towers. The end of the final world will also lead back to Eolis instead of going to the final dungeon.

    Enemies:
        Randomize Enemy Experience - Enemies give different xp from vanilla

        Randomize Enemy Drops - Enemies drop different things from vanilla (Gold, Bread, or nothing)

        Randomize Enemy Magic Immunities - Enemies can be immune to a spell. (Magic passes through)

        Try to move bosses - The randmizer will try to move bosses so that they are not stuck in the ground.

        Enemy Set - Changes what types of enemies can spawn, and gives some enemies new abilities. 

            No Mixed Enemy Types - Bosses will only appear in vanilla boss locations

            Easy - Some of the harder regular enemies will never spawn, and the boss frequency is low

            Normal - Same as Easy except more hard enemies in the pool and higher boss frequency

            Hard - Same as Normal except more hard enemies in the pool and higher boss frequency. Also upgrades some of the easy enemies to be harder.

            Very Hard - Much more boss enemies and hard regular enemies will appear.

            Extremely Hard - Like Very Hard, but superbosses like King Grieve can appear in normal enemy spawns

            Scaling - Enemies will be harder in later worlds (and possibly towers if tower shuffling is on)

            Unchanged - No enemy randomization

        Enemy HP - Changes enemy HP values by a random numerical value or percentage value. Affects each enemy type seperately

        Enemy Damage - Changes enemy Damage by a random numerical value or percantage value. Affects each enemy type seperately

    Items:
        Guarantee Elixir near Tower of Fortress - Guarantees that there will be an Elixir near the fountain that requires it

        Fix Pendant Bug - Collecting the pendant actually makes you stronger instead of weaker, but also makes it so you are weaker at the start

        Buff Gloves - Increases the glove duration

        Buff Hourglass - The hourglass will no longer take half your HP when used

        Randomize Victim bar rank requirement - Victim barkeep requires a random rank before giving you his item

        Guarantee spell in Eolis - Guarantees a spell in the first town

        Guarantee Mattock near Forepaw - There will be a Mattock somewhere after the breakable wall and before the Trunk exit

        Allow multiple gifts from Fortress and Joker Gurus - Can collect as many of the item given as you can hold. Normally if you have one, you cannot receive another. This only applies to the gurus that normally give the joker key and the ring of ruby. For the Eolis and Conflate guru, they will only give you an item if you don't have it, and for all other places, you can always receive multiple gifts.

        Replace Poison with Mana potions - Introduces a new item (Black Potion) that refills Mana, and removes all Poison from the game, replacing them with Black Potions

        Always spawn small items - Items that normally require the "count" to have a certain value will always spawn when enemies are cleared

        Mattock Usage - Allows Mattock to be used in more places

            Anywhere except Mist entrance - Mattock can be used anywhere except to break in to the Mist door

            Anywhere except Mist entrance, include Fraternal red potion in item shuffle - Same as above but a key item could be locked in a location requiring at least 1 Mattock

            Anywhere, Spring quest is considered required - Mattock can be used anywhere, but the spring quest is considered required by the randomizer so you will still be able to get to the Mist in the traditional way

            Anywhere, Spring not required - Mattock can be used anywhere, spring quest is not guaranteed to be completable

            Unchanged - Mattock can only be used in its vanilla locations

        Eolis Weapon - Can set if there is a guaranteed weapon in Eolis

            Random - the first item slot will be either a Dagger or a Longsword

            Dagger - Eolis will have at least a Dagger

            Longsword - Eolis will have at least a Longsword

            Guarantee if Eolis has no spells - Only guaranteed a weapon if you have no access to spells

            Not guaranteed - Eolis may or may not have a weapon, even if there are no spells available

        Wing Boot Duration - Changes how long Wing Boots are active, and how ranking up affects it

            Random - Start with a random time, and a random increase in time every 4 levels

            XX, Scales up with rank - Starts at XX, and increases every 4 ranks

            Unchanged - Same as Vanilla (40 seconds at the start, drops 10 seconds every 4 ranks)

        Shields - Changes how shields work

            Shields work with Ointment - Shields no longer cause you to get hit while Ointment is active

            Shields work with Ointment and are stronger - Same as above, but they further reduce Magic damage taken

            Unchanged - Same as Vanilla, getting hit in the shield by magic hurts a little even with Ointment on
            
        Big Items - Sets how "big" items like the dragon slayer spawns. It can be set to always spawn them, or always lock them behind a boss if there is one on the screen
            
        Item Shuffle - Changes how items are shuffled

            Shuffle, mix item types (beta) - Overworld items can appear in shops and shop items can appear on the overworld. Some shop items will have an incorrect appearance on the overworld, but can still be collected
            
            Shuffle, mix only shop and gift items - Overworld items and shop/gift items will be shuffled separately
            
            Shuffle, don' mix most gifts with shops - Key items that are normally gifts will still be gifts, for example the Joker key will not appear in a shop but can still be given by another gifter than vanilla. The "Fire" shop counts as a gift location for this setting.
            
            Unchanged - Items will be vanilla
            
        Key requirements - Changes how key requirements are handled

            Randomize, - Key requirements will be completely random
            
            Shuffle - The vanilla key requirements will be shuffled. This means that for example there will be exactly one door that requires the Ace key
            
            Unchanged - Key requirements will be vanilla
    Extra
        Randomize palettes - Randomizes the different palettes used for levels
        Randomize sound effects - Randomizes the different sound effects in the game
        Music - Change the music of the game
            Random - All music will be random
            None - There will be no music at all
            Unchanged - Music is unchanged