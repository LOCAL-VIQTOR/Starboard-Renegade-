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

    def determine_stock(self):
        add_tons = 0
        for i in range(self.tons_dice):
            add_tons += random.randint(1, 6)
        add_tons = add_tons * self.tons_mult
        self.tons += add_tons

    def determine_purchase_price(self, result, trade_code):
        mod = 1
        for i in range(len(self.p_dm)):
            if self.p_dm[i][0] in trade_code: result += self.p_dm[i][1]
            if self.s_dm[i][0] in trade_code: result -= self.s_dm[i][1]

        if result <= -1: mod = 4
        if result == 0: mod = 3
        if result == 1: mod = 2
        if result == 2: mod = 1.75
        if result == 3: mod = 1.5
        if result == 4: mod = 1.35
        if result == 5: mod = 1.25
        if result == 6: mod = 1.2
        if result == 7: mod = 1.15
        if result == 8: mod = 1.1
        if result == 9: mod = 1.05
        if result == 10: mod = 1
        if result == 11: mod = 0.95
        if result == 12: mod = 0.9
        if result == 13: mod = 0.85
        if result == 14: mod = 0.8
        if result == 15: mod = 0.75
        if result == 16: mod = 0.7
        if result == 17: mod = 0.65
        if result == 18: mod = 0.55
        if result == 19: mod = 0.5
        if result == 20: mod = 0.4
        if result >= 21: mod = 0.25

        self.p_price = int(round(self.base_price * mod, 2))

    def info(self):
        print(str(self.tons) + 't. | ' + self.name + ' | ' + str(self.p_price) + ' Cr. | ' + self.desc)


def planetary_goods(basic_items, all_items, planet):
    # Gives every planet the basic goods.
    available_goods = basic_items
    # For every inventory option there is...
    for i in range(len(all_items)):
        # If the item wasn't already included in the basic package...
        if all_items[i].availability != 'any':
            # For each item in the inventory's 'availability' tag
            for n in range(len(all_items[i].availability)):
                # If the item is available on the current planet...
                if all_items[i].availability[n] in planet.codes:
                    # And it's not already in the available goods list...
                    if all_items[i] not in available_goods:
                        # Then put it on the available goods list!
                        available_goods.append(all_items[i])
    return available_goods


def extra_goods(all_goods,
                available_goods):  # add implementation for illegal sellers . . . and designed inventory per making your own planet
    # Pick 1D6 extra goods to have available
    extra_goods = random.randint(1, 6)
    # For the number of extra items picked...
    for i in range(extra_goods):
        # Pick an item from the full options list
        extra = random.choice(all_goods)
        # If it's not already in the available goods list...
        if extra not in available_goods:
            # Put it on the available goods list!
            available_goods.append(extra)
        # If it is in the available goods list...
        if extra in available_goods:
            # For each item the planet already has...
            for i in range(len(available_goods)):
                # If that stock is concurrent to the added stock...
                if available_goods[i].name == extra.name:
                    # Set a baseline of the
                    extra_stock = available_goods[i].tons
                    # Roll basic stock inventory
                    for n in range(extra.tons_dice):
                        extra_stock += random.randint(1, 6)
                    extra_stock *= extra.tons_mult
                    # Add that stock to the inventory's tonnage'
                    available_goods[i].tons += extra_stock


# DOES NOT WORK AS INTENDED
# Removes empty freight from a planet's list
def removeEmptyFreight(planet):
    # Creates a list of freight to remove
    removeList = []
    # Adds the freight to the list if tons is 0
    for i in range(len(planet.goods)):
        if planet.goods[i].tons == 0:
            append.removeList(i)
    # Goes right-to-left removing 'empty' freight from the world
    x = len(removeList) - 1
    while x >= 0:
        planet.goods.remove(planet.goods[x])
        x -= 1


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

    return trade_goods_list

#def spawnPlanet(hexField, printX):
#    hallowsbelt = planet()
#    hallowsbelt.generate(hexField, printX)
#    return hallowsbelt


# Generates & returns a galaxy based on (y, x), 50% inhabited hexes
# Uses generateHexList()
#def generateGalaxy(rows, columns):
#    hexField = generateHexList(rows, columns)
#    galaxy = []
#    for l in range(len(hexField)):
#        hallowsbelt = spawnPlanet(hexField, False)
#        galaxy.append(hallowsbelt)
#    return galaxy


def generateFreight(galaxy):
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


def determineAvailableGoods(hex_field, trade_goods_list, printX):
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
