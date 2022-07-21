FFXED readme v1.5
by fuzzymillipede

#### Table of Contents ###############################################

# Table of Contents

# Instructions
== Requirements
== How to use FFXED with PCSX2
== How to use FFXED with a PS2
== How to use FFXED with a PS3
== Troubleshooting

# Feature Guide
== Keyboard Shortcuts
== Main Menu
== Sub-menus
== Character Menu
== Equipment Menu
== Item Menu
== Sphere Grid Menu
== Blitzball Menu
== Minigame Menu
== Misc Menu
== Import Menu

# License Information

#### Instructions ####################################################

==== Requirements ====================================================

FFXED requires Java to be installed on your computer. If Java is installed, you should be able to start FFXED by double-clicking FFXED.jar. If something isn't working for you, please check the troubleshooting section below.

Links
    Java
    http://java.com/

==== How to use FFXED with PCSX2 =====================================

1. Use FFXED to open your virtual memory card and edit a FFX save. In the PCSX2 menus, go to PCSX2=>Config=>Memory Cards to find the location of the virtual memory cards (Mcd001.ps2 and Mcd002.ps2). In Windows, this is usually the "Documents\PCSX2\memcards" directory. Make sure PCSX2 is not running when you edit your memory card! Otherwise, your memory card may become corrupted!
2. mymc is required for FFXED to work with virtual memory cards. You will be prompted for the location of mymc.exe the first time you try to edit a virtual memory card.

Links
    mymc
    http://www.csclub.uwaterloo.ca:11068/mymc/
    (mirror)
    http://forums.pcsx2.net/attachment.php?aid=41328

==== How to use FFXED with a PS2 =====================================

1. uLaunchELF
This is the best option because uLaunchELF is freely available to download. uLaunchELF can be used to move save files to and from your memory card, using a flash drive or FTP connection. However, you will need a way to run uLaunchELF on your PS2. The preferred method is to have Free McBoot installed on your memory card. You can either follow a tutorial to install it yourself or have one of the volunteers from PSX-Scene install it.

Please note that uLaunchELF will only work with flash drives if your PS2 is version SCPH-7500x or older (the version number is printed on a label on the back of the PS2), although it has been known to work on some SCPH-7700x consoles. If your PS2 is newer than that, you must use uLaunchELF's FTP capabilities or AR-MAX.

2. Code Breaker or AR-MAX
You can use Code Breaker or AR-MAX to move save files to and from your memory card. However, PS2 Save Builder must be used to extract the raw save file so you can edit it in FFXED. 

Please note that Code Breaker will only work if your PS2 is version SCPH-7500x or older.

Links
    uLaunchELF
    http://psx-scene.com/forums/official-ulaunchelf-forums/

    Free McBoot
    http://psx-scene.com/forums/official-free-mc-boot-forums/

    Free McBoot Tutorials
    http://psx-scene.com/forums/f153/fmcb-installer-boot-tutorials-58545/

    Free McBoot Volunteers
    http://psx-scene.com/forums/f153/%5Bread-first-post-%5D%5Bfree-service-%5Di-can-install-fmcb-you-58851/

    Video: How to use FFXED with AR-MAX or Codebreaker.
    http://www.youtube.com/watch?v=rWCecmoeWUo

==== How to use FFXED with a PS3 =====================================

You can use Swap Magic and uLaunchElf to transfer PS2 saves to and from a PS3.

Otherwise, you'll need someone to help you. For this method, you'll need two programs: PSV Exporter and PS2 Save Converter.

Steps:
    1. Get a PSV save off of your PS3 and extract all the files with PSV Exporter
    2. Use PS2 Save Converter to load up the files and give the new save the name of the folder that was extracted. Save the new save as a PSU.
    3. Edit the PSU save in FFXED.
    4. Have someone convert the PSU save into a PSV save, so you can put it onto your PS3.

Links
    Video: How to use FFXED with a PS3
    http://www.youtube.com/watch?v=nrv7pCGBo_Q

    Swap Magic + uLaunchElf Method
    http://www.ps3news.com/forums/ps3-guides-tutorials/guide-convert-ps2-game-saves-psv-format-103447.html

    PSV Exporter
    http://www.ps2savetools.com/download.php?op=viewdownloaddetails&lid=87

    PS2 Save Converter
    http://www.ps2savetools.com/download.php?op=viewdownloaddetails&lid=90

==== Troubleshooting =================================================

- If FFXED.jar doesn't start up when you double-click it, first make sure you have the latest version of the Java Runtime Environment installed on your machine.

- If you have installed Java and FFXED's JAR file is not associated with Java and some other program runs when you double-click it, run Jarfix.

- If mymc complains about missing DLL files, you'll have to download and extract them into the same folder as the rest of the mymc files. Look below for a link to some of the commonly missing DLL files.

- (For PCSX2 only) If you edit your save file and your edits do not show up when you play the game, check the following:
    1. Make sure PCSX2 is not running when you edit your save file.
    2. Make sure you are not loading any savestates through PCSX2. You should start the game normally and load your save file normally in-game.
    3. Verify that you are editing the correct memory card. In the PCSX2 menus, check that PCSX2=>Config=>Memory Cards is pointing to the correct memory card directory.
    4. Verify that your edits are being saved. After saving your edits, close FFXED and use it to open your save file again to make sure that the edits are still there.

Links
    Java Runtime Environment
    http://java.com/

    Jarfix
    http://johann.loefflmann.net/en/software/jarfix/index.html

    mymc DLLs
    http://forums.pcsx2.net/attachment.php?aid=42567

#### Feature Guide ###################################################

==== Keyboard Shortcuts ==============================================

Keyboard shortcuts are used in conjunction with the Alt key. The Escape key can be used to exit menus.

==== Main Menu =======================================================

From here you can load save files for editing. Supported file formats are raw and PSU.

- You can also right-click the "Load File..." button to access the saved locations menu. This determines the directory that FFXED will initially browse to when loading a file. It will default to the first valid directory in the list of saved locations. This can be useful if you want FFXED to default to your flash drive if you have it plugged in.

==== Sub-menus =======================================================

Each sub-menu has an "Apply," "Apply & Close," and "Cancel" button.

- Apply applies your changes.

- Apply & Close applies your changes and closes the menu.

- Cancel closes the menu.

- Note that FFXED does not "remember" the contents of fields when you switch between characters, weapon slots, etc. For example, if you are editing multiple characters, you must press the "Apply" button for each character.

==== Character Menu ==================================================

From here you can edit data that pertains to the characters and aeons.

- The overdrive mode counters count down from an initial value.

- Getting abilities will not affect the Sphere Grid, however to remove any abilities that you have activated on the Sphere Grid you must use the "Remove All" option.

- The stat maxing options do not affect the Sphere Grid.

- The second value for Sphere Level is the "Total Sphere Level," or the total number of levels that the character has gained, which maxes at 101. It determines how much AP is needed to level up.

- Poison Damage % is the percentage of max HP that characters lose from poison.

- The Activation field means the following:
-- Enabled: The character is able to be used.
-- Disabled: The character is temporarily unable to be used.
-- Inactivated: The character has yet to be encountered and is unable to be used.

- Overdrives and Special Abilities are global for all characters.

- The game may behave oddly if there are over seven characters in the party.

- The fonts used in character names are just the same 16 colors repeated over and over, with a minor change in hue as the font number increases. The pattern goes like this:
    Font #000: White
    Font #001: White
    Font #002: Light Gray
    Font #003: Yellow
    Font #004: Brown/Burgundy
    Font #005: White
    Font #006: Dark Gray
    Font #007: Pink
    Font #008: Light Blue
    Font #009: Dark Blue
    Font #010: Dark Blue
    Font #011: White
    Font #012: Green
    Font #013: Blue
    Font #014: Purple
    Font #015: Blue

==== Equipment Menu ==================================================

From here you can edit the properties of equipment.

- The "Equipment" selector dropdown uses bold text to indicate equipped equipment and gray text to indicate empty slots.

- The copy and paste functions can be used to copy and paste the current slot. This function ignores which character the current slot is equipped to. The keyboard shortcut for Paste is Alt+V.

- The "Name" field depends on the "Equip Character" field.

- Under the "Appearance" field, there are some extra options, including the Buster Sword and Samurai Sword. These can crash the game when used with normal attacks. You can avoid this by using Skills and Overdrives instead of normal attacks. The Jecht Sword only works if equipped as armor.

- There are many damage formulas available. These apply to normal attacks and Skills used with the weapon but not magic, overdrives, and other abilities.

-- List of damage formulas
    Normal
        Damage is calculated using the standard physical formula
    Ignore Defense
        Standard physical formula, ignores Defense
    Celestial High HP
        Tidus, Kimahri, Wakka, and Rikku's celestial weapon formula
    Celestial High MP
        Yuna and Lulu's celestial weapon formula
    Celestial Low HP
        Auron's celestial weapon formula
    Target Current HP
        Damage = (Target Current HP) * (Weapon Attack) / 16, Gravity type damage
    Target Max HP
        Damage = (Target Max HP) * (Weapon Attack) / 16, Gravity type damage
    Target Current MP
        Damage = (Target Current MP) * (Weapon Attack) / 16
    Target Max MP
        Damage = (Target Max MP) * (Weapon Attack) / 16
    Magic Formula
        Damage is calculated using Magic formula
    Ignore Magic Defense
        Damage is calculated using Magic formula and ignores Defense
    Special Magic
        Damage is calculated using the special magic formula (uses the physical formula calculations, but off of the Magic stat and ignores Defense)
    Healing Formula
        Damage is calculated using healing formula, doesn't heal
    User Max HP
        Damage = (Weapon Attack) * (Wielder Max HP) / 10
    Multiples of 50
        Damage = (Weapon Attack) * 50
    Multiples of 9999
        Damage = (Weapon Attack) * 9999
    Target Enemies Killed
        Damage = (Target Enemies Killed) * (Weapon Attack), only works against characters 
    Target Tick Speed
        Damage = (Target Tick Speed) * (Weapon Attack) * (3/16)
    Target Tick Counter
        Damage = (Target Tick Counter) * (Weapon Attack) / 16
    Ignore Defense (NR)
        Same as Ignore Defense but without random variance
    Special Magic (NR)
        Same as Special Magic but without random variance
    Multiples of 50 (R)
        Same as Multiples of 50 but with random variance
    No Damage
        0 damage

- You cannot unequip equipment as it can lead to an invalid game state.

- You cannot unoccupy an equipped slot as it can lead to an invalid game state.

- You cannot change the type of equipped equipment as it can lead to an invalid game state.

==== Item Menu =======================================================

From here you can edit the items and key items.

- Under the "Type" field, there are extra options. They allow any character to use abilities such as Summon and Zanmato as items. Some of these items can be accessed from the Item command, others from the Use ability.

- The camera does not work correctly for some of these abilities. Sometimes the camera works correctly for aeons but not characters. If you want to use items with an aeon, you must also enable the Item and/or Use abilities for the aeon.

- When some of these abilities are used with certain characters or against certain enemies, they can crash the game.

- Some abilities such as Break or Banish do not show up in the list because they end up in the Mix menu and cannot be used. Others either always crash the game or are redundant.

==== Sphere Grid Menu ================================================

From here you can edit the Sphere Grid.

- To assist node editing, there are images that map node numbers to actual positions on the Sphere Grid.

-- Standard Sphere Grid Index
https://drive.google.com/open?id=0Bwt6zklxaCPQODcwNWQxYjUtYTgzYS00Y2NjLWFmOTAtYzQ3NDFkNzkyZGU0

-- Expert Sphere Grid Index
https://drive.google.com/open?id=1t2BLebE495RzzxS5ztkWXWd8yuKfLpWa

-- Original Sphere Grid Index
https://drive.google.com/open?id=0Bwt6zklxaCPQYmFhMjE4MzItZTcyYy00YWM3LTlkZGItZGViNmRmNTQyZDM3

- Null nodes do not exist and cannot be edited.

- Empty nodes and lock nodes cannot be activated as this can lead to an invalid game state.

- The "Max Sphere Grid" option gives the following nodes:
    333 HP
    25 MP
    63 Strength
    63 Defense
    63 Magic
    63 Magic Defense
    0 Accuracy

-- The number of Agility, Luck, and Evasion nodes created depends on the grid type.

--- Standard Grid (For 250 Agility, 230 Luck, 290 Luck + Evasion)
    62 Agility
    54 Luck
    13 Evasion

--- Expert Grid (For 170 Agility, 230 Luck, 290 Luck + Evasion)
    43 Agility
    54 Luck
    13 Evasion

--- Original Grid (For 250 Agility, 133 Luck, 255 Luck + Evasion)
    62 Agility
    29 Luck
    30 Evasion

--- Explanation of the above stats
    http://www.gamefaqs.com/boards/197344-final-fantasy-x/55386150

==== Blitzball Menu ==================================================

From here you can edit data pertaining to Blitzball, such as player stats and team membership.

- All Blitzball data is reset when you start the first Blitzball game. This cannot be avoided.

- The game changes the levels of the players on the other teams to match the average level of your team. This cannot be avoided.

- The "Player" selector dropdown uses bold text to indicate which players are on the selected team.

- You can assign "Noname" players on teams as a hindrance, which have very poor stats.

==== Minigame Menu ===================================================

From here you can edit data pertaining to minigames such as chocobo training and lightning bolt dodging.

- The prizes from the butterfly catching minigame can be obtained from the Item menu.

==== Misc Menu =======================================================

- From here you can edit miscellaneous data such as gil and game coordinates.

- The save slot number can only be edited for PSU saves.

- If you want to use FFXED to skip to a certain point in the storyline, here are some helpful game coordinates:
    http://forums.pcsx2.net/Thread-FFX-Game-Coordinates

- Information about Yojimbo Compatibility
    http://www.gamefaqs.com/ps2/197344-final-fantasy-x/faqs/24392

- The "Enable New Game+" function has the option to set the game coordinates to the beginning of the game.

- If you encounter the Dark Valefor Glitch, you can use "Fix Dark Valefor Glitch" to fix it.

==== Import Menu =====================================================

From here you can import data from another save into the current save.

- You can convert save files to other regions.
    1. Use FFXED to open a save file of the region you want to convert to.
    2. Go to the Import menu and open the save you want to convert.
    3. Use the "Import Entire Save" function.

#### License Information #############################################

FFXED by fuzzymillipede is licensed under a Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License

License Details
http://creativecommons.org/licenses/by-nc-nd/3.0/