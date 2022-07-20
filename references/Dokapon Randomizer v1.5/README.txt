############################################
 WARNING FOR ALL USERS
############################################
This randomizer was made with Python 2.7.
As Python 2.7 is currently nearing End of Life at the time I wrote this, I will not be maintaining this randomizer. What you see is what you get and all that jazz.
This randomizer is not user-friendly by any means and has no safety precautions. Please make backups, especially when the program asks you to.
If anything goes wrong, I'm not liable for anything. I also don't recommend playing with the AI with this. You have been warned.

############################################
 HOW TO USE
############################################
This randomizer will only work with the Wii version of Dokapon Kindom (or so I think). You will obviously want to net yourself an ISO of the game. Legal options preferred here, but you do you.
Once that's all said and done, you will need to extract the "GAME.PAC" from the ISO. I recommend using Wii Backup Fusion.
Put the GAME.PAC file anywhere you can easily remember. If you put it in the root directory of the randomizer executable, it will make your life a bit easier.
Once you're done, run the program and follow the prompts CORRECTLY. The program can easily crash if you type in something wrong.
After you follow the prompts, it should write to your original GAME.PAC file. Move the GAME.PAC file back to where you stored your extracted Dokapon Kingdom files and rebuild the ISO.
You should be all set after this! Go ahead and use your favorite way to play the game to test it.

############################################
 OPTIONS
############################################
(+) Making a Backup (Boolean)
	This allows you to save a backup of your GAME.PAC file whereever it's located before writing to it.

(+) Randomizing Equipment (Boolean)
	This allows you to randomize the statistics of Weapons, Shields, and Accessories.
	If enabled, you get the following options:
	(+) SERIOUSLY Randomize Equipment (Boolean)
		This disregards the normal stats of whatever is being randomized and pulls numbers from a randomly generated table instead, making each item have REALLY fluctuated stats.
	(+) Equipment Strength Multiplier (Float)
		This multiplies the end result of the stat randomization for all items by a flat value.
	(+) Weapon, Shield, Accessory Strength Variance (Float)
		These will either drop or increase the stats of each type of item by 0% to the specified percentile value you give it.

(+) Randomizing Magic (Boolean)
	This allows you to randomize the statistics of Offensive, Defensive, and Field Magic.
	If enabled, you get similar options to Equipment Randomization, but for Magic (obviously).
	(+) SERIOUSLY Randomize Magic (Boolean)
		This disregards the normal stats of whatever is being randomized and pulls numbers from a randomly generated table instead, making each item have REALLY fluctuated stats.
	(+) Magic Strength Multiplier (Float)
		This multiplies the end result of the stat randomization for all items by a flat value.
	(+) Offensive, Defensive, and Field Magic Strength Variance (Float)
		These will either drop or increase the stats of each type of item by 0% to the specified percentile value you give it.

(+) Randomizing Player Classes (Boolean)
	This allows you to randomize the statistics of Player Classes. (NOTE: Both genders count as different sets of classes! Stats are not distributed equally to both genders!)
	If enabled, you get the following options:
	(+) SERIOUSLY Randomize Player Classes (Boolean)
		Again, disregards the original values and replaces them with randomly generated ones.
	(+) Base Stats Strength Multiplier (Float)
		Multiplies the base stats of the player by a flat value. This does not affect your class' carrying capacities or base HP.
	(+) Base Stats, Level-Up Bonuses, Salary, Inventory Capacity Variance (Float)
		These work like the other variance values. I recommend never setting these to zero. You do you though.

(+) Randomizing Monsters (Boolean)
	This allows you to randomize Monster statistics.
	If enabled, you get the following options:
	(+) SERIOUSLY Randomize Monsters (Boolean)
		Disregards the original values and replaces them with randomly generated ones.
	(+) Base Stats Strength Multiplier (Float)
		Multiplies the base stats of the player by a flat value. Unlike the Player Classes, this DOES affect HP.
	(+) Base Stats Variance (Float)
		Works like all the other variance values, increasing or decreasing stats up to the listed percentile value.

(+) Randomize Consumables (Boolean)
	This option shuffles some of the Consumable Item's internal IDs around. It also enables their Prices to be randomized.

(+) Randomize Shops and Drops (Boolean)
	These randomize the contents of Shops and Loot Spaces/Monster Drop Tables respectively.
	
(+) Randomize Prices (Boolean)
	This randomizes the price value of all items in the game.
	If enabled, you get the following options:
	(+) Minimum Price Value (Integer)
		The lowest value an item can cost for purchase.
	(+) Price Strength Variance (Float)
		Like all other variance values.
	(+) SERIOUSLY RANDOMIZE Consumable Item Prices (Boolean)
		Only shows up if Consumables are allowed to be randomized.
		This only affects anything you'd obtain that counts as either a Consumable (crystals, spinners, etc) or as a Gift for the King (gemstones, food, etc). It can make things insanely expensive.
	NOTE: Seriously randomizing anything with Random Prices enabled will randomize their prices dramatically like the consumable randomizer option listed above.
	
(+) Allow Exploits (Boolean)
	This allows some exploitable items to be put into shops and ignores Loot Space Types in regards to Loot Space Drop Table Randomization.
	NOT RECOMMENDED for seriously play. If you're playing casually, feel free to abuse it.
	
(+) Randomized Run Seed (String)
	The seed for the run. Optional. Will generate based on time if you don't supply one.
	
(+) Save Output Log (Boolean)
	This will output everything that was randomized to an output log. The file will end up varying in size depending on how much you randomize.