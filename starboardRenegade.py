#    ___________________________________________
#    |/0101\____/0301\____/0501\____/0701\____/|
#    |\____/0201\____/0401\____/0601\____/0801\|    Starboard, Renegade!
#    |/0102\____/0302\____/0502\____/0702\____/|
#    |\____/0202\____/0402\____/0602\____/0802\|    A referee's faithful
#    |/0103\____/0303\____/0503\____/0703\____/|    companion . . .
#    |\____/0203\____/0403\____/0603\____/0803\|
#    |/0104\____/0304\____/0504\____/0704\____/|    Amalgamated from:
#    |\____/0204\____/0404\____/0604\____/0804\|    - Mongoose Traveller
#    |/0105\____/0305\____/0505\____/0705\____/|    - Cyberpunk 2020
#    |\____/0205\____/0405\____/0605\____/0805\|    - GAMMAWORLD
#    |/0106\____/0306\____/0506\____/0706\____/|
#    |\____/0206\____/0406\____/0606\____/0806\|    Dedicated to the kobolds
#    |/0107\____/0307\____/0507\____/0707\____/|    who were killed for XP.
#    |\____/0207\____/0407\____/0607\____/0807\|
#    |/0108\____/0308\____/0508\____/0708\____/|    By LOCAL-VIQTOR
#    |\____/0208\____/0408\____/0608\____/0808\|
#    |/____\____/____\____/____\____/____\____/|    GitHub Build

import random
import math
from time import sleep

#    ____  ___   _____ __________
#   / __ )/   | / ___//  _/ ____/
#  / __  / /| | \__ \ / // /
# / /_/ / ___ |___/ // // /___
# /_____/_/  |_/____/___/\____/
# BASIC FUNCTIONS - DICE ROLLING,
# INTEGER AND LETTER SWITCHING

def d(dice,base,mod):   # Dice Roller, 2D6+1 = d(2,6,1)
    result = mod
    for i in range(dice):
        result += random.randint(1,base)
    return result

def dsixtysix(tens_modifier, ones_modifier):  # Rolls D66 with a modifier to 10s and 1s places
    return (random.randint(1, 6) * 10) + random.randint(1, 6) + (tens_modifier * 10) + ones_modifier

def hexSwitch(number):  # Takes a decimal and returns a hexadecimal string
    if number < 10: return str(number)
    if number == 10: return 'A'
    if number == 11: return 'B'
    if number == 12: return 'C'
    if number == 13: return 'D'
    if number == 14: return 'E'
    if number == 15: return 'F'
    if number == 16: return 'G'
    if number == 17: return 'H'
    if number == 18: return 'J'
    if number == 19: return 'K'
    if number == 20: return 'L'

def alphaSwitch(numLet):  # Takes either a number or a
    if str(numLet).isdigit() == True:  # letter and returns the inverse
        if numLet == 1: return 'A'
        if numLet == 2: return 'B'
        if numLet == 3: return 'C'
        if numLet == 4: return 'D'
        if numLet == 5: return 'E'
        if numLet == 6: return 'F'
        if numLet == 7: return 'G'
        if numLet == 8: return 'H'
        if numLet == 9: return 'I'
        if numLet == 10: return 'J'
        if numLet == 11: return 'K'
        if numLet == 12: return 'L'
        if numLet == 13: return 'M'
        if numLet == 14: return 'N'
        if numLet == 15: return 'O'
        if numLet == 16: return 'P'
        if numLet == 17: return 'Q'
        if numLet == 18: return 'R'
        if numLet == 19: return 'S'
        if numLet == 20: return 'T'
        if numLet == 21: return 'U'
        if numLet == 22: return 'V'
        if numLet == 23: return 'W'
        if numLet == 24: return 'X'
        if numLet == 25: return 'Y'
        if numLet == 26: return 'Z'
    if str(numLet).isdigit() == False:
        if numLet == 'A': return 1
        if numLet == 'B': return 2
        if numLet == 'C': return 3
        if numLet == 'D': return 4
        if numLet == 'E': return 5
        if numLet == 'F': return 6
        if numLet == 'G': return 7
        if numLet == 'H': return 8
        if numLet == 'I': return 9
        if numLet == 'J': return 10
        if numLet == 'K': return 11
        if numLet == 'L': return 12
        if numLet == 'M': return 13
        if numLet == 'N': return 14
        if numLet == 'O': return 15
        if numLet == 'P': return 16
        if numLet == 'Q': return 17
        if numLet == 'R': return 18
        if numLet == 'S': return 19
        if numLet == 'T': return 20
        if numLet == 'U': return 21
        if numLet == 'V': return 22
        if numLet == 'W': return 23
        if numLet == 'X': return 24
        if numLet == 'Y': return 25
        if numLet == 'Z': return 26

def generateName(): # List of first names, middle names as letters, and nouns as last name (See: Toast of London)
    first_names = ['John', 'Steven', 'Mark', 'Caitlyn', 'Stella', 'Jessica', 'James', 'Robert', 'Michael', 'David',
                   'William', 'Richard', 'Joseph', 'Thomas', 'Christopher', 'Calvin', 'Mary', 'Patricia',
                   'Jennifer', 'Henry', 'Elijah', 'Charles', 'Tobias', 'Philomena', 'Phillip', 'Patrick', 'Stewart',
                   'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Sarah', 'Karen', 'Gillian', 'William']
    middle_initial = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'RR']
    last_names = ['Toast', 'Rock', 'Pan', 'Bell', 'Camp', 'Waterfall', 'Safe', 'Canteen', 'Wheel', 'Time', 'Year',
                  'Man', 'Thing', 'Woman', 'Child', 'State', 'Hand', 'Case', 'Program', 'Money', 'Cordycepts', 'Tongs',
                  'Camera', 'Flower', 'Orchid', 'Rose', 'Boiler', 'Oven', 'Drum', 'Letter', 'Library', 'Brick', 'Corn',
                  'Whiskey', 'Rogers', 'Bedford', 'Lowe', 'Pistol', 'Revolver', 'Can', 'Van', 'Sedan', 'Armoire',
                  'Knife', 'Switchblade', 'Basket', 'Harpoon', 'Harpsichord', 'Taco', 'Burrito', 'Sock', 'Branch',
                  'Cane', 'Driftwood', 'Woods', 'Processor', 'Candlestick', 'Blunderbuss']
    return random.choice(first_names) + ' ' + random.choice(middle_initial) + '. ' + random.choice(last_names)

#    ____  __    ___    _   ______________
#   / __ \/ /   /   |  / | / / ____/_  __/
#  / /_/ / /   / /| | /  |/ / __/   / /
# / ____/ /___/ ___ |/ /|  / /___  / /
# /_/   /_____/_/  |_/_/ |_/_____/ /_/
# PLANET GENERATOR CLASS & FUNCTIONS

def generateHexList(rows, columns):         # Creates and returns a list of habited planets' hex locations.
    hexes = []                              # Creates an empty list waiting for hexes
    for x in range(columns):                # Creates a hex where the x location (x*100+y) up to 9999.
        for y in range(rows):
            z = (x + 1) * 100 + y + 1
            if x < 10:                      # Add a leading 0 if hex is less than 1000
                z = '0' + str(z)
            if x >= 10:
                z = str(z)
            c = random.randint(1, 2)   # Gives each hex a 50/50 shot of containing a settled world.
            if c == 2: hexes.append(z)      # Adds successful hexes to the hexes list
    return hexes

class planet():  # Planet Class
    def __init__(self):

        # PLANET DETAILS
        self.name = 'PlanetNameErr'                 # Name of the planet
        self.hex = 'PlanetHexErr'                   # Planet's hex location
        self.uwp = ['X', 0, 0, 0, 0, 0, 0, 0]       # Planet's Universal World Profile
        self.codes = []                             # Trade Codes

        # STARPORT DETAILS
        self.starportQuality = 'StarportQualErr'    # Starport's Quality
        self.berthingCost = 0                       # Starport's berthing cost
        self.fuel = 'PlanetFuelErr'                 # Type of fuel available at starport
        self.facilities = 'PlanetFacErr'            # Type of fuel available at starport
        self.bases = []                             # Bases available at starport or surrounding area

        # GEOGRAPHIC DETAILS
        self.size = 800                             # Diameter of planet (km)
        self.surfaceGravity = 0.0                   # Gravity on surface as percentage of earth's (gs)
        self.lowGravity = True
        self.highGravity = False
        self.negligibleGravity = True
        self.atmosphere = 'PlanetAtmoErr'           # Planet's Atmosphere & PPE
        self.taintedAtmosphere = False
        self.vaccSuit = True
        self.respirator = False
        self.filter = False
        self.airSupply = False
        self.ppeVaries = False
        self.hydrosphere = 0                        # Planet's percentage of surface area (water/total)
        self.climate = [0, 30, 'PlanetTempErr']     # Climate and temperature
        self.temperatureSwings = False

        # SOCIOECONOMIC DETAILS
        self.population = 0                         # Planet's population
        self.population_density = 0                 # People per square kilometer
        self.government = 'PlanetGovErr'            # PLanet Government type
        self.factions = []                          # Planet factions
        self.balkanization = False                  # Is the planet experiencing balkanization?
        self.culture = 'PlanetCultureErr'           # Planet Culture & Langauge Base
        self.language = 'PlanetLangErr'

        # TRADE GOODS
        self.goods = []

    # Generates a name for the planet
    def generate_name(self):
        prefix = ['Alph', 'Br', 'Ch', 'D', 'Ech', 'F', 'G', 'H', 'Ind', 'J', 'K', 'L', 'M', 'Nov', 'Osc', 'P', 'Qu',
                  'R', 'Si', 'T', 'Un', 'V', 'Wh', 'X', 'Y', 'Z', 'Calv', 'Dian', 'Rog']
        suffix = ['a', 'avo', 'arlie', 'elta', 'o', 'oxtrot', 'olf', 'otel', 'ia', 'uliett', 'ilo', 'ima', 'ike',
                  'ember', 'ar', 'apa', 'ebec', 'omeo', 'erra', 'ango', 'iform', 'ictor', 'iskey', '-ray', 'ankee',
                  'ulu', 'owe', 'iana', 'ers']
        self.name = random.choice(prefix) + random.choice(suffix) + '-' + str(random.randint(1, 13))

    # Takes the first hex in the hex list's locatons, then removes it from the list.
    def generate_hex(self, hex_field):
        self.hex = hex_field[0]
        hex_field.remove(self.hex)

    # Determines starport quality, berth, and fuel and repair availability
    def generate_starport(self, result):

        # No Starport
        if result == 0 or result == 1:
            self.uwp[0] = 'X'
            self.starportQuality = 'No'
            self.berthingCost = 0
            self.fuel = 'No Fuel'
            self.facilities = 'No Repair Facilities'

        # Frontier Starport
        if result == 2 or result == 3:
            self.uwp[0] = 'E'
            self.starportQuality = 'Frontier'
            self.berthingCost = 0
            self.fuel = 'No Fuel'
            self.facilities = 'No Repair Facilities'

        # Poor Starport
        if result == 4 or result == 5:
            self.uwp[0] = 'D'
            self.starportQuality = 'Poor'
            self.berthingCost = random.randint(1, 6) * 10
            self.fuel = 'Unrefined Fuel'
            self.facilities = 'Limited Repair Facilities'

        # Routine Starport
        if result == 6 or result == 7:
            self.uwp[0] = 'C'
            self.starportQuality = 'Routine'
            self.berthingCost = random.randint(1, 6) * 100
            self.fuel = 'Unrefined Fuel'
            self.facilities = 'Small Craft Repair Facilities'

        # Good Starport
        if result == 8 or result == 9:
            self.uwp[0] = 'B'
            self.starportQuality = 'Good'
            self.berthingCost = random.randint(1, 6) * 500
            self.fuel = 'Refined fuel'
            self.facilities = 'Spacecraft Repair Facilities'

        # Excellent Starport
        if result == 10:
            self.uwp[0] = 'A'
            self.starportQuality = 'Excellent'
            self.berthingCost = random.randint(1, 6) * 1000
            self.fuel = 'Refined Fuel'
            self.facilities = 'Repair Facilities (All)'

    # Determines a planet's size (km) and surface gravity (gs)
    def generate_size(self, size_result):
        self.uwp[1] = size_result

        # Determines whether the surface gravity is negligible
        if self.uwp[1] == 0:
            self.size = 800
            self.surfaceGravity = 0.0
            self.negligibleGravity = True
        if self.uwp[1] > 0:
            self.size = 1600 * self.uwp[1]
            self.negligibleGravity = False

        # Determines the surface gravity based on roll
        if self.uwp[1] == 1: self.surfaceGravity = 0.05
        if self.uwp[1] == 2: self.surfaceGravity = 0.15
        if self.uwp[1] == 3: self.surfaceGravity = 0.25
        if self.uwp[1] == 4: self.surfaceGravity = 0.35
        if self.uwp[1] == 5: self.surfaceGravity = 0.45
        if self.uwp[1] == 6: self.surfaceGravity = 0.7
        if self.uwp[1] == 7: self.surfaceGravity = 0.9
        if self.uwp[1] == 8: self.surfaceGravity = 1.0
        if self.uwp[1] == 9: self.surfaceGravity = 1.25
        if self.uwp[1] == 10: self.surfaceGravity = 1.4

        # Determines whether there is low/high gravity where acclimation is required
        self.lowGravity = False
        self.highGravity = False
        if self.surfaceGravity < 0.75: self.lowGravity = True
        if self.surfaceGravity >= 1.25: self.highGravity = True

    # Determines a planet's atmosphere and required PPE
    def generate_atmosphere(self, atmosphere_result):
        self.uwp[2] = atmosphere_result  # d(2,6,-7) + self.uwp[1]

        # Sets limits at 0 and 15
        if self.uwp[2] < 0: self.uwp[2] = 0
        if self.uwp[2] > 15: self.uwp[2] = 15

        # No Atmosphere
        if self.uwp[2] == 0:
            self.atmosphere = 'No'
            self.taintedAtmosphere = False
            self.vaccSuit = True
            self.respirator = False
            self.filter = False
            self.airSupply = False
            self.ppeVaries = False

        # Trace Atmosphere
        if self.uwp[2] == 1:
            self.atmosphere = 'Trace'
            self.taintedAtmosphere = False
            self.vaccSuit = True
            self.respirator = False
            self.filter = False
            self.airSupply = False
            self.ppeVaries = False

        # Very Thin, Tainted Atmosphere
        if self.uwp[2] == 2:
            self.atmosphere = 'Very Thin'
            self.taintedAtmosphere = True
            self.vaccSuit = False
            self.respirator = True
            self.filter = True
            self.airSupply = False
            self.ppeVaries = False

        # Very Thin Atmosphere
        if self.uwp[2] == 3:
            self.atmosphere = 'Very Thin'
            self.taintedAtmosphere = False
            self.vaccSuit = False
            self.respirator = True
            self.filter = False
            self.airSupply = False
            self.ppeVaries = False

        # Thin, Tainted Atmosphere
        if self.uwp[2] == 4:
            self.atmosphere = 'Thin'
            self.taintedAtmosphere = True
            self.vaccSuit = False
            self.respirator = False
            self.filter = True
            self.airSupply = False
            self.ppeVaries = False

        # Thin Atmosphere
        if self.uwp[2] == 5:
            self.atmosphere = 'Thin'
            self.taintedAtmosphere = False
            self.vaccSuit = False
            self.respirator = False
            self.filter = False
            self.airSupply = False
            self.ppeVaries = False

        # Standard Atmosphere
        if self.uwp[2] == 6:
            self.atmosphere = 'Standard'
            self.taintedAtmosphere = False
            self.vaccSuit = False
            self.respirator = False
            self.filter = False
            self.airSupply = False
            self.ppeVaries = False

        # Tainted Atmosphere
        if self.uwp[2] == 7:
            self.atmosphere = 'Standard'
            self.taintedAtmosphere = True
            self.vaccSuit = False
            self.respirator = False
            self.filter = True
            self.airSupply = False
            self.ppeVaries = False

        # Dense Atmosphere
        if self.uwp[2] == 8:
            self.atmosphere = 'Dense'
            self.taintedAtmosphere = False
            self.vaccSuit = False
            self.respirator = False
            self.filter = False
            self.airSupply = False
            self.ppeVaries = False

        # Dense, Tainted Atmosphere
        if self.uwp[2] == 9:
            self.atmosphere = 'Dense'
            self.taintedAtmosphere = True
            self.vaccSuit = False
            self.respirator = False
            self.filter = True
            self.airSupply = False
            self.ppeVaries = False

        # Exotic Atmosphere
        if self.uwp[2] == 10:
            self.atmosphere = 'Exotic'
            self.taintedAtmosphere = False
            self.vaccSuit = False
            self.respirator = False
            self.filter = False
            self.airSupply = True
            self.ppeVaries = False

        # Corrosive Atmosphere
        if self.uwp[2] == 11:
            self.atmosphere = 'Corrosive'
            self.taintedAtmosphere = False
            self.vaccSuit = True
            self.respirator = False
            self.filter = False
            self.airSupply = False
            self.ppeVaries = False

        # Insidious Atmosphere
        if self.uwp[2] == 12:
            self.atmosphere = 'Insidious'
            self.taintedAtmosphere = False
            self.vaccSuit = True
            self.respirator = False
            self.filter = False
            self.airSupply = False
            self.ppeVaries = False

        # Dense, High Atmosphere
        if self.uwp[2] == 13:
            self.atmosphere = 'Dense, High'
            self.taintedAtmosphere = False
            self.vaccSuit = False
            self.respirator = False
            self.filter = False
            self.airSupply = False
            self.ppeVaries = False

        # Thin, Low Atmosphere
        if self.uwp[2] == 14:
            self.atmosphere = 'Thin, Low'
            self.taintedAtmosphere = False
            self.vaccSuit = False
            self.respirator = False
            self.filter = False
            self.airSupply = False
            self.ppeVaries = False

        # Unusual Atmosphere
        if self.uwp[2] == 15:
            self.atmosphere = 'Unusual'
            self.taintedAtmosphere = False
            self.vaccSuit = False
            self.respirator = False
            self.filter = False
            self.airSupply = False
            self.ppeVaries = True

    # Determine's a planet's temperature
    def generate_climate(self):

        # Determines if temperature follows circadian rhythm
        self.temperatureSwings = False
        if self.uwp[2] == 0 or self.uwp[2] == 1:
            climate_roll = d(2,6,0)
            self.temperatureSwings = True

        # Rolls a number with DM based on atmosphere roll
        if self.uwp[2] == 2 or self.uwp[2] == 3: climate_roll = d(2,6,-2)
        if self.uwp[2] == 4 or self.uwp[2] == 5 or self.uwp[2] == 14: climate_roll = d(2,6,-1)
        if self.uwp[2] == 6 or self.uwp[2] == 7: climate_roll = d(2,6,0)
        if self.uwp[2] == 8 or self.uwp[2] == 9: climate_roll = d(2,6,1)
        if self.uwp[2] == 10 or self.uwp[2] == 13 or self.uwp[2] == 15: climate_roll = d(2,6,2)
        if self.uwp[2] == 11 or self.uwp[2] == 12: climate_roll = d(2,6,6)

        # Sets planet climate based on roll
        if climate_roll <= 2: self.climate = [-100, -51, 'Frozen']
        if climate_roll == 3 or climate_roll == 4: self.climate = [-51, 0, 'Cold']
        if climate_roll >= 5 and climate_roll <= 9: self.climate = [0, 30, 'Temperate']
        if climate_roll == 10 or climate_roll == 11: self.climate = [31, 80, 'Hot']
        if climate_roll >= 12: self.climate = [81, 100, 'Roasting']

    # Determines how much of the planet's surface is covered by liquid ocean
    def generate_hydrographics(self):

        # Determines modifier based on size, atmosphere and climate
        modifier = 0
        if self.uwp[2] <= 1: modifier = -4
        if self.uwp[2] >= 10 and self.uwp[2] <= 12: modifier = -4
        if self.uwp[2] != 13:
            if self.climate[2] == 'Hot': modifier = -2
            if self.climate[2] == 'Roasting': modifier = -6
        self.uwp[3] = d(2,6,modifier)
        if self.uwp[1] <= 1 or self.uwp[3] < 0: self.uwp[3] = 0

        # Sets roll limit
        if self.uwp[3] > 10: self.uwp[3] = 10

        # Gives % of hydrosphere based on roll
        if self.uwp[3] == 0: self.hydrosphere = random.randint(0, 5)
        if self.uwp[3] == 1: self.hydrosphere = random.randint(6, 15)
        if self.uwp[3] == 2: self.hydrosphere = random.randint(16, 25)
        if self.uwp[3] == 3: self.hydrosphere = random.randint(26, 35)
        if self.uwp[3] == 4: self.hydrosphere = random.randint(36, 45)
        if self.uwp[3] == 5: self.hydrosphere = random.randint(46, 55)
        if self.uwp[3] == 6: self.hydrosphere = random.randint(56, 65)
        if self.uwp[3] == 7: self.hydrosphere = random.randint(66, 75)
        if self.uwp[3] == 8: self.hydrosphere = random.randint(76, 85)
        if self.uwp[3] == 9: self.hydrosphere = random.randint(86, 95)
        if self.uwp[3] == 10: self.hydrosphere = random.randint(96, 100)

    # Determines a planet's sophont population
    def generate_population(self):
        self.uwp[4] = d(2,6,-2)

        # Sets roll limits of 0 and 12
        if self.uwp[4] < 0: self.uwp[4] = 0
        if self.uwp[4] > 12: self.uwp[4] = 12

        # Sets population beteen 10^roll and 10*10^roll
        minimum_population = int(math.pow(10, self.uwp[4]))
        self.population = random.randint(minimum_population, (10 * minimum_population))

        # Calculates population density and rounds it out
        self.population_density = self.population / self.size
        if self.population_density < 1: self.population_density = round(self.population_density, 2)
        if self.population_density >= 1: self.population_density = int(self.population_density)

    # Returns planetary government type from external roll
    def government_types(self, roll):
        if roll == 0: return 'No Ruling Government'
        if roll == 1: return 'Company/Corporation'
        if roll == 2: return 'Participating Democracy'
        if roll == 3: return 'Self-perpetuating Oligarchy'
        if roll == 4: return 'Representative Democracy'
        if roll == 5: return 'Feudal Technocracy'
        if roll == 6: return 'Captive Government'
        if roll == 7: return 'Balkanization'
        if roll == 8: return 'Civil Service Bureaucracy'
        if roll == 9: return 'Impersonal Bureaucracy'
        if roll == 10: return 'Charismatic Dictator'
        if roll == 11: return 'Non-charismatic Leader'
        if roll == 12: return 'Charismatic Oligarchy'
        if roll == 13: return 'Religious Dictatorship'

    # Returns planet's or faction's culture from external roll
    def culture_types(self, roll):
        if roll == 11: return "Sexist"
        if roll == 12: return "Religious"
        if roll == 13: return "Artistic"
        if roll == 14: return "Ritualized"
        if roll == 15: return "Conservative"
        if roll == 16: return "Xenophobic"
        if roll == 21: return "Taboo"
        if roll == 22: return "Deceptive"
        if roll == 23: return "Liberal"
        if roll == 24: return "Honourable"
        if roll == 25: return "Influenced"
        if roll == 26: return "Fusion"
        if roll == 31: return "Barbaric"
        if roll == 32: return "Remnant"
        if roll == 33: return "Degenerate"
        if roll == 34: return "Progressive"
        if roll == 35: return "Recovering"
        if roll == 36: return "Nexus"
        if roll == 41: return "Tourist Attraction"
        if roll == 42: return "Violent"
        if roll == 43: return "Peaceful"
        if roll == 44: return "Obsessed"
        if roll == 45: return "Fashion"
        if roll == 46: return "At War"
        if roll == 51: return "Unusual Custom: Offworlders"
        if roll == 52: return "Unusual Custom: Starport"
        if roll == 53: return "Unusual Custom: Media"
        if roll == 54: return "Unusual Custom: Technology"
        if roll == 55: return "Unusual Customs: Lifestyle"
        if roll == 56: return "Unusual Customs: Social Standings"
        if roll == 61: return "Unusual Customs: Trade"
        if roll == 62: return "Unusual Customs: Nobility"
        if roll == 63: return "Unusual Customs: Sex"
        if roll == 64: return "Unusual Customs: Eating"
        if roll == 65: return "Unusual Customs: Travel"
        if roll == 66: return "Unusual Customs: Conspiracy"

    # Determines the planet's main government and culture
    def generate_government_and_culture(self):
        self.balkanization = False
        self.uwp[5] = d(2,6,-7) + self.uwp[4]

        # Determines balkanization and sets roll limits
        if self.uwp[5] == 7: self.balkanization = True
        if self.uwp[5] < 0: self.uwp[5] = 0
        if self.uwp[5] > 13: self.uwp[5] = 13

        # Makes roll and sets governemt and culture
        self.government = self.government_types(self.uwp[5])
        self.culture = self.culture_types(dsixtysix(0, 0))

    # Determines any factions that may be present on the planet
    def generate_factions(self):

        # Resets faction, modifier, and cycle count
        factions = []
        modifier = 0
        i = 0

        # Sets limits based on population
        if self.uwp[5] == 0 or self.uwp[5] == 7: modifier = 1
        if self.uwp[5] >= 10: modifier = -1

        # Rolls number of factions and assigns strength and culture
        rolls = random.randint(1, 3) + modifier
        while i in range(rolls):
            i += 1
            faction_strength = d(2,6,0)
            faction_culture = self.culture_types(dsixtysix(0, 0))
            if faction_strength <= 3: factions.append(['Obscure', faction_culture])
            if faction_strength == 4 or faction_strength == 5: factions.append(['Fringe', faction_culture])
            if faction_strength == 6 or faction_strength == 7: factions.append(['Minor', faction_culture])
            if faction_strength == 8 or faction_strength == 9: factions.append(['Notable', faction_culture])
            if faction_strength == 10 or faction_strength == 11: factions.append(['Significant', faction_culture])
            if faction_strength >= 12: factions.append(['Overwhelming', faction_culture])
        self.factions = factions

    # Determines the law level of the planetary government
    def generate_law_level(self):
        # Makes flat roll with population modifier
        self.uwp[6] = d(2,6,-7) + self.uwp[5]
        if self.uwp[6] < 0: self.uwp[6] = 0

    # Determines tech level from planet's variables
    def generate_tech_level(self):
        self.uwp[7] = random.randint(1, 6)

        # Starport
        if self.uwp[0] == 'A': self.uwp[7] += 6
        if self.uwp[0] == 'B': self.uwp[7] += 4
        if self.uwp[0] == 'C': self.uwp[7] += 2

        # Size
        if self.uwp[1] == 0 or self.uwp[1] == 1: self.uwp[7] += 2
        if self.uwp[1] >= 3 and self.uwp[1] <= 4: self.uwp[7] += 1

        # Atmosphere
        if self.uwp[2] <= 3 or self.uwp[2] >= 10: self.uwp[7] += 1

        # Hydrosphere
        if self.uwp[3] == 0 or self.uwp[3] == 9: self.uwp[7] += 1
        if self.uwp[3] == 10: self.uwp[7] += 2

        # Population
        if self.uwp[4] >= 1 and self.uwp[4] <= 5: self.uwp[7] += 1
        if self.uwp[4] == 9: self.uwp[7] += 1
        if self.uwp[4] == 10: self.uwp[7] += 2
        if self.uwp[4] == 11: self.uwp[7] += 3
        if self.uwp[4] == 12: self.uwp[7] += 4

        # Government
        if self.uwp[5] == 0 or self.uwp[5] == 5: self.uwp[7] += 1
        if self.uwp[5] == 7: self.uwp[7] += 2
        if self.uwp[5] == 13 or self.uwp[5] == 14: self.uwp[7] -= 2

        # TL Minimums (Atmosphere)
        if self.uwp[7] <= 10 and self.uwp[2] == 12: self.uwp[7] = 10
        if self.uwp[7] <= 9 and self.uwp[2] == 11: self.uwp[7] = 9
        if self.uwp[7] <= 8:
            if self.uwp[2] == 10 or self.uwp[2] == 15: self.uwp[7] = 8
            if self.uwp[2] <= 1: self.uwp[7] = 8
        if self.uwp[7] <= 5:
            if self.uwp[2] == 2 or self.uwp[2] == 3: self.uwp[7] = 5
            if self.uwp[2] == 13 or self.uwp[2] == 14: self.uwp[7] = 5
        if self.uwp[7] <= 3:
            if self.uwp[2] == 4: self.uwp[7] = 3
            if self.uwp[2] == 7: self.uwp[7] = 3
            if self.uwp[2] == 9: self.uwp[7] = 3

    # Determines which travel codes are applicable to the planet
    def generate_travel_codes(self):
        self.codes = []

        # Agricultural
        if self.uwp[2] >= 4 and self.uwp[2] <= 9:
            if self.uwp[3] >= 4 and self.uwp[3] <= 8:
                if self.uwp[4] >= 5 and self.uwp[4] <= 7:
                    self.codes.append('Ag')

        # Asteroid
        if self.uwp[1] == 0:
            if self.uwp[2] == 0:
                if self.uwp[3] == 0:
                    self.codes.append('As')

        # Barren
        if self.uwp[4] == 0:
            if self.uwp[5] == 0:
                if self.uwp[6] == 0:
                    self.codes.append('Ba')

        # Desert
        if self.uwp[2] >= 2 and self.uwp[3] == 0: self.codes.append('De')

        # Fluid Oceans
        if self.uwp[2] >= 10 and self.uwp[3] >= 1: self.codes.append('Fl')

        # Garden
        if self.uwp[1] >= 5:
            if self.uwp[2] >= 4 and self.uwp[2] <= 9:
                if self.uwp[3] >= 4 and self.uwp[3] <= 8:
                    self.codes.append('Ga')

        # High Population
        if self.uwp[4] >= 9: self.codes.append('Hi')

        # High Technology
        if self.uwp[7] >= 12: self.codes.append('Ht')

        # Ice-Capped
        if self.uwp[2] <= 1 and self.uwp[3] >= 1: self.codes.append('IC')

        # Industrial
        if self.uwp[4] >= 9:
            if self.uwp[2] <= 2 or self.uwp[2] == 4: self.codes.append('In')
            if self.uwp[2] == 7 or self.uwp[2] == 9: self.codes.append('In')

        # Low Population
        if self.uwp[4] >= 1 and self.uwp[4] <= 3: self.codes.append('Lo')

        # Low Technology
        if self.uwp[7] <= 5: self.codes.append('Lt')

        # Non-Agricultural
        if self.uwp[2] <= 3 and self.uwp[3] <= 3:
            if self.uwp[4] >= 6: self.codes.append('Na')

        # Non-Industrial
        if self.uwp[4] >= 4 and self.uwp[4] <= 6: self.codes.append('NI')

        # Poor
        if self.uwp[2] >= 2 and self.uwp[2] <= 5:
            if self.uwp[3] <= 3: self.codes.append('Po')

        # Rich
        if self.uwp[2] == 6 or self.uwp[2] == 8:
            if self.uwp[4] >= 6 and self.uwp[4] <= 8: self.codes.append('Ri')

        # Vacuum
        if self.uwp[2] == 0: self.codes.append('Va')

        # Water World
        if self.uwp[3] == 10: self.codes.append('Wa')

    # Formats a readable string from the planet's UWP data
    def return_uwp(self):
        uwp_string = self.uwp[0] + hexSwitch(self.uwp[1]) + hexSwitch(self.uwp[2]) + hexSwitch(
            self.uwp[3]) + hexSwitch(self.uwp[4]) + hexSwitch(self.uwp[5]) + hexSwitch(
            self.uwp[6]) + '-' + hexSwitch(self.uwp[7])
        return uwp_string

    # Formats a readable string of travel codes
    def travel_codes_format(self):
        printString = ''
        for i in range(len(self.codes)):
            printString = printString + self.codes[i] + ' '
        return printString

    # Formats hex, name, UWP, and travel codes for printing
    def return_tagline(self):
        if len(self.codes) == 0: tagline = self.hex + ' ' + self.name + ' ' + self.return_uwp()
        if len(
                self.codes) >= 1: tagline = self.hex + ' ' + self.name + ' ' + self.return_uwp() + ' ' + self.travel_codes_format()
        return tagline

    # Formats PPE for printing
    def assess_ppe(self):
        # Determines the PPE needed to survive on the surface.
        ppe = []
        if self.vaccSuit == True:
            ppe.append('Vacc Suit')
        if self.respirator == True:
            ppe.append('Respirator')
        if self.filter == True:
            ppe.append('Filter')
        if self.airSupply == True:
            ppe.append('Air Supply')
        if self.ppeVaries == True:
            ppe.append('Varies')

        # Improved PPE string return
        printString = 'PPE: '
        for i in range(len(ppe)):
            if i < len(ppe) - 1:
                printString = printString + ppe[i] + ', '
            if i == len(ppe) - 1:
                printString = printString + ppe[i]
        return printString

    # Determines if any bases are available in/around the planet
    def generate_bases(self):
        self.bases = []

        # Excellent Quality Starbase
        if self.uwp[0] == 'A':
            base_rolls = [0, 0, 0, 0, 0]
            for i in range(len(base_rolls)):
                base_rolls[i - 1] = d(2,6,0)
            if base_rolls[0] >= 8: self.bases.append('Naval')
            if base_rolls[1] >= 10: self.bases.append('Scout')
            if base_rolls[2] >= 8: self.bases.append('Research')
            if base_rolls[3] >= 4: self.bases.append('TAS/TT')
            if base_rolls[4] >= 6: self.bases.append('Imperial Consulate')

        # Good Quality Starport
        if self.uwp[0] == 'B':
            base_rolls = [0, 0, 0, 0, 0, 0]
            for i in range(len(base_rolls)):
                base_rolls[i - 1] = d(2,6,0)
            if base_rolls[0] >= 8: self.bases.append('Naval')
            if base_rolls[1] >= 8: self.bases.append('Scout')
            if base_rolls[2] >= 10: self.bases.append('Research')
            if base_rolls[3] >= 6: self.bases.append('TAS/TT')
            if base_rolls[4] >= 8: self.bases.append('Imperial Consulate')
            if base_rolls[5] >= 12: self.bases.append('Pirate')

        # Routine Quality Starport
        if self.uwp[0] == 'C':
            base_rolls = [0, 0, 0, 0, 0]
            for i in range(len(base_rolls)):
                base_rolls[i - 1] = d(2,6,0)
            if base_rolls[0] >= 8: self.bases.append('Scout')
            if base_rolls[1] >= 10: self.bases.append('Research')
            if base_rolls[2] >= 10: self.bases.append('TAS/TT')
            if base_rolls[3] >= 10: self.bases.append('Imperial Consulate')
            if base_rolls[4] >= 10: self.bases.append('Pirate')

        # Poor Quality Starport
        if self.uwp[0] == 'D':
            base_rolls = [0, 0]
            for i in range(len(base_rolls)):
                base_rolls[i - 1] = d(2,6,0)
            if base_rolls[0] >= 8: self.bases.append('Scout')
            if base_rolls[1] >= 10: self.bases.append('Pirate')

        # No Starport
        if self.uwp[0] == 'E':
            x = d(2,6,0)
            if x >= 12: self.bases.append('Pirate')

    # Assigns a language base to the planet
    def generate_language(self):
        anglo_american = ['English']
        african = ['Bantu', 'Kongo', 'Ashandi', 'Zulu', 'Swahili']
        japanese_korean = ['Japanese', 'Korean']
        central_european_soviet = ['Bulgarian', 'Russian', 'Czech', 'Polish', 'Ukranian', 'Slovak']
        pacific_islander = ['Microneasian', 'Tagalog', 'Polynesian', 'Malayan', 'Sudanese', 'Indonesian', 'Hawaiian']
        chinese_southeast_asian = ['Burmese', 'Cantonese', 'Mandarin', 'Thai', 'Tibetan', 'Vietnamese']
        future_punk = ['Lingua Astra', 'Alien Language']
        hispanic_american = ['English', 'Spanish']
        central_south_american = ['Spanish', 'Portuguese']
        european = ['French', 'German', 'English', 'Spanish', 'Italian', 'Greek', 'Danish', 'Dutch', 'Norwegian',
                    'Swedish', 'Finnish']
        languages = [anglo_american, african, japanese_korean, central_european_soviet, pacific_islander,
                     chinese_southeast_asian, future_punk, hispanic_american, central_south_american, european]
        self.language = random.choice(random.choice(languages))

    # Prints planet
    def print(self):
        print()
        print('PLANET')
        print(self.return_tagline())
        if self.uwp[0] == 'X': print('No Starport | Berth ' + str(self.berthingCost) + ' Cr.')
        if self.uwp[0] != 'X': print(
            self.starportQuality + ' Starport Quality | Berth ' + str(self.berthingCost) + ' Cr.')
        print(self.fuel + ' | ' + self.facilities)
        if self.lowGravity == True:
            print('Diameter: ' + str(self.size) + 'km (' + str(self.surfaceGravity) + 'gs) | Low Grav. Wrn. (' + str(
                random.randint(1, 6)) + ' weeks acc.)')
        if self.highGravity == True:
            print('Diameter: ' + str(self.size) + 'km (' + str(self.surfaceGravity) + 'gs) | High Grav. Wrn. (' + str(
                random.randint(1, 6)) + ' weeks acc.)')
        if self.highGravity == False and self.lowGravity == False:
            print('Diameter: ' + str(self.size) + 'km (' + str(self.surfaceGravity) + 'gs)')
        if self.taintedAtmosphere == False: print(self.atmosphere + ' Atmosphere | ' +
                                                  str(self.hydrosphere) + '% Liquid Ocean')
        if self.taintedAtmosphere == True: print(self.atmosphere + ', Tainted Atmosphere | ' +
                                                 str(self.hydrosphere) + '% Liquid Ocean')
        if self.temperatureSwings == True: print('Warning: Temp Swings Wildly following Circadian Rhythm')
        if self.temperatureSwings == False: print(
            self.climate[2] + ' Climate | High ' + str(self.climate[1]) + '°C | Low ' + str(self.climate[0]) + '°C')
        if self.vaccSuit == True or self.respirator == True or self.filter == True or self.airSupply == True or self.ppeVaries == True:
            print(self.assess_ppe())
        print(self.government + ' | ' + self.culture + ' | Law ' + str(self.uwp[6]))
        print('pop. ' + str(self.population) + ' | ' + str(self.population_density) + ' people per sqkm')
        print('Language Base: ' + self.language)
        print('Known Factions:')
        for i in range(len(self.factions)):
            faction_to_print = self.factions[i]
            print(str(i + 1) + '. ' + faction_to_print[0] + ', ' + faction_to_print[1])
        if len(self.bases) >= 1: print(self.bases)
        if len(self.bases) <= 0: print('No Bases Nearby')

    # Master subprogram for generating a planet
    def generate(self, hex_field, printX):
        self.generate_hex(hex_field)
        self.generate_name()
        self.generate_starport(d(2,6,0))
        self.generate_size(d(2,6,-2))
        self.generate_atmosphere(d(2,6,-7) + self.uwp[1])
        self.generate_climate()
        self.generate_hydrographics()
        self.generate_population()
        self.generate_government_and_culture()
        self.generate_factions()
        self.generate_law_level()
        self.generate_tech_level()
        self.generate_travel_codes()
        self.generate_bases()
        self.generate_language()
        if printX == True:
            self.print()
            print()


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


def spawnPlanet(hex_field, printX):
    hallowsbelt = planet()

    # hallowsbelt.generate() contains .generate_hex(hex_field), which takes the first from the 'hex_field'
    # list, and then removes it from a list.
    hallowsbelt.generate(hex_field, printX)
    return hallowsbelt


# Generates & returns a galaxy based on (y, x), 50% inhabited hexes
# Uses generateHexList()
def generateGalaxy(rows, columns):
    hexField = generateHexList(rows, columns)
    galaxy = []
    for l in range(len(hexField)):
        hallowsbelt = spawnPlanet(hexField, False)
        galaxy.append(hallowsbelt)
    return galaxy


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


#   _____ ____  _____________       _____    ____  ______
#  / ___// __ \/ ____/_  __/ |     / /   |  / __ \/ ____/
#  \__ \/ / / / /_    / /  | | /| / / /| | / /_/ / __/
# ___/ / /_/ / __/   / /   | |/ |/ / ___ |/ _, _/ /___
# /____/\____/_/     /_/    |__/|__/_/  |_/_/ |_/_____/
# SOFTWARE FOR PERSONAL AND SHIP COMPUTERS

class program():
    def __init__(self, name, shipSoftware, tl, rating, cost, description):
        self.name = name
        self.shipSoftware = name
        self.tl = tl
        self.rating = rating
        self.skill = 'none'
        self.dm = -3
        self.cost = cost
        self.description = description

    def setSkill(self, skill, dm):
        self.skill = skill
        self.dm = dm

    def info(self):
        print(self.name + ': ' + self.description)

    # Manoeuvre Software


manoeuvre0 = program('Manoeuvre/0', True, 8, 9, 0, 'Allows basic control of ship')

# Voice Command Software
intellect = program('Intellect', True, 11, 10, 1, 'Allows verbal commands.')

# Jump Drive Control Software
jumpControl1 = program('Jump Control/1', True, 9, 5, 100000, 'Allows Auto-Jump/1')
jumpControl2 = program('Jump Control/2', True, 11, 10, 200000, 'Allows Auto-Jump/2')
jumpControl3 = program('Jump Control/3', True, 12, 15, 300000, 'Allows Auto-Jump/3')
jumpControl4 = program('Jump Control/4', True, 13, 20, 400000, 'Allows Auto-Jump/4')
jumpControl5 = program('Jump Control/5', True, 14, 25, 500000, 'Allows Auto-Jump/5')
jumpControl6 = program('Jump Control/6', True, 15, 30, 600000, 'Allows Auto-Jump/6')

# Evasive Manoeuvre Software
evade1 = program('Evade/1', True, 9, 10, 1000000, 'Auto-Evade, 1 Dodge, -1 DM')
evade2 = program('Evade/2', True, 11, 15, 2000000, 'Auto-Evade, 2 Dodges, -1 DM')
evade3 = program('Evade/3', True, 13, 25, 3000000, 'Auto-Evade, 3 Dodges, -1 DM')

# Fire Control Software
fireControl1 = program('Fire Control/1', True, 9, 5, 2000000, 'Fire 1 weapon or give +1 DM')
fireControl2 = program('Fire Control/2', True, 10, 10, 4000000, 'Fire 2 weapons or give +2 DM')
fireControl3 = program('Fire Control/3', True, 10, 15, 6000000, 'Fire 3 weapons or give +3 DM')
fireControl4 = program('Fire Control/4', True, 10, 20, 8000000, 'Fire 4 weapons or give +4 DM')
fireControl5 = program('Fire Control/5', True, 10, 25, 10000000, 'Fire 5 weapons or give +5 DM')

# Repair Drone Software
autoRepair1 = program('Auto-Repair/1', 1, 10, 10, 5000000, '1 Repair Attempt or give +1 DM')
autoRepair2 = program('Auto-Repair/2', 2, 12, 20, 10000000, '2 Repair Attempts or give +2 DM')

# Database Software
library = program('Library', 0, 8, 0, 0, 'Contains a wealth of knowledge')

jumpControlSoftware = [jumpControl1, jumpControl2, jumpControl3, jumpControl4, jumpControl5, jumpControl6]
evadeSoftware = [evade1, evade2, evade3]
fireControlSoftware = [fireControl1, fireControl2, fireControl3, fireControl4, fireControl5]
autoRepairSoftware = [autoRepair1, autoRepair2]

# Database Software
database = program('Database', False, 7, 0, random.randint(10, 10000),
                   'Store of information, can be checked with agent.')

# Human-Machine Interface Software
interface = program('Interface', False, 7, 0, 0, 'Displays data.')

# Security Software
security0 = program('Security/0', False, 7, 0, 0, 'Average +0 Security Program')
security1 = program('Security/1', False, 9, 1, 200, 'Difficult -2 Security Program')
security2 = program('Security/2', False, 11, 2, 1000, 'Very Difficult -4 Security Program')
security3 = program('Security/3', False, 12, 3, 20000, 'Formidible -6 Security Program')

# Translation Software
translator0 = program('Translator/0', False, 9, 0, 50, 'Near real-time specialized language program')
translator1 = program('Translator/1', False, 10, 1, 500, 'Real-time specialized language program')

# Intrusion Software
intrusion1 = program('Intrusion/1', False, 10, 1, 1000, 'Level 1 Hacking Program')
intrusion2 = program('Intrusion/2', False, 11, 2, 10000, 'Level 2 Hacking Program')
intrusion3 = program('Intrusion/3', False, 13, 3, 100000, 'Level 3 Hacking Program')
intrusion4 = program('Intrusion/4', False, 15, 4, -1, 'Level 4 Hacking Program')

# Vocal and Human-Controlled Expert Programming
intelligentInterface = program('Intelligent Interface', False, 11, 1, 100, 'Voice Control and Intelligent Data Display')

# Skill Programming
expert1 = program('Expert/1', False, 11, 1, 1000, 'Skill-based Expert Program')
expert2 = program('Expert/2', False, 12, 2, 10000, 'Skill-based Expert Program')
expert3 = program('Expert/3', False, 13, 3, 100000, 'Skill-based Expert Program')

# Computer-Controlled Computer Programming
agent0 = program('Agent/0', False, 11, 0, 500, 'AI with Computer 0')
agent1 = program('Agent/1', False, 12, 1, 2000, 'AI with Computer 1')
agent2 = program('Agent/2', False, 13, 2, 100000, 'AI with Computer 2')
agent3 = program('Agent/3', False, 14, 3, 250000, 'AI with Computer 3')

# Computer-Controlled Expert Programming
intellect1 = program('Intellect/1', False, 12, 1, 2000, 'AI for Expert Programming')
intellect2 = program('Intellect/2', False, 13, 2, 50000, 'AI for Expert Programming')
intellect3 = program('Intellect/3', False, 14, 3, -1, 'AI for Expert Programming')

computerSoftwareList = [[database],
                        [interface],
                        [security0, security1, security2, security3],
                        [translator0, translator1],
                        [intrusion1, intrusion2, intrusion3, intrusion4],
                        [intelligentInterface],
                        [expert1, expert2, expert3],
                        [agent0, agent1, agent2, agent3],
                        [intellect1, intellect2, intellect3]]


#   __________  __  _______  __  __________________  _____
#  / ____/ __ \/  |/  / __ \/ / / /_  __/ ____/ __ \/ ___/
# / /   / / / / /|_/ / /_/ / / / / / / / __/ / /_/ /\__ \
# / /___/ /_/ / /  / / ____/ /_/ / / / / /___/ _, _/___/ /
# \____/\____/_/  /_/_/    \____/ /_/ /_____/_/ |_|/____/
# SHIP AND PERSONAL COMPUTATIONAL DEVICES

class computer():
    def __init__(self, name, shipComputer, tl, power, mass, cost):
        self.name = name
        self.shipComputer = shipComputer
        self.bis = False
        self.fib = False
        self.tl = tl
        self.power = power
        self.programs = []
        self.softwareCost = 0
        self.mass = mass
        self.cost = cost

    def prototech(self, homeworld_tl):
        tlBelow = self.tl - homeworld_tl
        if tlBelow > 0 and tlBelow <= 2:
            self.name = 'Prototech ' + self.name
            self.tl -= tlBelow
            if tlBelow == 1:
                self.mass = self.mass * 10
                self.cost = self.cost * 10
            if tlBelow == 2:
                self.mass = self.mass * 100
                self.cost = self.cost * 100
        if tlBelow <= 0 or tlBelow > 2:
            print('prototech() TL error')

    def retrotech(self, homeworld_tl):
        self.name = 'Retrotech ' + self.name
        tl_difference = homeworld_tl - self.tl
        self.tl = homeworld_tl
        for i in range(tl_difference):
            self.mass = self.mass / 2
            self.cost = self.cost / 2

    def techShift(self, homeworld_tl):  # Determines proto- or retrotech level
        if homeworld_tl < self.tl:  # to apply to computer technology.
            if self.tl - homeworld_tl <= 2:
                self.prototech(homeworld_tl)
            if self.tl - homeworld_tl > 2:
                self.prototech(self.tl + 2)
        if homeworld_tl > self.tl:
            self.retrotech(homeworld_tl)

    def install(self, program):
        self.programs.append(program)
        self.softwareCost += program.cost

    def shipComputerOptions(self, option):
        self.bis = False
        self.fib = False
        if option == 'bis':
            self.bis = True
            self.cost = self.cost * 1.5
        if option == 'fib':
            self.fib = True
            self.cost += 1000000
        if option == 'both':
            self.bis = True
            self.fib = True
            self.cost = self.cost * 2

    def initializeShipSoftware(self, vessel, programTheme):
        self.programs = []

        self.install(manoeuvre0)

        if programTheme == 'random':
            x = d(2,6,0)
            if x > 8: self.install(intellect)

        jumpCapacity = vessel.jumpDrive[1]
        if self.bis == True: jumpCapacity += 5
        if jumpCapacity == 6: self.install(jumpControl6)
        if jumpCapacity == 5: self.install(jumpControl5)
        if jumpCapacity == 4: self.install(jumpControl4)
        if jumpCapacity == 3: self.install(jumpControl3)
        if jumpCapacity == 2: self.install(jumpControl2)
        if jumpCapacity == 1: self.install(jumpControl1)

        if programTheme == 'random':
            x = d(2,6,0)
            if x > 8: self.install(random.choice(evadeSoftware))

        if programTheme == 'random':
            x = d(2,6,0)
            if x > 8: self.install(random.choice(fireControlSoftware))

        # Library is installed with autoRepair in vessel vehicle options

    def info(self, fromEquipment):
        if self.shipComputer == False:
            if fromEquipment == False: print(self.name + ' | TL ' + str(self.tl))
            if fromEquipment == True: print(self.name)
            if fromEquipment == False:
                if self.mass >= 1: print(str(self.mass) + ' kg | ' + str(self.cost) + ' Cr.')
                if self.mass < 1: print(str(self.mass * 1000) + ' g | ' + str(self.cost) + ' Cr.')

            if self.programs == []: print('No programs loaded on this device')
            if self.programs != []:
                for i in range(len(self.programs)):
                    print(self.programs[i].name)
            if fromEquipment == False: print('Software Cost: ' + str(self.softwareCost) + ' Cr.')


model1 = computer('Model 1', True, 7, 5, 0, 30000)
model2 = computer('Model 2', True, 9, 10, 0, 160000)
model3 = computer('Model 3', True, 11, 15, 0, 2000000)
model4 = computer('Model 4', True, 12, 20, 0, 5000000)
model5 = computer('Model 5', True, 13, 25, 0, 10000000)
model6 = computer('Model 6', True, 14, 30, 0, 20000000)
model7 = computer('Model 7', True, 15, 35, 0, 30000000)

shipComputersList = [model1, model2, model3, model4, model5, model6, model7]

computer0 = computer('Computer/0', False, 7, 0, 10, 50)
tl8_computer1 = computer('Computer/1', False, 8, 1, 5, 250)
tl9_computer1 = computer('Computer/1', False, 9, 1, 5, 100)
tl10_computer2 = computer('Computer/2', False, 10, 2, 1, 500)
tl11_computer2 = computer('Computer/2', False, 11, 2, 1, 350)
computer3 = computer('Computer/3', False, 12, 3, 0.5, 1000)
computer4 = computer('Computer/4', False, 13, 4, 0.5, 1500)
computer5 = computer('Computer/5', False, 14, 5, 0.5, 5000)

computerTerminal = computer('Computer Terminal', False, 7, 0, 3, 200)

tl7_handComputer = computer('Hand Computer/0', False, 7, 0, 5, 100)
tl8_handComputer = computer('Hand Computer/1', False, 8, 1, 2.5, 500)
tl9_handComputer = computer('Hand Computer/1', False, 9, 1, 2.5, 200)
tl10_handComputer = computer('Hand Computer/2', False, 10, 2, 0.5, 1000)
tl11_handComputer = computer('Hand Computer/2', False, 11, 2, 0.5, 700)
tl12_handComputer = computer('hand Computer/3', False, 12, 3, 0.25, 2000)
tl13_handComputer = computer('Hand Computer/4', False, 13, 4, 0.25, 3000)
tl14_handComputer = computer('Hand Computer/5', False, 14, 5, 0.25, 10000)

computersList = [[computer0, tl8_computer1, tl9_computer1, tl10_computer2,
                  tl11_computer2, computer3, computer4, computer5],
                 [computerTerminal],
                 [tl7_handComputer, tl8_handComputer, tl9_handComputer, tl10_handComputer,
                  tl11_handComputer, tl12_handComputer, tl13_handComputer, tl14_handComputer]]


#    __________  __  __________  __  __________   ________
#   / ____/ __ \/ / / /  _/ __ \/  |/  / ____/ | / /_  __/
#  / __/ / / / / / / // // /_/ / /|_/ / __/ /  |/ / / /
# / /___/ /_/ / /_/ // // ____/ /  / / /___/ /|  / / /
# /_____/\___\_\____/___/_/   /_/  /_/_____/_/ |_/ /_/
# ITEMS, TOOLS, DRUGS, ANYTHING BUT COMPUTERS AND GUNS.

class equipment():
    def __init__(self, name, skill, description, tl, mass, cost):
        self.name = name
        self.skill = skill
        self.description = description
        self.tl = tl
        self.mass = mass
        self.cost = cost
        self.computerInstalled = False
        self.computer = 0

    def installComputer(self, computerToInstall):
        self.computerInstalled = True
        self.computer = computerToInstall

    def info(self):
        print(self.name + ' | TL ' + str(self.tl))
        print(self.description)
        print(str(self.mass) + ' kg | ' + str(self.cost) + ' Cr.')
        print('Skill for use: ' + self.skill)
        if self.computerInstalled == True:
            self.computer.info(True)

    # Communications

    # Bugs


tl5_bug = equipment('Bug', 'Recon', 'Audio Surveillance Device', 5, 3, 50)
tl7_bug = equipment('Bug', 'Recon', 'Audio or Visual', 7, 2, 50)
tl9_bug = equipment('Bug', 'Recon', 'Audio or visual or Data', 9, 1, 50)
tl11_bug = equipment('Bug', 'Recon', 'Audio/Visual/Data', 11, 0.1, 50)
tl13_bug = equipment('Bug', 'Recon', 'Audio/Visual/Data/Bioscan', 13, 0.01, 50)
tl15_bug = equipment('Bug', 'Recon', 'Audio/Visual/Data/Bioscan', 15, 0, 50)
tl15_bug.installComputer(tl8_computer1)

bugs_list = [tl5_bug, tl7_bug, tl9_bug, tl11_bug, tl13_bug, tl15_bug, tl15_bug]

# Tranceivers
tl5_radio_tranceiver = equipment('Radio Tranceiver', 'Comms', 'Range: 5 km', 5, 20, 50)
tl8_radio_tranceiver = equipment('Radio Tranceiver', 'Comms', 'Range: 5 km', 8, 2, 100)
tl9_radio_tranceiver = equipment('Radio Tranceiver', 'Comms', 'Range: 50 km', 9, 1, 250)
tl9_radio_tranceiver.installComputer(computer0)
tl12_radio_tranceiver = equipment('Radio Tranceiver', 'Comms', 'Range: 500 km', 12, 1, 500)
tl12_radio_tranceiver.installComputer(computer0)
tl13_radio_tranceiver = equipment('Radio Tranceiver', 'Comms', 'Range: 5000 km', 13, 1, 1000)
tl13_radio_tranceiver.installComputer(tl8_computer1)
tl9_laser_tranceiver = equipment('Laser Tranceiver', 'Comms', 'Range: 500 km', 9, 1.5, 100)
tl11_laser_tranceiver = equipment('Laser Tranceiver', 'Comms', 'Range: 500 km', 11, 0.5, 250)
tl11_laser_tranceiver.installComputer(computer0)
tl13_laser_tranceiver = equipment('Laser Tranceiver', 'Comms', 'Range: 500 km', 13, 0, 500)
tl13_laser_tranceiver.installComputer(tl8_computer1)

tranceivers_list = [tl5_radio_tranceiver, tl8_radio_tranceiver, tl9_radio_tranceiver, tl12_radio_tranceiver,
                    tl13_radio_tranceiver, tl9_laser_tranceiver, tl11_laser_tranceiver, tl13_laser_tranceiver]

# Comms
tl6_comm = equipment('Comm', 'Comms', 'Audio Only', 6, 1, 50)
tl8_comm = equipment('Comm', 'Comms', 'Audio and Visual', 8, 1, 150)
tl8_comm.installComputer(computer0)
tl10_comm = equipment('Comm', 'Comms', 'Multiple forms of data', 10, 1, 500)
tl10_comm.installComputer(tl8_computer1)

comms_list = [tl6_comm, tl8_comm, tl10_comm]

# Options
data_display_recorder = equipment('Data Display/Recorder', 'unknown', 'HUD Headpiece', 13, 1, 5000)
data_wafer = equipment('Data Wafer', 'n/a', 'Info Storage', 10, 0, 5)

computersEquipmentList = [data_display_recorder, data_wafer]

# ________________________________
# Medical Supplies

cryoberth = equipment('Cryoberth', 'Cryotech', 'Medical Cryogenics Contrainer', 10, 200, 50000)

# Medikits
tl8_medikit = equipment('Medikit', 'Medic', 'Advanced Medical Kit', 8, 8, 1000)
tl10_medikit = equipment('Medikit', 'Medic', 'Advanced Medical Kit', 10, 8, 1500)
tl12_medikit = equipment('Medikit', 'Medic', 'Advanced Medical Kit', 12, 8, 5000)
tl14_medikit = equipment('Medikit', 'Medic', 'Advanced Medical Kit', 14, 8, 10000)

# Drugs
medicinal_drugs = equipment('Medicinal Drugs', 'Medic', 'Basic Medicinal Drugs', 5, 2, 10)
panaceas = equipment('Panaceas', 'Medic', 'Wide-Spectrum Medicinal Drug Dose', 8, 1, 200)
antirad_drugs = equipment('Anto-Rad Drugs', 'Medic', 'Anti-Radiation Drugs', 8, 1, 1000)
stim_drugs = equipment('Stim Drugs', 'Medic', 'Reduce Fatigue at a Cost', 8, 1, 50)
metabolic_accelerator = equipment('Metabolic Accelerator', 'Medic', 'Slow Drug', 10, 1, 500)
combat_drug = equipment('Combat Drug', 'Medic', 'Adds initiative and extra dodge', 10, 1, 1000)
medicinal_slow = equipment('Medicinal Slow', 'Medic', 'Medical-Grade Metabolic Accelerator', 11, 1, 500)
fast_drug = equipment('Fast Drug', 'Medic', 'Suspended Animation Drug', 10, 1, 200)
anagathics = equipment('Anagathics', 'Medic', 'anti-Aging Drugs', 15, 1, 2000)

medical_supplies_list = [cryoberth, tl8_medikit, tl10_medikit, tl12_medikit, tl14_medikit, medicinal_drugs,
                         panaceas, antirad_drugs, stim_drugs, metabolic_accelerator, combat_drug, medicinal_slow,
                         fast_drug, anagathics]

# ________________________________
# Robots and Drones
cargo_robot = equipment('Cargo Robot', 'unknown', 'Simple heavy-Duty Robotics', 11, 500, 75000)
repair_robot = equipment('Repair Robot', 'unknown', 'Crab-Shaped Machine', 11, 10, 10000)
personal_drone = equipment('Personal Drone', 'unknown', 'Personal Holo-Projector', 11, 0.2, 2000)
probe_drone = equipment('Probe Drone', 'unkown', 'Hardened Personal Remote', 11, 6, 15000)
autodoc = equipment('Autodoc', 'unknown', 'Robot Doctor', 12, 100, 40000)
combat_drone = equipment('Combat Drone', 'unknown', 'Flying Guns', 12, 6, 90000)
servitor = equipment('Servitor', 'unknown', 'Robot Butler', 13, 9, 120000)

robots_list = [cargo_robot, repair_robot, personal_drone, probe_drone, autodoc, combat_drone, servitor]

# ________________________________
# Sensors
tl3_binoculars = equipment('Binoculars', 'Recon', 'Basic Pair of Binoculars', 3, 1, 75)
tl8_binoculars = equipment('Binoculars', 'Recon', 'Image Capture and Light Intenification', 8, 1, 750)
tl12_binoculars = equipment('Portable Radiation Imaging System', 'Sensors', 'EM-Spectrum Binoculars', 12, 2, 3500)
geiger_counter = equipment('Geiger Counter', 'Sensors', 'Detects radiation.', 5, 1, 250)
ir_goggles = equipment('IR Goggles', 'Recon', 'See Heat Signatures', 6, 1, 500)
tl7_li_goggles = equipment('Light-Intensifying Goggles', 'Recon', 'Night-Vision Goggles', 7, 1, 500)
tl9_li_goggles = equipment('Light-Intensifying Goggles', 'Recon', 'Night-Vision Goggles', 9, 1, 1250)
tl7_motion_sensor = equipment('Motion Sensor', 'Sensors', 'Detects Movement', 7, 4, 500)
tl9_motion_sensor = equipment('Motion Sensor', 'Sensors', 'Reports shape, size, duration', 9, 3, 1000)
electromagnetic_probe = equipment('Electromagnetic Probe', 'Sensors/Investigation', 'Detects EM Emissions', 10, 0.5,
                                  1000)
densitometer = equipment('Densitometer', 'Sensors', 'Measures density inside and out', 14, 5, 20000)
bioscanner = equipment('Bioscanner', 'Sensors/Life Sciences (Biology)', 'Analyzes biological matter', 15, 3.5, 350000)
nas = equipment('N.A.S.', 'Life Sciences (Biology)/Social Sciences (Sophontology)', 'Scans for neural activity', 15, 10,
                35000)

sensors_list = [tl3_binoculars, tl8_binoculars, tl12_binoculars, geiger_counter, ir_goggles, tl7_li_goggles,
                tl9_li_goggles, tl7_motion_sensor, tl9_motion_sensor, electromagnetic_probe, densitometer,
                bioscanner, nas]

# ________________________________
# Survival Gear and Supplies
tl3_tent = equipment('Tent', 'Survival', 'Basic Shelter for 2', 3, 3, 200)
tl7_tent = equipment('Tent', 'Survival', 'Pressurized Shelter for 2', 7, 5, 2000)
rebreather = equipment('Rebreather', 'n/a', 'Six hours of breathable atmosphere', 6, 10, 250)
tl6_respirator = equipment('Respirator', 'n/a', 'Oxygen Concentration', 6, 0.5, 100)
tl10_respirator = equipment('Respirator', 'n/a', 'Oxygen Concentration', 10, 0.1, 2000)
tl7_filter = equipment('Filter', 'n/a', 'Filters air', 7, 0.5, 100)
tl10_filter = equipment('Filter', 'n/a', 'Filters air', 10, 0.1, 2000)
breather_mask = equipment('Breather Mask', 'n/a', 'Filter + Respirator', 8, 0.5, 150)
artificial_gill = equipment('Artificial Gill', 'n/a', 'Extracts ocygen from water', 8, 4, 4000)
env_suit = equipment('Environment Suit', 'n/a', 'Protects against elements', 8, 3, 500)
tl8_habitat_mod = equipment('Habitat Module', 'n/a', 'Pop-up Living Quarters', 8, 15, 10000)
tl10_habitat_mod = equipment('Habitat Module', 'n/a', 'Pop-up Living Quarters', 10, 12, 20000)
rescue_bubble = equipment('Rescue Bubble', 'n/a', 'Lifeboat', 9, 1, 600)
tl9_thruster_pack = equipment('Thruster Pack', 'Zero-G', 'Jetpack', 9, 8, 2000)
tl12_thruster_pack = equipment('Thruster Pack', 'Zero-G', 'Jetpack', 12, 10, 14000)
tl14_thruster_pack = equipment('Thruster Pack', 'Zero-G', 'Jetpack', 14, 5, 20000)
portable_generator = equipment('Portable Generator', 'n/a', 'Fusion Generator', 10, 30, 500000)

survival_list = [tl3_tent, tl7_tent,
                 rebreather,
                 tl6_respirator, tl10_respirator,
                 tl7_filter, tl10_filter,
                 breather_mask, artificial_gill, env_suit,
                 tl8_habitat_mod, tl10_habitat_mod,
                 rescue_bubble,
                 tl9_thruster_pack, tl12_thruster_pack, tl14_thruster_pack,
                 portable_generator]

# ________________________________
# Toolkits
engineer_toolkit = equipment('Engineering Toolkit', 'Engineer (any)', 'Required for repairs or installation', 7, 12,
                             1000)
forensics_toolkit = equipment('Forensics Toolkit', 'Investigation', 'Required for testing samples and crime scenes', 7,
                              12, 1000)
mechanical_toolkit = equipment('Mechanical Toolkit', 'Mechanic', 'Required for repairs or construction', 7, 12, 1000)
scientific_toolkit = equipment('Scientific Toolkit', 'Science', 'Required for scientific testing', 7, 12, 1000)
surveying_toolkit = equipment('Surveying Toolkit', 'Space Science (any)', 'Required for planetary surveys', 7, 12, 1000)

toolkits_list = [mechanical_toolkit, forensics_toolkit, engineer_toolkit, scientific_toolkit, surveying_toolkit]

# Putting it all together
equipment_list = [bugs_list, tranceivers_list, comms_list, computersEquipmentList, medical_supplies_list, robots_list,
                  sensors_list, survival_list, toolkits_list]


#    ______________  _________    ____  __  ________
#   / ____/  _/ __ \/ ____/   |  / __ \/  |/  / ___/
#  / /_   / // /_/ / __/ / /| | / /_/ / /|_/ /\__ \
# / __/ _/ // _, _/ /___/ ___ |/ _, _/ /  / /___/ /
# /_/   /___/_/ |_/_____/_/  |_/_/ |_/_/  /_//____/
# GUNS, GUNS, GUNS, GUNS, GUNS

class firearm():
    def __init__(self, gunType, subtype, tl, accuracy, damageBase, damageDice, damageModifier, ammunition,
                 automaticFire, clipSize, rateOfFire, reliability, cost, gunRange, mass):
        self.origin = 'OriginErr'
        self.name = 'NameErr'
        self.type = gunType
        self.subtype = subtype
        self.tl = tl
        self.accuracy = accuracy
        self.damageBase = damageBase
        self.damageDice = damageDice
        self.damageMod = damageModifier
        self.ammo = ammunition
        self.auto = automaticFire
        self.clip = clipSize
        self.rof = rateOfFire
        self.reliability = reliability
        self.cost = cost
        self.range = gunRange
        self.mass = mass

    def designate(self, origin, name):
        self.origin = origin
        self.name = name

    def print(self):
        print(self.origin + ' ' + self.name)
        print(self.type + ' (' + self.subtype + ')')
        print('Acc: ' + str(self.accuracy) + ' | TL ' + str(self.tl))
        damage_string = str(self.damageBase) + 'd' + str(self.damageDice) + '+' + str(
            self.damageMod) + ' (' + self.ammo + ')'
        print(damage_string)
        # print(self.auto)
        print('Clip: ' + str(self.clip) + ' (' + str(self.rof) + ')')
        if self.reliability == 1: print('Unreliable')
        if self.reliability == 2: print('Standard Reliability')
        if self.reliability == 3: print('Very Reliable')
        print(str(self.cost) + ' Cr. | ' + str(self.range) + 'm | ' + str(self.mass) + 'kg')


# Sourceless Weapons
sw_combat_magnum = firearm('Revolver', 'Combat Magnum', 5, 1, 2, 6, 3, '.357', False, 6, 2, 3, 125, 50, 0.5)
revolver = firearm('Revolver', 'Medium', 5, -1, 3, 6, -3, 'RevAmmo', False, 6, 1, 2, 200, 50, 1)

# Cyberpunk Weapons
# Masses are 1 until I figure that shit out

# Light Autopistols
budgetArmsC13 = firearm('Autopistol', 'Light', 7, -1, 1, 6, 0, '5mm', False, 8, 2, 1, 75, 50, 0.5)
budgetArmsC13.designate('Earth', 'BudgetArms C-13')
lightAutopistols = [budgetArmsC13]

# Medium Autopistols
militechArmsAvenger = firearm('Autopistol', 'Medium', 7, 0, 2, 6, 1, '9mm', False, 10, 2, 3, 250, 50, 1)
militechArmsAvenger.designate('Earth', 'Militech Arms Avenger')
mediumAutopistols = [militechArmsAvenger]

# Heavy Autopistols
budgetArmsAuto3 = firearm('Autopistol', 'Heavy', 7, -1, 3, 6, 0, '11mm', False, 8, 2, 1, 350, 50, 1)
budgetArmsAuto3.designate('Earth', 'BudgetArms Auto 3')
heavyAutopistols = [budgetArmsAuto3]

# Very Heavy Autopistols
armalite44 = firearm('Autopistol', 'Very Heavy', 7, 0, 4, 6, 1, '11mm', False, 8, 1, 2, 450, 50, 1)
armalite44.designate('Earth', 'Armalite 44')
veryHeavyAutopistols = [armalite44]

# Light Submachineguns
uziMiniauto9 = firearm('Submachinegun', 'Light', 7, 1, 2, 6, 1, '9mm', False, 30, 35, 3, 475, 150, 1)
uziMiniauto9.designate('Earth', 'Uzi Miniauto 9')
lightSubmachineguns = [uziMiniauto9]

# Medium Submachineguns
arasakaMinami10 = firearm('Submachinegun', 'Medium', 7, 0, 2, 6, 3, '10mm', False, 40, 20, 3, 500, 200, 1)
arasakaMinami10.designate('Earth', 'Arasaka Minami 10')
mediumSubmachineguns = [arasakaMinami10]

# Heavy Submachineguns
sternmeyerSMG21 = firearm('Submachinegun', 'Heavy', 7, -1, 3, 6, 0, '11mm', False, 30, 15, 3, 500, 200, 1)
sternmeyerSMG21.designate('Earth', 'Sternmeyer SMG 21')
heavySubmachineguns = [sternmeyerSMG21]

# Light Assault Rifles
militechRoninLightAssault = firearm('Assault Rifle', 'Light', 7, 1, 5, 6, 0, '5.56', False, 35, 30, 3, 450, 400, 1)
militechRoninLightAssault.designate('Earth', 'Militech Ronin Light Assault')
lightAssaultRifles = [militechRoninLightAssault]

# Medium Assault Rifles
akr20MediumAssault = firearm('Assault Rifle', 'Medium', 7, 0, 5, 6, 0, '5.56', False, 30, 30, 2, 500, 400, 1)
akr20MediumAssault.designate('Earth', 'AKR-20 Medium Assault')
mediumAssaultRifles = [akr20MediumAssault]

# Heavy Assault Rifles
fnralHeavyAssaultRifle = firearm('Assault Rifle', 'Heavy', 7, -1, 6, 6, 0, '7.62', False, 30, 30, 3, 600, 400, 1)
fnralHeavyAssaultRifle.designate('Earth', 'AKR-20 Medium Assault')
heavyAssaultRifles = [fnralHeavyAssaultRifle]

# Shotguns
arasakaRapidAssault12 = firearm('Shotgun', 'None', 7, -1, 4, 6, 0, 'Shells', False, 20, 10, 2, 900, 50, 1)
arasakaRapidAssault12.designate('Earth', 'Arasaka Rapid Assault 12')
shotguns = [arasakaRapidAssault12]

# Heavy Weapons
barettArasakaLight20mm = firearm('Heavy Weapon', 'Heavy', 7, 0, 4, 10, 3, '20/9mm', False, 10, 1, 3, 2000, 450, 1)
barettArasakaLight20mm.designate('Earth', 'Barett-Arasaka Light 20mm')
heavyWeapons = [barettArasakaLight20mm]


# weapons_list = [sw_combat_magnum, budgetarms_c13, militech_ronin, revolver]

# _    __________________ ________   _____
# | |  / / ____/ ___/ ___// ____/ /  / ___/
# | | / / __/  \__ \\__ \/ __/ / /   \__ \
# | |/ / /___ ___/ /__/ / /___/ /______/ /
# |___/_____//____/____/_____/_____/____/
# SHIP CONSTRUCTION, PILOTING, MOUNTING (LOL)

class hardpoint():
    def __init__(self):
        self.designation = 'Hardpoint 0'
        self.isTurret = False
        self.turrets = 0
        self.isBay = False
        self.bay = []
        self.isScreen = False
        self.screen = []
        self.turretOne = []
        self.turretTwo = []
        self.turretThree = []
        self.tl = 0
        self.tons = 0
        self.price = 0
        self.range = 'None'
        self.damage = 'None'

    def installTurret(self, numTurrets, options):
        self.turrets = numTurrets
        if numTurrets == 0:
            self.designation = 'Empty'
            self.turrets = 0
            self.tl = 0
            self.price = 0
        if numTurrets == 1:
            self.designation = 'Single'
            self.turrets = 1
            self.tl = 7
            self.tons = 1
            self.price = 200000
        if numTurrets == 2:
            self.designation = 'Double'
            self.turrets = 2
            self.tl = 8
            self.tons = 1
            self.price = 500000
        if numTurrets == 3:
            self.designation = 'Triple'
            self.turrets = 3
            self.tl = 9
            self.tons = 1
            self.price = 1000000
        if options == 'popup':
            self.designation = self.designation + ' Pop-Up'
            self.tl = 10
            self.tons = 2
            self.price += 1000000
        if options == 'fixed':
            self.designation = self.designation + ' Fixed-Mount'
            self.tons = 0
            self.price = self.price * 0.5
        if options == 'both':
            self.designation = self.designation + ' Fixed-Mount Pop-Up'
            self.tl = 10
            self.tons = 1
            self.price = 0.5 * self.price + 500000
        self.designation = self.designation + ' Turret'

    def randomTurret(self):
        self.isTurret = True
        self.isBay = False
        self.isScreen = False

        options = ['none', 'popup', 'fixed']
        if random.randint(1, 4) == 4: options.append('both')
        turretRoll = random.randint(0, 3)
        if turretRoll <= 0: turretOption = 'none'
        if turretRoll > 0: turretOption = random.choice(options)
        self.installTurret(turretRoll, turretOption)
        self.installRandomTurretWeapons()

    def installRandomTurretWeapons(self):
        pulseLaser = ['Pulse Laser', 7, 'Short', '1d6', 500000]
        beamLaser = ['Beam Laser', 7, 'Medium', '2d6', 1000000]
        particleBeam = ['Particle Beam', 8, 'Long', '3d6 + crew hit', 4000000]
        missileRack = ['Missile Rack', 6, 'Special', 'Depends on missile', 750000]
        sandcaster = ['Sandcaster', 7, 'Special', 'Special', 250000]
        empty = ['Empty', 0, 'none', 'none', 0]
        turretWeapons = [pulseLaser, beamLaser, particleBeam, missileRack, sandcaster, empty]
        if self.turrets > 0:
            self.turretOne = random.choice(turretWeapons)
            self.price += self.turretOne[4]
        if self.turrets > 1:
            self.turretTwo = random.choice(turretWeapons)
            self.price += self.turretTwo[4]
        if self.turrets > 2:
            self.turretThree = random.choice(turretWeapons)
            self.price += self.turretThree[4]

    def installBay(self, bay):
        self.isTurret = False
        self.isBay = True
        self.isScreen = False

        missileBank = ['Missile Bank', 6, 'Special', 'Launch 12 Missiles', 12000000]
        particleBeam = ['Particle Beam', 8, 'Long', '6d6 + crew hit', 20000000]
        fusionGun = ['Fusion Gun', 12, 'Medium', '5d6', 8000000]
        mesonGun = ['Meson Gun', 11, 'Long', '5d6 + crew hit', 50000000]
        bays = [missileBank, particleBeam, fusionGun, mesonGun]
        if bay == 'missile': bayChoice = missileBank
        if bay == 'particle': bayChoice = particleBeam
        if bay == 'fusion': bayChoice = fusionGun
        if bay == 'meson': bayChoice = mesonGun
        if bay == 'random': bayChoice = random.choice(bays)
        self.designation = bayChoice[0]
        self.tl = bayChoice[1]
        self.range = bayChoice[2]
        self.damage = bayChoice[3]
        self.price = bayChoice[4]
        self.tons = 51

    def installScreen(self, screen):
        self.isTurret = False
        self.isBay = False
        self.isScreen = True

        nuclearDamper = ['Nuclear Damper', 12, 50, 50000000]
        mesonScreen = ['Meson Screen', 12, 50, 60000000]
        screens = [nuclearDamper, mesonScreen]
        if screen == 'nuclear': screenChoice = nuclearDamper
        if screen == 'meson': screenChoice = mesonScreen
        if screen == 'random': screenChoice = random.choice(screens)
        self.designation = screenChoice[0]
        self.tl = screenChoice[1]
        self.tons = screenChoice[2]
        self.price = screenChoice[3]


class vessel():
    def __init__(self):
        self.designation = 'Test Vessel'

        # Hull
        self.hullCode = 0  # Letter Code for Hull Mass
        self.hullMass = 0  # Mass of Hull in Tons
        self.config1 = 'config1Err'  # Hull Configuration Setting 1
        self.config2 = 'config2Err'  # Hull Configuration Setting 2
        self.armorType = ''  # Armor Configuration
        self.reflec = False  # Reflec Option
        self.selfSealing = False  # Self-Sealing Option
        self.stealth = False  # Stealth Option

        # Basic Stats
        self.hull = 0  # Hull Points
        self.structure = 0  # Structure Points
        self.armor = 0  # Armor Points

        # Engineering
        self.scope = 'scopeErr'  # Scope of Vessel's Drive Capability
        self.mannyDrive = ['<A', 0]  # Manoeuvre Drive Code, Thrust Rating
        self.jumpDrive = ['<A', 0]  # Jump Drive Code, Jump Rating
        self.jumpFuel = 0  # Amount of Fuel Used in Maximum Jump
        self.powerPlant = ['<A', 0]  # Power Plant Code and Fuel per 2 Weeks
        self.fuel = [0, 10]  # Current Fuel and Max Fuel Tank
        self.driveTons = [0, 0, 0]  # Tonnage of M-Drive, J-Drive, and Power Plant

        # Electronics
        self.computer = 'emptyShipComputer'  # Ship's Computer
        self.bis = False  # Jump Control Specialization
        self.fib = False  # EMP Defence Wiring
        self.sensorsSuite = []  # Sensors Installed in Ship

        # Hardpoints
        self.hardpoints = []  # Hardpoints Installed on Ship

        # Amenities
        self.passengers = 0  # Number of Planned Passengers
        self.staterooms = [0, 0, 0]  # Crew Staterooms, Passenger Staterooms, Low Berths
        self.lowBerths = 0  # Low Berths

        # Options & Cargo
        self.options = []  # Options Installed on Ship
        self.fuelScoops = False  # Fuel Scoops Installed on Hull
        self.fuelProcessors = 0  # Number of Fuel Processors Installed
        self.repairDrones = 0  # Tons of Repair Drones Onboard
        self.cargo = 0  # Tons of Cargo Space for Freight

        # Math Objects
        self.availableHull = 0  # Hull Left Available for Installations
        self.price = 0  # Price of the Ship
        self.mortgage = 0  # Mortgage to Buy Ship

    def constructHull(self, hullCode):
        if hullCode.isdigit() == False:
            if hullCode == 'random': self.hullCode = random.randint(1, 20)
            if hullCode != 'random': print("randomHull() Error: hullCode not 'random'")
        if hullCode.isdigit() == True: self.hullCode = hullCode
        self.hullMass = self.hullCode * 100
        self.availableHull = self.hullMass
        if self.hullCode == 1: self.price = 2000000
        if self.hullCode == 2: self.price = 8000000
        if self.hullCode == 3: self.price = 12000000
        if self.hullCode == 4: self.price = 16000000
        if self.hullCode == 5: self.price = 32000000
        if self.hullCode == 6: self.price = 48000000
        if self.hullCode == 7: self.price = 64000000
        if self.hullCode > 7: self.price = self.hullCode * 1000000
        self.hullCode = hexSwitch(self.hullCode)

    def determineHullStructure(self):
        points = int(self.hullMass // 50)
        self.hull = points
        self.structure = points

    def assignConfiguration(self, configuration):
        standard = ['Wedge', 'Cone', 'Sphere', 'Cylinder']
        streamlined = ['Wing', 'Disc', 'Other Lifting Body']
        distributed = ['Distributed']
        configurations = [standard, streamlined, distributed]
        self.config2 = configuration
        if configuration == 'random': self.config2 = random.choice(random.choice(configurations))
        if self.config2 in standard: self.config1 = 'Standard'
        if self.config2 in streamlined:
            self.config1 = 'Streamlined'
            self.price = self.price * 1.1
            self.fuelScoops = True
        if self.config2 == 'Distributed':
            self.config1 = 'Distributed'
            self.price = self.price * 0.9

    def installArmor(self, tit, cry, bon, randomSetting):

        # Determines the amount of mass the armor will take up
        if randomSetting == True: armorCount = random.randint(0, 4)
        if randomSetting == False: armorCount = tit + cry + bon
        fivePerc = self.hullMass * 0.05
        self.availableHull = self.availableHull - (armorCount * fivePerc)

        # Sets Values of the different Armors
        titanium = ['Titanium Steel', 2, 0.05]
        crystal = ['Crystaliron', 4, 0.2]
        bonded = ['Bonded Superdense', 6, 0.5]
        armorCost = 0

        if randomSetting == True:
            tit = 0
            cry = 0
            bon = 0

        # Adds price of the armor to the total cost
        for i in range(armorCount):
            if randomSetting == True:
                chosenArmor = random.choice([titanium, crystal, bonded])
                if chosenArmor[0] == 'Titanium Steel': tit += 1
                if chosenArmor[0] == 'Crystaliron': cry += 1
                if chosenArmor[0] == 'Bonded Superdense': bon += 1
                self.armor += chosenArmor[1]
                costPerc = self.price * chosenArmor[2]
                armorCost += costPerc
            if randomSetting == False:
                for i in range(tit): armorCost += self.price * titanium[2]
                for i in range(cry): armorCost += self.price * crystal[2]
                for i in range(bon): armorCost += self.price * bonded[2]
        self.price += armorCost

        # Sets up string to print for terminal

        if tit > 0:
            titString = 'Titanium Steel'
            if cry > 0 or bon > 0:
                if tit == 1: titString = titString + ', '
            if tit > 1:
                titString = titString + ' '
                for i in range(tit):
                    titString = titString + 'I'
                if cry > 0 or bon > 0: titString = titString + ', '
            self.armorType = titString

        if cry > 0:
            cryString = 'Crystaliron'
            if bon > 0:
                if cry == 1: cryString = cryString + ', '
            if cry > 1:
                cryString = cryString + ' '
                for i in range(cry):
                    cryString = cryString + 'I'
                if bon > 0: cryString = cryString + ', '
            self.armorType = self.armorType + cryString

        if bon > 0:
            bonString = 'Bonded Superdense'
            if bon > 1:
                bonString = bonString + ' '
                for i in range(bon):
                    bonString = bonString + 'I'
            self.armorType = self.armorType + bonString

    def installArmorOptions(self, reflec, selfSealing, stealth, randomArmor):
        optionsPrice = self.hullMass * 10000
        if randomArmor == False:
            x = 0
            y = 0
            z = 0
        if randomArmor == True: x = random.randint(1, 10)
        if x == 10 or reflec == True:
            self.reflec = True
            self.price += optionsPrice
        if randomArmor == True: y = random.randint(1, 10)
        if y == 10 or selfSealing == True:
            self.selfSealing = True
            self.price += optionsPrice
        if randomArmor == True: z = random.randint(1, 10)
        if z == 10 or stealth == True:
            self.stealth = True
            self.price += optionsPrice

    # Determines Jump, Manoeuvre Drives, Power Plant Tons and Cost
    def driveCodeTool(self, driveCode):
        jTons = driveCode * 5 + 5
        jCost = driveCode * 10
        if driveCode == 0: mTons = 0
        if driveCode == 1: mTons = 2
        if driveCode > 1: mTons = driveCode * 2 - 1
        mCost = driveCode * 4
        pTons = (driveCode - 1) * 3 + 4
        pCost = driveCode * 8
        return [jTons, jCost, mTons, mCost, pTons, pCost]

    # Determines how drives act based on hull volume
    def drivePerformanceTool(self):
        hullCode = self.hullMass // 100
        drivePerformance = [[1, 1]]
        if hullCode == 1: drivePerformance = [[1, 2], [2, 4], [3, 6]]
        if hullCode == 2: drivePerformance = [[1, 1], [2, 2], [3, 3],
                                              [4, 4], [5, 5], [6, 6]]
        if hullCode == 3: drivePerformance = [[2, 1], [3, 2], [4, 2],
                                              [5, 3], [6, 4], [7, 4],
                                              [8, 5], [9, 6]]
        if hullCode == 4: drivePerformance = [[2, 1], [3, 1], [4, 2],
                                              [5, 2], [6, 3], [7, 3],
                                              [8, 4], [9, 4], [10, 5],
                                              [11, 5], [12, 6], [13, 6]]
        if hullCode == 5: drivePerformance = [[3, 1], [4, 1], [5, 2],
                                              [6, 2], [7, 2], [8, 3],
                                              [9, 3], [10, 4], [11, 4],
                                              [12, 4], [13, 5], [14, 5],
                                              [15, 6], [16, 6], [17, 6]]
        if hullCode == 6: drivePerformance = [[3, 1], [4, 1], [5, 1],
                                              [6, 2], [7, 2], [8, 2],
                                              [9, 3], [10, 3], [11, 3],
                                              [12, 4], [13, 4], [14, 4],
                                              [15, 5], [16, 5], [17, 5],
                                              [18, 6], [19, 6], [20, 6]]
        if hullCode == 7: drivePerformance = [[4, 1], [5, 1], [6, 1],
                                              [7, 2], [8, 2], [9, 2],
                                              [10, 3], [11, 3], [12, 3],
                                              [13, 4], [14, 4], [15, 4],
                                              [16, 5], [17, 5], [18, 5],
                                              [19, 6], [20, 6], [21, 6],
                                              [22, 6], [23, 6], [24, 6]]
        if hullCode == 8: drivePerformance = [[4, 1], [5, 1], [6, 1],
                                              [7, 2], [8, 2], [9, 2],
                                              [10, 3], [11, 3], [12, 3],
                                              [13, 4], [14, 4], [15, 4],
                                              [16, 5], [17, 5], [18, 5],
                                              [19, 5], [20, 6], [21, 6],
                                              [22, 6], [23, 6], [24, 6]]
        if hullCode == 9: drivePerformance = [[5, 1], [6, 1],
                                              [7, 1], [8, 2], [9, 2],
                                              [10, 2], [11, 3], [12, 3],
                                              [13, 3], [14, 4], [15, 4],
                                              [16, 4], [17, 5], [18, 5],
                                              [19, 5], [20, 5], [21, 6],
                                              [22, 6], [23, 6], [24, 6]]
        if hullCode == 10 or hullCode == 11: drivePerformance = [[5, 1], [6, 1],
                                                                 [7, 1], [8, 2], [9, 2],
                                                                 [10, 2], [11, 3], [12, 3],
                                                                 [13, 3], [14, 4], [15, 4],
                                                                 [16, 4], [17, 5], [18, 5],
                                                                 [19, 5], [20, 5], [21, 5],
                                                                 [22, 6], [23, 6], [24, 6]]
        if hullCode == 12 or hullCode == 13: drivePerformance = [[6, 1],
                                                                 [7, 1], [8, 1], [9, 2],
                                                                 [10, 2], [11, 2], [12, 3],
                                                                 [13, 3], [14, 3], [15, 4],
                                                                 [16, 4], [17, 4], [18, 5],
                                                                 [19, 5], [20, 5], [21, 5],
                                                                 [22, 5], [23, 5], [24, 6]]
        if hullCode == 14 or hullCode == 15: drivePerformance = [[7, 1], [8, 1], [9, 1],
                                                                 [10, 2], [11, 2], [12, 2],
                                                                 [13, 3], [14, 3], [15, 3],
                                                                 [16, 4], [17, 4], [18, 4],
                                                                 [19, 4], [20, 5], [21, 5],
                                                                 [22, 5], [23, 5], [24, 5]]
        if hullCode == 16 or hullCode == 17: drivePerformance = [[8, 1], [9, 1],
                                                                 [10, 1], [11, 2], [12, 2],
                                                                 [13, 2], [14, 3], [15, 3],
                                                                 [16, 3], [17, 4], [18, 4],
                                                                 [19, 4], [20, 4], [21, 4],
                                                                 [22, 5], [23, 5], [24, 5]]
        if hullCode == 18 or hullCode == 19: drivePerformance = [[9, 1],
                                                                 [10, 1], [11, 1], [12, 2],
                                                                 [13, 2], [14, 2], [15, 3],
                                                                 [16, 3], [17, 3], [18, 4],
                                                                 [19, 4], [20, 4], [21, 4],
                                                                 [22, 4], [23, 4], [24, 5]]
        if hullCode >= 20: drivePerformance = [[10, 1], [11, 1], [12, 2],
                                               [13, 2], [14, 2], [15, 3],
                                               [16, 3], [17, 3], [18, 4],
                                               [19, 4], [20, 4], [21, 4],
                                               [22, 4], [23, 4], [24, 5]]

        return drivePerformance

    def decideScope(self, scope):
        scopes = ['Station', 'System', 'Jump', 'Star']
        self.scope = random.choice(scopes)

    def scopeDrives(self):
        drive = random.randint(1, 6)
        jump = random.randint(1, 6)

        if self.scope == 'Station': return [0, 0]
        if self.scope == 'System': return [0, drive]
        if self.scope == 'Jump': return [jump, 0]
        if self.scope == 'Star': return [jump, drive]

    def decideCruisingSpeed(self, thrust):
        if self.hullMass // 100 <= 1:
            if thrust < 2: thrust = 2
            if thrust > 2 and thrust < 4: thrust = 4
            if thrust < 4: thrust = 6
        if self.hullMass // 100 >= 14 and thrust == 6:
            thrust = 5
        drivePerformance = self.drivePerformanceTool()
        driveCode = [0, 0, 0, 0]
        for i in range(len(drivePerformance)):
            if drivePerformance[i][1] == thrust:
                driveCode = self.driveCodeTool(drivePerformance[i][0])
        self.availableHull -= driveCode[2]
        self.driveTons[1] = driveCode[2]
        self.price += driveCode[3]
        drivePerformance[0] = alphaSwitch(drivePerformance[0])
        self.mannyDrive = drivePerformance[1]
        self.mannyDrive[0] = alphaSwitch(self.mannyDrive[0])
        if thrust == 0: self.mannyDrive = ['N/A', 0]

    def decideJumpDistance(self, jumpDistance):
        if self.hullMass // 100 <= 1:
            if jumpDistance < 2: jumpDistance = 2
            if jumpDistance > 2 and jumpDistance < 4: jumpDistance = 4
            if jumpDistance < 4: jumpDistance = 6
        if self.hullMass // 100 >= 14 and jumpDistance == 6:
            jumpDistance = 5
        drivePerformance = self.drivePerformanceTool()
        driveCode = [0, 0, 0, 0]
        x = 0
        for i in range(len(drivePerformance)):
            if drivePerformance[i][1] == jumpDistance:
                driveCode = self.driveCodeTool(drivePerformance[i][0])
                x = i
        drivePerformance = drivePerformance[i]
        self.availableHull -= driveCode[0]
        self.driveTons[0] = driveCode[0]
        self.price += driveCode[1]
        drivePerformance[0] = alphaSwitch(drivePerformance[0])
        self.jumpDrive = drivePerformance
        if jumpDistance == 0: self.jumpDrive = ['N/A', 0]

    def installPowerPlant(self, driveScope):
        if self.jumpDrive[0] != 'N/A': x = alphaSwitch(self.jumpDrive[0])
        if self.jumpDrive[0] == 'N/A': x = 0
        if self.mannyDrive[0] != 'N/A': y = alphaSwitch(self.mannyDrive[0])
        if self.mannyDrive[0] == 'N/A': y = 0
        if x < y: x = y
        if x != 0:
            driveCode = self.driveCodeTool(x)
            self.availableHull -= driveCode[4]
            self.driveTons[2] = driveCode[5]
            self.powerPlant = [alphaSwitch(x), x * 2]
        if x == 0: self.powerPlant = ['A', 2]

    def allocateFuelTank(self):
        self.jumpFuel = [int((self.hullMass) // 10), int((self.hullMass * self.jumpDrive[1]) // 10)]
        self.fuel[1] = self.powerPlant[1] + self.jumpFuel[1]
        if self.fuelScoops == True:
            self.fuelProcessors = self.fuel[1] // 20
            self.price += self.fuelProcessors * 50000

    def installBridge(self):
        if self.hullMass <= 200: self.availableHull -= 10
        if self.hullMass >= 200: self.availableHull -= 20
        if self.hullMass >= 1000: self.availableHull -= 20
        if self.hullMass >= 2000: self.availableHull -= 20
        self.price += 0.5 * (self.hullMass // 100)

    def installComputer(self, compType, options):
        if options == 'random':
            x = d(2,6,0)
            if x <= 6: option = 'none'
            if x > 6 and x <= 8: option = 'bis'
            if x > 8 and x <= 10: option = 'fib'
            if x > 10: option = 'both'

        if options != 'random': option = options

        # if compType == 'optimal':
        #    compLevel = self.jumpDrive[1]
        #    if options == 'bis' or options == 'both': compLevel = self.jumpDrive[1] - 1
        #    for i in range(len(shipComputersList)):
        #        if shipComputersList[i].power == compLevel:
        #            self.computer = shipComputersList[i]
        #    if self.computer == 'emptyShipComputer':self.computer = random.choice(shipComputersList)

        if compType == 'optimal':
            ratingRequired = self.jumpDrive[1] * 5
            for i in range(len(shipComputersList)):
                if shipComputersList[i].power == ratingRequired:
                    self.computer = shipComputersList[i]
            if self.computer == 'emptyShipComputer':
                print('NO COMPUTER AVAILABLE ERR')
                self.computer = random.choice(shipComputersList)

        if computer == 'model1': self.computer = model1
        if computer == 'model2': self.computer = model2
        if computer == 'model3': self.computer = model3
        if computer == 'model4': self.computer = model4
        if computer == 'model5': self.computer = model5
        if computer == 'model6': self.computer = model6
        if computer == 'model7': self.computer = model7
        if option == 'bis' or option == 'fib' or option == 'both':
            self.computer.shipComputerOptions(option)

    def installSensorsSuite(self, sensorsSuite):
        standardElectronics = ['Standard', 8, -4, ['Radar', 'Lidar'], 0, 0]
        civilianElectronics = ['Basic Civilian', 9, -2, ['Radar', 'Lidar'], 1, 50000]
        militaryElectronics = ['Basic Military', 10, 0, ['Radar', 'Lidar', 'Jammers'], 2, 1000000]
        advancedElectronics = ['Advanced', 11, 1, ['Radar', 'Lidar', 'Densitometer', 'Jammers'], 3, 2000000]
        veryAdvancedElectronics = ['Very Advanced', 12, 2,
                                   ['Radar', 'Lidar', 'Densitometer', 'Jammers', 'Neural Activity Sensor'], 5, 4000000]

        sensorsList = [standardElectronics, civilianElectronics, militaryElectronics,
                       advancedElectronics, veryAdvancedElectronics]

        if sensorsSuite == 'random': self.sensorsSuite = random.choice(sensorsList)
        if sensorsSuite == 'standard': self.sensorsSuite = standardElectronics
        if sensorsSuite == 'civilian': self.sensorsSuite = civilianElectronics
        if sensorsSuite == 'military': self.sensorsSuite = militaryElectronics
        if sensorsSuite == 'advanced': self.sensorsSuite = advancedElectronics
        if sensorsSuite == 'very advanced': self.sensorsSuite = veryAdvancedElectronics

    # New themes for hardpoint generation:
    # - pacifist, low-tonnage, stealth, fixed, maxxed, high-tonnage

    def createHardpoints(self):
        hardpoints = self.hullMass // 100
        armaments = []
        for i in range(hardpoints):
            armament = hardpoint()
            if self.availableHull >= 200 or self.availableHull > self.hullMass / 4:
                x = d(2,6,0)
                if x <= 7: armament.randomTurret()
                if x >= 8 and x <= 10: armament.installBay('random')
                if x >= 11: armament.installScreen('random')
            armaments.append(armament)
            self.availableHull -= armament.tons
        self.hardpoints = armaments

    def attachArmaments(self, percent):
        hardpoints = self.hullMass // 100
        armaments = []
        armorBudget = int((self.availableHull // 1) * (percent / 100))
        totalArmaments = 0
        for i in range(hardpoints):
            armament = hardpoint()
            hardpointsRemaining = hardpoints - i
            if armorBudget // hardpointsRemaining < 51 and hardpointsRemaining >= 10:
                armament.randomTurret()
            if armorBudget // hardpointsRemaining >= 51:
                x = d(2,6,0)
                if x <= 7: armament.randomTurret()
                if x >= 8 and x <= 10: armament.installBay('random')
                if x >= 11: armament.installScreen('random')
            armaments.append(armament)
            armorBudget -= armament.tons
            totalArmaments += armament.tons
        self.hardpoints = armaments
        self.availableHull -= totalArmaments

    def compileShipManifest(self, low, work, middle, high, doubleOccupancy, luxuries):
        stewardRequired = ((work + middle) // 5) + (high // 2)
        if luxuries == True:
            luxuriesRequired = stewardRequired
            stewardRequired = 0
        if luxuries == False: luxuriesRequired = 0
        medicRequired = (low + work + middle + high) // 120
        staterooms = stewardRequired + medicRequired
        lowBerths = low
        if doubleOccupancy == False: staterooms = work + middle + high
        if doubleOccupancy == True: staterooms = ((work + middle) // 2) + high
        return [staterooms, lowBerths, luxuriesRequired]

    def determineCrew(self, coverage, manifest, doubleOccupancy):
        if coverage == 'minimum': staterooms = 2
        if coverage == 'average':
            staterooms = 4 + ((self.driveTons[0] + self.driveTons[1]) // 50)

            for i in range(len(self.hardpoints)):
                if self.hardpoints[i].isScreen == False: staterooms += 1
            addExtra = False
            if doubleOccupancy == True:
                if staterooms % 2 == 1: addExtra = True
                staterooms = staterooms // 2
                if addExtra == True: staterooms += 1
            staterooms += manifest[0]
            self.staterooms = staterooms
            self.lowBerts = manifest[1]
            self.availableHull -= self.lowBerths * 0.5
            self.price += self.lowBerths * 50000
            self.price += self.staterooms * 500000

    def vehicleOptions(self, option):
        miningDrones = ['Mining Drones', 10, 1000000]
        repairDronesTons = 0.01 * self.hullMass
        repairDrones = ['Repair Drones', repairDronesTons, (repairDronesTons * 200000)]
        probeDrones = ['5 Probe Drones', 1, 500000]
        escapePods = ['Escape Pods', 0.5, 100000]
        lifeBoat = ['Life Boat', 20, 14000000]
        shipsBoat = ["Ship's Boat", 30, 16000000]
        pinnacle = ['Pinnacle', 40, 20000000]
        cutter = ['Cutter', 50, 28000000]
        shuttle = ['Shuttle', 95, 33000000]
        airRaft = ['Air/Raft', 4, 275000]
        atv = ['ATV', 10, 50000]
        options = [miningDrones, repairDrones, probeDrones, escapePods, lifeBoat,
                   shipsBoat, pinnacle, cutter, shuttle, airRaft, atv]
        availableOptions = []
        chosenOption = ['X', 0, 0]
        for i in range(len(options)):
            if self.availableHull > options[i][1]:
                availableOptions.append(options[i])
            if options[i][0] == option: chosenOption = options[i]
        if option == 'random' and availableOptions != []:
            self.options.append(random.choice(availableOptions))
        if option != 'random':
            self.options.append(chosenOption)
        if repairDrones in self.options:
            self.computer.install(random.choice(autoRepairSoftware))
        for i in range(len(self.options)):
            self.availableHull -= self.options[i][1]
            self.price += self.options[i][2]
        self.computer.install(library)

    def technicalData(self):
        if self.hullMass // 100 == 1: scopeTag = 'craft'
        if self.hullMass // 100 > 1: scopeTag = 'ship'
        print('Designation:       ' + self.designation + ' | ' + self.scope + scopeTag)
        print('Hull:              ' + str(self.hullMass) + ' tons | Hull ' + str(self.hull))
        print('                   ' + self.config2 + ' | Structure ' + str(self.structure))
        if self.armor > 0:
            print('Armour:            ' + self.armorType + ' | ' + str(self.armor) + ' points')
        if self.jumpDrive != ['N/A', 0]:
            print('Jump Drive ' + str(self.jumpDrive[0]) + '       Jump ' + str(self.jumpDrive[1]))
        if self.jumpDrive == ['N/A', 0]:
            print('No Jump Drive')
        if self.mannyDrive != ['N/A', 0]:
            print('Manoeuvre Drive ' + str(self.mannyDrive[0]) + '  Thrust ' + str(self.mannyDrive[1]))
        if self.mannyDrive == ['N/A', 0]:
            print('No Manoeuvre Drive')
        print('Power Plant ' + self.powerPlant[0])
        print('Bridge')
        if self.computer.bis == False:
            print('Computer           ' + self.computer.name + ' | Rating: ' + str(self.computer.power))
        if self.computer.bis == True:
            print('Computer           ' + self.computer.name + ' | Rating: ' + str(self.computer.rating) + ' (' + str(
                self.computer.rating + 5) + ' for Jump Control)')
        if self.sensorsSuite[2] >= 0: print(
            'Electronics        ' + self.sensorsSuite[0] + ' | +' + str(self.sensorsSuite[2]) + ' DM')
        if self.sensorsSuite[2] < 0: print(
            'Electronics        ' + self.sensorsSuite[0] + ' | ' + str(self.sensorsSuite[2]) + ' DM')
        print()
        for i in range(len(self.hardpoints)):
            if i >= 9: spacer = '    '
            if i < 9: spacer = '     '
            turretWeapons = ''
            if self.hardpoints[i].turrets > 0: turretWeapons = self.hardpoints[i].turretOne[0]
            if self.hardpoints[i].turrets > 1: turretWeapons = self.hardpoints[i].turretOne[0] + '/' + \
                                                               self.hardpoints[i].turretTwo[0]
            if self.hardpoints[i].turrets > 2: turretWeapons = self.hardpoints[i].turretOne[0] + '/' + \
                                                               self.hardpoints[i].turretTwo[0] + '/' + \
                                                               self.hardpoints[i].turretThree[0]
            if self.hardpoints[i].isTurret == True:
                if self.hardpoints[i].designation != 'Empty Turret':
                    print('Hardpoint #' + str(i + 1) + '  ' + spacer + self.hardpoints[
                        i].designation + ' (' + turretWeapons + ')')
                if self.hardpoints[i].designation == 'Empty Turret':
                    print('Hardpoint #' + str(i + 1) + '  ' + spacer + 'Empty Turret')
            if self.hardpoints[i].isBay == True:
                print(
                    'Hardpoint #' + str(i + 1) + '  ' + spacer + 'Weapon Bay (' + self.hardpoints[i].designation + ')')
            if self.hardpoints[i].isScreen == True:
                print('Hardpoint #' + str(i + 1) + '  ' + spacer + 'Screen (' + self.hardpoints[i].designation + ')')
            if self.hardpoints[i].isTurret == False and self.hardpoints[i].isBay == False and self.hardpoints[
                i].isScreen == False:
                print('Hardpoint #' + str(i + 1) + '  ' + spacer + 'Empty')
        print()
        if self.jumpDrive[0] != 'N/A':
            print('Fuel               ' + str(self.fuel[1]) + ' tons | One Jump-' + str(
                self.jumpDrive[1]) + " and two weeks' operation")
        if self.jumpDrive[0] == 'N/A':
            print('Fuel               ' + str(self.fuel[1]) + " tons |  Two weeks' operation")
        print('Cargo:             ' + str(self.cargo) + ' tons')
        print(str(self.staterooms) + ' Staterooms')
        print(str(self.lowBerths) + ' Low Berths')
        print()
        print("Extras:            Ship's Locker")
        if self.fuelScoops == True: print('                   Fuel Scoops')
        if self.fuelProcessors > 0: print('                   ' + str(self.fuelProcessors) + ' Fuel Processors')
        for i in range(len(self.options)):
            print('                   ' + self.options[i][0])
        print()
        for i in range(len(self.computer.programs)):
            if i == 0:
                print('Software           ' + self.computer.programs[i].name)
            if i > 0:
                print('                   ' + self.computer.programs[i].name)
        print()
        print('Price:             ' + str(round(self.price)) + ' Cr.')
        self.mortgage = self.price // 240
        self.maintenance = self.price // 1000
        print('Mortgage:          ' + str(int(self.mortgage)) + ' Cr./mo.')
        print('Maintenance:       ' + str(int(self.maintenance)) + ' Cr./yr.')


def constructVessel(vessel):
    # 1. Choose Hull Mass
    vessel.constructHull('random')
    vessel.determineHullStructure()

    # 2. Choose Hull Configuration
    vessel.assignConfiguration('random')

    # 3. Install Armor
    vessel.installArmor(0, 0, 0, True)

    # 4. Install Hull Options
    vessel.installArmorOptions(False, False, False, True)

    # 5. Decide Ship Scope
    vessel.decideScope('random')
    driveScope = vessel.scopeDrives()
    print(driveScope)

    # 6. Decide Cruising Altitude (Thrust)
    vessel.decideCruisingSpeed(driveScope[1])

    # 7. Decide Jump Rating
    vessel.decideJumpDistance(driveScope[0])

    # 8. Choose Power Plant
    vessel.installPowerPlant(driveScope)

    # 9. Fuel Allocation
    vessel.allocateFuelTank()

    # 10. Install Bridge
    vessel.installBridge()

    # 11. Install Computer
    vessel.installComputer('optimal', 'none')

    # 12. Install Computer Software
    vessel.computer.initializeShipSoftware(vessel, ['random'])

    # 13. Install Sensors
    vessel.installSensorsSuite('random')

    # 16. Hardpoints
    vessel.attachArmaments(50)

    # 14. Staterooms, Low berths, luxuries
    vesselManifest = vessel.compileShipManifest(0, 0, 0, 0, True, False)
    vessel.determineCrew('average', vesselManifest, True)

    # 15. Vehicles / cargo options
    vessel.vehicleOptions('random')

    # 17. Final Cargo space allocation
    vessel.cargo = int(vessel.availableHull)

    # 18. Printing to Terminal
    vessel.technicalData()

#   ________  ______  __________  ____  __  ___   ____ __
#  / ____/\ \/ / __ )/ ____/ __ \/ __ \/ / / / | / / //_/
# / /      \  / __  / __/ / /_/ / /_/ / / / /  |/ / ,<
# / /___    / / /_/ / /___/ _, _/ ____/ /_/ / /|  / /| |
# \____/   /_/_____/_____/_/ |_/_/    \____/_/ |_/_/ |_|
# CYBERPUNK NPC GENERATOR FUNCTIONS

class cyberpunkSkills():
    def __init__(self):
        # Special Abilities
        self.authority = 0
        self.charismaticLeadership = 0
        self.combatSense = 0
        self.credibility = 0
        self.family = 0
        self.interface = 0
        self.juryRig = 0
        self.medicalTech = 0
        self.resources = 0
        self.streetdeal = 0

        # Attr Skills
        self.personalGrooming = 0
        self.wardrobeStyle = 0

        # Body Skills
        self.endurance = 0
        self.strengthFeat = 0
        self.swimming = 0

        # Cool Skills
        self.interrogation = 0
        self.intimidate = 0
        self.oratory = 0
        self.resistTortureDrugs = 0
        self.streetwise = 0

        # Empathy Skills
        self.humanPerception = 0
        self.interview = 0
        self.leadership = 0
        self.seduction = 0
        self.social = 0
        self.persuasion = 0
        self.performance = 0

        # Intelligence Skills
        self.accounting = 0
        self.anthropology = 0
        self.awarenessNotice = 0
        self.biology = 0
        self.botany = 0
        self.chemistry = 0
        self.composition = 0
        self.diagnoseIllness = 0
        self.education = 0
        self.expert = 0
        self.gamble = 0
        self.hideEvade = 0
        self.history = 0
        self.language = 0
        self.librarySearch = 0
        self.math = 0
        self.physics = 0
        self.programming = 0
        self.shadowTrack = 0
        self.stockMarket = 0
        self.systemKnowledge = 0
        self.teaching = 0
        self.survival = 0
        self.zoology = 0

        # Reflex Skills
        self.archery = 0
        self.athletics = 0
        self.brawling = 0
        self.dancing = 0
        self.dodgeEscape = 0
        self.driving = 0
        self.fencing = 0
        self.handgun = 0
        self.heavyWeapons = 0
        self.aikido = 0
        self.animalKungFu = 0
        self.boxing = 0
        self.capoeria = 0
        self.choiLiFut = 0
        self.judo = 0
        self.karate = 0
        self.taeKwonDo = 0
        self.thaiKickBoxing = 0
        self.wrestling = 0
        self.melee = 0
        self.motorcycle = 0
        self.heavyMachinery = 0
        self.gyro = 0
        self.fixedWing = 0
        self.dirigible = 0
        self.vectorThrust = 0
        self.rifle = 0
        self.stealth = 0
        self.submachinegun = 0

        # Technical Skills
        self.aeroTech = 0
        self.vectorThrustTech = 0
        self.basicTech = 0  #
        self.cryotank = 0
        self.cyberdeckDesign = 0
        self.cyberTech = 0  #
        self.demolitions = 0
        self.disguise = 0
        self.electronics = 0  #
        self.electronicSecurity = 0
        self.firstAid = 0
        self.forgery = 0
        self.gyroTech = 0
        self.paintDraw = 0
        self.photoFilm = 0
        self.pharmaceuticals = 0
        self.pickLock = 0
        self.pickPocket = 0
        self.instrument = 0
        self.weaponsmith = 0

    def rollClassSkills(self, character):
        skillDistribution = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(39):
            x = random.randint(0, len(skillDistribution) - 1)
            while skillDistribution[x] >= 10: x = random.randint(0, len(skillDistribution) - 1)
            skillDistribution[x] += 1
        if character.role == 'Solo':
            self.combatSense = skillDistribution[0]
            self.awarenessNotice = skillDistribution[1]
            self.handgun = skillDistribution[2]
            x = random.randint(0, 9)  # Martial Arts Choice
            if x == 0: self.aikido = skillDistribution[3]
            if x == 1: self.animalKungFu = skillDistribution[3]
            if x == 2: self.boxing = skillDistribution[3]
            if x == 3: self.capoeria = skillDistribution[3]
            if x == 4: self.choiLiFut = skillDistribution[3]
            if x == 5: self.judo = skillDistribution[3]
            if x == 6: self.karate = skillDistribution[3]
            if x == 7: self.taeKwonDo = skillDistribution[3]
            if x == 8: self.thaiKickBoxing = skillDistribution[3]
            if x == 9: self.wrestling = skillDistribution[3]
            self.brawling = skillDistribution[4]
            self.weaponsmith = skillDistribution[5]
            self.rifle = skillDistribution[6]
            self.athletics = skillDistribution[7]
            self.submachinegun = skillDistribution[8]
            self.stealth = skillDistribution[9]
        if character.role == 'Corporate':
            self.resource = skillDistribution[0]
            self.awarenessNotice = skillDistribution[1]
            self.humanPerception = skillDistribution[2]
            self.education = skillDistribution[3]
            self.librarySearch = skillDistribution[4]
            self.social = skillDistribution[5]
            self.persuasion = skillDistribution[6]
            self.stockMarket = skillDistribution[7]
            self.wardrobeStyle = skillDistribution[8]
            self.personalGrooming = skillDistribution[9]
        if character.role == 'Media':
            self.credibility = skillDistribution[0]
            self.awarenessNotice = skillDistribution[1]
            self.composition = skillDistribution[2]
            self.education = skillDistribution[3]
            self.persuasion = skillDistribution[4]
            self.humanPerception = skillDistribution[5]
            self.social = skillDistribution[6]
            self.streetwise = skillDistribution[7]
            self.photoFilm = skillDistribution[8]
            self.interview = skillDistribution[9]
        if character.role == 'Nomad':
            self.family = skillDistribution[0]
            self.awarenessNotice = skillDistribution[1]
            self.endurance = skillDistribution[2]
            self.melee = skillDistribution[3]
            self.rifle = skillDistribution[4]
            self.driving = skillDistribution[5]
            self.basicTech = skillDistribution[6]
            self.survival = skillDistribution[7]
            self.brawling = skillDistribution[8]
            self.athletics = skillDistribution[9]
        if character.role == 'Techie':
            self.juryRig = skillDistribution[0]
            self.awarenessNotice = skillDistribution[1]
            self.basicTech = skillDistribution[2]
            self.cyberTech = skillDistribution[3]
            self.teaching = skillDistribution[4]
            self.education = skillDistribution[5]
            self.electronics = skillDistribution[6]
            # Add 3 other tech skills
            techSkillsList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
            for i in range(3):
                x = random.randint(0, len(techSkillsList) - 1)
                y = techSkillsList[x]
                del techSkillsList[x]
                if y == 1: self.aeroTech = skillDistribution[7 + i]
                if y == 2: self.vectorThrustTech = skillDistribution[7 + i]
                if y == 3: self.cryotank = skillDistribution[7 + i]
                if y == 4: self.cyberdeckDesign = skillDistribution[7 + i]
                if y == 5: self.demolitions = skillDistribution[7 + i]
                if y == 6: self.disguise = skillDistribution[7 + i]
                if y == 7: self.electronicSecurity = skillDistribution[7 + i]
                if y == 8: self.firstAid = skillDistribution[7 + i]
                if y == 9: self.forgery = skillDistribution[7 + i]
                if y == 10: self.gyroTech = skillDistribution[7 + i]
                if y == 11: self.paintDraw = skillDistribution[7 + i]
                if y == 12: self.photoFilm = skillDistribution[7 + i]
                if y == 13: self.pharmaceuticals = skillDistribution[7 + i]
                if y == 14: self.pickLock = skillDistribution[7 + i]
                if y == 15: self.pickPocket = skillDistribution[7 + i]
                if y == 16: self.instrument = skillDistribution[7 + i]
                if y == 17: self.weaponsmith = skillDistribution[7 + i]
        if character.role == 'Cop':
            self.authority = skillDistribution[0]
            self.awarenessNotice = skillDistribution[1]
            self.handgun = skillDistribution[2]
            self.humanPerception = skillDistribution[3]
            self.athletics = skillDistribution[4]
            self.education = skillDistribution[5]
            self.brawling = skillDistribution[6]
            self.melee = skillDistribution[7]
            self.interrogation = skillDistribution[8]
            self.streetwise = skillDistribution[9]
        if character.role == 'Rockerboy':
            self.charismaticLeadership = skillDistribution[0]
            self.awarenessNotice = skillDistribution[1]
            self.performance = skillDistribution[2]
            self.wardrobeStyle = skillDistribution[3]
            self.composition = skillDistribution[4]
            self.brawling = skillDistribution[5]
            self.instrument = skillDistribution[6]
            self.streetwise = skillDistribution[7]
            self.persuasuion = skillDistribution[8]
            self.seduction = skillDistribution[9]
        if character.role == 'Medtechie':
            self.medicalTech = skillDistribution[0]
            self.awarenessNotice = skillDistribution[1]
            self.basicTech = skillDistribution[2]
            self.diagnoseIllness = skillDistribution[3]
            self.education = skillDistribution[4]
            self.cryotank = skillDistribution[5]
            self.librarySearch = skillDistribution[6]
            self.pharmaceuticals = skillDistribution[7]
            self.zoology = skillDistribution[8]
            self.humanPerception = skillDistribution[9]
        if character.role == 'Fixer':
            self.streetdeal = skillDistribution[0]
            self.awarenessNotice = skillDistribution[1]
            self.forgery = skillDistribution[2]
            self.handgun = skillDistribution[3]
            self.brawling = skillDistribution[4]
            self.melee = skillDistribution[5]
            self.pickLock = skillDistribution[6]
            self.pickPocket = skillDistribution[7]
            self.intimidate = skillDistribution[8]
            self.persuasion = skillDistribution[9]
        if character.role == 'Netrunner':
            self.interface = skillDistribution[0]
            self.awarenessNotice = skillDistribution[1]
            self.basicTech = skillDistribution[2]
            self.education = skillDistribution[3]
            self.systemKnowledge = skillDistribution[4]
            self.cyberTech = skillDistribution[5]
            self.cyberdeckDesign = skillDistribution[6]
            self.composition = skillDistribution[7]
            self.electronics = skillDistribution[8]
            self.programming = skillDistribution[9]

    def rollPickupSkills(self, character):
        pointsAvailable = character.int + character.ref[1]
        numSkills = random.randint(1, pointsAvailable)
        newSkillsChoices = []
        for i in range(numSkills):
            x = random.randint(1, 90)
            while x in newSkillsChoices: x = random.randint(1, 90)
            if x not in newSkillsChoices: newSkillsChoices.append(x)

        newSkillPoints = []
        for i in range(len(newSkillsChoices)):
            newSkillPoints.append(0)

        for i in range(pointsAvailable):
            x = random.randint(0, len(newSkillPoints) - 1)
            while newSkillPoints[x] >= 10: x = random.randint(0, len(newSkillPoints) - 1)
            newSkillPoints[x] += 1

        for i in range(len(newSkillsChoices)):
            # Attr Skills
            if newSkillsChoices[i] == 1: self.personalGrooming += newSkillPoints[i]
            if newSkillsChoices[i] == 2: self.wardrobeStyle += newSkillPoints[i]

            # Body Skills
            if newSkillsChoices[i] == 3: self.endurance += newSkillPoints[i]
            if newSkillsChoices[i] == 4: self.strengthFeat += newSkillPoints[i]
            if newSkillsChoices[i] == 5: self.swimming += newSkillPoints[i]

            # Cool Skills
            if newSkillsChoices[i] == 6: self.interrogation += newSkillPoints[i]
            if newSkillsChoices[i] == 7: self.intimidate += newSkillPoints[i]
            if newSkillsChoices[i] == 8: self.oratory += newSkillPoints[i]
            if newSkillsChoices[i] == 9: self.resistTortureDrugs += newSkillPoints[i]
            if newSkillsChoices[i] == 10: self.streetwise += newSkillPoints[i]

            # Empathy Skills
            if newSkillsChoices[i] == 11: self.humanPerception += newSkillPoints[i]
            if newSkillsChoices[i] == 12: self.interview += newSkillPoints[i]
            if newSkillsChoices[i] == 13: self.leadership += newSkillPoints[i]
            if newSkillsChoices[i] == 14: self.seduction += newSkillPoints[i]
            if newSkillsChoices[i] == 15: self.social += newSkillPoints[i]
            if newSkillsChoices[i] == 16: self.persuasion += newSkillPoints[i]
            if newSkillsChoices[i] == 17: self.performance += newSkillPoints[i]

            # Intelligence Skills
            if newSkillsChoices[i] == 18: self.accounting += newSkillPoints[i]
            if newSkillsChoices[i] == 19: self.anthropology += newSkillPoints[i]
            if newSkillsChoices[i] == 20: self.awarenessNotice += newSkillPoints[i]
            if newSkillsChoices[i] == 21: self.biology += newSkillPoints[i]
            if newSkillsChoices[i] == 22: self.botany += newSkillPoints[i]
            if newSkillsChoices[i] == 23: self.chemistry += newSkillPoints[i]
            if newSkillsChoices[i] == 24: self.composition += newSkillPoints[i]
            if newSkillsChoices[i] == 25: self.diagnoseIllness += newSkillPoints[i]
            if newSkillsChoices[i] == 26: self.education += newSkillPoints[i]
            if newSkillsChoices[i] == 27: self.expert += newSkillPoints[i]
            if newSkillsChoices[i] == 28: self.gamble += newSkillPoints[i]
            if newSkillsChoices[i] == 29: self.hideEvade += newSkillPoints[i]
            if newSkillsChoices[i] == 30: self.history += newSkillPoints[i]
            if newSkillsChoices[i] == 31: self.language += newSkillPoints[i]
            if newSkillsChoices[i] == 32: self.librarySearch += newSkillPoints[i]
            if newSkillsChoices[i] == 33: self.math += newSkillPoints[i]
            if newSkillsChoices[i] == 34: self.physics += newSkillPoints[i]
            if newSkillsChoices[i] == 35: self.programming += newSkillPoints[i]
            if newSkillsChoices[i] == 36: self.shadowTrack += newSkillPoints[i]
            if newSkillsChoices[i] == 37: self.stockMarket += newSkillPoints[i]
            if newSkillsChoices[i] == 38: self.systemKnowledge += newSkillPoints[i]
            if newSkillsChoices[i] == 39: self.teaching += newSkillPoints[i]
            if newSkillsChoices[i] == 40: self.survival += newSkillPoints[i]
            if newSkillsChoices[i] == 41: self.zoology += newSkillPoints[i]

            # Reflex Skills
            if newSkillsChoices[i] == 42: self.archery += newSkillPoints[i]
            if newSkillsChoices[i] == 43: self.athletics += newSkillPoints[i]
            if newSkillsChoices[i] == 44: self.brawling += newSkillPoints[i]
            if newSkillsChoices[i] == 45: self.dancing += newSkillPoints[i]
            if newSkillsChoices[i] == 46: self.dodgeEscape += newSkillPoints[i]
            if newSkillsChoices[i] == 47: self.driving += newSkillPoints[i]
            if newSkillsChoices[i] == 48: self.fencing += newSkillPoints[i]
            if newSkillsChoices[i] == 49: self.handgun += newSkillPoints[i]
            if newSkillsChoices[i] == 50: self.heavyWeapons += newSkillPoints[i]
            if newSkillsChoices[i] == 51: self.aikido += newSkillPoints[i]
            if newSkillsChoices[i] == 52: self.animalKungFu += newSkillPoints[i]
            if newSkillsChoices[i] == 53: self.boxing += newSkillPoints[i]
            if newSkillsChoices[i] == 54: self.capoeria += newSkillPoints[i]
            if newSkillsChoices[i] == 55: self.choiLiFut += newSkillPoints[i]
            if newSkillsChoices[i] == 56: self.judo += newSkillPoints[i]
            if newSkillsChoices[i] == 57: self.karate += newSkillPoints[i]
            if newSkillsChoices[i] == 58: self.taeKwonDo += newSkillPoints[i]
            if newSkillsChoices[i] == 59: self.thaiKickBoxing += newSkillPoints[i]
            if newSkillsChoices[i] == 60: self.wrestling += newSkillPoints[i]
            if newSkillsChoices[i] == 61: self.melee += newSkillPoints[i]
            if newSkillsChoices[i] == 62: self.motorcycle += newSkillPoints[i]
            if newSkillsChoices[i] == 63: self.heavyMachinery += newSkillPoints[i]
            if newSkillsChoices[i] == 64: self.gyro += newSkillPoints[i]
            if newSkillsChoices[i] == 65: self.fixedWing += newSkillPoints[i]
            if newSkillsChoices[i] == 66: self.dirigible += newSkillPoints[i]
            if newSkillsChoices[i] == 67: self.vectorThrust += newSkillPoints[i]
            if newSkillsChoices[i] == 68: self.rifle += newSkillPoints[i]
            if newSkillsChoices[i] == 69: self.stealth += newSkillPoints[i]
            if newSkillsChoices[i] == 70: self.submachinegun += newSkillPoints[i]

            # Technical Skills
            if newSkillsChoices[i] == 71: self.aeroTech += newSkillPoints[i]
            if newSkillsChoices[i] == 72: self.vectorThrustTech += newSkillPoints[i]
            if newSkillsChoices[i] == 73: self.basicTech += newSkillPoints[i]
            if newSkillsChoices[i] == 74: self.cryotank += newSkillPoints[i]
            if newSkillsChoices[i] == 75: self.cyberdeckDesign += newSkillPoints[i]
            if newSkillsChoices[i] == 76: self.cyberTech += newSkillPoints[i]
            if newSkillsChoices[i] == 77: self.demolitions += newSkillPoints[i]
            if newSkillsChoices[i] == 78: self.disguise += newSkillPoints[i]
            if newSkillsChoices[i] == 79: self.electronics += newSkillPoints[i]
            if newSkillsChoices[i] == 80: self.electronicSecurity += newSkillPoints[i]
            if newSkillsChoices[i] == 81: self.firstAid += newSkillPoints[i]
            if newSkillsChoices[i] == 82: self.forgery += newSkillPoints[i]
            if newSkillsChoices[i] == 83: self.gyroTech += newSkillPoints[i]
            if newSkillsChoices[i] == 84: self.paintDraw += newSkillPoints[i]
            if newSkillsChoices[i] == 85: self.photoFilm += newSkillPoints[i]
            if newSkillsChoices[i] == 86: self.pharmaceuticals += newSkillPoints[i]
            if newSkillsChoices[i] == 87: self.pickLock += newSkillPoints[i]
            if newSkillsChoices[i] == 88: self.pickPocket += newSkillPoints[i]
            if newSkillsChoices[i] == 89: self.instrument += newSkillPoints[i]
            if newSkillsChoices[i] == 90: self.weaponsmith += newSkillPoints[i]

    def printSkills(self):
        # Special Abilities
        if self.authority > 0: print('Authority (' + str(self.authority) + ')')
        if self.charismaticLeadership > 0: print('Charismatic Leadership (' + str(self.charismaticLeadership) + ')')
        if self.combatSense > 0: print('Combat Sense (' + str(self.combatSense) + ')')
        if self.credibility > 0: print('Credibility (' + str(self.credibility) + ')')
        if self.family > 0: print('Family (' + str(self.family) + ')')
        if self.interface > 0: print('Interface (' + str(self.interface) + ')')
        if self.juryRig > 0: print('Jury Rig (' + str(self.juryRig) + ')')
        if self.medicalTech > 0: print('Medical Tech (' + str(self.medicalTech) + ')')
        if self.resources > 0: print('Resources (' + str(self.resources) + ')')
        if self.streetdeal > 0: print('Streetdeal (' + str(self.streetdeal) + ')')

        # Attr Skills
        if self.personalGrooming > 0: print('Personal Grooming (' + str(self.personalGrooming) + ')')
        if self.wardrobeStyle > 0: print('Wardrobe & Style (' + str(self.wardrobeStyle) + ')')

        # Body Skills
        if self.endurance > 0: print('Endurance (' + str(self.endurance) + ')')
        if self.strengthFeat > 0: print('Strength Feat (' + str(self.strengthFeat) + ')')
        if self.swimming > 0: print('Swimming (' + str(self.swimming) + ')')

        # Cool Skills
        if self.interrogation > 0: print('Interrogation (' + str(self.interrogation) + ')')
        if self.intimidate > 0: print('Intimidate (' + str(self.intimidate) + ')')
        if self.oratory > 0: print('Oratory (' + str(self.oratory) + ')')
        if self.resistTortureDrugs > 0: print('Resist Torture/Drugs (' + str(self.resistTortureDrugs) + ')')
        if self.streetwise > 0: print('Streetwise (' + str(self.streetwise) + ')')

        # Empathy Skills
        if self.humanPerception > 0: print('Human Perception (' + str(self.humanPerception) + ')')
        if self.interview > 0: print('Interview (' + str(self.interview) + ')')
        if self.leadership > 0: print('Leadership (' + str(self.leadership) + ')')
        if self.seduction > 0: print('Seduction (' + str(self.seduction) + ')')
        if self.social > 0: print('Social (' + str(self.social) + ')')
        if self.persuasion > 0: print('Persuasion (' + str(self.persuasion) + ')')
        if self.performance > 0: print('Performance (' + str(self.performance) + ')')

        # Intelligence Skills
        if self.accounting > 0: print('Accounting (' + str(self.accounting) + ')')
        if self.anthropology > 0: print('Anthropology (' + str(self.anthropology) + ')')
        if self.awarenessNotice > 0: print('Awareness/Notice (' + str(self.awarenessNotice) + ')')
        if self.biology > 0: print('Biology (' + str(self.biology) + ')')
        if self.botany > 0: print('Botany (' + str(self.botany) + ')')
        if self.chemistry > 0: print('Chemistry (' + str(self.chemistry) + ')')
        if self.composition > 0: print('Composition (' + str(self.composition) + ')')
        if self.diagnoseIllness > 0: print('Diagnose Illness (' + str(self.diagnoseIllness) + ')')
        if self.education > 0: print('Education (' + str(self.education) + ')')
        if self.expert > 0: print('Expert (' + str(self.expert) + ')')
        if self.gamble > 0: print('Gamble (' + str(self.gamble) + ')')
        if self.hideEvade > 0: print('Hide/Evade (' + str(self.hideEvade) + ')')
        if self.history > 0: print('History (' + str(self.history) + ')')
        if self.language > 0: print('Language (' + str(self.language) + ')')
        if self.librarySearch > 0: print('Library Search (' + str(self.librarySearch) + ')')
        if self.math > 0: print('Mathematics (' + str(self.math) + ')')
        if self.physics > 0: print('Physics (' + str(self.physics) + ')')
        if self.programming > 0: print('Programming (' + str(self.programming) + ')')
        if self.shadowTrack > 0: print('Shadow/Track (' + str(self.shadowTrack) + ')')
        if self.stockMarket > 0: print('Stock Market (' + str(self.stockMarket) + ')')
        if self.systemKnowledge > 0: print('System Knowledge (' + str(self.systemKnowledge) + ')')
        if self.teaching > 0: print('Teaching (' + str(self.teaching) + ')')
        if self.survival > 0: print('Wilderness Survival (' + str(self.survival) + ')')
        if self.zoology > 0: print('Zoology (' + str(self.zoology) + ')')

        # Reflex Skills
        if self.archery > 0: print('Archery (' + str(self.archery) + ')')
        if self.athletics > 0: print('Athletics (' + str(self.athletics) + ')')
        if self.brawling > 0: print('Brawling (' + str(self.brawling) + ')')
        if self.dancing > 0: print('Dance (' + str(self.dancing) + ')')
        if self.dodgeEscape > 0: print('Dodge & Escape (' + str(self.dodgeEscape) + ')')
        if self.driving > 0: print('Drive (' + str(self.driving) + ')')
        if self.fencing > 0: print('Fencing (' + str(self.fencing) + ')')
        if self.handgun > 0: print('Handgun (' + str(self.handgun) + ')')
        if self.heavyWeapons > 0: print('Heavy Weapons (' + str(self.heavyWeapons) + ')')
        if self.aikido > 0: print('Aikido (' + str(self.aikido) + ')')
        if self.animalKungFu > 0: print('Animal Kung Fu (' + str(self.animalKungFu) + ')')
        if self.boxing > 0: print('Boxing (' + str(self.boxing) + ')')
        if self.capoeria > 0: print('Capoeria (' + str(self.capoeria) + ')')
        if self.choiLiFut > 0: print('Choi Li Fut (' + str(self.choiLiFut) + ')')
        if self.judo > 0: print('Judo (' + str(self.judo) + ')')
        if self.karate > 0: print('Karate (' + str(self.karate) + ')')
        if self.taeKwonDo > 0: print('Tae Kwon Do (' + str(self.taeKwonDo) + ')')
        if self.thaiKickBoxing > 0: print('Thai Kick Boxing (' + str(self.thaiKickBoxing) + ')')
        if self.wrestling > 0: print('Wrestling (' + str(self.wrestling) + ')')
        if self.melee > 0: print('Melee (' + str(self.melee) + ')')
        if self.motorcycle > 0: print('Motorcycle (' + str(self.motorcycle) + ')')
        if self.heavyMachinery > 0: print('Heavy Machinery (' + str(self.heavyMachinery) + ')')
        if self.gyro > 0: print('Pilot Gyro (' + str(self.gyro) + ')')
        if self.fixedWing > 0: print('Pilot Fixed Wing (' + str(self.fixedWing) + ')')
        if self.dirigible > 0: print('Pilot Dirigible (' + str(self.dirigible) + ')')
        if self.vectorThrust > 0: print('Pilot Vector Thrust (' + str(self.vectorThrust) + ')')
        if self.rifle > 0: print('Rifle (' + str(self.rifle) + ')')
        if self.stealth > 0: print('Stealth (' + str(self.stealth) + ')')
        if self.submachinegun > 0: print('Submachinegun (' + str(self.submachinegun) + ')')

        # Technical Skills
        if self.aeroTech > 0: print('Aero Tech (' + str(self.aeroTech) + ')')
        if self.vectorThrustTech > 0: print('Vector Thrust Tech (' + str(self.vectorThrustTech) + ')')
        if self.basicTech > 0: print('Basic Tech (' + str(self.basicTech) + ')')
        if self.cryotank > 0: print('Cryotank (' + str(self.cryotank) + ')')
        if self.cyberdeckDesign > 0: print('Cyberdeck Design (' + str(self.cyberdeckDesign) + ')')
        if self.cyberTech > 0: print('CyberTech (' + str(self.cyberTech) + ')')
        if self.demolitions > 0: print('Demolitions (' + str(self.demolitions) + ')')
        if self.disguise > 0: print('Disguise (' + str(self.disguise) + ')')
        if self.electronics > 0: print('Electronics (' + str(self.electronics) + ')')
        if self.electronicSecurity > 0: print('Electronic Security (' + str(self.electronicSecurity) + ')')
        if self.firstAid > 0: print('First Aid (' + str(self.firstAid) + ')')
        if self.forgery > 0: print('Forgery (' + str(self.forgery) + ')')
        if self.gyroTech > 0: print('Gyro Tech (' + str(self.gyroTech) + ')')
        if self.paintDraw > 0: print('Paint or Draw (' + str(self.paintDraw) + ')')
        if self.photoFilm > 0: print('Photo & Film (' + str(self.photoFilm) + ')')
        if self.pharmaceuticals > 0: print('Pharmaceuticals (' + str(self.pharmaceuticals) + ')')
        if self.pickLock > 0: print('Pick Lock (' + str(self.pickLock) + ')')
        if self.pickPocket > 0: print('Pick Pocket (' + str(self.pickPocket) + ')')
        if self.instrument > 0: print('Instrument (' + str(self.instrument) + ')')
        if self.weaponsmith > 0: print('Weaponsmith (' + str(self.weaponsmith) + ')')


def stat_roll():  # Statistic roll ONLY for CP2020 -cl 1/26
    x = d(2,6,0)
    while x > 10: x = d(2,6,0)
    return x


class cyberpunkCharacter():
    def __init__(self):
        self.name = 'Odysseus'
        self.role = 'Solo'
        self.score_sum = [18, 'Average']
        self.int = 2
        self.ref = [2, 2]
        self.tech = 2
        self.cool = 2
        self.attr = 2
        self.luck = 2
        self.ma = 2
        self.body = [2, 'Very Weak']
        self.emp = [float(2), 2]
        self.run = 6  # MAx3 (meters)
        self.leap = float(1.5)  # Run/4 (meters)
        self.lift = 80  # 40x BT (kilos)
        self.save = 2
        self.btm = 0
        self.cyberware = []
        self.ability = ['Combat Sense', 1]
        self.occupation = ['Street Ronin', 2000]
        self.armor = 'Heavy Leather'
        self.weapon = 'Knife'
        self.skills = 'Skills Err'
        self.family_ranking = 'Corporate Executive'
        self.parents = 'Alive'
        self.family_status = False
        self.tragedy = 'Family lost everything through betrayal'
        self.childhood_env = 'Spent on the Street, with no adult supervision'
        self.siblings = []
        self.age = 16
        self.possessions = []

        self.homeworld = 'HomeWorldErr'
        self.languages = []
        self.clothes = 'Naked'
        self.hairstyle = 'Bald'
        self.affectations = 'None'
        self.personality = 'Shy and Secretive'
        self.valuedPerson = 'A parent'
        self.virtue = 'Money'
        self.disposition = 'Neutral'
        self.valuedPossession = 'A weapon'
        self.lifeEvents = []

    def rollStats(self):
        self.int = stat_roll()
        self.ref[0] = stat_roll()
        self.ref[1] = self.ref[0]
        self.tech = stat_roll()
        self.cool = stat_roll()
        self.attr = stat_roll()
        self.ma = stat_roll()
        self.body[0] = stat_roll()
        self.emp[0] = stat_roll()
        self.emp[1] = self.emp[0]
        self.run = self.ma * 3
        self.leap = self.run // 4
        self.lift = 40 * self.body[0]
        self.save = self.body[0]
        if self.body[0] <= 2:
            self.body[1] = 'Very Weak'
            self.btm = 0
        if self.body[0] >= 3 and self.body[0] <= 4:
            self.body[1] = 'Weak'
            self.btm = -1
        if self.body[0] >= 5 and self.body[0] <= 7:
            self.body[1] = 'Average'
            self.btm = -2
        if self.body[0] == 8 or self.body[0] == 9:
            self.body[1] = 'Strong'
            self.btm = -3
        if self.body[0] == 10:
            self.body[1] = 'Very Strong'
            self.btm = -5

    def scoreSumCalculator(self):
        self.score_sum[0] = self.int + self.ref[1] + self.tech + self.cool + self.attr + self.luck + self.ma + \
                            self.body[0] + self.emp[1]
        if self.score_sum[0] < 40: self.score_sum[1] = 'Bullet Fodder'
        if self.score_sum[0] >= 40 and self.score_sum[0] < 50: self.score_sum[1] = 'Film Extra'
        if self.score_sum[0] >= 50 and self.score_sum[0] < 60: self.score_sum[1] = 'Background Character'
        if self.score_sum[0] >= 60 and self.score_sum[0] < 70: self.score_sum[1] = 'Minor Supporting Character'
        if self.score_sum[0] >= 70 and self.score_sum[0] < 75: self.score_sum[1] = 'Major Supporting Character'
        if self.score_sum[0] >= 75 and self.score_sum[0] < 80: self.score_sum[1] = 'Minor Hero'
        if self.score_sum[0] >= 80 and self.score_sum[0] < 90: self.score_sum[1] = 'Major Hero'
        if self.score_sum[0] == 90: self.score_sum[1] = 'Impossibility'

    def sibling_generator(self, sibling_num):
        for i in range(sibling_num):
            x = random.randint(1, 7)
            ages = 'indexErr'
            if x <= 5: ages = 'older'
            if x >= 6 and x != 10: ages = 'younger'
            if x == 10: ages = 'twin'
            genders = ['brother', 'sister']
            feelings = ['dislikes you', 'likes you', 'neutral', 'hero-worship you', 'hate you']
            x = ages + ' ' + random.choice(genders) + ' (' + random.choice(feelings) + ')'
            self.siblings.append(x)

    def originHandler(self):
        anglo_american = ['English']
        african = ['Bantu', 'Kongo', 'Ashandi', 'Zulu', 'Swahili']
        japanese_korean = ['Japanese', 'Korean']
        central_european_soviet = ['Bulgarian', 'Russian', 'Czech', 'Polish', 'Ukranian', 'Slovak']
        pacific_islander = ['Microneasian', 'Tagalog', 'Polynesian', 'Malayan', 'Sudanese', 'Indonesian', 'Hawaiian']
        chinese_southeast_asian = ['Burmese', 'Cantonese', 'Mandarin', 'Thai', 'Tibetan', 'Vietnamese']
        future_punk = ['Lingua Astra', 'Alien Language']
        hispanic_american = ['English', 'Spanish']
        central_south_american = ['Spanish', 'Portuguese']
        european = ['French', 'German', 'English', 'Spanish', 'Italian', 'Greek', 'Danish', 'Dutch', 'Norwegian',
                    'Swedish', 'Finnish']
        languages = [anglo_american, african, japanese_korean, central_european_soviet, pacific_islander,
                     chinese_southeast_asian, future_punk, hispanic_american, central_south_american, european]
        origin = random.choice(languages)
        if origin == anglo_american:
            self.homeworld = 'Anglo-American'
            self.languages.append(random.choice(anglo_american))
        if origin == african:
            self.homeworld = 'African'
            self.languages.append(random.choice(african))
        if origin == japanese_korean:
            self.homeworld = 'Japanese/Korean'
            self.languages.append(random.choice(japanese_korean))
        if origin == central_european_soviet:
            self.homeworld = 'Central European/Soviet'
            self.languages.append(random.choice(central_european_soviet))
        if origin == pacific_islander:
            self.homeworld = 'Pacific Islander'
            self.languages.append(random.choice(pacific_islander))
        if origin == chinese_southeast_asian:
            self.homeworld = 'Chinese/Southeast Asian'
            self.languages.append(random.choice(chinese_southeast_asian))
        if origin == future_punk:
            self.homeworld = 'Future-Punk'
            self.languages.append(random.choice(future_punk))
        if origin == hispanic_american:
            self.homeworld = 'Hispanic American'
            self.languages.append(random.choice(hispanic_american))
        if origin == central_south_american:
            self.homeworld = 'Central/South American'
            self.languages.append(random.choice(central_south_american))
        if origin == european:
            self.homeworld = 'European'
            self.languages.append(random.choice(european))

    def personalStylist(self):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        if x == 1: self.clothes = 'Biker Leathers'
        if x == 2: self.clothes = 'Blue Jeans'
        if x == 3: self.clothes = 'Corporate Suits'
        if x == 4: self.clothes = 'Jumpsuits'
        if x == 5: self.clothes = 'Mikiskirts'
        if x == 6: self.clothes = 'High Fashion'
        if x == 7: self.clothes = 'Cammos'
        if x == 8: self.clothes = 'Normal Clothes'
        if x == 9: self.clothes = 'Nude'
        if x == 10: self.clothes = 'Bag Lady Chic'
        if y == 1: self.hairstyle = 'Mohawk'
        if y == 2: self.hairstyle = 'Long & Ratty'
        if y == 3: self.hairstyle = 'Short & Spiked'
        if y == 4: self.hairstyle = 'Wild & All Over'
        if y == 5: self.hairstyle = 'Bald'
        if y == 6: self.hairstyle = 'Striped'
        if y == 7: self.hairstyle = 'Tinted'
        if y == 8: self.hairstyle = 'Neat, Short'
        if y == 9: self.hairstyle = 'Short, Curly'
        if y == 10: self.hairstyle = 'Long, Straight'
        if z == 1: self.affectations = 'Tattoos'
        if z == 2: self.affectations = 'Mirrorshades'
        if z == 3: self.affectations = 'Ritual Scars'
        if z == 4: self.affectations = 'Spiked Gloves'
        if z == 5: self.affectations = 'Nose Rings'
        if z == 6: self.affectations = 'Earrings'
        if z == 7: self.affectations = 'Long Fingernails'
        if z == 8: self.affectations = 'Spike-Heeled Boots'
        if z == 9: self.affectations = 'Weird Contact Lenses'
        if z == 10: self.affectations = 'Fingerless Gloves'

    def originAndPersonalStyle(self, readFromPlanet, planet):
        if readFromPlanet == True:
            self.homeworld = planet
            self.languages.append(planet.language)
        if readFromPlanet == False: self.originHandler()
        self.personalStylist()

    def childhood(self):
        family_rankings = ['Corporate Executive', 'Corporate Manager', 'Corporate Technician',
                           'Nomad Pack', 'Pirate Fleet', 'Gang Family', 'Crime Lord', 'Combat Zone Poor',
                           'Urban homeless', 'Arcology Family']
        shtyp_list = ['Your parent(s) died in warfare', 'Your parent(s) died in an accident',
                      'Your parent(s) were murdered', "Your parent(s) have amnesia and don't remember you",
                      'You never knew your parents', 'Your parent(s) are in hiding to protect you',
                      'You were left with relatives for safekeeping', 'You grew up on the Street and never had parents',
                      'Your parent(s) gave you up for adoption', 'Your parents sold you for money']
        family_tragedies = ['Family lost everything through betrayal', 'Family lost everything through bad management',
                            'Family exiled or otherwise driven from their original home/nation/corporation',
                            'Family is in prison and you alone escaped',
                            'Family vanished-- you are the only remaining member',
                            'Family was murdered/killed and you were the only survivor',
                            'Family is involved in a longterm conspiracy, organization or association, such as a crime family or revolutionary group',
                            'Your family was scattered to the winds due to misfortune',
                            'Your family is cursed with a hereditary feud that has lasted for generations',
                            'You are the inheritor of a family debt; you must honor this debt before moving on with your life']
        environments = ['Spent on the Street, with no adult supervision', 'Spent in a safe Corporate Suburbia',
                        'In a Nomad Pack moving from town to town', 'In a decaying, once upscale neighborhood',
                        'In a defended Corporate Zone in the central city', 'In the heart of the Combat Zone',
                        'In a small village or town far from the city', 'In an arcology city',
                        'In an aquatic Pirate Pack', 'On a Corporate controlled Farm or Research Facility']

        self.family_ranking = random.choice(family_rankings)
        x = random.randint(1, 10)
        if x <= 6: self.parents = random.choice(shtyp_list)
        if x >= 7: self.parents = 'Both alive'
        x = random.randint(1, 10)
        if x <= 6: self.family_status = True
        if self.family_status == True: self.family_tragedy = random.choice(family_tragedies)
        self.childhood_env = random.choice(environments)
        self.siblings = []
        x = random.randint(1, 10)
        if x <= 7: self.sibling_generator(x)
        if x >= 8: self.siblings = ['none']

    def randomPersonalityTrait(self):
        x = random.randint(1, 10)
        if x == 1: self.personality = 'Shy and Secretive'
        if x == 2: self.personality = 'Rebellious, Antisocial, Violent'
        if x == 3: self.personality = 'Arrogant, Proud and Aloof'
        if x == 4: self.personality = 'Moody, Rash and Headstrong'
        if x == 5: self.personality = 'Picky, Fussy and Nervous'
        if x == 6: self.personality = 'Stable and Serious'
        if x == 7: self.personality = 'Silly and Fluffheaded'
        if x == 8: self.personality = 'Sneaky and Deceptive'
        if x == 9: self.personality = 'Intellectual and Detached'
        if x == 10: self.personality = 'Friendly and Outgoing'

    def randomValuedPerson(self):
        x = random.randint(1, 10)
        if x == 1: self.valuedPerson = 'A parent'
        if x == 2: self.valuedPerson = 'Brother or Sister'
        if x == 3: self.valuedPerson = 'Lover'
        if x == 4: self.valuedPerson = 'Friend'
        if x == 5: self.valuedPerson = 'Yourself'
        if x == 6: self.valuedPerson = 'A Pet'
        if x == 7: self.valuedPerson = 'Teacher or Mentor'
        if x == 8: self.valuedPerson = 'Public Figure'
        if x == 9: self.valuedPerson = 'Personal Hero'
        if x == 10: self.valuedPerson = 'No One'

    def randomVirtue(self):
        x = random.randint(1, 10)
        if x == 1: self.virtue = 'Money'
        if x == 2: self.virtue = 'Honor'
        if x == 3: self.virtue = 'Your Word'
        if x == 4: self.virtue = 'Honesty'
        if x == 5: self.virtue = 'Knowledge'
        if x == 6: self.virtue = 'Vengeance'
        if x == 7: self.virtue = 'Love'
        if x == 8: self.virtue = 'Power'
        if x == 9: self.virtue = 'Having a Good Time'
        if x == 10: self.virtue = 'Friendship'

    def randomDisposition(self):
        x = random.randint(1, 10)
        if x <= 2: self.disposition = 'Neutral'
        if x == 3: self.disposition = 'Like Almost Everyone'
        if x == 4: self.disposition = 'Hate Almost Everyone'
        if x == 5: self.disposition = 'People are Tools'
        if x == 6: self.disposition = 'Everyone is Valuable'
        if x == 7: self.disposition = 'People are Obstacles'
        if x == 8: self.disposition = 'People are Untrustworthy'
        if x == 9: self.disposition = "Wipe 'em Out"
        if x == 10: self.disposition = 'People are Wonderful'

    def randomValuedPossession(self):
        x = random.randint(1, 10)
        if x == 1: self.valuedPossession = 'A Weapon'
        if x == 2: self.valuedPossession = 'A Tool'
        if x == 3: self.valuedPossession = 'Piece of Clothing'
        if x == 4: self.valuedPossession = 'A Photograph'
        if x == 5: self.valuedPossession = 'Book or Diary'
        if x == 6: self.valuedPossession = 'A Recording'
        if x == 7: self.valuedPossession = 'Musical Instrument'
        if x == 8: self.valuedPossession = "Piece of Jewelry"
        if x == 9: self.valuedPossession = 'A Toy'
        if x == 10: self.valuedPossession = 'A Letter'

    def motivations(self):
        self.randomPersonalityTrait()
        self.randomValuedPerson()
        self.randomVirtue()
        self.randomDisposition()
        self.randomValuedPossession()

    def careerAptitudeTest(self):
        classesList = ['Rockerboy', 'Solo', 'Netrunner', 'Techie', 'Medtechie', 'Cop', 'Corporate', 'Fixer', 'Nomad']
        if self.int > 7:
            classesList.append('Netrunner')
            classesList.append('Corporate')
        if self.ref[1] > 7:
            classesList.append('Solo')
            classesList.append('Nomad')
            classesList.append('Rockerboy')
        if self.tech > 7:
            classesList.append('Techie')
            classesList.append('Medtechie')
        if self.cool > 7:
            classesList.append('Solo')
            classesList.append('Nomad')
            classesList.append('Rocker')
            classesList.append('Fixer')
        if self.attr > 7:
            classesList.append('Media')
            classesList.append('Rockerboy')
        if self.body[0] > 7:
            classesList.append('Solo')
            classesList.append('Rockerboy')
            classesList.append('Nomad')
        role = random.choice(classesList)
        self.role = role

    def occupationTable(self):
        # Returns occupation from CP2020 p.58 'Occupation Table'.
        # Rocker
        if self.role == 'Rockerboy':
            if self.skills.charismaticLeadership <= 5: self.occupation = ['Desperate for gigs', 1000]
            if self.skills.charismaticLeadership == 6: self.occupation = ['Regular Club Jobs', 1500]
            if self.skills.charismaticLeadership == 7: self.occupation = ['Play the Big Clubs', 2000]
            if self.skills.charismaticLeadership == 8: self.occupation = ["You've got a Contract", 5000]
            if self.skills.charismaticLeadership == 9: self.occupation = ['Concert Band', 8000]
            if self.skills.charismaticLeadership == 10: self.occupation = ['Major Act', 12000]
        # Solo
        if self.role == 'Solo':
            if self.skills.combatSense <= 5: self.occupation = ['Street Ronin', 2000]
            if self.skills.combatSense == 6: self.occupation = ['Private Enforcer', 3000]
            if self.skills.combatSense == 7: self.occupation = ['Corporate Muscle', 4500]
            if self.skills.combatSense == 8: self.occupation = ['Professional Operative', 7000]
            if self.skills.combatSense == 9: self.occupation = ['Major League Hitter', 9000]
            if self.skills.combatSense == 10: self.occupation = ['Solo Elite', 12000]
        # Cop
        if self.role == 'Cop':
            if self.skills.authority <= 5: self.occupation = ['Private Guard', 1000]
            if self.skills.authority == 6: self.occupation = ['City Cop', 1200]
            if self.skills.authority == 7: self.occupation = ['Corporate Guard/Detective', 3000]
            if self.skills.authority == 8: self.occupation = ['Corporate Secutiry/Psycho Squad', 5000]
            if self.skills.authority == 9: self.occupation = ['Enforcement Team Leader', 7000]
            if self.skills.authority == 10: self.occupation = ['Security Head/Police Chief', 9000]
        # Corporate
        if self.role == 'Corporate':
            if self.skills.resources <= 5: self.occupation = ['Assistant', 1500]
            if self.skills.resources == 6: self.occupation = ['Manager', 3000]
            if self.skills.resources == 7: self.occupation = ['Junior Executive', 5000]
            if self.skills.resources == 8: self.occupation = ['Executive', 7000]
            if self.skills.resources == 9: self.occupation = ['Department Head', 9000]
            if self.skills.resources == 10: self.occupation = ['Division Head', 12000]
        # Media
        if self.role == 'Media':
            if self.skills.credibility <= 5: self.occupation = ['Stringer Reporter', 1000]
            if self.skills.credibility == 6: self.occupation = ['Staff Reporter', 1200]
            if self.skills.credibility == 7: self.occupation = ['Section Editor', 3000]
            if self.skills.credibility == 8: self.occupation = ['Producer/Managing Editor', 5000]
            if self.skills.credibility == 9: self.occupation = ['Local Media Personality', 7000]
            if self.skills.credibility == 10: self.occupation = ['National Media Personality', 10000]
        # Fixer
        if self.role == 'Fixer':
            if self.skills.streetdeal <= 5: self.occupation = ['Street Punk', 1500]
            if self.skills.streetdeal == 6: self.occupation = ['Gang Leader', 3000]
            if self.skills.streetdeal == 7: self.occupation = ['Enforcer', 5000]
            if self.skills.streetdeal == 8: self.occupation = ['Sub-Lieutenant', 7000]
            if self.skills.streetdeal == 9: self.occupation = ['Lieutenant', 8000]
            if self.skills.streetdeal == 10: self.occupation = ['Crime Boss', 10000]
        # Techie
        if self.role == 'Techie':
            if self.skills.juryRig <= 5: self.occupation = ['Local Fixit Man', 1000]
            if self.skills.juryRig == 6: self.occupation = ['Private Operator', 2000]
            if self.skills.juryRig == 7: self.occupation = ['Corporate Tech', 3000]
            if self.skills.juryRig == 8: self.occupation = ['Junior Engineer', 4000]
            if self.skills.juryRig == 9: self.occupation = ['Engineer', 5000]
            if self.skills.juryRig == 10: self.occupation = ['Senior Engineer', 8000]
        # Netrunner
        if self.role == 'Netrunner':
            if self.skills.interface <= 5: self.occupation = ['Weefle Runner', 1000]
            if self.skills.interface == 6: self.occupation = ['Hacker', 2000]
            if self.skills.interface == 7: self.occupation = ['Bit Jockey', 3000]
            if self.skills.interface == 8: self.occupation = ['Net Cowboy', 5000]
            if self.skills.interface == 9: self.occupation = ['Deckslinger', 7000]
            if self.skills.interface == 10: self.occupation = ['Sysop', 10000]
        # Medtechie
        if self.role == 'Medtechie':
            if self.skills.medicalTech <= 5: self.occupation = ['Patchman', 1600]
            if self.skills.medicalTech == 6: self.occupation = ['Medical Technician', 3000]
            if self.skills.medicalTech == 7: self.occupation = ['RipperDoc', 5000]
            if self.skills.medicalTech == 8: self.occupation = ['Trauma Team Medic', 7000]
            if self.skills.medicalTech == 9: self.occupation = ['General Practitioner', 10000]
            if self.skills.medicalTech == 10: self.occupation = ['Specialist Physician', 15000]
        # Nomad
        if self.role == 'Nomad':
            if self.skills.family <= 5: self.occupation = ['Clanmember', 1000]
            if self.skills.family == 6: self.occupation = ['Warrior', 1500]
            if self.skills.family == 7: self.occupation = ['Head of Household', 2000]
            if self.skills.family == 8: self.occupation = ['Scout', 3000]
            if self.skills.family == 9: self.occupation = ['Clan Senior', 4000]
            if self.skills.family == 10: self.occupation = ['Family Head', 5000]

    def bigProblemsBigWins(self):
        oddOrEven = d(1,10,0)
        oddResult = False
        evenResult = False
        if oddOrEven % 2 == 1: oddResult = True
        if oddOrEven % 2 == 0: evenResult = True
        x = d(1,10,0)
        # Disaster Strikes!
        if oddResult == True:
            whatToDo = ['Clear your name',
                        'Try to forget',
                        'Hunt them down',
                        "Get what's yours",
                        'Save anyone involved']
            action = random.choice(whatToDo)
            if x == 1:
                debt = random.randint(1, 10) * 100
                return ('Financial Loss/Debt: ' + str(debt) + ' Cr.' + ' (' + action + ')')
            if x == 2:
                timeImprisoned = random.randint(1, 10)
                imprisonment = ['imprisoned', 'held hostage']
                return ('You have been ' + random.choice(imprisonment) + ' for ' + str(
                    timeImprisoned) + ' months.' + ' (' + action + ')')
            if x == 3:
                issues = ['an illness', 'a drug habit']
                self.ref[1] -= 1
                return ('You pick up ' + random.choice(
                    issues) + ' during this time and lose 1 REF.' + ' (' + action + ')')
            if x == 4:
                y = d(1,10,0)
                backstabbers = ['during a romance', 'within your career']
                if y < 4: return 'You have been backstabbed and are being blackmailed' + ' (' + action + ')'
                if y >= 4 and y < 8: return 'You have been backstabbed and a secret about you has been exposed' + ' (' + action + ')'
                if y >= 8: return 'You were backstabbed by a close friend ' + random.choice(
                    backstabbers) + ' (' + action + ')'
            if x == 5:
                y = d(1,10,0)
                z = d(1,10,0)
                if y < 5:
                    return 'You are disfigured in a horrible accidents (-5 ATT)' + ' (' + action + ')'
                    self.attr -= 5
                if y == 5 or y == 6:
                    return 'You had a bad accident and were hospitalized for ' + str(
                        z) + ' months' + ' (' + action + ')'
                if y == 7 or y == 8:
                    return 'You had a bad accident and lost ' + str(z) + ' months of your memory' + ' (' + action + ')'
                if y == 9 or y == 10:
                    return 'You had an awful accident and the memory of it wakes you up screaming (8/10 chance)' + ' (' + action + ')'

            if x == 6:
                y = d(1,10,0)
                victim = random.choice(['lover', 'friend', 'relative'])
                if y < 6: return 'Your ' + victim + ' was killed accidentally (' + action + ')'
                if y >= 6 and y < 9: return 'Your ' + victim + ' was murdered by unknown parties' + ' (' + action + ')'
                if y >= 9: return 'Your ' + victim + ' was murdered, and you know who did it' + ' (' + action + ')'

            if x == 7:
                y = d(1,10,0)
                accusation = 'accusationErr'
                if y < 4: accusation = 'theft'
                if y == 4 or y == 5: accusation = 'cowardace'
                if y >= 6 and y <= 8: accusation = 'murder'
                if y == 9: accusation = 'rape'
                if y == 10: accusation = random.choice(['lying', 'betrayal'])
                return 'You were set up and accused of ' + accusation + ' (' + action + ')'

            if x == 8:
                y = d(1,10,0)
                policeForce = 'policeErr'
                if y < 4: policeForce = 'a few local cops'
                if y >= 4 and y <= 6: policeForce = 'the local department'
                if y == 7 or y == 8: policeForce = 'the state ' + random.choice(['police', 'militia'])
                if y > 8: policeForce = 'the Federal Government'
                return 'You are hunted by ' + policeForce + ' for crimes you ' + random.choice(
                    ['did', 'did not']) + ' commit' + ' (' + action + ')'

            if x == 9:
                y = d(1,10,0)
                corporation = 'corporationErr'
                if y < 4: corporation = 'a small, local firm'
                if y >= 4 and y <= 6: corporation = 'a statewide corporation'
                if y == 7 or y == 8: corporation = 'a nationwide corporation'
                if y > 8: corporation = 'a multinational corporation'
                return 'You have angered ' + corporation + "'s honcho" + ' (' + action + ')'

            if x == 10:
                y = d(1,10,0)
                if y < 4:
                    self.ref[1] -= 1
                    return 'You suffer some kind of nervous disorder, probably from bioplague (-1 REF)' + ' (' + action + ')'
                if y >= 4 and y <= 7:
                    self.cool -= 1
                    return 'You suffer from anxiety attacks and phobias (-1 CL)' + ' (' + action + ')'
                if y > 8:
                    self.ref[1] -= 1
                    self.cool -= 1
                    return 'You suffer from a major psychosis and hear voices, are irrational, violent, depressive (-1 CL -1 REF)' + ' (' + action + ')'

        # YOU GET LUCKY
        if oddResult == False:
            x = d(1,10,0)

            if x == 1:
                connections = ['Police Department', "District Attorney's Office", "Mayor's Office"]
                return 'Make a powerful connection in the ' + random.choice(connections)

            if x == 2:
                windfall = d(1,10,0) * 100
                return 'Financial Windfall: +' + str(windfall) + ' Cr.'

            if x == 3:
                yourCut = d(1,10,0) * 100
                return 'Big score on a ' + random.choice(['job', 'deal']) + ': +' + str(yourCut) + ' Cr.'

            if x == 4:
                y = d(1,10,0)
                if y == 1:
                    martialArt = 'an Aikido'
                    if self.skills.aikido > 0: self.skills.aikido += 1
                    if self.skills.aikido <= 0: self.skills.aikido = 2
                if y == 2:
                    martialArt = 'an Animal Kung Fu'
                    if self.skills.animalKungFu > 0: self.skills.animalKungFu += 1
                    if self.skills.animalKungFu <= 0: self.skills.animalKungFu = 2
                if y == 3:
                    martialArt = 'a Capoeria'
                    if self.skills.capoeria > 0: self.skills.capoeria += 1
                    if self.skills.capoeria <= 0: self.skills.capoeria = 2
                if y == 4:
                    martialArt = 'a Choi Li Fut'
                    if self.skills.choiLiFut > 0: self.skills.choiLiFut += 1
                    if self.skills.choiLiFut <= 0: self.skills.choiLiFut = 2
                if y == 5:
                    martialArt = 'a Judo'
                    if self.skills.judo > 0: self.skills.judo += 1
                    if self.skills.judo <= 0: self.skills.judo = 2
                if y == 6:
                    martialArt = 'a Karate'
                    if self.skills.karate > 0: self.skills.karate += 1
                    if self.skills.karate <= 0: self.skills.karate = 2
                if y == 7:
                    martialArt = 'a Tae Kwon Do'
                    if self.skills.taeKwonDo > 0: self.skills.taeKwonDo += 1
                    if self.skills.taeKwonDo <= 0: self.skills.taeKwonDo = 2
                if y == 8:
                    martialArt = 'a Thai Kick Boxing'
                    if self.skills.thaiKickBoxing > 0: self.skills.thaiKickBoxing += 1
                    if self.skills.thaiKickBoxing <= 0: self.skills.thaiKickBoxing = 2
                if y == 9:
                    martialArt = 'a Wrestling'
                    if self.skills.wrestling > 0: self.skills.wrestling += 1
                    if self.skills.wrestling <= 0: self.skills.wrestling = 2
                return 'You find ' + martialArt + ' Sensei'

            if x == 5:
                intSkills = ['Accounting', 'Anthropology', 'Awareness/Notice', 'Biology',
                             'Botany', 'Chemistry', 'Composition', 'Diagnose Illness', 'Education',
                             'Expert', 'Gamble', 'Hide/Evade', 'History', 'Language', 'Library Search',
                             'Mathematics', 'Physics', 'Programming', 'Shadow/Track', 'Stock Market',
                             'System Knowledge', 'Teaching', 'Wilderness Survival', 'Zoology']
                intSkill = random.choice(intSkills)
                if intSkill == 'Accounting':
                    if self.skills.accounting > 0: self.skills.accounting += 1
                    if self.skills.accounting <= 0: self.skills.accounting = 2
                if intSkill == 'Anthropology':
                    if self.skills.anthropology > 0: self.skills.anthropology += 1
                    if self.skills.anthropology <= 0: self.skills.anthropology = 2
                if intSkill == 'Awareness/Notice':
                    if self.skills.awarenessNotice > 0: self.skills.awarenessNotice += 1
                    if self.skills.awarenessNotice <= 0: self.skills.awarenessNotice = 2
                if intSkill == 'Biology':
                    if self.skills.biology > 0: self.skills.biology += 1
                    if self.skills.biology <= 0: self.skills.biology = 2
                if intSkill == 'Botany':
                    if self.skills.botany > 0: self.skills.botany += 1
                    if self.skills.botany <= 0: self.skills.botany = 2
                if intSkill == 'Chemistry':
                    if self.skills.chemistry > 0: self.skills.chemistry += 1
                    if self.skills.chemistry <= 0: self.skills.chemistry = 2
                if intSkill == 'Composition':
                    if self.skills.composition > 0: self.skills.composition += 1
                    if self.skills.composition <= 0: self.skills.composition = 2
                if intSkill == 'Diagnose Illness':
                    if self.skills.diagnoseIllness > 0: self.skills.diagnoseIllness += 1
                    if self.skills.diagnoseIllness <= 0: self.skills.diagnoseIllness = 2
                if intSkill == 'Education':
                    if self.skills.education > 0: self.skills.education += 1
                    if self.skills.education <= 0: self.skills.education = 2
                if intSkill == 'Expert':
                    if self.skills.expert > 0: self.skills.expert += 1
                    if self.skills.expert <= 0: self.skills.expert = 2
                if intSkill == 'Gamble':
                    if self.skills.gamble > 0: self.skills.gamble += 1
                    if self.skills.gamble <= 0: self.skills.gamble = 2
                if intSkill == 'Hide/Evade':
                    if self.skills.hideEvade > 0: self.skills.hideEvade += 1
                    if self.skills.hideEvade <= 0: self.skills.hideEvade = 2
                if intSkill == 'History':
                    if self.skills.history > 0: self.skills.history += 1
                    if self.skills.history <= 0: self.skills.history = 2
                if intSkill == 'Language':
                    if self.skills.language > 0: self.skills.language += 1
                    if self.skills.language <= 0: self.skills.language = 2
                if intSkill == 'Library Search':
                    if self.skills.librarySearch > 0: self.skills.librarySearch += 1
                    if self.skills.librarySearch <= 0: self.skills.librarySearch = 2
                if intSkill == 'Mathematics':
                    if self.skills.math > 0: self.skills.math += 1
                    if self.skills.math <= 0: self.skills.math = 2
                if intSkill == 'Physics':
                    if self.skills.physics > 0: self.skills.physics += 1
                    if self.skills.physics <= 0: self.skills.physics = 2
                if intSkill == 'Programming':
                    if self.skills.programming > 0: self.skills.programming += 1
                    if self.skills.programming <= 0: self.skills.programming = 2
                if intSkill == 'Shadow/Track':
                    if self.skills.shadowTrack > 0: self.skills.shadowTrack += 1
                    if self.skills.shadowTrack <= 0: self.skills.shadowTrack = 2
                if intSkill == 'Stock Market':
                    if self.skills.stockMarket > 0: self.skills.stockMarket += 1
                    if self.skills.stockMarket <= 0: self.skills.stockMarket = 2
                if intSkill == 'System Knowledge':
                    if self.skills.systemKnowledge > 0: self.skills.systemKnowledge += 1
                    if self.skills.systemKnowledge <= 0: self.skills.systemKnowledge = 2
                if intSkill == 'Teaching':
                    if self.skills.teaching > 0: self.skills.teaching += 1
                    if self.skills.teaching <= 0: self.skills.teaching = 2
                if intSkill == 'Wilderness Survival':
                    if self.skills.survival > 0: self.skills.survival += 1
                    if self.skills.survival <= 0: self.skills.survival = 2
                if intSkill == 'Zoology':
                    if self.skills.zoology > 0: self.skills.zoology += 1
                    if self.skills.zoology <= 0: self.skills.zoology = 2
                return 'You find a legendary ' + intSkill + ' teacher.'

            if x == 6: return 'Powerful corporate exec owes you one favor'
            if x == 7: return 'Befriended Nomad Pack: Family +2 1/mo.'
            if x == 8: return 'Befriend Police Force Member: +2 Streetwise with Police Business'
            if x == 9: return 'Befriended Local Boostergang: Family +2 1/mo.'

            if x == 10:
                combatSkills = ['Dodge/Escape', 'Fencing', 'Handgun', 'Heavy Weapons', 'Melee', 'Rifle',
                                'Submachinegun']
                chosenSkill = random.choice(combatSkills)
                if chosenSkill == 'Dodge/Escape':
                    print(self.skills.dodgeEscape)
                    if self.skills.dodgeEscape > 0: self.skills.dodgeEscape += 1
                    if self.skills.dodgeEscape <= 0: self.skills.dodgeEscape = 2
                if chosenSkill == 'Fencing':
                    if self.skills.fencing > 0: self.skills.fencing += 1
                    if self.skills.fencing <= 0: self.skills.fencing = 2
                if chosenSkill == 'Handgun':
                    if self.skills.handgun > 0: self.skills.handgun += 1
                    if self.skills.handgun <= 0: self.skills.handgun = 2
                if chosenSkill == 'Heavy Weapons':
                    if self.skills.heavyWeapons > 0: self.skills.heavyWeapons += 1
                    if self.skills.heavyWeapons <= 0: self.skills.heavyWeapons = 2
                if chosenSkill == 'Melee':
                    if self.skills.melee > 0: self.skills.melee += 1
                    if self.skills.melee <= 0: self.skills.melee = 2
                if chosenSkill == 'Rifle':
                    if self.skills.rifle > 0: self.skills.rifle += 1
                    if self.skills.rifle <= 0: self.skills.rifle = 2
                if chosenSkill == 'Submachinegun':
                    if self.skills.submachinegun > 0: self.skills.submachinegun += 1
                    if self.skills.submachinegun <= 0: self.skills.submachinegun = 2
                return 'You find a legendary ' + chosenSkill + ' teacher'

    # TODO Add Enemies
    def friendsAndEnemies(self):
        friendOrEnemy = d(1,10,0)
        if friendOrEnemy < 6:
            maleOrFemale = random.randint(1, 2)
            if maleOrFemale == 1: gender = 'female'
            if maleOrFemale == 2: gender = 'male'
            x = d(1,10,0)
            if x == 1: friend = 'Like a big sibling to you'
            if x == 2: friend = 'Like a little sibling to you'
            if x == 3: friend = 'A ' + random.choice(['Teacher', 'Mentor'])
            if x == 4: friend = 'A ' + random.choice(['Partner', 'Co-worker'])
            if x == 5: friend = 'An old lover'
            if x == 6: friend = 'An old enemy'
            if x == 7: friend = 'Like a foster parent'
            if x == 8: friend = 'A relative'
            if x == 9: friend = 'A childhood friend'
            if x == 10: friend = 'Met through common interest'
            return 'New Friend: ' + friend + ' (' + gender + ')'
        if friendOrEnemy >= 6: return 'Made Enemy'

    def romanticLife(self):
        x = d(1,10,0)
        if x < 5: return 'Happy Love Affair'
        if x == 5:
            y = d(1,10,0)
            if y == 1: return 'Lover Died in an Accident'
            if y == 2: return 'Lover Mysteriously Vanished'
            if y == 3: return 'You and your Lover Did Not Make It Work'
            if y == 4: return 'A Personal Vendetta Came Between You and your Lover'
            if y == 5: return 'Lover Kidnapped'
            if y == 6: return 'Lover Went Insane'
            if y == 7: return 'Lover Committed Suicide'
            if y == 8: return 'Lover Killed in a Fight'
            if y == 9: return 'Rival Cut You Off from your Lover'
            if y == 10: return random.choice(['Lover Imprisoned', 'Lover Exiled'])
        if x == 6 or x == 7:
            y = d(1,10,0)
            z = d(1,10,0)
            if y == 1: affair = 'Their ' + random.choice(['friends', 'family']) + ' hate you'
            if y == 2: affair = 'Their ' + random.choice(
                ['friends', 'family']) + ' would use any means to get rid of you'
            if y == 3: affair = 'Your ' + random.choice(['friends', 'family']) + ' hate them'
            if y == 4: affair = random.choice(['You', 'They']) + ' have a romantic rival'
            if y == 5: affair = 'You are separated in some way'
            if y == 6: affair = 'You fight constantly'
            if y == 7: affair = 'You are Professional Rivals'
            if y == 8: affair = random.choice(['You', 'They']) + ' are insanely jealous'
            if y == 9: affair = random.choice(['You', 'They']) + ' are messing around'
            if y == 10: affair = 'You have conflicting backgrounds and families'
            if z == 1: feelings = 'They still love you'
            if z == 2: feelings = 'You still love them'
            if z == 3: feelings = 'You still love each other'
            if z == 4: feelings = 'You hate them'
            if z == 5: feelings = 'They hate you'
            if z == 6: feelings = 'You hate each other'
            if z == 7: feelings = 'You are friends'
            if z == 8: feelings = 'No feelings either way, it is over'
            if z == 9: feelings = 'You like them, they hate you'
            if z == 10: feelings = 'They like you, you hate them'
            return 'Problem Lover: ' + affair + ' NOW ' + feelings
        if x > 7: return 'Fast Affairs and Hot Dates'

    def lifeEventsGenerator(self):
        self.lifeEvents = []
        self.age = d(2,6,16)
        yearsToRoll = self.age - 16
        for i in range(yearsToRoll):
            x = d(1,10,0)
            if x < 4:
                self.lifeEvents.append(self.bigProblemsBigWins())
            if x >= 4 and x < 7: self.lifeEvents.append(self.friendsAndEnemies())
            if x == 7 or x == 8:
                self.lifeEvents.append(self.romanticLife())
            if x > 8: self.lifeEvents.append('Nothing Happened')

    def info(self):
        print('Name: ' + self.name)
        print('Role: ' + self.role + ' | ' + self.occupation[0] + ' (' + str(self.occupation[1]) + ' Cr./mo.)')
        print(self.homeworld + ' | ' + self.languages[0])
        print(self.clothes + ' | ' + self.hairstyle + ' | ' + self.affectations)
        print(self.personality + ' | ' + self.disposition)
        print()
        print(self.score_sum[1] + ' (' + str(self.score_sum[0]) + ' points)')
        print('Int: ' + str(self.int) + ' | Ref: ' + str(self.ref[0]) + '/' + str(self.ref[1]) + ' | Tech: ' + str(
            self.tech))
        print('Cool: ' + str(self.cool) + ' | Attr: ' + str(self.attr) + ' | Luck: ' + str(self.luck))
        print('MA: ' + str(self.ma) + ' | Body: ' + str(self.body[0]) + ' (' + self.body[1] + ') | Emp: ' + str(
            self.emp[0]) + '/' + str(self.emp[1]))
        print('Run: ' + str(self.run) + 'm | Leap: ' + str(self.leap) + 'm | Lift: ' + str(self.lift) + 'kg')
        print('Save: ' + str(self.save) + ' | BTM: ' + str(self.btm))
        print()
        print('Skills:')
        self.skills.printSkills()
        print()
        print('Family / Childhood')
        print('Family Ranking:        ' + self.family_ranking)
        print('Parents:               ' + self.parents)
        if self.family_status == True: print('Tragedy:               ' + self.family_tragedy)
        print('Siblings:              ' + self.siblings[0])
        if len(self.siblings) > 1:
            for i in range(len(self.siblings) - 1):
                print('                    ' + str(i + 2) + '. ' + self.siblings[i + 1])
        print('Childhood Environment: ' + self.childhood_env)
        print()
        print('Life Events:')
        for i in range(len(self.lifeEvents)):
            if isinstance(self.lifeEvents[i], str): print(str(17 + i) + ' y/o: ' + self.lifeEvents[i])

    def cyberpunkCharacterGenerator(self):
        self.name = generateName()
        self.rollStats()
        self.scoreSumCalculator()
        self.originAndPersonalStyle(False, 'Random Origin')
        self.childhood()
        self.motivations()
        self.careerAptitudeTest()
        skillPackage = cyberpunkSkills()
        self.skills = skillPackage
        self.skills.rollClassSkills(self)
        self.skills.rollPickupSkills(self)
        self.occupationTable()
        self.lifeEventsGenerator()  # TODO Write Enemies Subsection

        # self.randomWeapon()
        self.info()
        print()


#   ________  _____    ____  ___   ______________________  _____
#  / ____/ / / /   |  / __ \/   | / ____/_  __/ ____/ __ \/ ___/
# / /   / /_/ / /| | / /_/ / /| |/ /     / / / __/ / /_/ /\__ \
# / /___/ __  / ___ |/ _, _/ ___ / /___  / / / /___/ _, _/___/ /
# \____/_/ /_/_/  |_/_/ |_/_/  |_\____/ /_/ /_____/_/ |_|/____/
# IT'S NOT JUST CHARACTERS, IT'S GODDAMN TRAVELLER SPACE RPG


# For skill overhaul when traveller npcs get made
class travellerSkills():
    def __init__():
        self.admin = -3
        self.advocate = -3
        self.animals = -3  #
        self.athletics = -3  #
        self.art = -3  #
        self.astrogation = -3
        self.battleDress = -3
        self.broker = -3
        self.carouse = -3
        self.comms = -3
        self.computers = -3
        self.deception = -3
        self.diplomat = -3
        self.drive = -3  #
        self.engineer = -3  #
        self.explosioves = -3
        self.flyer = -3
        self.gambler = -3
        self.gunner = -3  #
        self.heavyWeapons = -3  #
        self.investigate = -3
        self.jackOfAllTrades = -3
        self.language = -3  #
        self.leadership = -3
        self.lifeSciences = -3  #
        self.mechanic = -3
        self.medic = -3
        self.melee = -3  #
        self.navigation = -3
        self.persuade = -3
        self.pilot = -3  #
        self.physicalSciences = -3  #
        self.recon = -3
        self.remoteOperations = -3
        self.seafarer = -3  #
        self.sensors = -3
        self.socialSciences = -3  #
        self.spaceSciences = -3  #
        self.stealth = -3
        self.steward = -3
        self.streetwise = -3
        self.survival = -3
        self.tactics = -3  #
        self.trade = -3  #
        self.vaccSuit = -3
        self.zeroG = -3


def travellerCharacter():
    def __init__(self):
        self.name = 'TravellerNameErr'


# Returns a modifier based on a character's ability score
def characteristic_modifier(score):
    if score == 0: return -3
    if score == 1 or score == 2: return -2
    if score >= 3 and score <= 5: return -1
    if score >= 6 and score <= 8: return 0
    if score >= 9 and score <= 11: return 1
    if score >= 12 and score <= 14: return 2
    if score >= 15: return 3


class traveller_npc():
    def __init__(self):
        self.name = 'NameErr'
        self.str = 0
        self.dex = 0
        self.end = 0
        self.int = 0
        self.edu = 0
        self.soc = 0
        self.homeworld = 'HomeworldErr'
        self.skills = []
        self.career = 'CarErr'
        self.specialization = 'SpecErr'

    def generate_name(self):
        first_names = ['John', 'Steven', 'Mark', 'Caitlyn', 'Stella', 'Jessica', 'James', 'Robert', 'Michael', 'David',
                       'William', 'Richard', 'Joseph', 'Thomas', 'Christopher', 'Calvin', 'Mary', 'Patricia',
                       'Jennifer',
                       'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Sarah', 'Karen']
        middle_initial = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                          'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        last_names = ['Toast', 'Rock', 'Pan', 'Bell', 'Camp', 'Waterfall', 'Safe', 'Canteen', 'Wheel', 'Time', 'Year',
                      'Man', 'Thing', 'Woman', 'Child', 'State', 'Hand', 'Case', 'Program', 'Money']
        self.name = random.choice(first_names) + ' ' + random.choice(middle_initial) + '. ' + random.choice(last_names)

    def roll_scores(self):
        self.str = d(2,6,0)
        self.dex = d(2,6,0)
        self.end = d(2,6,0)
        self.int = d(2,6,0)
        self.edu = d(2,6,0)
        self.soc = d(2,6,0)

    # skills: untrained - (-3)
    # 0: Little Experience
    # 1: Trained Individual
    # 2-3: Skilled Professional
    # 4: Famous or High Renown

    def homeworld_skills(self):
        homeworlds = ['Ag', 'As', 'De', 'Fl', 'Ga', 'Ht', 'Hi', 'IC', 'In', 'Lt', 'Po', 'Ri', 'Wa', 'Va']
        if 'Ag' in self.homeworld or 'Ga' in self.homeworld or 'Po' in self.homeworld:
            a = ['Animals (any)', 0]
            self.skills.append(a)
        if 'As' in self.homeworld:
            a = ['Zero-G', 0]
            self.skills.append(a)
        if 'De' in self.homeworld or 'Lt' in self.homeworld:
            a = ['Survival', 0]
            self.skills.append(a)
        if 'Fl' in self.homeworld or 'Wa' in self.homeworld:
            a = ['Seafarer (any)', 0]
            self.skills.append(a)
        if 'Ht' in self.homeworld:
            a = ['Computers', 0]
            self.skills.append(a)
        if 'Hi' in self.homeworld:
            a = ['Streetwise', 0]
            self.skills.append(a)
        if 'IC' in self.homeworld or 'Va' in self.homeworld:
            a = ['Vacc Suit', 0]
            self.skills.append(a)
        if 'In' in self.homeworld:
            a = ['Trade (any)', 0]
            self.skills.append(a)
        if 'Ri' in self.homeworld:
            a = ['Carouse (any)', 0]
            self.skills.append(a)

    def education_skills(self):
        edu_skills_list = ['Admin', 'Advocate', 'Art (any)', 'Carouse (any)', 'Comms', 'Computer', 'Drive (any)',
                           'Engineer (any)', 'Language (any)', 'Medic', 'Physical Science (any)',
                           'Life Science (any)', 'Social Science (any)', 'Space Science (any)', 'Trade (any)']
        for i in range(len(self.skills)):
            if (self.skills[i - 1][0]) in edu_skills_list:
                edu_skills_list.remove(self.skills[i - 1][0])
        x = (3 - (len(self.skills))) + characteristic_modifier(self.edu)
        # technically the 'drive' was not 'any' in the text 8/27
        for i in range(x):
            a = [random.choice(edu_skills_list), 0]
            edu_skills_list.remove(a[0])
            self.skills.append(a)

    def draft(self):
        # draft_careers = ['Navy','Army','Marines','Merchant','Scout','Agent']
        draft_careers = ['Navy']  # Troubleshooting Navy Career
        self.career = random.choice(draft_careers)
        if self.career == 'Navy': self.navy_career('none', 0, True)
        if self.career == 'Army': self.army_career()
        if self.career == 'Marines': self.marines_career()
        if self.career == 'Merchant': self.merchants_career()
        if self.career == 'Scout': self.scouts_career()
        if self.career == 'Agent': self.agents_career()

    def navy_career(self, assignment, term, draft):
        assignments = ['Line/Crew', 'Engineering/Gunner', 'Flight']
        service_skills = ['Pilot (any)', 'Vacc Suit', 'Zero-G', 'Gunner (any)', 'Mechanic', 'Gun Combat (any)']
        enlistment = d(2,6,characteristic_modifier(self.int))
        if enlistment >= 6:
            if assignment == 'none': self.specialization = random.choice(assignments)
            if assignment == 'Line/Crew': self.specialization = assignment
            if assignment == 'Engineering/Gunner': self.specialization = assignment
            if assignment == 'Flight': self.specialization = assignment
            if term == 0:
                for i in range(len(service_skills)):
                    a = [service_skills[i - 1], 0]
                    self.skills.append(a)
        if enlistment < 6 and draft == True:
            self.career = 'Drifter'
            self.specialization = 'Drifter'

    def army_career(self):
        assignments = ['Support', 'Infantry', 'Cavalry']
        service_skills = ['Drive (any)', 'Athletics (any)', 'Gun Combat (any)', 'Recon', 'Melee (any)',
                          'Heavy Weapons (any)']
        enlistment = d(2,6,characteristic_modifier(self.end))
        if enlistment >= 5:
            self.specialization = random.choice(assignments)
            for i in range(len(service_skills)):
                a = [service_skills[i - 1], 0]
                self.skills.append(a)
        if enlistment < 5:
            self.career = 'Drifter'
            self.specialization = 'Drifter'

    def marines_career(self):
        assignments = ['Support', 'Star Marines', 'Ground Assault']
        service_skills = ['Athletics (any)', 'Battle Dress', 'Tactics (any)', 'Heavy Weapons (any)', 'Gun Combat (any)',
                          'Stealth']
        enlistment = d(2,6,characteristic_modifier(self.end))
        if enlistment >= 6:
            self.specialization = random.choice(assignments)
            for i in range(len(service_skills)):
                a = [service_skills[i - 1], 0]
                self.skills.append(a)
        if enlistment < 6:
            self.career = 'Drifter'
            self.specialization = 'Drifter'

    def merchants_career(self):
        # For the draft, only merchant marine has been added
        assignments = ['Merchant Marine']  # free trader, broker
        service_skills = ['Drive (any)', 'Vacc Suit', 'Broker', 'Steward', 'Comms', 'Persuade']
        enlistment = d(2,6,characteristic_modifier(self.int))
        if enlistment >= 4:
            self.specialization = random.choice(assignments)
            for i in range(len(service_skills)):
                a = [service_skills[i - 1], 0]
                self.skills.append(a)
        if enlistment < 4:
            self.career = 'Drifter'
            self.specialization = 'Drifter'

    def scouts_career(self):
        assignments = ['Courier', 'Survey', 'Exploration']
        pilot_options = ['Pilot (Spacecraft)', 'Pilot (Small Craft)']
        service_skills = [random.choice(pilot_options), 'Survival', 'Mechanic', 'Astrogation', 'Gun Combat (any)',
                          'Comms']
        enlistment = d(2,6,characteristic_modifier(self.int))
        if enlistment >= 5:
            self.specialization = random.choice(assignments)
            for i in range(len(service_skills)):
                a = [service_skills[i - 1], 0]
                self.skills.append(a)
        if enlistment < 5:
            self.career = 'Drifter'
            self.specialization = 'Drifter'

    def agents_career(self):
        # For the draft, only merchant marine has been added
        assignments = ['Law Enforcement']  # free trader, broker
        service_skills = ['Drive (any)', 'Streetwise', 'Investigate', 'Computers', 'Recon', 'Gun Combat (any)']
        enlistment = d(2,6,characteristic_modifier(self.int))
        if enlistment >= 6:
            self.specialization = random.choice(assignments)
            for i in range(len(service_skills)):
                a = [service_skills[i - 1], 0]
                self.skills.append(a)
        if enlistment < 6:
            self.career = 'Drifter'
            self.specialization = 'Drifter'

    def drifter_career_check(self):
        if self.career == 'Drifter':
            assignments = ['Barbarian', 'Wanderer', 'Scavenger']
            self.specialization = random.choice(assignments)
            if self.specialization == 'Barbarian':
                service_skills = ['Animals (any)', 'Carouse (any)', 'Melee (Blade)', 'Stealth', 'Seafarer (any)',
                                  'Survival']
                for i in range(len(service_skills)):
                    a = [service_skills[i - 1], 0]
                    self.skills.append(a)
            if self.specialization == 'Wanderer':
                service_skills = ['Athletics (any)', 'Deception', 'Recon', 'Stealth', 'Streetwise', 'Survival']
                for i in range(len(service_skills)):
                    a = [service_skills[i - 1], 0]
                    self.skills.append(a)
            if self.specialization == 'Scavenger':
                service_skills = ['Pilot (Small Craft)', 'Mechanic', 'Astrogation', 'Vacc Suit', 'Zero-G',
                                  'Gun Combat (any)']
                for i in range(len(service_skills)):
                    a = [service_skills[i - 1], 0]
                    self.skills.append(a)

    def any_skill_determinism(self):
        # makes the skills in the skill list marked as '(any)' into a specific skill
        for i in range(len(self.skills)):
            # Make a copy for manipulation
            x = self.skills[i - 1]
            # Replace '(any)' with a specific skill
            if x[0] == 'Art (any)':
                specs = ['Acting', 'Dance', 'Holography', 'Instrument', 'Sculpting', 'Writing']
                specialty = 'Art (' + random.choice(specs) + ')'
                x[0] = specialty
                self.skills[i - 1] = x
            if x[0] == 'Animals (any)':
                specs = ['Riding', 'Veterinary', 'Training', 'Farming']
                specialty = 'Animals (' + random.choice(specs) + ')'
                x[0] = specialty
                self.skills[i - 1] = x
            if x[0] == 'Athletics (any)':
                specs = ['Co-ordination', 'Endurance', 'Strength', 'Flying']
                specialty = 'Athletics (' + random.choice(specs) + ')'
                x[0] = specialty
                self.skills[i - 1] = x
            if x[0] == 'Carouse (any)':
                specs = ['Liquor', 'Chance Gambling', 'Narcotics', 'Skill Gambling']
                specialty = 'Carouse (' + random.choice(specs) + ')'
                x[0] = specialty
                self.skills[i - 1] = x
            if x[0] == 'Drive (any)':
                specs = ['Mole', 'Tracked', 'Wheeled']
                specialty = 'Drive (' + random.choice(specs) + ')'
                x[0] = specialty
                self.skills[i - 1] = x
            if x[0] == 'Engineer (any)':
                specs = ['M-Drive', 'J-Drive', 'Life Support', 'Power']
                specialty = 'Engineer (' + random.choice(specs) + ')'
                x[0] = specialty
                self.skills[i - 1] = x
            if x[0] == 'Flyer (any)':
                specs = ['Grav', 'Rotor', 'Wing']
                specialty = 'Engineer (' + random.choice(specs) + ')'
                x[0] = specialty
                self.skills[i - 1] = x
            if x[0] == 'Gunner (any)':
                specs = ['Turrets', 'Ortillery', 'Screens', 'Capital Weapons']
                specialty = 'Gunner (' + random.choice(specs) + ')'
                x[0] = specialty
                self.skills[i - 1] = x
            if x[0] == 'Gun Combat (any)':
                specs = ['Slug Rifle', 'Slug Pistol', 'Shotgun', 'Energy Rifle', 'Energy Pistol']
                specialty = 'Gun Combat (' + random.choice(specs) + ')'
                x[0] = specialty
                self.skills[i - 1] = x
            if x[0] == 'Heavy Weapons (any)':
                specs = ['Launchers', 'Man Portable Artillery', 'Field Artillery']
                specialty = 'Heavy Weapons (' + random.choice(specs) + ')'
                x[0] = specialty
                self.skills[i - 1] = x
            if x[0] == 'Language (any)':
                specs = ['Anglo-American', 'African', 'Japanese/Korean', 'Central European/Soviet', 'Pacific Islander',
                         'Chinese/Southeast Asian', 'Urban Streetfolk', 'Hispanic American', 'Central/South American',
                         'European']
                specialty = 'Language (' + random.choice(specs) + ')'
                x[0] = specialty
                self.skills[i - 1] = x
            if x[0] == 'Melee (any)':
                specs = ['Unarmed Combat', 'Blade', 'Bludgeon', 'Natural Weapons']
                specialty = 'Melee (' + random.choice(specs) + ')'
                x[0] = specialty
            if x[0] == 'Pilot (any)':
                specs = ['Small Craft', 'Spacecraft', 'Capital Ships']
                specialty = 'Pilot (' + random.choice(specs) + ')'
                x[0] = specialty
                self.skills[i - 1] = x
            if x[0] == 'Physical Science (any)':
                specs = ['Physics', 'Chemistry', 'Electronics']
                specialty = 'Physical Science (' + random.choice(specs) + ')'
                x[0] = specialty
                self.skills[i - 1] = x
            if x[0] == 'Life Science (any)':
                specs = ['Biology', 'Cybernetics', 'Genetics', 'Mutational Psionicology']
                specialty = 'Life Science (' + random.choice(specs) + ')'
                x[0] = specialty
                self.skills[i - 1] = x
            if x[0] == 'Social Science (any)':
                specs = ['Archeology', 'Economics', 'History', 'Linguistics', 'Philosophy', 'Psychology',
                         'Sophontology']
                specialty = 'Social Science (' + random.choice(specs) + ')'
                x[0] = specialty
                self.skills[i - 1] = x
            if x[0] == 'Space Science (any)':
                specs = ['Planetology', 'Robotics', 'Xenology']
                specialty = 'Space Science (' + random.choice(specs) + ')'
                x[0] = specialty
                self.skills[i - 1] = x
            if x[0] == 'Seafarer (any)':
                specs = ['Sail', 'Submarine', 'Ocean Ships', 'Motorboats']
                specialty = 'Seafarer (' + random.choice(specs) + ')'
                x[0] = specialty
                self.skills[i - 1] = x
            if x[0] == 'Tactics (any)':
                specs = ['Military', 'Naval']
                specialty = 'Tactics (' + random.choice(specs) + ')'
                x[0] = specialty
                self.skills[i - 1] = x
            if x[0] == 'Trade (any)':
                specs = ['Biologicals', 'Civil Engineering', 'Space Construction', 'Hydroponics', 'Polymers']
                specialty = 'Trade (' + random.choice(specs) + ')'
                x[0] = specialty
                self.skills[i - 1] = x

    def skill_compiler(self):
        skill_blueprint = self.skills
        faux_list = []
        removal_list = []
        for i in range(len(self.skills)):
            if self.skills[i][0] in faux_list: removal_list.append(i)
            faux_list.append(self.skills[i][0])
        if removal_list != []:
            for n in range(len(removal_list)):
                print('skill ex check: ' + skill_blueprint[n][0])
                skill_ex = skill_blueprint[removal_list[n]][0]  # LIST OUT OF RANGE ERR COUNT: 26
                skill_ex_val = skill_blueprint[removal_list[n]][1]
                for x in range(len(self.skills)):
                    if self.skills[x][0] == skill_ex:
                        if skill_ex_val == 0: self.skills[x][1] += 1
                        if skill_ex_val >= 1: self.skills[x][1] += skill_ex_val
                del self.skills[removal_list[n]]

    def title_printer(self):
        if self.soc == 11: print('Title: Knight')
        if self.soc == 12: print('Title: Baron')
        if self.soc == 13: print('Title: Marquis')
        if self.soc == 14: print('Title: Count')
        if self.soc == 15: print('Title: Duke')

    def print(self):
        self.title_printer()
        print(self.name)
        print(self.career + ' Career (' + self.specialization + ')')
        print('Str: ' + str(self.str) + ' (' + str(characteristic_modifier(self.str)) + ')')
        print('Dex: ' + str(self.dex) + ' (' + str(characteristic_modifier(self.dex)) + ')')
        print('End: ' + str(self.end) + ' (' + str(characteristic_modifier(self.end)) + ')')
        print('Int: ' + str(self.int) + ' (' + str(characteristic_modifier(self.int)) + ')')
        print('Edu: ' + str(self.edu) + ' (' + str(characteristic_modifier(self.edu)) + ')')
        print('Soc: ' + str(self.soc) + ' (' + str(characteristic_modifier(self.soc)) + ')')
        for i in range(len(self.skills)):
            x = self.skills[i]
            print(x)

    def generate(self, homeworld):
        self.generate_name()
        self.roll_scores()
        self.homeworld = homeworld.codes
        self.homeworld_skills()
        self.education_skills()
        self.draft()
        self.drifter_career_check()
        self.any_skill_determinism()
        self.skill_compiler()
        self.print()
        print()


#    __    ____________________  ___  ________  __
#   / /   /  _/ ____/ ____/ __ \/   |/_  __/ / / /
#  / /    / // /_  / __/ / /_/ / /| | / / / /_/ /
# / /____/ // __/ / /___/ ____/ ___ |/ / / __  /
# /_____/___/_/   /_____/_/   /_/  |_/_/ /_/ /_/
# LIFEPATH AND CHARACTER BACKSTORY GENERATOR (TRAVELLER)

class navy_career():
    def __init__(self):
        enlistment = 6
        nco_ranks = [[0, 'Crewman', 'none'], [1, 'Able Spacehand', 'Mechanic 1'],
                     [2, 'Petty Officer, 3rd Class', 'Vacc Suit 1'],
                     [3, 'Petty Officer, 2nd Class', 'none'], [4, 'Petty Officer, 1st Class', '+1 End'],
                     [5, 'Chief Petty Officer', 'none'],
                     [6, 'Master Chief', 'none']]
        # officer_ranks = [[0,'none','none'],[1,'Ensign','Melee (Blade) 1'][2,'Sublieutenant','Leadership 1'],[3,'Lieutenant','none'],
        # [4,'Commander','Tactics (Naval) 1'],[5,'Captain','Social Standing 10 or +1'],[6,'Admiral','Social Standing 12 or +1']]
        self.rank = 0
        self.commission = False
        self.ejected = False
        self.term_descriptions = []

    def gain_skill(self, npc):
        personal_development_skills = ['+1 Str', '+1 Dex', '+1 End', '+1 Int', '+1 Edu', '+1 Soc']
        service_skills = ['Pilot (any)', 'Vacc Suit', 'Zero-G', 'Gunner (any)', 'Mechanic', 'Gun Combat (any)']
        adv_edu_min = 8
        adv_edu_skills = ['Remote Operations', 'Astrogation', 'Engineer (any)', 'Computers', 'Navigation', 'Admin']
        officer_skills = ['Leadership', 'Tactics (Naval)', 'Pilot (any)', 'Melee (Blade)', 'Admin',
                          'Tactics (Naval)']  # Commission Only!
        crew_skills = ['Comms', 'Mechanic', 'Gun Combat (any)', 'Sensors', 'Melee (any)', 'Vacc Suit']
        eng_gun_skills = ['Engineer (any)', 'Mechanic', 'Sensors', 'Engineer (any)', 'Gunner (any)', 'Computer']
        flight_skills = ['Pilot (any)', 'Flyer (any)', 'Gunner (any)', 'Pilot (Small Craft)', 'Astrogation', 'Zero-G']
        skill_tables = [personal_development_skills, service_skills]
        commission_roll = d(2,6,characteristic_modifier(npc.soc))
        if commission_roll >= 8:
            self.commission = True
            skill_tables.append(officer_skills)
        if npc.edu >= 8: skill_tables.append(adv_edu_skills)
        if npc.specialization == 'Line/Crew': skill_tables.append(crew_skills)
        if npc.specialization == 'Engineering/Gunner': skill_tables.append(eng_gun_skills)
        if npc.specialization == 'Flight': skill_tables.append(flight_skills)
        skill = random.choice(random.choice(skill_tables))
        print('Term Skill: ' + skill)

    def mishap(self):
        mishap = random.randint(1, 6)
        if mishap == 1:
            return ('Severely injured in action.')
            print(self.injury_table(2))
        if mishap == 2:
            scores = ['Str', 'Dex', 'End']
            score = random.choice(scores)
            return (
                    'Placed in cryogenics and revived improperly. ' + score + ' -1 due to muscle waste.')  # NOT KICKED OUT OF NAVY ERR COUNT 1
        if mishap == 3:
            assignments = ['Crew', 'Engineering', 'Flight']
            skill = 'err'
            assignment = random.choice(assignments)
            if assignment == 'Crew': skills = ['Sensors', 'Gunner (any)']
            if assignment == 'Engineering': skills = ['Mechanic', 'Vacc Suit']
            if assignment == 'Flight': skills = ['Pilot (Small or Spacecraft)', 'Tactics (Naval)']
            roll = d(2,6,0)
            if roll >= 8: return ('During a Battle: Honourable Discharge; keep benefits roll')
            if roll <= 7: return (
                'During a battle: Your ship suffers severe damage and you are blamed for the disaster.')
        if mishap == 4: return ('mishap 4 needed')
        if mishap == 5: return ('You have a quarrel. Gain enemy.')
        if mishap == 6: return self.injury_table(0)

    def events(self):
        # events are rolled on 2d6 however
        event = d(2,6,0)
        if event == 2:
            event_desc = 'Disaster! Roll on mishap table, but do not leave the navy.'
            print(self.mishap())
        if event == 3:
            event_desc = 'Join gambling circle on board.'
            skills = ['Gambler 1', 'Deception 1']
            skill = random.choice(skills)
            print('Skill: ' + skill)
            x = 0
            if skill == 'Gambler 1': x = 1
            gambler_check = d(2,6,x)
            if gambler_check >= 8: print('You won! Gain a benefit.')
            if gambler_check <= 7: print('You lost. Lose a benefit.')
        if event == 4:
            event_desc = 'You are given a special assignment or duty on board a ship.'
            print('Gain +1 dm to any one benefit roll')
        if event == 5:
            event_desc = 'You are given advanced training in a specialist field.'
            edu_check = d(2,6,0)
            if edu_check >= 8: print('Gain one level in any skill you already have.')
            if edu_check <= 7: print('You did not pass the education check.')
        if event == 6:
            event_desc = 'Your vessel participates in a military engagement.'
            skills = ['Engineering (any) 1', 'Gunnery (any) 1', 'Pilot (any) 1']
            print('Skill: ' + random.choice(skills))
        if event == 7: event_desc = 'life event. roll on life events table page 34'
        if event == 8:
            event_desc = 'Your vessel participates in a diplomatic mission.'
            benefits = ['Recon 1', 'Diplomacy 1', 'Steward 1', 'Contact']
            gain = random.choice(benefits)
            if gain == 'Contact': print('You gain a contact.')
            if gain != 'Contact': print('Skill: ' + gain)
        if event == 9:
            crimes = ['mutiny', 'sabotage', 'smuggling', 'comspiracy']
            crime = random.choice(crimes)
            print('Gain Enemy. +2 DM Advancement Roll')
            event_desc = 'You foil an attempted ' + crime + ' on board.'
        if event == 10:
            x = random.randint(1, 2)
            if x == 1:
                print('Gain extra benefit roll.')
                event_desc = 'You take an opportunity to abuse your position for profit.'
            if x == 2:
                print('+2 Advancement Roll')
                event_desc = 'You deny an opportunity to abuse position for profit.'
        if event == 11:
            bonus = ['Skill: Tactics (Naval) 1', '+4 Advancement Roll']
            event_desc = 'You commanding officer takes an interest in your career.'
        if event == 12:
            bonuses = ['Gain a promotion', 'Gain a commission']
            bonus = random.choice(bonuses)
            print(bonus)
            event_desc = 'You display heroism in battle, saving the whole ship.'
        return event_desc

    # Life Events Table

    def injury_table(self, x):
        if x == 0:
            x = random.randint(1, 6)
        if x == 1:
            ability_loss = ['Str', 'Dex', 'End']
            ability_lost = random.choice(ability_loss)
            loss_amount = random.randint(1, 6)
            y = random.randint(1, 3)
            if y == 1:
                if ability_lost == 'Str': return 'Nearly Killed. (Str -' + str(loss_amount) + ' Dex -2 End -2)'
                if ability_lost == 'Dex': return 'Nearly Killed. (Str -2 Dex -' + str(loss_amount) + ' End -2)'
                if ability_lost == 'End': return 'Nearly Killed. (Str -' + str(loss_amount) + ' Dex -2 End -2)'
            if y == 2:
                if ability_lost == 'Str': return 'Nearly Killed. (Str -' + str(loss_amount) + ' Dex -4)'
                if ability_lost == 'End': return 'Nearly Killed. (Str -' + str(loss_amount) + ' Dex -4)'
                if ability_lost == 'Dex': return 'Nearly Killed. (Str -4 Dex -' + str(loss_amount) + ')'
            if y == 3:
                if ability_lost == 'Str': return 'Nearly Killed. (Str -' + str(loss_amount) + ' End -4)'
                if ability_lost == 'Dex': return 'Nearly Killed. (Dex -' + str(loss_amount) + ' End -4)'
                if ability_lost == 'End': return 'Nearly Killed. (Str -' + str(loss_amount) + ' End -4)'
        if x == 2:
            ability_loss = ['Str', 'Dex', 'End']
            ability_lost = random.choice(ability_loss)
            return 'Severely Injured (' + ability_lost + ' -' + str(random.randint(1, 6)) + ')'
        if x == 3:
            ability_loss = ['Str', 'Dex']
            ability_lost = random.choice(ability_loss)
            if ability_lost == 'Dex': part_lost = ['Missing eye (Dex -2)', 'Missing Arm (Dex -2)']
            if ability_lost == 'Str': part_lost = ['Missing Leg (Str -2)', 'Missing Arm (Str -2)']
            injury = random.choice(part_lost)
            return injury
        if x == 4:
            ability_loss = ['Str', 'Dex', 'End']
            ability_lost = random.choice(ability_loss)
            return 'Scarred (' + ability_lost + ' -2)'
        if x == 5:
            ability_loss = ['Str', 'Dex', 'End']
            ability_lost = random.choice(ability_loss)
            return 'Injured (' + ability_lost + ' -2)'
        if x == 6: return 'Lightly Injured: No permanent effect'


#    ____  ___  __________  ____  _   _______
#   / __ \/   |/_  __/ __ \/ __ \/ | / / ___/
#  / /_/ / /| | / / / /_/ / / / /  |/ /\__ \
# / ____/ ___ |/ / / _, _/ /_/ / /|  /___/ /
# /_/   /_/  |_/_/ /_/ |_|\____/_/ |_//____/
# MISSION PATRONS AND MISSION STATEMENTS

class patron():
    def __init__(self):
        self.name = 'patronNameErr'
        self.type = 'patronTypeErr'
        self.occupation = 'patronOccupationErr'
        self.mission = 'missionErr'
        self.missionTarget = 'missionTargetErr'
        self.opposition = 'missionOppositionErr'

    def randomOccupation(self):
        patronTypes = ['Criminal', 'Local Leader', 'High Society',
                       'Commercial', 'Spacer', 'Unusual']
        self.type = random.choice(patronTypes)
        if self.type == 'Criminal': self.occupation = random.choice([
            'Assassin', 'Smuggler', 'Terrorist', 'Embezzler',
            'Thief', 'Revolutionary'])
        if self.type == 'Local Leader': self.occupation = random.choice([
            'Clerk', 'Administrator', 'Mayor', 'Minor Noble', 'Physician', 'Tribal Leader'])
        if self.type == 'High Society': self.occupation = random.choice([
            'Diplomat', 'Courier', 'Spy', 'Ambassador', 'Noble', 'Police Officer'])
        if self.type == 'Commercial': self.occupation = random.choice([
            'Merchant', 'Free Trader', 'Broker', 'Corporate Executive', 'Corporate Agent', 'Financier'])
        if self.type == 'Spacer': self.occupation = random.choice([
            'Belter', 'Researcher', 'Naval Officer', 'Pilot', 'Starport Administrator', 'Scout'])
        if self.type == 'Unusual': self.occupation = random.choice([
            'Alien', 'Playboy', 'Stowaway', 'Family Relative',
            'Agent of a Foreign Power', 'Imperial Agent'])

    def randomMission(self):
        missions = ['Assassinate a target', 'Frame a target', 'Destroy a target',
                    'Steal from a target', 'Aid in a burglary', 'Stop a burglary',
                    'Retrieve data or an object from a secure facility', 'Discredit a target',
                    'Find a lost cargo', 'Find a lost person', 'Deceive a target',
                    'Sabotage a target', 'Transport goods', 'Transport a person',
                    'Transport data', 'Transport goods secretly',
                    'Transport goods quickly', 'Transport dangerous goods',
                    'Investigate a crime', 'Investigate a theft', 'Investigate a murder',
                    'Investigate a mystery', 'Investigate a target', 'Investigate an event',
                    'Join an expidition', 'Survey a planet', 'Explore a new system',
                    'Explore a ruin', 'Salvage a ship', 'Capture a creature',
                    'Hijack a ship', 'Entertain a noble', 'Protect a target',
                    'Save a target', 'Aid a target', "It's a trap by the patron"]
        self.mission = random.choice(missions)

    def randomMissionTarget(self):
        targetTypes = ['Trade Goods', 'Objects', 'Places', 'NPCs',
                       'Organizations', 'Vessels']
        typeChosen = random.choice(targetTypes)
        if typeChosen == 'Trade Goods': self.missionTarget = random.choice([
            'Common Trade Goods', 'Random Trade Goods', 'Illegal Trade Goods'])
        if typeChosen == 'Objects': self.missionTarget = random.choice([
            'Computer Data', 'Alien Artifact', 'Personal Effects', 'Work of Art',
            'Historical Artifact', 'Weapon'])
        if typeChosen == 'Places': self.missionTarget = random.choice([
            'Starport', 'Asteroid Base', 'City', 'Research Station',
            'Bar or Nightclub', 'Medical Facility'])
        if typeChosen == 'NPCs':
            self.missionTarget = random.choice(['Random Patron', 'Random Opposition'])
            placeHolder = patron()
            placeHolder.randomOccupation()
            placeHolder.randomOpposition()
            placeHolder.name = generateName()
            if self.missionTarget == 'Random Patron':
                self.missionTarget = placeHolder.name + ', ' + placeHolder.occupation
            if self.missionTarget == 'Random Opposition':
                self.missionTarget = placeHolder.opposition
        if typeChosen == 'Organizations':
            self.missionTarget = random.choice(['Local Government', 'Planetary Government',
                                                'Corporation', 'Imperial Intelligence',
                                                'Criminal Syndicate', 'Criminal Gang'])
        if typeChosen == 'Vessels':
            self.missionTarget = random.choice(['Free Trader', 'Yacht', 'Cargo Hauler',
                                                'Police Cutter', 'Space Station', 'Warship'])

    def randomOpposition(self):
        oppositions = ['Low Tech', 'Average Tech', 'High Tech', 'Environmental',
                       'Technology', 'Social']
        typeChosen = random.choice(oppositions)
        if typeChosen == 'Low Tech': self.opposition = random.choice([
            'Animals', 'Large Animals', 'Bandits & Thieves', 'Fearful Peasants', 'Local Lord'])
        if typeChosen == 'Average Tech': self.opposition = random.choice([
            'Crminals (Thugs/Corsairs]', 'Criminals (Thieves/Sabateurs)', 'Police (Ordinary Security)',
            'Police (Inspectors/Detectives', 'Corporate Agents', 'Corporate Legal'])
        if typeChosen == 'High Tech': self.opposition = random.choice([
            'Starport Security', 'Imperial Marines', 'Interstellar Corporation', 'Alien Private Citizen or Corporation',
            'Alien Government', 'Space Travellers/Rival Ship'])
        if typeChosen == 'Environmental': self.opposition = random.choice([
            'Target in Deep Space', 'Target in Orbit', 'Hostile Weather', 'Dangerous Organisms/Radiation',
            'Target in Dangerous Region', 'Target in Restricted Area'])
        if typeChosen == 'Technology': self.opposition = random.choice([
            'Target under Elec. Observation', 'Hostile Guard Robots/Ships', 'Biometric Identification Needed',
            'Mechanical Failure/Computer Hacking', 'Characters under Surveillance', 'Out of fuel/ammunition'])
        if typeChosen == 'Social': self.opposition = random.choice([
            'Police Investigation', 'Legal Barriers', 'Nobility', 'Government Officials',
            'Target Protected by Third Party', 'Hostages'])

    def info(self):
        print(self.name + ', ' + self.occupation + '.')
        print(self.mission + ' | ' + self.missionTarget)
        print('Opposition: ' + self.opposition)


lydia = patron()
lydia.name = generateName()
lydia.randomOccupation()
lydia.randomMission()
lydia.randomMissionTarget()
lydia.randomOpposition()
lydia.info()
print()


#  __________  ____  __  ______  __    ___________ __  ______  ____  ___________   ________
# /_  __/ __ \/ __ \/ / / / __ )/ /   / ____/ ___// / / / __ \/ __ \/_  __/  _/ | / / ____/
#  / / / /_/ / / / / / / / __  / /   / __/  \__ \/ /_/ / / / / / / / / /  / //  |/ / / __
# / / / _, _/ /_/ / /_/ / /_/ / /___/ /___ ___/ / __  / /_/ / /_/ / / / _/ // /|  / /_/ /
# /_/ /_/ |_|\____/\____/_____/_____/_____//____/_/ /_/\____/\____/ /_/ /___/_/ |_/\____/
# FUNCTIONS WITH THE INTENT TO FIGURE OUT WHAT THE HELL IS GOING ON

def tl_printer(planet):
    if planet.uwp[7] <= 3: print('Primitive Tech')
    if planet.uwp[7] >= 4 and planet.uwp[7] <= 6: print('Industrial Tech')
    if planet.uwp[7] >= 7 and planet.uwp[7] <= 9: print('Pre-Stellar Tech')
    if planet.uwp[7] >= 10 and planet.uwp[7] <= 11: print('Early Stellar Tech')
    if planet.uwp[7] >= 12 and planet.uwp[7] <= 14: print('Average Stellar Tech')
    if planet.uwp[7] >= 15: print('High Stellar Tech')
    if planet.uwp[7] == 0: print('No Tech')
    if planet.uwp[7] == 1: print('Bronze/Iron Age')
    if planet.uwp[7] == 2: print('Renaissance')
    if planet.uwp[7] == 3:
        print('Steam Power, 19th Century')
        print('Antique Pistol/Rifle')
    if planet.uwp[7] == 4:
        print('Industrial Revolution, 19th/20th Century')
        print('Shotgun')
    if planet.uwp[7] == 5:
        print('Electrification, mid-20th Century')
        print('Revolver, Rifle')
    if planet.uwp[7] == 6:
        print('Fission Power / Dawn of Space Age')
        print('Autopistol, Autorifle')
    if planet.uwp[7] == 7:
        print('Satellites / Computers')
        print('Assault Rifle')
    if planet.uwp[7] == 8:
        print('Reach Other Worlds')
        print('Snub / Body Pistol, Stunner I')
    if planet.uwp[7] == 9:
        print('Gravity Manipulation / Colonies')
        print('Accelerator Rifle, Laser Pistol / Carbine / Rifle I')
    if planet.uwp[7] == 10:
        print('Jump Drive')
        print('Advanced Combat Rifle, Stunner II')
    if planet.uwp[7] == 11:
        print('AI / Jump-2')
        print('Laser Pistol /Carbine / Rifle II')
    if planet.uwp[7] == 12:
        print('Weather Control / Plasma Weaponry / J-3')
        print('Gauss Rifle, Stunner III')
    if planet.uwp[7] == 13:
        print('Battle Dress / Human Cloning / J-4')
        print('Gauss Pistol')
    if planet.uwp[7] == 14: print('Fusion Weaponry / J-5')
    if planet.uwp[7] == 15: print('Black Globe Generators / J-6')
    if planet.uwp[7] == 16: print('Plasma Rifle')


def generate_traveller_npc(jean_luc, hallowsbelt, noble):
    if noble == True:
        while jean_luc.soc < 11: jean_luc.roll_scores()
    if noble == False: jean_luc.roll_scores()
    jean_luc.homeworld = hallowsbelt.codes
    jean_luc.homeworld_skills()
    jean_luc.education_skills()
    jean_luc.draft()
    jean_luc.drifter_career_check()
    jean_luc.any_skill_determinism()
    jean_luc.skill_compiler()
    jean_luc.print()
    print()


def navy_progression(nick_carl, naval):
    term_desc = 'TermDescErr'
    print(nick_carl.specialization)
    naval.gain_skill(nick_carl)
    if nick_carl.specialization == 'Line/Crew':
        survival_roll = d(2,6,characteristic_modifier(nick_carl.int))
        advancement_roll = d(2,6,characteristic_modifier(nick_carl.edu))
        print(survival_roll, advancement_roll)
        if survival_roll >= 5:
            term_desc = naval.events()
            if advancement_roll >= 7: print('Advanced!')
        if survival_roll < 5:
            term_desc = naval.mishap()
            naval.ejected = True
        print(term_desc)
    if nick_carl.specialization == 'Engineering/Gunner':  # NOT KICKED OUT ERR COUNT 1
        survival_roll = d(2,6,characteristic_modifier(nick_carl.int))  # ERR COUNT 1
        advancement_roll = d(2,6,characteristic_modifier(nick_carl.edu))
        print(survival_roll, advancement_roll)
        if survival_roll >= 6:
            term_desc = naval.events()
            if advancement_roll >= 6: print('Advanced!')
        if survival_roll < 6:
            term_desc = naval.mishap()
            naval.ejected = True
        print(term_desc)
    if nick_carl.specialization == 'Flight':
        survival_roll = d(2,6,characteristic_modifier(nick_carl.dex))
        advancement_roll = d(2,6,characteristic_modifier(nick_carl.edu))
        print(survival_roll, advancement_roll)
        if survival_roll >= 7:
            term_desc = naval.events()
            if advancement_roll >= 5: print('Advanced!')
        if survival_roll < 7:
            term_desc = naval.mishap()
            naval.ejected = True
        print(term_desc)
        if naval.ejected == True: print('You have been ejected from the Navy.')


#    __  ______    _____   __   __    ____  ____  ____
#   /  |/  /   |  /  _/ | / /  / /   / __ \/ __ \/ __ \
#  / /|_/ / /| |  / //  |/ /  / /   / / / / / / / /_/ /
# / /  / / ___ |_/ // /|  /  / /___/ /_/ / /_/ / ____/
# /_/  /_/_/  |_/___/_/ |_/  /_____/\____/\____/_/
# THIS IS WHERE THE MAGIC HAPPENS, BABE!

galaxy = defaultGalaxy()
menuChoice = 0
terminalRunning = True
print('Starboard, Renegade! by Calvin L.')
print('Build 2024.01.26')
print()
print('Welcome to the terminal.')
while terminalRunning == True:

    # Placeholder Terminal Locations
    if menuChoice == -2:
        print('Vessel Terminal')
        print()
        print('<<< Returning to Terminal ')
        menuChoice = 0

    if menuChoice == -3:
        print('Character Terminal')
        print()
        print('<<< Returning to Terminal ')
        menuChoice = 0

    if menuChoice == -4:
        print('Equiment Terminal')
        print()
        print('<<< Returning to Terminal ')
        menuChoice = 0

    # 0.0 Main Terminal
    if menuChoice == 0:
        print('Please enter one of the following integers: ')
        print('1. Galaxy Terminal')
        print('2. Vessel Terminal')
        print('3. Character Terminal (B)')
        print('4. Equipment Terminal (X)')
        print('99. Exit Program')
        menuChoice = int(input('>>: '))

    # 1 Galaxy Terminal
    if menuChoice == 1:
        galaxyTerminal = 0
        while galaxyTerminal < 7:

            # 1.0 Galaxy Terminal Main Menu
            if galaxyTerminal == 0:
                print('Galaxy Terminal')
                print('1. Print Current Galaxy')
                print('2. Generate New Galaxy')
                print('3. Construct Planet')
                print('4. Print Planet Details')
                print('5. Edit Planet Details')
                print('6. Generate New Freight')
                print('99. Back to Terminal.')
                galaxyTerminal = int(input('>>>: '))

            # 1.1 Print Current Galaxy
            if galaxyTerminal == 1:
                print()
                print('---> CURRENT GALAXY <---')
                for i in range(len(galaxy)):
                    print(
                        galaxy[i].return_tagline() + '| ' + galaxy[i].government + ' | ' + galaxy[i].culture + ' | ' +
                        galaxy[i].climate[2] + ' | Factions: ' + str(len(galaxy[i].factions)))
                print('<<< Returning to Terminal')
                print()
                galaxyTerminal = 0

            # 1.2 Generate New Galaxy
            if galaxyTerminal == 2:
                print()
                print('Rows and columns multiply for the total possible hexes.')
                print('Each hex has a 50% chance of containing a planet.')
                rows = int(input('How many rows of hexes? '))
                columns = int(input('How many columns? '))
                galaxy = generateGalaxy(rows, columns)
                generateFreight(galaxy)
                print('New Galaxy Successfully Generated')
                print()
                print('<<< Returning to Terminal ')
                galaxyTerminal = 0

            # 1.3 Create Planet
            if galaxyTerminal == 3:
                print()
                print('Welcome to the Planet Construction Interface (PCI).')
                print('Here, you will input data to create a planet.')
                hallowsbelt = planet()
                hallowsbelt.hex = input('What hex is your planet located in? >>: ')
                hallowsbelt.name = input("What is your planet's name? >>: ")

                # Starport
                print('What is the Quality of the Starport?')
                print('A = Excellent, B = Good, C = Routine, D = Poor, E = Frontier, X = None')
                starport_choice = input('>>: ')
                if starport_choice == 'A': hallowsbelt.generate_starport(10)
                if starport_choice == 'B': hallowsbelt.generate_starport(8)
                if starport_choice == 'C': hallowsbelt.generate_starport(6)
                if starport_choice == 'D': hallowsbelt.generate_starport(4)
                if starport_choice == 'E': hallowsbelt.generate_starport(2)
                if starport_choice == 'X': hallowsbelt.generate_starport(0)

                # Size
                print('Enter diameter of planet in kilometers.')
                size_choice = int(input('>>: '))
                size_choice = size_choice // 1600
                hallowsbelt.generate_size(int(size_choice))

                # Atmosphere
                print("What is the planet's atmosphere?")
                print('0 = None, 1 = Trace, 2 = Very Thin,')
                print('3 = Very Thin + Tainted, 4 = Thin, 5 = Thin + Tainted,')
                print('6 = Standard, 7 = Standard + Tainted, 8 = Dense,')
                print('9 = Dense + Tainted, 10 = Exotic, 11 = Corrosive,')
                print('12 = Insidious, 13 = Dense + High, 14 = Thin + Low,')
                print('15 = Unusual.')
                hallowsbelt.generate_atmosphere(int(input('>>: ')))

                # Climate
                print("What is the planet's climate?")
                print('1 = Frozen, 2 = Cold, 3 = Temperate, 4 = Hot, 5 = Roasting')
                climate = int(input('>>: '))
                if climate == 1: hallowsbelt.climate = [-100, -51, 'Frozen']
                if climate == 2: hallowsbelt.climate = [-51, 0, 'Cold']
                if climate == 3: hallowsbelt.climate = [0, 30, 'Temperate']
                if climate == 4: hallowsbelt.climate = [31, 80, 'Hot']
                if climate == 5: hallowsbelt.climate = [81, 100, 'Roasting']

                # Print & Exit
                hallowsbelt.print()
                print()
                print('<<< Returning to Terminal ')
                galaxyTerminal = 0

            # 1.4 Print Planet Details & Freight
            if galaxyTerminal == 4:
                print()
                planetFound = False
                print('Will print out details and freight.')
                planetFocus = input('Enter planet hex: ')
                for i in range(len(galaxy)):
                    if galaxy[i].hex == planetFocus:
                        galaxy[i].print()
                        for x in range(len(galaxy[i].goods)):
                            galaxy[i].goods[x].info()
                        print()
                        planetFound = True
                if planetFound == False:
                    print()
                    print('Planet not found.')
                    print()
                print('<<< Returning to Terminal ')
                galaxyTerminal = 0

            # 1.5 Edit Planet Details
            if galaxyTerminal == 5:
                print()
                print('FEATURE NOT YET AVAILABLE')
                print()
                print('<<< Returning to Terminal ')
                galaxyTerminal = 0

            # 1.6 Generate New Freight
            if galaxyTerminal == 6:
                print()
                generateFreight(galaxy)
                print('New Galaxy Freight Successfully Generated')
                print()
                print('<<< Returning to Terminal ')
                galaxyTerminal = 0

        # Galaxy Terminal Return to Main Terminal
        print()
        print('<<< Returning to Terminal ')
        menuChoice = 0

    # 2. Vessel Terminal
    if menuChoice == 2:
        vesselTerminal = 0
        while vesselTerminal < 3:

            # 2.0 Main Vessel Terminal
            if vesselTerminal == 0:
                print()
                print('Vessel Terminal')
                print('1. Generate Random Vessel')
                print('2. Design Vessel')
                vesselTerminal = int(input('>>>: '))

            # 2.1 Generate Random Vessel
            if vesselTerminal == 1:
                print()
                print('Generated Space Vessel: ')
                enterprise = vessel()
                constructVessel(enterprise)
                print()
                print('<<< Returning to Terminal ')
                vesselTerminal = 0

            # 2.2 Design Vessel
            if vesselTerminal == 2:
                print()
                print('Designing Vessels is currently unavailable')
                print()
                print('<<< Returning to Terminal ')
                vesselTerminal = 0

        # Vessel Terminal Return to Main Terminal
        print()
        print('<<< Returning to Terminal ')
        menuChoice = 0

    # 3. Character Terminal
    if menuChoice == 3:
        characterTerminal = 0
        while characterTerminal < 6:

            # 3.0 Main Character Terminal
            if characterTerminal == 0:
                print()
                print('Vessel Terminal')
                print('1. Traveller (LP)')
                print('2. Traveller (FDE)')
                print('3. Cyberpunk (LP)')
                print('4. Cyberpunk (FDE)')
                print('2. Design Character')
                print('6. Draft Generator')
                print('99. Return to Terminal')
                characterTerminal = int(input('>>>: '))

            # 3.1 Traveller NPC with Lifepath
            if characterTerminal == 1:
                print()
                print('For now, please use the draft generator. ')
                print()
                print('<<< Returning to Terminal ')
                characterTerminal = 0

            # 3.2 Traveller NPC without Lifepath
            if characterTerminal == 2:
                print()
                print('This feature is currently unavailable')
                print()
                print('<<< Returning to Terminal ')
                characterTerminal = 0

            # 3.3 Cyberpunk NPC with Lifepath
            if characterTerminal == 3:
                print()
                print('This feature is currently unavailable')
                print()
                print('<<< Returning to Terminal ')
                characterTerminal = 0

            # 3.4 Cyberpunk NPC without Lifepath
            if characterTerminal == 4:
                print()
                x = int(input('How many FDEs? >>: '))
                for i in range(x):
                    silverhand = cyberpunk_npc()
                    silverhand.generate()
                print()
                print('<<< Returning to Terminal ')
                characterTerminal = 0

            # 3.5 Design Character
            if characterTerminal == 5:
                print()
                print('This feature  is currently unavailable')
                print()
                print('<<< Returning to Terminal ')
                characterTerminal = 0

            # 3.6 Draft Generator
            if characterTerminal == 6:
                print()
                for i in range(int(input('How many draftees? >>: '))):
                    homeworld = random.choice(galaxy)
                    print('Homeworld: ' + homeworld.return_tagline())
                    # ^^^^^ ADDED
                    nick_carl = traveller_npc()
                    print('chk1')
                    nick_carl.generate(homeworld)
                    while nick_carl.career == 'Drifter': nick_carl.generate(homeworld)
                    naval = navy_career()
                    terms = []
                    # terms.append(naval.events())
                    # terms.append(naval.mishap())

                    navy_progression(nick_carl, naval)
                    print()
                    # for i in range(len(terms)):
                    # print(terms[i])
                print()
                print('<<< Returning to Terminal ')
                characterTerminal = 0

        # Character Terminal Return to Main Terminal
        print()
        print('<<< Returning to Terminal ')
        menuChoice = 0

    if menuChoice == 4:
        answer = 100
        while answer != 99:
            print('1. Print Equipment')
            print('2. Random Prototech')
            print('3. Generate by TL')
            print('4. Firearm Registration')
            print('5. Return to terminal')
            answer = int(input('?: '))
            print()

            # ________________________________
            # 1. Print Equipment
            if answer == 1:
                for i in range(len(equipment_list)):
                    to_print_list = equipment_list[i]
                    for n in range(len(to_print_list)):
                        to_print_list[n].info()

            # ________________________________
            # 2. Random Prototech (Defunct)
            if answer == 2:
                x = random.choice(equipment_list)
                while x == []:
                    x = random.choice(equipment_list)
                y = random.choice(x)
                y.prototech()
                y.info()

            # ________________________________
            # 3. Generate by TL
            if answer == 3:
                planet_tl = int(input('Planetary TL: '))
                products = []
                for i in range(len(equipment_list)):
                    tl_check_list = equipment_list[i]
                    for n in range(len(tl_check_list)):
                        tl_check_item = tl_check_list[n]
                        if tl_check_item.tl == planet_tl:
                            products.append(tl_check_item)
                        if tl_check_item.tl == planet_tl + 1:
                            tl_check_item.prototech(1)
                            products.append(tl_check_item)
                        if tl_check_item.tl == planet_tl + 2:
                            tl_check_item.prototech(2)
                            products.append(tl_check_item)
                        if tl_check_item.tl <= planet_tl - 1:
                            tl_check_item.retrotech(planet_tl)
                            products.append(tl_check_item)
                for i in range(len(products)):
                    products[i].print()

            # ________________________________
            # Firearms Registration
            if answer == 4:
                for i in range(len(weapons_list)):
                    homeworld = input('Planet of Origin: ')
                    if homeworld == 'random':
                        placeHolder = random.choice(galaxy)
                        homeworld = placeHolder.name
                    name = input('Model Name: ')
                    weapons_list[i].designate(homeworld, name)
                    print('FIREARM REGISTRATION COMPLETE')
                    print('-----------------------------------------------------------')
                    weapons_list[i].print()
                    print('-----------------------------------------------------------')

            if answer == 5:
                menuChoice = 0
                answer = 99

    if menuChoice == 5:
        haspJamesT = cyberpunkCharacter()
        haspJamesT.cyberpunkCharacterGenerator()
        menuChoice = 0

    if menuChoice >= 99:
        print('Closing program. . . Goodbye! Click OK on the popup window to close this window.')
        exit()

    if menuChoice < 99 and menuChoice > 6:
        print('Incorrect integer choice, returning to terminal.')
        menuChoice = 0

