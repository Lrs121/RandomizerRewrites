import re
import random
import struct
import copy
import argparse

# Table Variables
TABLE_SHOP_EQUIP = 0x0B1C9844
TABLE_SHOP_CONSUME = 0x0B1C98F0
TABLE_SHOP_MAGIC = 0x0B1C9994

TABLE_DROPS_MONSTERS = 0x0B1E0CD8
TABLE_DROPS_SPACES = 0x0B1C84CC

#TABLE_STATS_SPACES = 0x0B1C7BD8
TABLE_STATS_WEAPONS = 0x0B1CCC08
TABLE_STATS_SHIELDS = 0x0B1CF380
TABLE_STATS_MISC = 0x0B1D05E0
TABLE_STATS_CONSUME = 0x0B1D2780
TABLE_STATS_GIFT = 0x0B1D3020
TABLE_STATS_MAGIC_ATTACK = 0x0B1D945C
TABLE_STATS_MAGIC_DEFENSE = 0x0B1D970C
TABLE_STATS_MAGIC_FIELD = 0x0B1D9964
TABLE_STATS_CLASS = 0x0B1DCCAC
TABLE_STATS_MONSTER = 0x0B1DF888

#TABLE_CLASS_INIT = 0x0B1DCB8C
TABLE_CLASS_LEVELUP = 0x0B1DCE0C
TABLE_CLASS_SALARY = 0x0B1DD20C
TABLE_CLASS_CAPACITY = 0x0B1DD0AC

def clamp(var, min, max):
        if max < min:
                max = min
        if var >= min:
                if var <= max:
                        return var
                return max
        return min

def write_data(s, offset):
        for i in range(len(s)):
                DATA_BASE[offset + i] = s[i]

def get_offset_data(offset, endoffset):
        if endoffset > 0:
                s = ""
                for i in range(0, endoffset, 1):
                        s += chr(DATA_BASE[offset + i])
                return s
        return chr(DATA_BASE[offset])

def randomize_consumables():
        print("Randomizing Consumables...")
        # Set up Regular Expression Formulas
        consume_regex = re.compile('(?s)(\x69\x00{3})([\x01-\x46])([\x00\s\S])([\s\S]{2})([0-9A-Za-z\+\'\x20\-]+)(\x00{1,8})([\x01-\xff][\x00-\xff]{3})([\s\S]{2})([\s\S]{2})')
        gift_regex = re.compile('(?s)(\x6c\x00{3})([\x47-\x9d])(\x00)([\s\S]{2})([0-9A-Za-z\+\'\x20\-]+)(\x00{1,8})([\x01-\xff][\x00-\xff]{3})([\s\S]{4})([\s\S]{4})')
        
        # Consumable Table Output Log
        global sOutputLog
        sOutputLog += "    ========\n"
        sOutputLog += "CONSUMABLE TABLE\n"
        sOutputLog += "    ========\n\n"
        
        # Consumable Table Search and Edit
        for match in consume_regex.finditer(get_offset_data(TABLE_STATS_CONSUME, 0x7DC)):
                id = struct.unpack("<B", bytes(match.group(2), encoding="raw_unicode_escape"))[0]
                type = struct.unpack("<B", bytes(match.group(3), encoding="raw_unicode_escape"))[0]
                name = match.group(5)
                namelen = len(match.group(5)) + len(match.group(6))
                price = [0,0]
                price[0] = struct.unpack("<i", bytes(match.group(7), encoding="raw_unicode_escape"))[0]
                
                # Consumable Price Randomize
                price[1] = price[0]
                # Actual Random Prices
                if bRANDOM_PRICES:
                        if bSTATSHUFFLE_CONSUME:
                                price[1] = random.choice([random.randint(10,1000),random.randint(10,1000),random.randint(100,10000),random.randint(100,10000),random.randint(1000,100000),random.randint(10000,1000000),random.randint(100000,10000000)])
                                price[1] = int(float(price[1]) * (float(random.randint(10,1000))/100))
                        price[1] = clamp(price[1], iMINIMUM_VALUE, int(float(price[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_VALUES)))
                
                # Write data to GAME.PAC
                write_data(struct.pack("<B", id), TABLE_STATS_CONSUME + match.start(2))
                write_data(struct.pack("<i", price[1]), TABLE_STATS_CONSUME + match.start(7))
                
                # Write to Output Log
                sOutputLog += "Consumable ID # " + str(id) + "\n"
                sOutputLog += "Consumable Type #" + str(type) + "\n"
                sOutputLog += "Name: " + name + "\n"
                sOutputLog += "Price: " + str(price) + " G\n\n"
        
        # Gift Table Output Log
        sOutputLog += "  ======\n"
        sOutputLog += "GIFT TABLE\n"
        sOutputLog += "  ======\n\n"
        
        # Gift Table Search and Edit
        for match in gift_regex.finditer(get_offset_data(TABLE_STATS_GIFT, 0xAF8)):
                id = struct.unpack("<B", bytes(match.group(2), encoding="raw_unicode_escape"))[0]
                name = match.group(5)
                namelen = len(match.group(5)) + len(match.group(6))
                price = [0,0]
                giftvalue = [0,0]
                price[0] = struct.unpack("<i", bytes(match.group(7), encoding="raw_unicode_escape"))[0]
                giftvalue[0] = struct.unpack("<i", bytes(match.group(8), encoding="raw_unicode_escape"))[0]
                
                # Gift Price Randomize
                price[1] = price[0]
                giftvalue[1] = giftvalue[0]
                if bRANDOM_PRICES:
                        if bSTATSHUFFLE_CONSUME:
                                price[1] = random.choice([random.randint(10,1000),random.randint(10,1000),random.randint(100,10000),random.randint(100,10000),random.randint(1000,100000),random.randint(10000,1000000),random.randint(100000,10000000)])
                                price[1] = int(float(price[1]) * (float(random.randint(10,500))/100))
                                giftvalue[1] = random.choice([random.randint(-1000,1000)*2,random.randint(-1000,1000)*2,random.randint(-10000,10000)*2,random.randint(-5000,5000)*2,random.randint(-50000,50000)*2,random.randint(-500000,500000),random.randint(-1000000,1000000)*2])
                        price[1] = clamp(price[1], iMINIMUM_VALUE, int(float(price[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_VALUES)))
                        giftvalue[1] = int(float(giftvalue[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_VALUES))
                
                # Write data to GAME.PAC
                write_data(struct.pack("<i", price[1]), TABLE_STATS_GIFT + match.start(7))
                write_data(struct.pack("<i", giftvalue[1]), TABLE_STATS_GIFT + match.start(8))
                
                # Write to Output Log
                sOutputLog += "Gift ID #" + str(id) + "\n"
                sOutputLog += "Name: " + name + "\n"
                sOutputLog += "Price: " + str(price) + " G\n"
                sOutputLog += "King's Gift Value: " + str(giftvalue) + " G\n\n"
        
        print("Done.")

def randomize_equipment():
        print("Randomizing Equipment...")
        # Set up Regular Expression Formulas
        weapon_regex = re.compile('(?s)(\x58\x00\x00\x00)([\s\S])([\s\S])([\s\S]{2})([0-9A-Za-z\+\'\x20\-]+)(\x00\x00?\x00?\x00?)([\s\S]{4})([\s\S]{4})([\s\S]{2})([\s\S]{2})([\s\S]{2})([\s\S]{2})([\s\S]{2})([\s\S]{2})')
        shield_regex = re.compile('(?s)(\^[\x00\s]{3})([\x01-\x28])([\s\S])([\s\S]{2})((Demon Shield)[\x00\s\S]{6,10}|([0-9A-Za-z\+\'\-]+( Guard| Shield)?)([\x00\s]{8}|[\x00\s]{7}|[\x00\s]{6}|[\x00\s]{3}[\x01-\xff][\x00\s]{2}|[\x00\s]{1,3}[\x01-\xff]{2}[\x00\s]{2}|[\x00\s][\x01-\xff]{2}[\x00\s]{2}|[\x00\s]{0,3}[\S\x01-xFF]{0,3}?[\x00\s]{0,3}))([\x00\s\S]{3}[\s\x00\x01\xff\xfe])([\x00\s\S][\s\x00\x01\xff\xfe])([\x00\s\s\S][\s\x00\x01\xff\xfe])([\x00\s\S][\s\x00\x01\xff\xfe])([\x00\s\S][\s\x00\x01\xff\xfe])([\x00\s\S][\s\x00\x01\xff\xfe])([\x00\s\S]{2})')
        misc_regex = re.compile('(?s)(\x64\x00\x00\x00)([\s\S])([\s\S])([\s\S]{2})([0-9A-Za-z\+\'\x20\-]+)(\x00{0,4}(\x64\x00|[\s\S]{2})[\x00\s\S]{0,2})([\s\S]{4})([\s\S]{2})([\s\S]{2})([\s\S]{2})([\s\S]{2})([\s\S]{2})([\s\S]{2})([\s\S]{4})')
        
        # Weapon Table Output Log
        global sOutputLog
        sOutputLog += "  ========\n"
        sOutputLog += "WEAPON TABLE\n"
        sOutputLog += "  ========\n\n"
        
        # Weapon Table Search and Edit
        for match in weapon_regex.finditer(get_offset_data(TABLE_STATS_WEAPONS, 0xAB4)):
                id = struct.unpack("<B", bytes(match.group(2), encoding="raw_unicode_escape"))[0]
                name = match.group(5)
                namelen = len(match.group(5)) + len(match.group(6))
                price = [0,0]
                at = [0,0]
                df = [0,0]
                mg = [0,0]
                spd = [0,0]
                hp = [0,0]
                price[0] = struct.unpack("<i", bytes(match.group(8), encoding="raw_unicode_escape"))[0]
                at[0] = struct.unpack("<h",bytes(match.group(9), encoding="raw_unicode_escape"))[0]
                df[0] = struct.unpack("<h",bytes(match.group(10), encoding="raw_unicode_escape"))[0]
                mg[0] = struct.unpack("<h",bytes(match.group(11), encoding="raw_unicode_escape"))[0]
                spd[0] = struct.unpack("<h",bytes(match.group(12), encoding="raw_unicode_escape"))[0]
                hp[0] = struct.unpack("<h",bytes(match.group(13), encoding="raw_unicode_escape"))[0]
                
                # Item Price Randomize
                price[1] = price[0]
                if bRANDOM_PRICES:
                        if bSTATSHUFFLE_EQUIP:
                                price[1] = random.choice([random.randint(10,1000),random.randint(10,1000),random.randint(100,10000),random.randint(100,10000),random.randint(1000,100000),random.randint(10000,1000000),random.randint(100000,10000000)])
                                price[1] = int(float(price[1]) * (float(random.randint(10,1000))/100))
                        price[1] = clamp(price[1], iMINIMUM_VALUE, int(float(price[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_VALUES)))
                
                # Item Stat Randomize
                at[1] = at[0]
                df[1] = df[0]
                mg[1] = mg[0]
                spd[1] = spd[0]
                hp[1] = hp[0]
                if bSTATSHUFFLE_EQUIP:
                        at[1] = random.choice([random.randint(1,10),random.randint(1,10),random.randint(1,50),random.randint(1,50),random.randint(1,100),random.randint(1,300)])
                        df[1] = random.choice([random.randint(-2,10),random.randint(-2,10),random.randint(-10,50),random.randint(-10,50),random.randint(-20,100),random.randint(-60,300)])
                        mg[1] = random.choice([random.randint(-2,10),random.randint(-2,10),random.randint(-10,50),random.randint(-10,50),random.randint(-20,100),random.randint(-60,300)])
                        spd[1] = random.choice([random.randint(-2,10),random.randint(-2,10),random.randint(-10,50),random.randint(-10,50),random.randint(-20,100),random.randint(-60,300)])
                        hp[1] = random.choice([random.randint(0,10),random.randint(0,10),random.randint(0,50),random.randint(0,50),random.randint(0,100),random.randint(0,300)])
                at[1] = int(float(at[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_EQATTACK) * fMULTIPLIER_EQUIP)
                df[1] = int(float(df[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_EQATTACK) * fMULTIPLIER_EQUIP)
                mg[1] = int(float(mg[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_EQATTACK) * fMULTIPLIER_EQUIP)
                spd[1] = int(float(spd[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_EQATTACK) * fMULTIPLIER_EQUIP)
                hp[1] = int(float(hp[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_EQATTACK) * fMULTIPLIER_EQUIP)
                
                # Write data to GAME.PAC
                write_data(struct.pack("<i", price[1]), TABLE_STATS_WEAPONS + match.start(8))
                write_data(struct.pack("<h", at[1]), TABLE_STATS_WEAPONS + match.start(9))
                write_data(struct.pack("<h", df[1]), TABLE_STATS_WEAPONS + match.start(10))
                write_data(struct.pack("<h", mg[1]), TABLE_STATS_WEAPONS + match.start(11))
                write_data(struct.pack("<h", spd[1]), TABLE_STATS_WEAPONS + match.start(12))
                write_data(struct.pack("<h", hp[1]), TABLE_STATS_WEAPONS + match.start(13))
                
                # Write to Output Log
                sOutputLog += "Weapon ID #" + str(id) + "\n"
                sOutputLog += "Name: " + name + "\n"
                sOutputLog += "Price: " + str(price) + " G\nStats: " + str(at) + " ATK / " + str(df) + " DEF / " + str(mg) + " MAG / " + str(spd) + " SPD / " + str([hp[0]*10, hp[1]*10]) + " HP\n\n"
        
        # Shield Table Output Log
        sOutputLog += "  ========\n"
        sOutputLog += "SHIELD TABLE\n"
        sOutputLog += "  ========\n\n"
        
        # Shield Table Search and Edit
        for match in shield_regex.finditer(get_offset_data(TABLE_STATS_SHIELDS, 0x6AC)):
                id = struct.unpack("<B", bytes(match.group(2), encoding="raw_unicode_escape"))[0]
                namelen = len(match.group(5))
                name = ""
                if match.group(6) == None:
                        name = match.group(7)
                else:
                        name = match.group(6)
                price = [0,0]
                at = [0,0]
                df = [0,0]
                mg = [0,0]
                spd = [0,0]
                hp = [0,0]
                price[0] = struct.unpack("<i", bytes(match.group(10), encoding="raw_unicode_escape"))[0]
                at[0] = struct.unpack("<h",bytes(match.group(12), encoding="raw_unicode_escape"))[0]
                df[0] = struct.unpack("<h",bytes(match.group(11), encoding="raw_unicode_escape"))[0]
                mg[0] = struct.unpack("<h",bytes(match.group(13), encoding="raw_unicode_escape"))[0]
                spd[0] = struct.unpack("<h",bytes(match.group(14), encoding="raw_unicode_escape"))[0]
                hp[0] = struct.unpack("<h",bytes(match.group(15), encoding="raw_unicode_escape"))[0]
                
                # Item Price Randomize
                price[1] = price[0]
                if bRANDOM_PRICES:
                        if bSTATSHUFFLE_EQUIP:
                                price[1] = random.choice([random.randint(10,1000),random.randint(10,1000),random.randint(100,10000),random.randint(100,10000),random.randint(1000,100000),random.randint(10000,1000000),random.randint(100000,10000000)])
                                price[1] = int(float(price[1]) * (float(random.randint(10,1000))/100))
                        price[1] = clamp(price[1], iMINIMUM_VALUE, int(float(price[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_VALUES)))
                
                # Item Stat Randomize
                at[1] = at[0]
                df[1] = df[0]
                mg[1] = mg[0]
                spd[1] = spd[0]
                hp[1] = hp[0]
                if bSTATSHUFFLE_EQUIP:
                        at[1] = random.choice([random.randint(-2,10),random.randint(-2,10),random.randint(-10,50),random.randint(-10,50),random.randint(-20,100),random.randint(-60,300)])
                        df[1] = random.choice([random.randint(1,10),random.randint(1,10),random.randint(1,50),random.randint(1,50),random.randint(1,100),random.randint(1,300)])
                        mg[1] = random.choice([random.randint(-2,10),random.randint(-2,10),random.randint(-10,50),random.randint(-10,50),random.randint(-20,100),random.randint(-60,300)])
                        spd[1] = random.choice([random.randint(-2,10),random.randint(-2,10),random.randint(-10,50),random.randint(-10,50),random.randint(-20,100),random.randint(-60,300)])
                        hp[1] = random.choice([random.randint(0,10),random.randint(0,10),random.randint(0,50),random.randint(0,50),random.randint(0,100),random.randint(0,300)])
                at[1] = int(float(at[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_EQDEFENSE) * fMULTIPLIER_EQUIP)
                df[1] = int(float(df[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_EQDEFENSE) * fMULTIPLIER_EQUIP)
                mg[1] = int(float(mg[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_EQDEFENSE) * fMULTIPLIER_EQUIP)
                spd[1] = int(float(spd[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_EQDEFENSE) * fMULTIPLIER_EQUIP)
                hp[1] = int(float(hp[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_EQDEFENSE) * fMULTIPLIER_EQUIP)
                
                # Write data to GAME.PAC
                write_data(struct.pack("<i", price[1]), TABLE_STATS_SHIELDS + match.start(10))
                write_data(struct.pack("<h", at[1]), TABLE_STATS_SHIELDS + match.start(12))
                write_data(struct.pack("<h", df[1]), TABLE_STATS_SHIELDS + match.start(11))
                write_data(struct.pack("<h", mg[1]), TABLE_STATS_SHIELDS + match.start(13))
                write_data(struct.pack("<h", spd[1]), TABLE_STATS_SHIELDS + match.start(14))
                write_data(struct.pack("<h", hp[1]), TABLE_STATS_SHIELDS + match.start(15))
                
                # Write to Output Log
                sOutputLog += "Shield ID #" + str(id) + "\n"
                sOutputLog += "Name: " + name + "\n"
                sOutputLog += "Price: " + str(price) + " G\nStats: " + str(at) + " ATK / " + str(df) + " DEF / " + str(mg) + " MAG / " + str(spd) + " SPD / " + str([hp[0]*10, hp[1]*10]) + " HP\n\n"
        
        # Accessory Table Output Log
        sOutputLog += "   ========\n"
        sOutputLog += "ACCESSORY TABLE\n"
        sOutputLog += "   ========\n\n"
        
        # Accessory Table Search and Edit
        for match in misc_regex.finditer(get_offset_data(TABLE_STATS_MISC, 0x61A)):
                id = struct.unpack("<B", bytes(match.group(2), encoding="raw_unicode_escape"))[0]
                name = match.group(5)
                namelen = len(match.group(5)) + len(match.group(6))
                price = [0,0]
                at = [0,0]
                df = [0,0]
                mg = [0,0]
                spd = [0,0]
                hp = [0,0]
                price[0] = struct.unpack("<i", bytes(match.group(8), encoding="raw_unicode_escape"))[0]
                at[0] = struct.unpack("<h",bytes(match.group(9), encoding="raw_unicode_escape"))[0]
                df[0] = struct.unpack("<h",bytes(match.group(10), encoding="raw_unicode_escape"))[0]
                mg[0] = struct.unpack("<h",bytes(match.group(11), encoding="raw_unicode_escape"))[0]
                spd[0] = struct.unpack("<h",bytes(match.group(12), encoding="raw_unicode_escape"))[0]
                hp[0] = struct.unpack("<h",bytes(match.group(13), encoding="raw_unicode_escape"))[0]
                
                # Item Price Randomize
                price[1] = price[0]
                if bRANDOM_PRICES:
                        if bSTATSHUFFLE_EQUIP:
                                price[1] = random.choice([random.randint(10,1000),random.randint(10,1000),random.randint(100,10000),random.randint(100,10000),random.randint(1000,100000),random.randint(10000,1000000),random.randint(100000,10000000)])
                                price[1] = int(float(price[1]) * (float(random.randint(10,1000))/100))
                        price[1] = clamp(price[1], iMINIMUM_VALUE, int(float(price[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_VALUES)))
                
                # Item Stat Randomize
                at[1] = at[0]
                df[1] = df[0]
                mg[1] = mg[0]
                spd[1] = spd[0]
                hp[1] = hp[0]
                if bSTATSHUFFLE_EQUIP:
                        at[1] = random.choice([random.randint(0,10),random.randint(0,10),random.randint(-2,50),random.randint(-2,50),random.randint(-5,100),random.randint(-15,300)])
                        df[1] = random.choice([random.randint(0,10),random.randint(0,10),random.randint(-2,50),random.randint(-2,50),random.randint(-5,100),random.randint(-15,300)])
                        mg[1] = random.choice([random.randint(0,10),random.randint(0,10),random.randint(-2,50),random.randint(-2,50),random.randint(-5,100),random.randint(-15,300)])
                        spd[1] = random.choice([random.randint(0,10),random.randint(0,10),random.randint(-2,50),random.randint(-2,50),random.randint(-5,100),random.randint(-15,300)])
                        hp[1] = random.choice([random.randint(0,10),random.randint(0,10),random.randint(-2,50),random.randint(-2,50),random.randint(-5,100),random.randint(-15,300)])
                at[1] = int(float(at[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_EQMISC) * fMULTIPLIER_EQUIP)
                df[1] = int(float(df[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_EQMISC) * fMULTIPLIER_EQUIP)
                mg[1] = int(float(mg[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_EQMISC) * fMULTIPLIER_EQUIP)
                spd[1] = int(float(spd[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_EQMISC) * fMULTIPLIER_EQUIP)
                hp[1] = int(float(hp[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_EQMISC) * fMULTIPLIER_EQUIP)
                
                # Write data to GAME.PAC
                write_data(struct.pack("<i", price[1]), TABLE_STATS_MISC + match.start(8))
                write_data(struct.pack("<h", at[1]), TABLE_STATS_MISC + match.start(9))
                write_data(struct.pack("<h", df[1]), TABLE_STATS_MISC + match.start(10))
                write_data(struct.pack("<h", mg[1]), TABLE_STATS_MISC + match.start(11))
                write_data(struct.pack("<h", spd[1]), TABLE_STATS_MISC + match.start(12))
                write_data(struct.pack("<h", hp[1]), TABLE_STATS_MISC + match.start(13))
                
                # Write to Output Log
                sOutputLog += "Accessory ID #" + str(id) + "\n"
                sOutputLog += "Name: " + name + "\n"
                sOutputLog += "Price: " + str(price) + " G\nStats: " + str(at) + " ATK / " + str(df) + " DEF / " + str(mg) + " MAG / " + str(spd) + " SPD / " + str([hp[0]*10, hp[1]*10]) + " HP\n\n"

        print("Done.")

def randomize_magic():
        print("Randomizing Magic...")
        # Set up Regular Expression Formulas
        offensemagic_regex = re.compile('(?s)(\x70\x00{3})([\x01-\x17])(\x00)([\s\S]{2})([0-9A-Za-z\+\'\x20\-]+)\x00(\x00{0,3})(\x00[\s\S]{2}\x00|[\x00-\xff]{4})([\s\S][\x00\x01])([\s\S]{4})[\s\S]{2}')
        defensemagic_regex = re.compile('(?s)(\x72\x00{3})([\x01-\x13])(\x00)([\s\S]{2})([0-9A-Za-z\+\'\x20\-]+)\x00(\x00{0,3})(\x00[\s\S]{2}\x00|[\x00-\xff]{4})([\s\S][\x00\x01])([\s\S]{4})[\s\S]{2}')
        fieldmagic_regex = re.compile('(?s)(\x74\x00{3})([\x01-\x26])(\x00)([\s\S]{2})([0-9A-Za-z\+\'\x20\-]+)\x00(\x00{0,3})(\x00[\s\S]{2}\x00|[\x00-\xff]{4})([\s\S][\x00\x01])([\s\S]{4})[\s\S]{2}')

        # Offensive Magic Table Output Log
        global sOutputLog
        sOutputLog += "     =========\n"
        sOutputLog += "OFFENSE MAGIC TABLE\n"
        sOutputLog += "     =========\n\n"
        
        # Offensive Magic Table Search and Edit
        for match in offensemagic_regex.finditer(get_offset_data(TABLE_STATS_MAGIC_ATTACK, 0x2A4)):
                id = struct.unpack("<B", bytes(match.group(2), encoding="raw_unicode_escape"))[0]
                name = match.group(5)
                namelen = len(match.group(5)) + len(match.group(6))
                price = [0,0]
                potency = [0,0]
                price[0] = struct.unpack("<i", bytes(match.group(7), encoding="raw_unicode_escape"))[0]
                potency[0] = struct.unpack("<h", bytes(match.group(8), encoding="raw_unicode_escape"))[0]
                
                # Magic Price Randomize
                price[1] = price[0]
                if bRANDOM_PRICES:
                        if bSTATSHUFFLE_MAGIC:
                                price[1] = random.choice([random.randint(10,1000),random.randint(10,1000),random.randint(100,10000),random.randint(100,10000),random.randint(1000,100000),random.randint(10000,1000000),random.randint(100000,10000000)])
                                price[1] = int(float(price[1]) * (float(random.randint(10,1000))/100))
                        price[1] = clamp(price[1], iMINIMUM_VALUE, int(float(price[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_VALUES)))

                # Magic Stat Randomize
                potency[1] = potency[0]
                if bSTATSHUFFLE_MAGIC:
                        potency[1] = random.choice([random.randint(50,300),random.randint(50,300),random.randint(100,500),random.randint(100,500),random.randint(250,1000),random.randint(10,2500)])
                potency[1] = int(float(potency[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_MGATTACK) * fMULTIPLIER_MAGIC)
                
                # Write data to GAME.PAC
                write_data(struct.pack("<i", price[1]), TABLE_STATS_MAGIC_ATTACK + match.start() + 9 + namelen + 0)
                write_data(struct.pack("<h", potency[1]), TABLE_STATS_MAGIC_ATTACK + match.start() + 9 + namelen + 4)
                
                # Write to Output Log
                sOutputLog += "Offensive Magic ID #" + str(id) + "\n"
                sOutputLog += "Name: " + name + "\n"
                sOutputLog += "Price: " + str(price) + " G\nPotency: " + str([float(potency[0])/100, float(potency[1])/100]) + "\n\n"
        
        # Defensive Magic Table Output Log
        sOutputLog += "     =========\n"
        sOutputLog += "DEFENSE MAGIC TABLE\n"
        sOutputLog += "     =========\n\n"
        
        # Defensive Magic Table Search and Edit
        for match in defensemagic_regex.finditer(get_offset_data(TABLE_STATS_MAGIC_DEFENSE, 0x250)):
                id = struct.unpack("<B", bytes(match.group(2), encoding="raw_unicode_escape"))[0]
                name = match.group(5)
                namelen = len(match.group(5)) + len(match.group(6))
                price = [0,0]
                potency = [0,0]
                price[0] = struct.unpack("<i", bytes(match.group(7), encoding="raw_unicode_escape"))[0]
                potency[0] = struct.unpack("<h", bytes(match.group(8), encoding="raw_unicode_escape"))[0]
                
                # Magic Price Randomize
                price[1] = price[0]
                if bRANDOM_PRICES:
                        if bSTATSHUFFLE_MAGIC:
                                price[1] = random.choice([random.randint(10,1000),random.randint(10,1000),random.randint(100,10000),random.randint(100,10000),random.randint(1000,100000),random.randint(10000,1000000),random.randint(100000,10000000)])
                                price[1] = int(float(price[1]) * (float(random.randint(10,1000))/100))
                        price[1] = clamp(price[1], iMINIMUM_VALUE, int(float(price[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_VALUES)))

                # Magic Stat Randomize
                potency[1] = potency[0]
                if bSTATSHUFFLE_MAGIC:
                        potency[1] = random.choice([random.randint(1,10),random.randint(1,10),random.randint(3,30),random.randint(3,30),random.randint(5,50),random.randint(1,90)])
                potency[1] = int(float(potency[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_MGDEFENSE) * fMULTIPLIER_MAGIC)
                
                # Write data to GAME.PAC
                write_data(struct.pack("<i", price[1]), TABLE_STATS_MAGIC_DEFENSE + match.start(7))
                write_data(struct.pack("<h", potency[1]), TABLE_STATS_MAGIC_DEFENSE + match.start(8))
                
                # Write to Output Log
                sOutputLog += "Defensive Magic ID #" + str(id) + "\n"
                sOutputLog += "Name: " + name + "\n"
                sOutputLog += "Price: " + str(price) + " G\nPotency: " + str([float(potency[0])/100, float(potency[1])/100]) + "\n\n"
        
        # Field Magic Table Output Log
        sOutputLog += "    =========\n"
        sOutputLog += "FIELD MAGIC TABLE\n"
        sOutputLog += "    =========\n\n"
        
        # Field Magic Table Search and Edit
        for match in fieldmagic_regex.finditer(get_offset_data(TABLE_STATS_MAGIC_FIELD, 0x480)):
                id = struct.unpack("<B", bytes(match.group(2), encoding="raw_unicode_escape"))[0]
                name = match.group(5)
                namelen = len(match.group(5)) + len(match.group(6))
                price = [0,0]
                potency = [0,0]
                price[0] = struct.unpack("<i", bytes(match.group(7), encoding="raw_unicode_escape"))[0]
                potency[0] = struct.unpack("<h", bytes(match.group(8), encoding="raw_unicode_escape"))[0]
                
                # Magic Price Randomize
                price[1] = price[0]
                if bRANDOM_PRICES:
                        if bSTATSHUFFLE_MAGIC:
                                price[1] = random.choice([random.randint(10,1000),random.randint(10,1000),random.randint(100,10000),random.randint(100,10000),random.randint(1000,100000),random.randint(10000,1000000),random.randint(100000,10000000)])
                                price[1] = int(float(price[1]) * (float(random.randint(10,1000))/100))
                        price[1] = clamp(price[1], iMINIMUM_VALUE, int(float(price[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_VALUES)))

                # Magic Stat Randomize
                potency[1] = potency[0]
                if bSTATSHUFFLE_MAGIC:
                        potency[1] = random.choice([random.randint(1,10),random.randint(1,10),random.randint(3,30),random.randint(3,30),random.randint(5,50),random.randint(1,90)])
                potency[1] = int(float(potency[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_MGFIELD) * fMULTIPLIER_MAGIC)
                
                # Write data to GAME.PAC
                write_data(struct.pack("<i", price[1]), TABLE_STATS_MAGIC_FIELD + match.start(7))
                write_data(struct.pack("<h", potency[1]), TABLE_STATS_MAGIC_FIELD + match.start(8))
                
                # Write to Output Log
                sOutputLog += "Field Magic ID #" + str(id) + "\n"
                sOutputLog += "Name: " + name + "\n"
                sOutputLog += "Price: " + str(price) + " G\nPotency: " + str([float(potency[0])/100, float(potency[1])/100]) + "\n\n"
        
        print("Done.")

def randomize_classes():
        print("Randomizing Classes...")
        # Set up Regular Expression Formulas
        class_base_regex = re.compile('(?s)(\x40\x00{3})([\x00-\x0A])([\x00\x01])([\s\S]{2})([\s\S]{2})([\s\S]{2})([\s\S]{2})([\s\S]{2})')
        class_lvbonus_regex = re.compile('(?s)(\x3B\x00{3})([\x00-\x0A])([\x00\x01])([\s\S]{2})([\s\S]{2})([\s\S]{2})([\s\S]{2})([\s\S]{2})([\s\S]{12})')
        class_salary_regex = re.compile('(?s)(\x2E\x00{3})([\x00-\x0A])([\x00\x01])([\s\S]{2})([\s\S]{2})\x00\x00([\s\S]{2})([\s\S]{2})')
        class_capacity_regex = re.compile('(?s)(\x44\x00{3})([\x00-\x0A])([\x00\x01])([\x04-\x0c])([\x04-\x0c])')
        
        # Class Base Stats Table Output Log
        global sOutputLog
        sOutputLog += "      ==========\n"
        sOutputLog += "CLASS BASE STATS TABLE\n"
        sOutputLog += "      ==========\n\n"
        
        # Class Base Stats Table Search and Edit
        for match in class_base_regex.finditer(get_offset_data(TABLE_STATS_CLASS, 0x160)):
                tid = struct.unpack("<B", bytes(match.group(2), encoding="raw_unicode_escape"))[0]
                gid = struct.unpack("<B", bytes(match.group(3), encoding="raw_unicode_escape"))[0]
                at = [0,0]
                df = [0,0]
                mg = [0,0]
                spd = [0,0]
                at[0] = struct.unpack("<H",bytes(match.group(4), encoding="raw_unicode_escape"))[0]
                df[0] = struct.unpack("<H",bytes(match.group(5), encoding="raw_unicode_escape"))[0]
                mg[0] = struct.unpack("<H",bytes(match.group(6), encoding="raw_unicode_escape"))[0]
                spd[0] = struct.unpack("<H",bytes(match.group(7), encoding="raw_unicode_escape"))[0]
                
                at[1] = at[0]
                df[1] = df[0]
                mg[1] = mg[0]
                spd[1] = spd[0]
                if bSTATSHUFFLE_CLASS:
                        at[1] = random.choice([random.randint(1,3),random.randint(1,3),random.randint(2,5),random.randint(2,5),random.randint(4,8),random.randint(1,15)])
                        df[1] = random.choice([random.randint(1,3),random.randint(1,3),random.randint(2,5),random.randint(2,5),random.randint(4,8),random.randint(1,15)])
                        mg[1] = random.choice([random.randint(1,3),random.randint(1,3),random.randint(2,5),random.randint(2,5),random.randint(4,8),random.randint(1,15)])
                        spd[1] = random.choice([random.randint(1,3),random.randint(1,3),random.randint(2,5),random.randint(2,5),random.randint(4,8),random.randint(1,15)])
                at[1] = int(float(at[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_CBASE) * fMULTIPLIER_CLASS)
                if at[1] < 0:
                    at[1] = 0
                df[1] = int(float(df[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_CBASE) * fMULTIPLIER_CLASS)
                if df[1] < 0:
                    df[1] = 0
                mg[1] = int(float(mg[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_CBASE) * fMULTIPLIER_CLASS)
                if mg[1] < 0:
                    mg[1] = 0
                spd[1] = int(float(spd[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_CBASE) * fMULTIPLIER_CLASS)
                if spd[1] < 0:
                    spd[1] = 0
                
                # Write data to GAME.PAC
                write_data(struct.pack("<H", at[1]), TABLE_STATS_CLASS + match.start(4))
                write_data(struct.pack("<H", df[1]), TABLE_STATS_CLASS + match.start(5))
                write_data(struct.pack("<H", mg[1]), TABLE_STATS_CLASS + match.start(6))
                write_data(struct.pack("<H", spd[1]), TABLE_STATS_CLASS + match.start(7))
                
                # Write to Output Log
                sOutputLog += "Class ID #" + str(tid) + "\n"
                sOutputLog += "Gender ID #" + str(gid) + "\n"
                sOutputLog += "Stats: " + str(at) + " ATK / " + str(df) + " DEF / " + str(mg) + " MAG / " + str(spd) + " SPD\n\n"
        
        # Class Level Up Bonus Table Output Log
        sOutputLog += "        ==========\n"
        sOutputLog += "CLASS LEVEL-UP BONUS TABLE\n"
        sOutputLog += "        ==========\n\n"
        
        # Class Level Up Bonus Table Search and Edit
        for match in class_lvbonus_regex.finditer(get_offset_data(TABLE_CLASS_LEVELUP, 0x2A0)):
                tid = struct.unpack("<B", bytes(match.group(2), encoding="raw_unicode_escape"))[0]
                gid = struct.unpack("<B", bytes(match.group(3), encoding="raw_unicode_escape"))[0]
                at = [0,0]
                df = [0,0]
                mg = [0,0]
                spd = [0,0]
                hp = [0,0]
                at[0] = struct.unpack("<H",bytes(match.group(4), encoding="raw_unicode_escape"))[0]
                df[0] = struct.unpack("<H",bytes(match.group(5), encoding="raw_unicode_escape"))[0]
                mg[0] = struct.unpack("<H",bytes(match.group(6), encoding="raw_unicode_escape"))[0]
                spd[0] = struct.unpack("<H",bytes(match.group(7), encoding="raw_unicode_escape"))[0]
                hp[0] = struct.unpack("<H",bytes(match.group(8), encoding="raw_unicode_escape"))[0]
                
                at[1] = at[0]
                df[1] = df[0]
                mg[1] = mg[0]
                spd[1] = spd[0]
                hp[1] = hp[0]
                if bSTATSHUFFLE_CLASS:
                        at[1] = random.choice([random.randint(0,3),random.randint(0,3),random.randint(2,5),random.randint(2,5),random.randint(4,7),random.randint(1,10)])
                        df[1] = random.choice([random.randint(0,3),random.randint(0,3),random.randint(2,5),random.randint(2,5),random.randint(4,7),random.randint(1,10)])
                        mg[1] = random.choice([random.randint(0,3),random.randint(0,3),random.randint(2,5),random.randint(2,5),random.randint(4,7),random.randint(1,10)])
                        spd[1] = random.choice([random.randint(0,3),random.randint(0,3),random.randint(2,5),random.randint(2,5),random.randint(4,7),random.randint(1,10)])
                        hp[1] = random.choice([random.randint(0,3),random.randint(0,3),random.randint(2,5),random.randint(2,5),random.randint(4,7),random.randint(1,10)])
                at[1] = int(float(at[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_CLEVELUP) * fMULTIPLIER_CLASS)
                if at[1] < 0:
                    at[1] = 0
                df[1] = int(float(df[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_CLEVELUP) * fMULTIPLIER_CLASS)
                if df[1] < 0:
                    df[1] = 0
                mg[1] = int(float(mg[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_CLEVELUP) * fMULTIPLIER_CLASS)
                if mg[1] < 0:
                    mg[1] = 0
                spd[1] = int(float(spd[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_CLEVELUP) * fMULTIPLIER_CLASS)
                if spd[1] < 0:
                    spd[1] = 0
                hp[1] = int(float(hp[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_CLEVELUP) * fMULTIPLIER_CLASS)
                if hp[1] < 0:
                    hp[1] = 0
                
                # Write data to GAME.PAC
                write_data(struct.pack("<H", at[1]), TABLE_CLASS_LEVELUP + match.start(4))
                write_data(struct.pack("<H", df[1]), TABLE_CLASS_LEVELUP + match.start(5))
                write_data(struct.pack("<H", mg[1]), TABLE_CLASS_LEVELUP + match.start(6))
                write_data(struct.pack("<H", spd[1]), TABLE_CLASS_LEVELUP + match.start(7))
                write_data(struct.pack("<H", hp[1]), TABLE_CLASS_LEVELUP + match.start(8))
                
                # Write to Output Log
                sOutputLog += "Class ID #" + str(tid) + "\n"
                sOutputLog += "Gender ID #" + str(gid) + "\n"
                sOutputLog += "Stats: " + str(at) + " ATK / " + str(df) + " DEF / " + str(mg) + " MAG / " + str(spd) + " SPD / " + str([hp[0]*10, hp[1]*10]) + " HP\n\n"
        
        # Class Salary Table Output Log
        sOutputLog += "     ========\n"
        sOutputLog += "CLASS SALARY TABLE\n"
        sOutputLog += "     ========\n\n"
        
        # Class Salary Table Search and Edit
        for match in class_salary_regex.finditer(get_offset_data(TABLE_CLASS_SALARY, 0x160)):
                tid = struct.unpack("<B", bytes(match.group(2), encoding="raw_unicode_escape"))[0]
                gid = struct.unpack("<B", bytes(match.group(3), encoding="raw_unicode_escape"))[0]
                salary = [0,0]
                smallbonus = [0,0]
                bigbonus = [0,0]
                salary[0] = struct.unpack("<H",bytes(match.group(5), encoding="raw_unicode_escape"))[0]
                smallbonus[0] = struct.unpack("<H",bytes(match.group(6), encoding="raw_unicode_escape"))[0]
                bigbonus[0] = struct.unpack("<H",bytes(match.group(7), encoding="raw_unicode_escape"))[0]
                
                salary[1] = salary[0]
                smallbonus[1] = smallbonus[0]
                bigbonus[1] = bigbonus[0]
                if bSTATSHUFFLE_CLASS:
                        salary[1] = random.choice([random.randint(5,50)*10,random.randint(5,50)*10,random.randint(50,250)*10,random.randint(50,250)*10,random.randint(100,500)*10,random.randint(100,1000)*10])
                        smallbonus[1] = random.choice([random.randint(5,15)*10,random.randint(5,15)*10,random.randint(10,50)*10,random.randint(10,50)*10,random.randint(50,100)*10,random.randint(5,200)*10])
                        bigbonus[1] = random.choice([random.randint(5,25)*10,random.randint(5,25)*10,random.randint(10,100)*10,random.randint(10,100)*10,random.randint(50,250)*10,random.randint(5,500)*10])
                salary[1] = int(float(salary[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_CSALARY) * fMULTIPLIER_CLASS)
                smallbonus[1] = int(float(smallbonus[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_CSALARY) * fMULTIPLIER_CLASS)
                bigbonus[1] = int(float(bigbonus[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_CSALARY) * fMULTIPLIER_CLASS)
                
                # Hard-coded check to make sure the Big Bonus is always larger.
                if bigbonus[1] <= int(smallbonus[1] * 1.5):
                        bigbonus[1] = int(smallbonus[1] * 1.5)
                
                # Write data to GAME.PAC
                write_data(struct.pack("<H", int(salary[1])), TABLE_CLASS_SALARY + match.start(5))
                write_data(struct.pack("<H", int(smallbonus[1])), TABLE_CLASS_SALARY + match.start(6))
                write_data(struct.pack("<H", int(bigbonus[1])), TABLE_CLASS_SALARY + match.start(7))
                
                # Write to Output Log
                sOutputLog += "Class ID #" + str(tid) + "\n"
                sOutputLog += "Gender ID #" + str(gid) + "\n"
                sOutputLog += "Salary: " + str(salary) + " G\n"
                sOutputLog += "Potential Salary Bonuses: " + str(smallbonus) + " G, " + str(bigbonus) + " G\n\n"
                
        # Class Capacity Table Output Log
        sOutputLog += "      ========\n"
        sOutputLog += "CLASS CAPACITY TABLE\n"
        sOutputLog += "      ========\n\n"
        
        # Class Capacity Table Search and Edit
        for match in class_capacity_regex.finditer(get_offset_data(TABLE_CLASS_CAPACITY, 0xB0)):
                tid = struct.unpack("<B", bytes(match.group(2), encoding="raw_unicode_escape"))[0]
                gid = struct.unpack("<B", bytes(match.group(3), encoding="raw_unicode_escape"))[0]
                c_items = [0,0]
                c_magic = [0,0]
                c_items[0] = struct.unpack("<B",bytes(match.group(4), encoding="raw_unicode_escape"))[0]
                c_magic[0] = struct.unpack("<B",bytes(match.group(5), encoding="raw_unicode_escape"))[0]
                
                c_items[1] = c_items[0]
                c_magic[1] = c_magic[0]
                if bSTATSHUFFLE_CLASS:
                        c_items[1] = random.randint(1,5)*2
                        c_magic[1] = random.randint(1,5)*2
                c_items[1] = clamp(c_items[1], 2, clamp(c_items[1], int(float(c_items[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_CCAPACITY)), 10))
                c_magic[1] = clamp(c_magic[1], 2, clamp(c_magic[1], int(float(c_magic[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_CCAPACITY)), 10))
                
                # Write data to GAME.PAC
                write_data(struct.pack("<B", c_items[1]), TABLE_CLASS_CAPACITY + match.start(4))
                write_data(struct.pack("<B", c_magic[1]), TABLE_CLASS_CAPACITY + match.start(5))
                
                # Write to Output Log
                sOutputLog += "Class ID #" + str(tid) + "\n"
                sOutputLog += "Gender ID #" + str(gid) + "\n"
                sOutputLog += "Consumable Item Capacity: " + str(c_items) + "\n"
                sOutputLog += "Field Magic Capacity: " + str(c_magic) + "\n\n"
        
        print("Done.")
        
def randomize_monsters():
        print("Randomizing Monsters...")
        # Set up Regular Expression Formulas
        monster_base_regex = re.compile('(?s)(\x50\x00{3})([\x00-\x88])([\x00-\xff])([\x00-\xff])\x00([0-9A-Za-z\+\'\x20\-]+)\x00(\x00{0,3})([\s\S]{2})([\s\S]{2})([\s\S]{2})([\s\S]{2})([\s\S]{2})(\x00\x00[\s\S]{4})([\s\S]{2})([\s\S]{2})')
        
        # Class Base Stats Table Output Log
        global sOutputLog
        sOutputLog += "       ==========\n"
        sOutputLog += "MONSTER BASE STATS TABLE\n"
        sOutputLog += "       ==========\n\n"
        
        # Monster Base Stats Table Search and Edit
        for match in monster_base_regex.finditer(get_offset_data(TABLE_STATS_MONSTER, 0x144C)):
                id = struct.unpack("<B", bytes(match.group(2), encoding="raw_unicode_escape"))[0]
                name = match.group(5)
                # namelen = len(match.group(5)) + len(match.group(6))
                hp = [0,0]
                at = [0,0]
                df = [0,0]
                mg = [0,0]
                spd = [0,0]
                xp = [0,0]
                gold = [0,0]
                hp[0] = struct.unpack("<h",bytes(match.group(7), encoding="raw_unicode_escape"))[0]
                at[0] = struct.unpack("<h",bytes(match.group(8), encoding="raw_unicode_escape"))[0]
                df[0] = struct.unpack("<h",bytes(match.group(9), encoding="raw_unicode_escape"))[0]
                mg[0] = struct.unpack("<h",bytes(match.group(10), encoding="raw_unicode_escape"))[0]
                spd[0] = struct.unpack("<h",bytes(match.group(11), encoding="raw_unicode_escape"))[0]
                xp[0] = struct.unpack("<h",bytes(match.group(13), encoding="raw_unicode_escape"))[0]
                gold[0] = struct.unpack("<h",bytes(match.group(14), encoding="raw_unicode_escape"))[0]
                
                # Monster Randomize
                at[1] = at[0]
                df[1] = df[0]
                mg[1] = mg[0]
                spd[1] = spd[0]
                hp[1] = hp[0]
                xp[1] = xp[0]
                gold[1] = gold[0]
                if bSTATSHUFFLE_MONSTER:
                        if at[0] > 0:
                                at[1] = random.choice([random.randint(1,10),random.randint(1,10),random.randint(10,50),random.randint(10,50),random.randint(50,100),random.randint(50,300)])
                        if df[0] > 0:
                                df[1] = random.choice([random.randint(1,10),random.randint(1,10),random.randint(10,50),random.randint(10,50),random.randint(50,100),random.randint(50,300)])
                        if mg[0] > 0:
                                mg[1] = random.choice([random.randint(1,10),random.randint(1,10),random.randint(10,50),random.randint(10,50),random.randint(50,100),random.randint(50,300)])
                        if spd[0] > 0:
                                spd[1] = random.choice([random.randint(1,10),random.randint(1,10),random.randint(10,50),random.randint(10,50),random.randint(50,100),random.randint(50,300)])
                        if hp[0] > 0:
                                hp[1] = random.choice([random.randint(10,100),random.randint(10,100),random.randint(100,1000),random.randint(100,1000),random.randint(200,2000),random.randint(330,3300)])
                        xp[1] = random.choice([random.randint(0,50),random.randint(0,50),random.randint(50,500),random.randint(50,500),random.randint(500,5000),random.randint(500,50000)])
                        gold[1] = random.choice([random.randint(-50,500),random.randint(-50,500),random.randint(-500,5000),random.randint(-500,5000),random.randint(-1000,10000),random.randint(-1000,10000)])
                if at[0] > 0:
                        at[1] = int(float(at[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_MONBASE) * fMULTIPLIER_MONSTER)
                        at[1] = clamp(at[1], 0, 999)
                if df[0] > 0:
                        df[1] = int(float(df[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_MONBASE) * fMULTIPLIER_MONSTER)
                        df[1] = clamp(df[1], 0, 999)
                if mg[0] > 0:
                        mg[1] = int(float(mg[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_MONBASE) * fMULTIPLIER_MONSTER)
                        mg[1] = clamp(mg[1], 0, 999)
                if spd[0] > 0:
                        spd[1] = int(float(spd[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_MONBASE) * fMULTIPLIER_MONSTER)
                        spd[1] = clamp(spd[1], 0, 999)
                if hp[0] > 0:
                        hp[1] = int(float(hp[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_MONBASE) * fMULTIPLIER_MONSTER)
                        hp[1] = clamp(hp[1], 0, 9999)
                xp[1] = min(30000, max(-30000, int(float(xp[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_MONBASE) * fMULTIPLIER_MONSTER)))
                gold[1] = min(30000, max(-30000, int(float(gold[1]) * float(1 + float(random.randint(-100,100))/100 * fSTRENGTH_MONBASE) * fMULTIPLIER_MONSTER)))
                
                # Write data to GAME.PAC
                write_data(struct.pack("<h", hp[1]), TABLE_STATS_MONSTER + match.start(7))
                write_data(struct.pack("<h", at[1]), TABLE_STATS_MONSTER + match.start(8))
                write_data(struct.pack("<h", df[1]), TABLE_STATS_MONSTER + match.start(9))
                write_data(struct.pack("<h", mg[1]), TABLE_STATS_MONSTER + match.start(10))
                write_data(struct.pack("<h", spd[1]), TABLE_STATS_MONSTER + match.start(11))
                write_data(struct.pack("<h", xp[1]), TABLE_STATS_MONSTER + match.start(13))
                write_data(struct.pack("<h", gold[1]), TABLE_STATS_MONSTER + match.start(14))
                
                # Write to Output Log
                sOutputLog += "Monster ID #" + str(id) + "\n"
                sOutputLog += "Name: " + name + "\n"
                sOutputLog += "Stats: " + str(at) + " ATK / " + str(df) + " DEF / " + str(mg) + " MAG / " + str(spd) + " SPD / " + str(hp) + " HP\n"
                sOutputLog += "Experience: " + str(xp) + "\n"
                sOutputLog += "Gold: " + str(gold) + "\n\n"
        
        print("Done.")
        
def randomize_shops():
        print("Randomizing Shops...")
        # Set up Regular Expression Formulas
        shop_equips_regex = re.compile('(?s)([\x01-\x43]{1,10})\x00([\x01-\x28]{1,10})\x00')
        shop_consume_regex = re.compile('(?s)([\x01-\x31]{8,9}?)[\x00]')
        shop_magic_regex = re.compile('(?s)([\x38-\]]{8})\x00([\x01-\x17]{4})\x00([\x1f-\x30]{4})\x00')
        
        # Weapon Shop Table Output Log
        global sOutputLog
        sOutputLog += "    =========\n"
        sOutputLog += "WEAPON SHOP TABLE\n"
        sOutputLog += "    =========\n\n"
        
        # Weapon Shop Table Search and Edit
        for match in shop_equips_regex.finditer(get_offset_data(TABLE_SHOP_EQUIP, 0x70)):
                # Weapons
                old_wids = list()
                new_wids = list()
                for i in range(len(match.group(1))):
                        old_wids.append(struct.unpack("<B", bytes(match.group(1)[i], encoding="raw_unicode_escape"))[0])
                        id = 1
                        if bEXPLOITS:
                                id = random.randint(1, 67)
                        else:
                                id = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0xa, 0xb, 0xc, 0xd, 0xe, 0xf, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f, 0x20, 0x21, 0x22, 0x24, 0x26, 0x27, 0x28, 0x2a, 0x2b, 0x2c, 0x2d, 0x2e, 0x2f, 0x30, 0x31, 0x32, 0x33, 0x34, 0x36, 0x39, 0x3c, ])
                        new_wids.append(id)
                        
                        # Write data to GAME.PAC
                        write_data(struct.pack("<B", new_wids[i]), TABLE_SHOP_EQUIP + match.start() + i)
                        
                        # Write to Output Log
                        sOutputLog += "Weapon ID Change: " + str(old_wids[i]) + " -> " + str(new_wids[i]) + "\n"
                
                sOutputLog += "\n"
                
                # Shields
                old_sids = list()
                new_sids = list()
                for i in range(len(match.group(2))):
                        old_sids.append(struct.unpack("<B", bytes(match.group(2)[i], encoding="raw_unicode_escape"))[0])
                        id = 1
                        if bEXPLOITS:
                                id = random.randint(1, 40)
                        else:
                                id = random.choice([1,2,3,4,5,6,7,8,9,0xa,0xb,0xc,0xd,0xe,0xf,0x10,0x11,0x12,0x13,0x14,0x15,0x16,0x17,0x18,0x19,0x1a,0x1b,0x1c,0x1d,0x1e,0x1f,0x21,0x22,0x23,0x24,0x25])
                        new_sids.append(id)
                        
                        # Write data to GAME.PAC
                        write_data(struct.pack("<B", new_sids[i]), TABLE_SHOP_EQUIP + 1 + len(old_wids) + match.start() + i)
                        
                        # Write to Output Log
                        sOutputLog += "Shield ID Change: " + str(old_sids[i]) + " -> " + str(new_sids[i]) + "\n"
                        
                sOutputLog += "\n"
        
        # Item Shop Table Output Log
        sOutputLog += "    =======\n"
        sOutputLog += "ITEM SHOP TABLE\n"
        sOutputLog += "    =======\n\n"
        
        # Item Shop Table Search and Edit
        matchcount = 0
        forced = [0x8, 0x14, 0x1C, 0x1E, 0x20, 0x24, 0x27, 0x28] # Chapter 3 Fix
        for match in shop_consume_regex.finditer(get_offset_data(TABLE_SHOP_CONSUME, 0x76)):
                matchcount += 1
                # Consumable Items
                old_cids = list()
                new_cids = list()
                for i in range(len(match.group(1))):
                        old_cids.append(struct.unpack("<B", bytes(match.group(1)[i], encoding="raw_unicode_escape"))[0])
                        id = 1
                        if (matchcount <= 6 and i == 0) or (matchcount >= 5 and matchcount <= 6 and i == 1): # Each store open during Chapter 3 gets at least 1 potential Progress Item for Chapter 3
                            id = random.choice(forced)
                            forced.remove(id)
                        elif bEXPLOITS:
                                id = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0xa, 0xb, 0xd, 0xe, 0xf, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x17, 0x18, 0x19, 0x1a, 0x1c, 0x1d, 0x1e, 0x1f, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2a, 0x2b, 0x2c, 0x2d, 0x2e, 0x2f, 0x30, 0x31])
                        else:
                                id = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0xa, 0xb, 0xd, 0xe, 0xf, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x17, 0x18, 0x19, 0x1a, 0x1c, 0x1d, 0x1e, 0x1f, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2a, 0x2b, 0x2c, 0x2e])
                        new_cids.append(id)
                        
                        # Write data to GAME.PAC
                        write_data(struct.pack("<B", new_cids[i]), TABLE_SHOP_CONSUME + match.start() + i)
                        
                        # Write to Output Log
                        sOutputLog += "Consume ID Change: " + str(old_cids[i]) + " -> " + str(new_cids[i]) + "\n"
                
                sOutputLog += "\n"
        
        # Magic Shop Table Output Log
        sOutputLog += "    ========\n"
        sOutputLog += "MAGIC SHOP TABLE\n"
        sOutputLog += "    ========\n\n"
        
        # Magic Shop Table Search and Edit
        for match in shop_magic_regex.finditer(get_offset_data(TABLE_SHOP_MAGIC, 0xBE)):
                # Field Magic
                old_fids = list()
                new_fids = list()
                for i in range(len(match.group(1))):
                        old_fids.append(struct.unpack("<B", bytes(match.group(1)[i], encoding="raw_unicode_escape"))[0])
                        new_fids.append(random.randint(0x38,0x5d))
                        
                        # Write data to GAME.PAC
                        write_data(struct.pack("<B", new_fids[i]), TABLE_SHOP_MAGIC + match.start() + i)
                        
                        # Write to Output Log
                        sOutputLog += "Field Magic ID Change: " + str(old_fids[i]) + " -> " + str(new_fids[i]) + "\n"
                        
                sOutputLog += "\n"
                
                # Attack Magic
                old_atids = list()
                new_atids = list()
                for i in range(len(match.group(2))):
                        old_atids.append(struct.unpack("<B", bytes(match.group(2)[i], encoding="raw_unicode_escape"))[0])
                        new_atids.append(random.randint(0x1,0x17))
                        
                        # Write data to GAME.PAC
                        write_data(struct.pack("<B", new_atids[i]), TABLE_SHOP_MAGIC + match.start() + i + len(old_fids) + 1)
                        
                        # Write to Output Log
                        sOutputLog += "Offense Magic ID Change: " + str(old_atids[i]) + " -> " + str(new_atids[i]) + "\n"
                        
                sOutputLog += "\n"
                        
                # Defense Magic
                old_dfids = list()
                new_dfids = list()
                for i in range(len(match.group(3))):
                        old_dfids.append(struct.unpack("<B", bytes(match.group(3)[i], encoding="raw_unicode_escape"))[0])
                        new_dfids.append(random.randint(0x1F,0x30))
                        
                        # Write data to GAME.PAC
                        write_data(struct.pack("<B", new_dfids[i]), TABLE_SHOP_MAGIC + match.start() + i + len(old_fids) + len(old_atids) + 2)
                        
                        # Write to Output Log
                        sOutputLog += "Defense Magic ID Change: " + str(old_dfids[i]) + " -> " + str(new_dfids[i]) + "\n"
                        
                sOutputLog += "\n"
        
        print("Done.")
        
def randomize_drops():
        print("Randomizing Drops...")
        # Set up Regular Expression Formulas
        drop_spaces_regex = re.compile(r'(?s)([\x04-\x42])\x00([\x06\x08\x0A])\x00(([\s\S][\x01-\x08\x80-\x87])+)')
        drop_monsters_regex = re.compile(r'(?s)(\x53\x00\x00\x00)([\x00-\x88])([\x00-\x64]{2})\x00([\s\S]{4})')
        
        # Loot Space Drop Table Output Log
        global sOutputLog
        sOutputLog += "      =========\n"
        sOutputLog += "LOOT SPACE DROP TABLE\n"
        sOutputLog += "      =========\n\n"
        
        # Loot Space Drop Table Search and Edit
        for match in drop_spaces_regex.finditer(get_offset_data(TABLE_DROPS_SPACES, 0x134C)):
                # Loot Space Drops
                old_spaceids = list()
                old_spacetbls = list()
                new_spaceids = list()
                new_spacetbls = list()
                for i in range(0, len(match.group(3)), 2):
                        old_spaceids.append(struct.unpack("<B", bytes(match.group(3)[i], encoding="raw_unicode_escape"))[0])
                        old_spacetbls.append(struct.unpack("<B", bytes(match.group(3)[i+1], encoding="raw_unicode_escape"))[0])
                        tbl = 0
                        if bEXPLOITS:
                                tbl = random.choice([1,1,2,2,3,3,5,5,5,5,6,6,7,7,8,8,8,8,0x80,0x80,0x80,0x80,0x81,0x81,0x81,0x81,0x82,0x82,0x82,0x82,0x83,0x84,0x84,0x85,0x85,0x86,0x86,0x87,0x87,0x87,0x87])
                        else:
                                tbl = old_spacetbls[len(old_spacetbls)-1]
                        new_spaceids.append(get_random_item(tbl))
                        new_spacetbls.append(tbl)
                        
                        # Write data to GAME.PAC
                        write_data(struct.pack("<BB", new_spaceids[len(new_spaceids)-1], new_spacetbls[len(new_spacetbls)-1]), TABLE_DROPS_SPACES + 4 + match.start() + i)
                        
                        # Write to Output Log
                        sOutputLog += "Loot ID Change: " + str([old_spaceids[len(old_spaceids)-1], old_spacetbls[len(old_spacetbls)-1]]) + " -> " + str([new_spaceids[len(new_spaceids)-1], new_spacetbls[len(new_spacetbls)-1]]) + "\n"
                        
                sOutputLog += "\n"
                
        # Monster Drop Table Output Log
        sOutputLog += "     ========\n"
        sOutputLog += "MONSTER DROP TABLE\n"
        sOutputLog += "     ========\n\n"
        
        # Loot Space Drop Table Search and Edit
        for match in drop_monsters_regex.finditer(get_offset_data(TABLE_DROPS_MONSTERS, 0x66C)):
                sOutputLog += "Monster ID #" + str(struct.unpack("<B", bytes(match.group(2), encoding="raw_unicode_escape"))[0]) + "\n"
                
                # Monster Drops
                dropchances = [struct.unpack("<B", bytes(match.group(3)[0], encoding="raw_unicode_escape"))[0],struct.unpack("<B", bytes(match.group(3)[1], encoding="raw_unicode_escape"))[0]]
                newchances = [random.randint(0,20)*5,random.randint(0,20)*5]
                # Fix for 0% Drop Rate items
                if dropchances[0] == 0:
                    newchances[0] = 0
                if dropchances[1] == 0:
                    newchances[1] = 0
                old_spaceids = list()
                old_spacetbls = list()
                new_spaceids = list()
                new_spacetbls = list()
                for i in range(0, len(match.group(4)), 2):
                        old_spaceids.append(struct.unpack("<B", bytes(match.group(4)[i], encoding="raw_unicode_escape"))[0])
                        old_spacetbls.append(struct.unpack("<B", bytes(match.group(4)[i+1], encoding="raw_unicode_escape"))[0])
                        tbl = old_spacetbls[len(old_spacetbls)-1]
                        new_spaceids.append(get_random_item(tbl))
                        new_spacetbls.append(tbl)
                        
                        # Check for appropriate table rewrite
                        if (new_spacetbls[len(new_spacetbls)-1] > 0 and new_spacetbls[len(new_spacetbls)-1] < 9) or (new_spacetbls[len(new_spacetbls)-1] > 0x7f and new_spacetbls[len(new_spacetbls)-1] < 0x88):
                                # Royal Ring Fix
                                if old_spaceids[len(old_spaceids)-1] == 0x37 and old_spacetbls[len(old_spacetbls)-1] == 0x05:
                                    newchances[int(i/2)] = 100
                                    new_spacetbls[len(new_spacetbls)-1] = 0x05
                                    new_spaceids[len(new_spaceids)-1] = 0x37
                                # Write data to GAME.PAC
                                write_data(struct.pack("<BB", new_spaceids[len(new_spaceids)-1], new_spacetbls[len(new_spacetbls)-1]), TABLE_DROPS_MONSTERS + match.start(4) + i)
                                # Write to Output Log
                                sOutputLog += "Loot ID Change: " + str([old_spaceids[len(old_spaceids)-1], old_spacetbls[len(old_spacetbls)-1]]) + " -> " + str([new_spaceids[len(new_spaceids)-1], new_spacetbls[len(new_spacetbls)-1]]) + "\n"
                        else:
                                newchances[int(i/2)] = 0

                # Write data to GAME.PAC
                if newchances[0] > 0 or newchances[1] > 0:
                        write_data(struct.pack("<BB", newchances[0], newchances[1]), TABLE_DROPS_MONSTERS + match.start(3))
                        
                        # Write to Output Log
                        sOutputLog += "Drop Chances: " + str(dropchances) + " -> " + str(newchances) + "\n\n"
        
        print("Done.")
        
def get_random_item(table_id):
        id = 0
        # Weapons
        if table_id == 0x1:
                id = random.randint(0x1, 0x43)
        # Shields
        elif table_id == 0x2:
                id = random.randint(0x1, 0x28)
        # Accessories
        elif table_id == 0x3:
                id = random.randint(0x1, 0x21)
        # Consumables
        elif table_id == 0x5:
                id = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0xa, 0xb, 0xd, 0xe, 0xf, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x17, 0x18, 0x19, 0x1a, 0x1c, 0x1d, 0x1e, 0x1f, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2a, 0x2b, 0x2c, 0x2e])
        # Attack Magic
        elif table_id == 0x6:
                id = random.randint(0x1, 0x17)
        # Defense Magic
        elif table_id == 0x7:
                id = random.randint(0x1, 0x13)
        # Field Magic
        elif table_id == 0x8:
                id = random.randint(0x1, 0x26)
        # Gain Money Effect
        elif table_id == 0x80:
                id = random.randint(0, 0x13)
        # Lose HP Effect
        elif table_id == 0x81:
                id = random.randint(0, 0x6)
        # Gain Status Effect
        elif table_id == 0x82:
                id = random.randint(0, 0x9)
        # Random Warp Effect
        elif table_id == 0x83:
                id = 0
        # Bankrupt Effect
        elif table_id == 0x84:
                id = 0
        # Lose Random Consumable Items Effect
        elif table_id == 0x85:
                id = random.randint(0, 0x2)
        # Lose Random Field Magic Effect
        elif table_id == 0x86:
                id = random.randint(0, 0x2)
        # Lose Money Effect
        elif table_id == 0x87:
                id = random.randint(0, 0x8)
        return id

def main(pacfile_path):
        # Game.pac Data
        global DATA_BASE
        DATA_BASE = list(open(pacfile_path, 'rb').read())
        
        # Variables
        global bRANDOM_EQUIP
        global bSTATSHUFFLE_EQUIP
        global fMULTIPLIER_EQUIP
        global fSTRENGTH_EQATTACK
        global fSTRENGTH_EQDEFENSE
        global fSTRENGTH_EQMISC
        global bRANDOM_MAGIC
        global bSTATSHUFFLE_MAGIC
        global fMULTIPLIER_MAGIC
        global fSTRENGTH_MGATTACK
        global fSTRENGTH_MGDEFENSE
        global fSTRENGTH_MGFIELD
        global bRANDOM_CLASS
        global bSTATSHUFFLE_CLASS
        global fMULTIPLIER_CLASS
        global fSTRENGTH_CBASE
        global fSTRENGTH_CLEVELUP
        global fSTRENGTH_CSALARY
        global fSTRENGTH_CCAPACITY
        global bRANDOM_MONSTER
        global bSTATSHUFFLE_MONSTER
        global fMULTIPLIER_MONSTER
        global fSTRENGTH_MONBASE
        global bRANDOM_SHOPS
        global bRANDOM_DROPS
        global bRANDOM_PRICES
        global bRANDOM_CONSUME
        global bSTATSHUFFLE_CONSUME
        global bEXPLOITS
        global fSTRENGTH_VALUES
        global iMINIMUM_VALUE
        global sSEED
        global bOUTPUTLOG
        global sOutputLog
        
        # Set the rest of the variables.
        bRANDOM_EQUIP = bool(int(input("Allow Randomized Equipment? [0-1]> ")) % 2)
        bSTATSHUFFLE_EQUIP = False
        if bRANDOM_EQUIP:
                bSTATSHUFFLE_EQUIP = bool(int(input("Allow SERIOUSLY RANDOMIZED Equipment? [0-1]> ")) % 2)
                fMULTIPLIER_EQUIP = float(input("Equipment Strength Multiplier [0.05-2.00]> "))
                fSTRENGTH_EQATTACK = float(input("Weapon Strength Variance [0.0-1.00]> "))
                fSTRENGTH_EQDEFENSE = float(input("Shield Strength Variance [0.0-1.00]> "))
                fSTRENGTH_EQMISC = float(input("Accessory Strength Variance [0.0-1.00]> "))
        
        bRANDOM_MAGIC = bool(int(input("Allow Randomized Magic? [0-1]> ")) % 2)
        bSTATSHUFFLE_MAGIC = False
        if bRANDOM_MAGIC:
                bSTATSHUFFLE_MAGIC = bool(int(input("Allow SERIOUSLY RANDOMIZED Magic? [0-1]> ")) % 2)
                fMULTIPLIER_MAGIC = float(input("Magic Strength Multiplier [0.05-2.00]> "))
                fSTRENGTH_MGATTACK = float(input("Offense Magic Strength Variance [0.0-1.00]> "))
                fSTRENGTH_MGDEFENSE = float(input("Defense Magic Strength Variance [0.0-1.00]> "))
                fSTRENGTH_MGFIELD = float(input("Field Magic Strength Variance [0.0-1.00]> "))
        
        bRANDOM_CLASS = bool(int(input("Allow Randomized Class Data? [0-1]> ")) % 2)
        bSTATSHUFFLE_CLASS = False
        if bRANDOM_CLASS:
                bSTATSHUFFLE_CLASS = bool(int(input("Allow SERIOUSLY RANDOMIZED Classes? [0-1]> ")) % 2)
                fMULTIPLIER_CLASS = float(input("Class Strength Multiplier [0.25-3.00] (NOTE: Does not affect Inventory Capacity)> "))
                fSTRENGTH_CBASE = float(input("Class Base Stats Strength Variance [0.0-1.00]> "))
                fSTRENGTH_CLEVELUP = float(input("Class Level Up Bonus Strength Variance [0.0-1.00]> "))
                fSTRENGTH_CSALARY = float(input("Class Salary Strength Variance [0.0-1.00]> "))
                fSTRENGTH_CCAPACITY = float(input("Class Inventory Capacity Strength Variance [0.0-1.00]> "))
        
        bRANDOM_MONSTER = bool(int(input("Allow Randomized Monsters? [0-1]> ")) % 2)
        bSTATSHUFFLE_MONSTER = False
        if bRANDOM_MONSTER:
                bSTATSHUFFLE_MONSTER = bool(int(input("Allow SERIOUSLY RANDOMIZED Monsters? [0-1]> ")) % 2)
                fMULTIPLIER_MONSTER = float(input("Monster Strength Multiplier [0.25-3.00]> "))
                fSTRENGTH_MONBASE = float(input("Monster Base Stats Strength Variance [0.0-1.00]> "))
        
        bRANDOM_CONSUME = bool(int(input("Allow Randomized Consumables? [0-1]> ")) % 2)
        bRANDOM_SHOPS = bool(int(input("Allow Randomized Shops? [0-1]> ")) % 2)
        bRANDOM_DROPS = bool(int(input("Allow Randomized Drops? [0-1]> ")) % 2)
        
        bRANDOM_PRICES = bool(int(input("Allow Randomized Prices? [0-1]> ")) % 2)
        bSTATSHUFFLE_CONSUME = False
        if bRANDOM_PRICES:
                iMINIMUM_VALUE = int(input("Price Minimum Value [2-1000]> "))
                fSTRENGTH_VALUES = float(input("Price Strength Variance [0.0-1.00]> "))
                if bRANDOM_CONSUME:
                        bSTATSHUFFLE_CONSUME = bool(int(input("Allow SERIOUSLY RANDOMIZED Consumable Item Prices? [0-1]> ")))
        
        bEXPLOITS = bool(int(input("Allow Exploits? [0-1] (Not Recommended for serious play)> ")) % 2)
        
        sSEED = str(input("Input Seed (or leave blank to generate one)> "))
        bOUTPUTLOG = bool(int(input("Save Output Log? [0-1]> ")) % 2)
        
        # Random Seed
        if len(sSEED) < 1:
                import time
                sSEED = str(time.time())
        random.seed(sSEED)
        
        # Write Output log data
        sOutputLog = "#########################################\n"
        sOutputLog += "# DOKAPON KINGDOM RANDOMIZED\n"
        sOutputLog += "# Randomized Equipment: " + str(bRANDOM_EQUIP) + "\n"
        sOutputLog += "# Randomized Magic: " + str(bRANDOM_MAGIC) + "\n"
        sOutputLog += "# Randomized Classes: " + str(bRANDOM_CLASS) + "\n"
        sOutputLog += "# Randomized Monsters: " + str(bRANDOM_MONSTER) + "\n"
        sOutputLog += "# Randomized Consumables: " + str(bRANDOM_CONSUME) + "\n"
        sOutputLog += "# Randomized Shops: " + str(bRANDOM_SHOPS) + "\n"
        sOutputLog += "# Randomized Drops: " + str(bRANDOM_DROPS) + "\n"
        sOutputLog += "# Randomized Prices: " + str(bRANDOM_PRICES) + "\n\n"
        sOutputLog += "# Seriously Randomized Equipment: " + str(bSTATSHUFFLE_EQUIP) + "\n"
        sOutputLog += "# Seriously Randomized Magic: " + str(bSTATSHUFFLE_MAGIC) + "\n"
        sOutputLog += "# Seriously Randomized Classes: " + str(bSTATSHUFFLE_CLASS) + "\n"
        sOutputLog += "# Seriously Randomized Monsters: " + str(bSTATSHUFFLE_MONSTER) + "\n"
        sOutputLog += "# Seriously Randomized Consumable Prices: " + str(bSTATSHUFFLE_CONSUME) + "\n\n"
        sOutputLog += "# Seed: " + sSEED + "\n"
        sOutputLog += "#########################################\n\n"
        
        # Adjust Floats and Integers and output to Log file
        if bRANDOM_PRICES:
                sOutputLog += "|------------------>\n"
                sOutputLog += "| PRICE SETTINGS  <\n"
                sOutputLog += "|------------------>\n"
                fSTRENGTH_VALUES = clamp(fSTRENGTH_VALUES, 0.00, 1.0)
                iMINIMUM_VALUE = clamp(iMINIMUM_VALUE, 2, 1000)
                sOutputLog += "Price Variance: " + str(fSTRENGTH_VALUES) + "\n"
                sOutputLog += "Minimum Price: " + str(iMINIMUM_VALUE) + "\n\n"
        if bRANDOM_EQUIP:
                sOutputLog += "|---------------------->\n"
                sOutputLog += "| EQUIPMENT SETTINGS  <\n"
                sOutputLog += "|---------------------->\n"
                fMULTIPLIER_EQUIP = clamp(fMULTIPLIER_EQUIP, 0.05, 2.0)
                fSTRENGTH_EQATTACK = clamp(fSTRENGTH_EQATTACK, 0.0, 1.0)
                fSTRENGTH_EQDEFENSE = clamp(fSTRENGTH_EQDEFENSE, 0.0, 1.0)
                fSTRENGTH_EQMISC = clamp(fSTRENGTH_EQMISC, 0.0, 1.0)
                sOutputLog += "Equipment Strength Multiplier: " + str(fMULTIPLIER_EQUIP) + "\n"
                sOutputLog += "Weapon Strength Variance: " + str(fSTRENGTH_EQATTACK) + "\n"
                sOutputLog += "Shield Strength Variance: " + str(fSTRENGTH_EQDEFENSE) + "\n"
                sOutputLog += "Accessory Strength Variance: " + str(fSTRENGTH_EQMISC) + "\n\n"
        if bRANDOM_MAGIC:
                sOutputLog += "|------------------>\n"
                sOutputLog += "| MAGIC SETTINGS  <\n"
                sOutputLog += "|------------------>\n"
                fMULTIPLIER_MAGIC = clamp(fMULTIPLIER_MAGIC, 0.05, 2.0)
                fSTRENGTH_MGATTACK = clamp(fSTRENGTH_MGATTACK, 0.0, 1.0)
                fSTRENGTH_MGDEFENSE = clamp(fSTRENGTH_MGDEFENSE, 0.0, 1.0)
                fSTRENGTH_MGFIELD = clamp(fSTRENGTH_MGFIELD, 0.0, 1.0)
                sOutputLog += "Magic Strength Multiplier: " + str(fMULTIPLIER_MAGIC) + "\n"
                sOutputLog += "Offensive Magic Strength Variance: " + str(fSTRENGTH_MGATTACK) + "\n"
                sOutputLog += "Defensive Magic Strength Variance: " + str(fSTRENGTH_MGDEFENSE) + "\n"
                sOutputLog += "Field Magic Strength Variance: " + str(fSTRENGTH_MGFIELD) + "\n\n"
        if bRANDOM_CLASS:
                sOutputLog += "|------------------>\n"
                sOutputLog += "| CLASS SETTINGS  <\n"
                sOutputLog += "|------------------>\n"
                fMULTIPLIER_CLASS = clamp(fMULTIPLIER_CLASS, 0.25, 3.0)
                fSTRENGTH_CBASE = clamp(fSTRENGTH_CBASE, 0.0, 1.0)
                fSTRENGTH_CLEVELUP = clamp(fSTRENGTH_CLEVELUP, 0.0, 1.0)
                fSTRENGTH_CSALARY = clamp(fSTRENGTH_CLEVELUP, 0.0, 1.0)
                fSTRENGTH_CCAPACITY = clamp(fSTRENGTH_CLEVELUP, 0.0, 1.0)
                sOutputLog += "Class Strength Multiplier: " + str(fMULTIPLIER_CLASS) + "\n"
                sOutputLog += "Class Base Stats Strength Variance: " + str(fSTRENGTH_CBASE) + "\n"
                sOutputLog += "Class Level Up Bonus Strength Variance: " + str(fSTRENGTH_CLEVELUP) + "\n"
                sOutputLog += "Class Salary Strength Variance: " + str(fSTRENGTH_CSALARY) + "\n"
                sOutputLog += "Class Inventory Capacity Strength Variance: " + str(fSTRENGTH_CCAPACITY) + "\n\n"
        if bRANDOM_MONSTER:
                sOutputLog += "|-------------------->\n"
                sOutputLog += "| MONSTER SETTINGS  <\n"
                sOutputLog += "|-------------------->\n"
                fMULTIPLIER_MONSTER = clamp(fMULTIPLIER_MONSTER, 0.25, 3.0)
                fSTRENGTH_MONBASE = clamp(fSTRENGTH_MONBASE, 0.0, 1.0)
                sOutputLog += "Monster Strength Multiplier: " + str(fMULTIPLIER_MONSTER) + "\n"
                sOutputLog += "Monster Base Stats Strength Variance: " + str(fSTRENGTH_MONBASE) + "\n\n"
        
        # Randomize Everything
        if bRANDOM_EQUIP:
                randomize_equipment()
        if bRANDOM_MAGIC:
                randomize_magic()
        if bRANDOM_CLASS:
                randomize_classes()
        if bRANDOM_MONSTER:
                randomize_monsters()
        if bRANDOM_SHOPS:
                randomize_shops()
        if bRANDOM_DROPS:
                randomize_drops()
        if bRANDOM_CONSUME:
                randomize_consumables()
        
        # Write to file
        print("Writing to GAME.PAC...")
        open(pacfile_path, 'wb').write(bytes(''.join((chr(x) for x in DATA_BASE)),encoding="raw_unicode_escape"))
        print("Done.")
        
        # Save Output Log if enabled
        if bOUTPUTLOG:
                print("Writing to output log...")
                open("DokaponKingdomWii_" + sSEED + ".txt", 'w').write(sOutputLog)
                print("Done.")

if __name__ == '__main__':
        print(" --------------------------------------- ")
        print("Dokapon Kingdom Wii Randomizer by X Kirby")
        print(" --------------------------------------- \n")
        while True:
                path = str(input("Type in path to game.pac file (or leave blank for 'GAME.PAC'). This will take a while to load.> "))
                if len(path) < 1:
                        path = "GAME.PAC"
                # Ask to make a backup first, just in case.
                bMAKE_BACKUP = bool(int(input("Make a backup of the .pac file? [0-1] (Recommended if you haven't yet)> ")) % 2)
                if bMAKE_BACKUP:
                        print("Making backup, this might take a while...")
                        open(path + ".backup", 'wb').write(bytes(''.join((chr(x) for x in list(open(path, 'rb').read()))),encoding="raw_unicode_escape"))
                        print("Done.")
                main(path)
