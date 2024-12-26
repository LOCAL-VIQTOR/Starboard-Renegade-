import random
from SRtools import *
from SRplanets import *

# This is just extra information I'm keeping
# here for a game I have with my roommate.

dhomeworld = planet()
dhomeworld.hex = '0505'
dhomeworld.name = 'Delta-4'
dhomeworld.generateStarport(10)
dhomeworld.generateSize(5)
dhomeworld.generateAtmosphere(4)
dhomeworld.climate = [-51, 0, 'Cold']
dhomeworld.uwp[3] = 5
dhomeworld.hydrosphere = 53
dhomeworld.population = 1000000
dhomeworld.uwp[4] = 6
dhomeworld.population_density = dhomeworld.population / dhomeworld.size
dhomeworld.government = dhomeworld.government_types(1)
dhomeworld.uwp[5] = 1
dhomeworld.culture = dhomeworld.culture_types(24)
dhomeworld.uwp[7] = 12
dhomeworld.generateTravelCodes()
dhomeworld.bases = ['Naval','Scout','TAS/TT','Imperial Consulate']
dhomeworld.language = 'English (Hispanic American)'
dhomeworld.print()

