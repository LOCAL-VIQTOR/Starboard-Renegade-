import random
from SRtools import *
from SRplanets import *

#    __________  __________________  ________
#   / ____/ __ \/ ____/  _/ ____/ / / /_  __/
#  / /_  / /_/ / __/  / // / __/ /_/ / / /
# / __/ / _, _/ /____/ // /_/ / __  / / /
# /_/   /_/ |_/_____/___/\____/_/ /_/ /_/
# FREIGHT & TRADE GOODS CLASS & FUNCTIONS

class trade_goods():
    def __init__(self, ref, name, avail, tons, mult, price, p_dm, s_dm):
        self.reference = ref
        self.name = name
        self.availability = avail
        self.tons_dice = tons
        self.tons_mult = mult
        self.base_price = price
        self.p_dm = p_dm
        self.s_dm = s_dm
        self.tons = 0
        self.p_price = 0
        self.s_price = 0
        self.desc = 'GoodsDescErr'

    def determine_stock(self,troubleshooting=False):
        if troubleshooting:
            print('determine_stock() Troubleshooting: '+self.name)
            print('Current Stock: '+str(self.tons)+' t.')
        add_tons = 0
        for i in range(self.tons_dice):
            add_tons += random.randint(1, 6)
        add_tons = add_tons * self.tons_mult
        if troubleshooting: 
            print('Calculated tons to add: ' + str(add_tons))
        self.tons += add_tons
        if troubleshooting: print('New tonnage of '+self.name+': '+str(self.tons))
        if troubleshooting: print()

    def determine_purchase_price(self, result, trade_code,troubleshooting=False):
        mod = 1
        for i in range(len(self.p_dm)):
            if self.p_dm[i][0] in trade_code: result += self.p_dm[i][1]
        for i in range(len(self.s_dm)):
            if self.s_dm[i][0] in trade_code: result -= self.s_dm[i][1]
        if result < -1: result = -1
        if result >= 21: result = 21
        purchase_modifier = {-1:4,0:3,1:2,2:1.75,3:1.5,4:1.35,5:1.25,6:1.2,7:1.15,8:1.1,9:1.05,10:1,11:0.95,
                             12:0.9,13:0.85,14:0.8,15:0.75,16:0.7,17:0.65,18:0.55,19:0.5,20:0.4,21:0.25}
        mod = purchase_modifier[result]
        self.p_price = int(round(self.base_price * mod, 2))
        if troubleshooting: print(self.name+' | Sale Price: '+str(self.base_price)+', Purchase Modifier: '+str(mod)+'x, Purchase Price: '+str(self.p_price)+' Cr.')

    def info(self):
        print(str(self.tons) + 't. | ' + self.name + ' | ' + str(self.p_price) + ' Cr. | ' + self.desc)


def planetary_goods(basic_items, all_items, planet, troubleshooting=False):
    if troubleshooting:
        print('planetary_goods() Troubleshooting: '+planet.name)
        print('basic_items = '+str(len(basic_items))+', all_items = '+str(len(all_items)))
        print('Goods Added:')
    available_goods = basic_items                                   # Gives every planet the basic goods.
    for i in range(len(all_items)):                                 # For every inventory option there is...
        if all_items[i].availability != 'any':                      # If the item wasn't already included in the basic package...
            for n in range(len(all_items[i].availability)):         # For each item in the inventory's 'availability' tag
                if all_items[i].availability[n] in planet.codes:    # If the item is available on the current planet...
                    if all_items[i] not in available_goods:         # And it's not already in the available goods list...
                        available_goods.append(all_items[i])        # Then put it on the available goods list!
                        if troubleshooting: print('- '+all_items[i].name)
    if troubleshooting: print()
    return available_goods



def extra_goods(all_goods, available_goods,black_market=False,troubleshooting=False):  
    # add implementation for illegal sellers . . . and designed inventory per making your own planet
    extra_goods = random.randint(1, 6)  # Pick 1D6 extra goods to have available
    if troubleshooting: 
         print('extra_goods() Troubleshooting:')
         print('all_goods = '+str(len(all_goods))+', available_goods = '+str(len(available_goods))+', extra_goods = '+str(extra_goods))
         print('Added Freight:')
    for i in range(extra_goods):    # For the number of extra items picked...
        extra = random.choice(all_goods)    # Pick an item from the full options list
        if extra not in available_goods:    # If it's not already in the available goods list...
            available_goods.append(extra)   # Put it on the available goods list!
            if troubleshooting: print('- NEW: '+extra.name)
        else:    # If it is in the available goods list...
            for i in range(len(available_goods)):   # For each item the planet already has...
                if available_goods[i].name == extra.name:   # If that stock is concurrent to the added stock...
                    extra_stock = available_goods[i].tons   # Set a baseline of the
                    for n in range(extra.tons_dice):    # Roll basic stock inventory
                        extra_stock += random.randint(1, 6)
                    extra_stock *= extra.tons_mult
                    available_goods[i].tons += extra_stock  # Add that stock to the inventory's tonnage'
                    if troubleshooting: print('- '+extra.name+' '+str(extra_stock)+' t.')
    if troubleshooting: print()


# Removes empty freight from a planet's list
def removeEmptyFreight(planet,troubleshooting=False):
    removeList = []                             # Creates a list of freight to remove
    for i in range(len(planet.goods)):          # Adds the freight to the list if tons is 0
        if planet.goods[i].tons == 0:
            removeList.append(planet.goods[i])  #append.removeList(i)
    if troubleshooting: 
        removed_string = ''
        for good in removeList:
            removed_string = removed_string + good.name + ', '
        print(planet.name + ' removeEmptyFreight() | List of Removed Goods: ' + removed_string)
        print()
    for x in range(len(removeList)):
        planet.goods.remove(removeList[x])


# GOAL: COMPLETE TRADE GOODS LIST
def initialize_trade_goods():
    # Incomplete Trade Goods List
    # Stange bug gives error if first list (sale?) is longer than 2nd list (purchase)
    trade_goods_list = []

    b_electronics = trade_goods(11, 'Basic Electronics', 'all', 1, 10, 10000,
                                [['In', 2], ['Ht', 3], ['Ri', 1]],
                                [['NI', 2], ['Lt', 1], ['Po', 1]])
    b_electronics.desc = 'Simple electronics including basic computers up to TL 10.'
    trade_goods_list.append(b_electronics)

    b_machine_parts = trade_goods(12, 'Basic Machine Parts', 'all', 1, 10, 10000,
                                  [['Na', 2], ['In', 5]],
                                  [['NI', 3], ['Ag', 2]])
    b_machine_parts.desc = 'Machine components and spare parts for common machinery.'
    trade_goods_list.append(b_machine_parts)

    b_manufactured_goods = trade_goods(13, 'Basic Manufactured Goods', 'all', 1, 10, 10000,
                                       [['Na', 2], ['In', 5]],
                                       [['NI', 3], ['Hi', 2]])
    b_manufactured_goods.desc = 'Household appliances, clothing and so forth.'
    trade_goods_list.append(b_manufactured_goods)

    b_raw_materials = trade_goods(14, 'Basic Raw Materials', 'all', 1, 10, 5000,
                                  [['Ag', 3], ['Ga', 2]],
                                  [['In', 2], ['Po', 2]])
    b_raw_materials.desc = 'Metal, plastics, chemicals and other basic materials.'
    trade_goods_list.append(b_raw_materials)

    b_consumables = trade_goods(15, 'Basic Consumables', 'all', 1, 10, 2000,
                                [['Ag', 3], ['Wa', 2], ['Ga', 1], ['As', -4]],
                                [['As', 1], ['Fl', 1], ['IC', 1], ['Hi', 1]])
    b_consumables.desc = 'Food, drink, and other agricultural products.'
    trade_goods_list.append(b_consumables)

    b_ore = trade_goods(16, 'Basic Ore', 'all', 1, 10, 1000,
                        [['As', 4], ['IC', 0]],
                        [['In', 3], ['NI', 1]])
    b_ore.desc = 'Ore bearing common materials.'
    trade_goods_list.append(b_ore)

    adv_electronics = trade_goods(21, 'Advanced Electronics', ['In', 'Ht'], 1, 5, 100000,
                                  [['In', 2], ['Ht', 3]],
                                  [['NI', 1], ['Ri', 2], ['As', 3]])
    adv_electronics.desc = 'Advanced sensors, computers, and other equipment up to TL 15.'
    trade_goods_list.append(adv_electronics)

    adv_machine_parts = trade_goods(22, 'Advanced Machine Parts', ['In', 'Ht'], 1, 5, 75000,
                                    [['In', 2], ['Ht', 1]],
                                    [['As', 2], ['NI', 2]])
    adv_machine_parts.desc = 'Machine components and spare parts, including gravitic components.'
    trade_goods_list.append(adv_machine_parts)

    adv_manufactured_goods = trade_goods(23, 'Advanced Manufactured Goods', ['In', 'Ht'], 1, 5, 100000,
                                         [['In', 1], ['Ht', 0]],
                                         [['Hi', 1], ['Ri', 2]])
    adv_manufactured_goods.desc = 'Devices and clothing incorporating advanced technologies.'
    trade_goods_list.append(adv_manufactured_goods)

    adv_weapons = trade_goods(24, 'Advanced Weapons', ['In', 'Ht'], 1, 5, 150000,
                              [['In', 0], ['Ht', 2]],
                              [['Po', 1], ['AZ', 2], ['RZ', 4]])
    adv_weapons.desc = 'Firearms, explosives, ammunition, artillery and other military-grade weaponry.'
    trade_goods_list.append(adv_weapons)

    adv_vehicles = trade_goods(25, 'Advanced Vehicles', ['In', 'Ht'], 1, 5, 180000,
                               [['In', 0], ['Ht', 2]],
                               [['As', 2], ['Ri', 2]])
    adv_vehicles.desc = 'Air/rafts, spacecraft,grav tanks and other vehicles up to TL 15.'
    trade_goods_list.append(adv_vehicles)

    biochemicals = trade_goods(26, 'Biochemicals', ['Ag', 'Wa'], 1, 5, 50000,
                               [['Ag', 1], ['Wa', 2]],
                               [['In', 2], ['In', 2]])  # had to add extra?
    biochemicals.desc = 'Biofuels, organic chemicals, extracts.'
    trade_goods_list.append(biochemicals)

    crystals_gems = trade_goods(31, 'Crystals & Gems', ['As', 'De', 'IC'], 1, 5, 20000,
                                [['As', 2], ['De', 1], ['IC', 1]],
                                [['In', 3], ['Ri', 2], ['x', 0]])  # had to add extra?
    crystals_gems.desc = 'Diamonds, synthetic or natural gemstones.'
    trade_goods_list.append(crystals_gems)

    cybernetics = trade_goods(32, 'Cybernetics', ['Ht'], 1, 1, 250000,
                              [['Ht', 0]],
                              [['As', 1], ['IC', 1], ['Ri', 2]])
    cybernetics.desc = 'Cybernetic components, replacement limbs.'
    trade_goods_list.append(cybernetics)

    animals = trade_goods(33, 'Live Animals', ['Ag', 'Ga'], 1, 10, 10000,
                          [['Ag', 2], ['Ga', 0]],
                          [['Lo', 3], ['Lo', 3]])  # added another
    animals.desc = 'Riding animals, beasts of burden, exotic pets.'
    trade_goods_list.append(animals)

    l_consumables = trade_goods(34, 'Luxury Consumables', ['Ag', 'Ga', 'Wa'], 1, 10, 20000,
                                [['Ag', 2], ['Ga', 0], ['Wa', 1]],
                                [['Ri', 2], ['Hi', 2], ['Hi', 2]])  # Added another??
    l_consumables.desc = 'Rare foods, fine liquors.'
    trade_goods_list.append(l_consumables)

    l_goods = trade_goods(35, 'Luxury Goods', ['Hi'], 1, 1, 200000,
                          [['Hi', 0]],
                          [['Ri', 4]])
    l_goods.desc = 'Rare or extremely high-quality manufactured goods.'
    trade_goods_list.append(l_goods)

    medical_supplies = trade_goods(36, 'Medical Supplies', ['Ht', 'Hi'], 1, 5, 50000,
                                   [['Ht', 2], ['Hi', 0]],
                                   [['In', 2], ['Po', 1], ['Ri', 1]])
    medical_supplies.desc = 'Diagnostic equipment, basic drugs, cloning technology.'
    trade_goods_list.append(medical_supplies)

    petrochemicals = trade_goods(41, 'Petrochemicals', ['De', 'Fl', 'IC', 'Wa'], 1, 10, 10000,
                                 [['De', 2], ['Fl', 0], ['IC', 0], ['Wa', 0]],
                                 [['In', 2], ['Ag', 1], ['Lt', 2], ['Lt', 2]])  # added another
    petrochemicals.desc = 'Oil, liquid fuels.'
    trade_goods_list.append(petrochemicals)

    pharmaceuticals = trade_goods(42, 'Pharmaceuticals', ['As', 'De', 'Hi', 'Wa'], 1, 1, 100000,
                                  [['As', 2], ['De', 0], ['Hi', 1], ['Wa', 0]],
                                  [['Ri', 2], ['Lt', 1], ['X', 0], ['X', 0]])  # ADDED 2 HYPO: EQU OR GRTR THAN PURCH DM
    pharmaceuticals.desc = 'Drugs, medical supplies, anagathatics,fast or slow drugs.'
    trade_goods_list.append(pharmaceuticals)

    polymers = trade_goods(43, 'Polymers', ['In'], 1, 10, 7000,
                           [['In', 0]],
                           [['Ri', 2], ['NI', 1]])
    polymers.desc = 'Plastics and other synthetics.'
    trade_goods_list.append(polymers)

    radioactives = trade_goods(45, 'Radioactives', ['As', 'De', 'Lo'], 1, 1, 1000000,
                               [['As', 2], ['De', 0], ['Lo', -4]],
                               [['In', 3], ['Ht', 1], ['NI', -2], ['Ag', -3]])
    radioactives.desc = 'Uranium, plutonium, unobtanium, rare elements.'
    trade_goods_list.append(radioactives)

    textiles = trade_goods(52, 'Textiles', ['Ag', 'NI'], 1, 10, 3000,
                           [['Ag', 7], ['NI', 0]],
                           [['Hi', 3], ['Na', 2]])
    textiles.desc = 'Clothing and fabrics.'
    trade_goods_list.append(textiles)

    u_ore = trade_goods(53, 'Uncommon Ore', ['As', 'IC'], 1, 10, 5000,
                           [['As', 4], ['IC', 0]],
                           [['In', 3], ['NI', 1]])
    u_ore.desc = 'Ore containing precious or valuable metals.'
    trade_goods_list.append(u_ore)

    u_raw_materials = trade_goods(53, 'Uncommon Raw Materials', ['Ag', 'De', 'Wa'], 1, 10, 20000,
                           [['Ag', 2], ['De', 0], ['Wa', 1]],
                           [['In', 2], ['Ht', 1], ['X', 0]])
    u_raw_materials.desc = 'Valuable metals like titanium, rare elements.'
    trade_goods_list.append(u_raw_materials)

    wood = trade_goods(53, 'Wood', ['Ag', 'Ga'], 1, 10, 1000,
                           [['Ag', 6], ['Ga', 0]],
                           [['In', 2], ['Ri', 1]])
    wood.desc = 'Hard or beautiful woods and plant extracts.'
    trade_goods_list.append(wood)

    return trade_goods_list

def generateFreight(galaxy,troubleshoot=False):
    trade_goods_list = initialize_trade_goods()
    for l in range(len(galaxy)):

        # Reset 'any' list to exclude all non-basic inventory
        any = []
        for i in range(6):
            any.append(trade_goods_list[i])

        # Reset all inventory's tonnage to 0
        for i in range(len(trade_goods_list)):
            trade_goods_list[i].tons = 0

        # Determine Available and Extra Goods
        available_goods = planetary_goods(any, trade_goods_list, galaxy[l])
        extra_goods(trade_goods_list, available_goods)

        # Roll Purchase Modifier, determine purchase price, tonnage, print to monitor
        result = d(2,6,0) + random.randint(1, 6)
        for i in range(len(available_goods)):
            available_goods[i].determine_purchase_price(result, galaxy[l].codes)
            available_goods[i].determine_stock()

        galaxy[l].goods = available_goods
        removeEmptyFreight(galaxy[l])
        # Reset available goods
        available_goods = []


def defaultGalaxy():
    galaxy = generateGalaxy(10, 8)
    generateFreight(galaxy)
    return galaxy


def determineAvailableGoods(hex_field, trade_goods_list, printX=False):
    testGalaxy = []
    for l in range(len(hex_field)):

        # Reset 'any' list to exclude all non-basic inventory
        any = []
        for i in range(6):
            any.append(trade_goods_list[i])

        # Reset all inventory's tonnage to 0
        for i in range(len(trade_goods_list)):
            trade_goods_list[i].tons = 0

        # Reset Hallowsbelt & Hexfield
        hallowsbelt = spawnPlanet(hex_field, printX)

        # Determine Available and Extra Goods
        available_goods = planetary_goods(any, trade_goods_list, hallowsbelt)
        extra_goods(trade_goods_list, available_goods)

        # Roll Purchase Modifier, determine purchase price, tonnage, print to monitor
        result = d(2,6,0) + random.randint(1, 6)
        for i in range(len(available_goods)):
            available_goods[i].determine_purchase_price(result, hallowsbelt.codes)
            available_goods[i].determine_stock()
            if printX == True:
                available_goods[i].info()

        hallowsbelt.goods = available_goods
        # Reset available goods
        available_goods = []
        testGalaxy.append(hallowsbelt)
    return testGalaxy

def planet_economy(planet,goods_list,trade_mod='random',troubleshooting=False):
    if troubleshooting: print('Troubleshooting planet_economy() '+planet.name+' \n')
    basic_goods = []                                                        # Reset / define basic goods
    trade_goods_list = initialize_trade_goods()                             # Initialize trade goods list
    if troubleshooting:
        print('Initialized Trade List:')
        for good in trade_goods_list: good.info()
        print()
    for trade_good in trade_goods_list:                                     # RESET TONS TO 0
        trade_good.tons = 0
    for i in range(6): basic_goods.append(trade_goods_list[i])              # Add basic goods to basic_goods_list
    if troubleshooting: 
        print('Basic Goods List: ')
        for good in basic_goods: good.info()
        print()
    for i in range(len(trade_goods_list)): trade_goods_list[i].tons = 0     # RESET TONS TO 0 AGAIN
    available_goods = planetary_goods(basic_goods,trade_goods_list,planet,troubleshooting=troubleshooting)  # Determine Available goods, does not rol any tonnage
    if troubleshooting:
        print('Planetary Goods List: ')
        for good in available_goods: good.info()
        print()
    extra_goods(trade_goods_list,available_goods,troubleshooting=troubleshooting)                           # Determine extra goods, rolls tonnage ONLY for goods already in list
    if troubleshooting:
        print('Extra Goods: ')
        for good in available_goods: good.info()
        print()
    if isinstance(trade_mod,str) == True: result = d(3,6,0)
    else:
        result = d(2,6,0) + trade_mod
    if troubleshooting:
        print('Trade Modifier: '+str(result))
        print('Post-Trade Mod Available Goods (Length '+str(len(available_goods))+'):')
        for good in available_goods: good.info()
        print()
    for i in range(len(available_goods)):
        if troubleshooting: 
            print('Available Goods Index Number: '+str(i))
            print(len(available_goods))
            available_goods[i].info()
        available_goods[i].determine_purchase_price(result,planet.codes,troubleshooting=troubleshooting) #OOR
        if troubleshooting:
            print('trblsht p_price:')
            available_goods[i].info
        available_goods[i].determine_stock(troubleshooting=troubleshooting)                                # Determines stock based on any stock that still has 0 in the available list
        planet.goods = available_goods
        #available_goods = []
        
        #print(planet.name)
    removeEmptyFreight(planet,troubleshooting=troubleshooting)
    if troubleshooting: print('--- End of planet_economy() troubleshooting ---')


def galactic_economy(galaxy,initialize=True,print=False,trade_mod='random',troubleshooting=False):
    basic_goods = []
    trade_goods_list = initialize_trade_goods()
    for trade_good in trade_goods_list: 
        trade_good.tons = 0
        #if troubleshooting == True: print(trade_good.tons)
    for i in range(6): basic_goods.append(trade_goods_list[i])
    for i in range(len(trade_goods_list)): trade_goods_list[i].tons = 0
    for i in range(len(galaxy)):
        available_goods = planetary_goods(basic_goods,trade_goods_list,galaxy[i])
        extra_goods(trade_goods_list,available_goods)
        if isinstance(trade_mod,str) == True: result = d(3,6,0)
        else:
            result = d(2,6,0)
        for tg in range(len(available_goods)):
            available_goods[tg].determine_purchase_price(result,galaxy[i].codes)
            #print('determine stock: '+trade_good.name)
            available_goods[tg].determine_stock()
        galaxy[i].goods = available_goods
        available_goods = []
        removeEmptyFreight(galaxy[i])
        cheat = galaxy[i]
        print(cheat.name)


