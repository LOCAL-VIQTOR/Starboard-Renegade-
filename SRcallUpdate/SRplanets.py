# Starboard, Renegade! Planets Handler

import random
import math
from SRtools import *
from SRskills import returnEthnics

# Where does this go?
def spawnPlanet(hexField, printX):
    hallowsbelt = planet()
    hallowsbelt.generate(hexField, printX)
    return hallowsbelt

#    ____  __    ___    _   ______________
#   / __ \/ /   /   |  / | / / ____/_  __/
#  / /_/ / /   / /| | /  |/ / __/   / /
# / ____/ /___/ ___ |/ /|  / /___  / /
#/_/   /_____/_/  |_/_/ |_/_____/ /_/
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
            c = random.randint(1, 2)       # Gives each hex a 50/50 shot of containing a settled world.
            if c == 2: hexes.append(z)      # Adds successful hexes to the hexes list
    return hexes

def generateGalaxy(rows, columns):
    hexField = generateHexList(rows, columns)
    galaxy = []
    for l in range(len(hexField)):
        hallowsbelt = spawnPlanet(hexField, False)
        galaxy.append(hallowsbelt)
    return galaxy

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
        self.stock = 'stockErr'
        self.language = 'PlanetLangErr'

        # TRADE GOODS
        self.goods = []

    # Generates a name for the planet
    def generateName(self):
        prefix = ['Alph', 'Br', 'Ch', 'D', 'Ech', 'F', 'G', 'H', 'Ind', 'J', 'K', 'L', 'M', 'Nov', 'Osc', 'P', 'Qu',
                  'R', 'Si', 'T', 'Un', 'V', 'Wh', 'X', 'Y', 'Z', 'Calv', 'Dian', 'Rog']
        suffix = ['a', 'avo', 'arlie', 'elta', 'o', 'oxtrot', 'olf', 'otel', 'ia', 'uliett', 'ilo', 'ima', 'ike',
                  'ember', 'ar', 'apa', 'ebec', 'omeo', 'erra', 'ango', 'iform', 'ictor', 'iskey', '-ray', 'ankee',
                  'ulu', 'owe', 'iana', 'ers']
        self.name = random.choice(prefix) + random.choice(suffix) + '-' + str(random.randint(1, 13))

    # Takes the first hex in the hex list's locatons, then removes it from the list.
    def generateHex(self, hexField):
        self.hex = hexField[0]
        hexField.remove(self.hex)

    # Determines starport quality, berth, and fuel and repair availability
    def generateStarport(self, result):

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
    def generateSize(self, size_result):
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
    def generateAtmosphere(self, atmosphere_result):
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
    def generateClimate(self):

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
    # Would be useful with a result input option
    def generateHydrographics(self):

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
    def generatePopulation(self):
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
    def generateGovernmentAndCulture(self):
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
    def generateFactions(self):

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
    def generateLawLevel(self):
        # Makes flat roll with population modifier
        self.uwp[6] = d(2,6,-7) + self.uwp[5]
        if self.uwp[6] < 0: self.uwp[6] = 0

    # Determines tech level from planet's variables
    def generateTechLevel(self):
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
    def generateTravelCodes(self):
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
    def generateBases(self):
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
    def generateLanguage(self):
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
        print('Population Stock: '+ self.stock)
        print('Language Base: ' + self.language)
        print('Known Factions:')
        for i in range(len(self.factions)):
            faction_to_print = self.factions[i]
            print(str(i + 1) + '. ' + faction_to_print[0] + ', ' + faction_to_print[1])
        if len(self.bases) >= 1: print(self.bases)
        if len(self.bases) <= 0: print('No Bases Nearby')

    def generate(self, hexField, printX):
        self.generateHex(hexField)
        self.generateName()
        self.generateStarport(d(2,6,0))
        self.generateSize(d(2,6,-2))
        self.generateAtmosphere(d(2,6,-7) + self.uwp[1])
        self.generateClimate()
        self.generateHydrographics()
        self.generatePopulation()
        self.generateGovernmentAndCulture()
        self.generateFactions()
        self.generateLawLevel()
        self.generateTechLevel()
        self.generateTravelCodes()
        self.generateBases()
        
        #self.generateLanguage()
        stock = returnEthnics()
        self.stock = stock[0]
        self.language = stock[1]
        
        if printX == True:
            self.print()
            print()

