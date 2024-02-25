# traveller overhaul v20240207

# This is an overhaul started 20240207 for the Traveller RPG character generatorc
# section of "Starboard, Renegade!". In the overhaul of the Cyberpunk character
# generator, I decided to separate skills into their own class and then put that
# class into a variable of the character class. I remember the career generator
# being an excessive bitch when I wrote what is (or was) currently in the SBRG
# main program. My plan is a main skills class, a character class containing
# basic math and other info, and then a career class to help explain exactly
# what the character's backstory is. This will play heavily into both the skills
# and character classes.

# Starboard, Renegade! Skeleton Code

import random


def d(numDice, dieType, mod):
    result = mod
    for i in range(numDice):
        result += random.randint(1, dieType)
    return result


class planet():
    def __init__(self):
        self.codes = []

    def generateCodes(self):
        homeworldCodes = ['Ag', 'As', 'De', 'Fl', 'Ga', 'Ht', 'Hi', 'IC', 'In', 'Lt', 'Po', 'Ri', 'Wa', 'Va']
        for i in range(len(homeworldCodes)):
            x = random.randint(1, 10)
            if x == 1: self.codes.append(homeworldCodes[i])


# I. SKILLS

# Skill Levels Breakdown:
#  -3: Untrained
#   0: Little Experience
#   1: Trained Individual
# 2-3: Skilled Professional
#   4: Famous or High Renown

class travellerSkills():
    def __init__(self):
        self.admin = -3
        self.advocate = -3

        self.animals = -3
        self.animalRiding = -3
        self.animalVet = -3
        self.animalTraining = -3
        self.animalFarming = -3

        self.athletics = -3
        self.athleticsCoordination = -3
        self.athleticsEndurance = -3
        self.athleticsStrength = -3
        self.athleticsFlying = -3

        self.art = -3
        self.artActing = -3
        self.artDance = -3
        self.artHolography = -3
        self.artInstrument = -3
        self.artSculpting = -3
        self.artWriting = -3

        self.astrogation = -3
        self.battleDress = -3
        self.broker = -3
        self.carouse = -3
        self.comms = -3
        self.computers = -3
        self.deception = -3
        self.diplomat = -3

        self.drive = -3
        self.driveMole = -3
        self.driveTracked = -3
        self.driveWheeled = -3

        self.engineer = -3
        self.engineerMDrive = -3
        self.engineerJDrive = -3
        self.engineerElectronics = -3
        self.engineerLifeSupport = -3
        self.engineerPower = -3
        self.explosives = -3

        self.flyer = -3
        self.flyerGrav = -3
        self.flyerRotor = -3
        self.flyerWing = -3

        self.gambler = -3

        self.gunner = -3
        self.gunnerTurrets = -3
        self.gunnerOrtillery = -3
        self.gunnerScreens = -3
        self.gunnerCapitalWeapons = -3

        self.gunCombat = -3
        self.gunCombatSlugRifle = -3
        self.gunCombatSlugPistol = -3
        self.gunCombatShotgun = -3
        self.gunCombatEnergyRifle = -3
        self.gunCombatEnergyPistol = -3

        self.heavyWeapons = -3
        self.heavyWeaponsLaunchers = -3
        self.heavyWeaponsMPA = -3  # man portable artillery
        self.heavyWeaponsFieldArtillery = -3

        self.investigate = -3
        self.jackOfAllTrades = -3
        self.language = -3  # must be extrapolated
        self.leadership = -3
        self.mechanic = -3
        self.medic = -3

        self.melee = -3
        self.meleeUnarmed = -3
        self.meleeBlade = -3
        self.meleeBludgeon = -3
        self.meleeNatural = -3

        self.navigation = -3
        self.persuade = -3

        self.pilot = -3
        self.pilotSmallCraft = -3
        self.pilotSpacecraft = -3
        self.pilotCapitalShips = -3

        self.recon = -3
        self.remoteOperation = -3

        self.physicalScience = -3
        self.physicalSciencePhysics = -3
        self.physicalScienceChemistry = -3
        self.physicalScienceElectronics = -3

        self.lifeScience = -3
        self.lifeScienceBiology = -3
        self.lifeScienceCybernetics = -3
        self.lifeScienceGenetics = -3
        self.lifeSciencePsionicology = -3

        self.socialScience = -3
        self.socialScienceArcheology = -3
        self.socialScienceEconomics = -3
        self.socialScienceHistory = -3
        self.socialScienceLinguistics = -3
        self.socialSciencePhilosophy = -3
        self.socialSciencePsychology = -3
        self.socialScienceSophontology = -3

        self.spaceScience = -3
        self.spaceSciencePlanetology = -3
        self.spaceScienceRobotics = -3
        self.spaceScienceXenology = -3

        self.seafarer = -3
        self.seafarerSail = -3
        self.seafarerSubmarine = -3
        self.seafarerOceanShips = -3
        self.seafarerMotorboats = -3

        self.sensors = -3
        self.stealth = -3
        self.steward = -3
        self.streetwise = -3
        self.survival = -3

        self.tactics = -3
        self.tacticsMilitary = -3
        self.tacticsNaval = -3

        self.trade = -3
        self.tradeBiologicals = -3
        self.tradeCivilEngineering = -3
        self.tradeSpaceConstruction = -3
        self.tradeHydroponics = -3
        self.tradePolymers = -3

        self.vaccSuit = -3
        self.zeroG = -3

    def homeworldSkills(self, homeworld):
        if 'Ag' in homeworld.codes or 'Ga' in homeworld.codes or 'Po' in homeworld.codes:
            self.animals = 0  # could be animals any i suppose
        if 'As' in homeworld.codes:
            self.zeroG = 0
        if 'De' in homeworld.codes or 'Lt' in homeworld.codes:
            self.survival = 0
        if 'Fl' in homeworld.codes or 'Wa' in homeworld.codes:
            x = random.randint(1, 5)
            if x == 1: self.seafarer = 0
            if x == 2: self.seafarerSail = 0
            if x == 3: self.seafarerSubmarine = 0
            if x == 4: self.seafarerOceanShips = 0
            if x == 5: self.seafarerMotorboats = 0
        if 'Ht' in homeworld.codes:
            self.computers = 0
        if 'Hi' in homeworld.codes:
            self.streetwise = 0
        if 'IC' in homeworld.codes or 'Va' in homeworld.codes:
            self.vaccSuit = 0
        if 'In' in homeworld.codes:
            x = random.randint(1, 6)
            if x == 1: self.trade = 0
            if x == 2: self.tradeBiologicals = 0
            if x == 3: self.tradeCivilEngineering = 0
            if x == 4: self.tradeSpaceConstruction = 0
            if x == 5: self.tradeHydroponics = 0
            if x == 6: self.tradePolymers = 0
        if 'Ri' in homeworld.codes:
            self.carouse = 0

    def educationSkills(self, character):

        spaceSciences = [self.spaceScience, self.spaceSciencePlanetology, self.spaceScienceRobotics,
                         self.spaceScienceXenology]
        tradeSkills = [self.trade, self.tradeBiologicals, self.tradeCivilEngineering, self.tradeSpaceConstruction,
                       self.tradeHydroponics, self.tradePolymers]

        eduSkillsNum = 3 + charMod(character.edu)
        for i in range(eduSkillsNum):
            skillChosen = False
            while skillChosen == False:
                x = random.randint(1, 15)
                y = 0
                if x == 1 and self.admin == -3:
                    self.admin = 0
                    skillChosen = True
                if x == 2 and self.advocate == -3:
                    self.advocate = 0
                    skillChosen = True
                if x == 3:
                    y = random.randint(1, 7)
                    if y == 1 and self.art == -3:
                        self.art = 0
                        skillChosen = True
                    if y == 2 and self.artActing == -3:
                        self.artActing = 0
                        skillChosen = True
                    if y == 3 and self.artDance == -3:
                        self.artDance = 0
                        skillChosen = True
                    if y == 4 and self.artHolography == -3:
                        self.artHolography = 0
                        skillChosen = True
                    if y == 5 and self.artInstrument == -3:
                        self.artInstrument = 0
                        skillChosen = True
                    if y == 6 and self.artSculpting == -3:
                        self.artSculpture = 0
                        skillChosen = True
                    if y == 7 and self.artWriting == -3:
                        self.artWriting = 0
                        skillChosen = True
                if x == 4 and self.carouse == -3:
                    self.carouse = 0
                    skillChosen = True
                if x == 5 and self.comms == -3:
                    self.comms = 0
                    skillChosen = True
                if x == 6 and self.computers == -3:
                    self.computers = 0
                    skillChosen = True
                if x == 7:
                    y = random.randint(1, 4)
                    if y == 1 and self.drive == -3:
                        self.drive = 0
                        skillChosen = True
                    if y == 2 and self.driveMole == -3:
                        self.driveMole = 0
                        skillChosen = True
                    if y == 3 and self.driveTracked == -3:
                        self.driveTracked = 0
                        skillChosen = True
                    if y == 4 and self.driveWheeled == -3:
                        self.driveWheeled = 0
                        skillChosen = True
                if x == 8:
                    y = random.randint(1, 6)
                    if y == 1 and self.engineer == -3:
                        self.engineer = 0
                        skillChosen = True
                    if y == 2 and self.engineerMDrive == -3:
                        self.engineerMDrive = 0
                        skillChosen = True
                    if y == 3 and self.engineerJDrive == -3:
                        self.engineerJDrive = 0
                        skillChosen = True
                    if y == 4 and self.engineerElectronics == -3:
                        self.engineerElectronics = 0
                        skillChosen = True
                    if y == 5 and self.engineerLifeSupport == -3:
                        self.engineerLifeSupport = 0
                        skillChosen = True
                    if y == 6 and self.engineerPower == -3:
                        self.engineerPower = 0
                        skillChosen = True
                if x == 9 and self.language == -3:
                    self.language = 0
                    skillChosen = True
                if x == 10 and self.medic == -3:
                    self.medic = 0
                    skillChosen = True
                if x == 11:
                    y = random.randint(1, 4)
                    if y == 1 and self.physicalScience == -3:
                        self.physicalScience = 0
                        skillChosen = True
                    if y == 2 and self.physicalSciencePhysics == -3:
                        self.physicalSciencePhysics = 0
                        skillChosen = True
                    if y == 3 and self.physicalScienceChemistry == -3:
                        self.physicalScienceChemistry = 0
                        skillChosen = True
                    if y == 4 and self.physicalScienceElectronics == -3:
                        self.physicalScienceElectronics = 0
                        skillChosen = True
                if x == 13:
                    y = random.randint(1, 8)
                    if y == 1 and self.socialScience == -3:
                        self.socialScience = 0
                        skillChosen = True
                    if y == 2 and self.socialScienceArcheology == -3:
                        self.socialScienceArcheology = 0
                        skillChosen = True
                    if y == 3 and self.socialScienceEconomics == -3:
                        self.socialScienceEconomics = 0
                        skillChosen = True
                    if y == 4 and self.socialScienceHistory == -3:
                        self.socialScienceHistory = 0
                        skillChosen = True
                    if y == 5 and self.socialScienceLinguistics == -3:
                        self.socialScienceLinguistics = 0
                        skillChosen = True
                    if y == 6 and self.socialSciencePhilosophy == -3:
                        self.socialSciencePhilosophy = 0
                        skillChosen = True
                    if y == 7 and self.socialSciencePsychology == -3:
                        self.socialSciencePsychology = 0
                        skillChosen = True
                    if y == 8 and self.socialScienceSophontology == -3:
                        self.socialScienceSophontology = 0
                        skillChosen = True
                if x == 14:
                    y = random.randint(1, 4)
                    if y == 1 and self.spaceScience == -3:
                        self.drive = 0
                        skillChosen = True
                    if y == 2 and self.spaceSciencePlanetology == -3:
                        self.driveMole = 0
                        skillChosen = True
                    if y == 3 and self.spaceScienceRobotics == -3:
                        self.driveTracked = 0
                        skillChosen = True
                    if y == 4 and self.spaceScienceXenology == -3:
                        self.driveWheeled = 0
                        skillChosen = True
                if x == 15:
                    y = random.randint(1, 5)
                    if y == 1 and self.trade == -3:
                        self.trade = 0
                        skillChosen = True
                    if y == 2 and self.tradeBiologicals == -3:
                        self.tradeBiologicals = 0
                        skillChosen = True
                    if y == 3 and self.tradeCivilEngineering == -3:
                        self.tradeCivilEngineering = 0
                        skillChosen = True
                    if y == 4 and self.tradeHydroponics == -3:
                        self.tradeHydroponics = 0
                        skillChosen = True
                    if y == 5 and self.tradePolymers == -3:
                        self.tradePolymers = 0
                        skillChosen = True

        # for i in range(eduSkillsNum):
        #    x = random.randint(1,15)
        #    while x in eduSkills: x = random.randint(1,15)
        #    eduSkills.append(x)
        # edu_skills_list = ['Admin', 'Advocate', 'Art (any)', 'Carouse (any)', 'Comms', 'Computer', 'Drive (any)',
        #                   'Engineer (any)', 'Language (any)', 'Medic', 'Physical Science (any)',
        #                   'Life Science (any)', 'Social Science (any)', 'Space Science (any)', 'Trade (any)']

    def train(self, character, skill, num):

        if skill == '+1 STR': character.str += 1
        if skill == '+1 DEX': character.dex += 1
        if skill == '+1 END': character.end += 1
        if skill == '+1 INT': character.int += 1
        if skill == '+1 EDU': character.edu += 1
        if skill == '+1 SOC': character.soc += 1

        if skill == 'Admin':
            if num == -1: self.admin += 1
            if num != -1: self.admin == 0

        if skill == 'Animals (Any)':
            skill = random.choice(
                ['Animals (Animals)', 'Animals (Riding)', 'Animals (Vet)', 'Animals (Training)', 'Animals (Farming)'])
        if skill == 'Animals':
            if self.animals == -3: self.animals = 0
            if num == -1: self.animals += 1
            if num != -1: self.animals == num
        if skill == 'Animals (Riding)':
            if self.animalRiding == -3: self.animalRiding = 0
            if num == -1: self.animalRiding += 1
            if num != -1: self.animalRiding == num
        if skill == 'Animals (Vet)':
            if self.animalVet == -3: self.animalVet = 0
            if num == -1: self.animalVet += 1
            if num != -1: self.animalVet == num
        if skill == 'Animals (Training)':
            if self.animalTraining == -3: self.animalTraining = 0
            if num == -1: self.animalTraining += 1
            if num != -1: self.animalTraining == num
        if skill == 'Animals (Farming)':
            if self.animalFarming == -3: self.animalFarming = 0
            if num == -1: self.animalFarming += 1
            if num != -1: self.animalFarming == num

        if skill == 'Astrogation':
            if self.astrogation == -3: self.astrogation = 0
            if num == -1: self.astrogation += 1
            if num != -1: self.astrogation == num

        if skill == 'Athletics (Any)':
            skill = random.choice(
                ['Athletics', 'Athletics (Coordination)', 'Athletics (Endurance)', 'Athletics (Strength)',
                 'Athletics (Flying)'])
        if skill == 'Athletics':
            if self.athletics == -3: self.athletics = 0
            if num == -1: self.athletics += 1
            if num != -1: self.athletics = num
        if skill == 'Athletics (Coordination)':
            if self.athleticsCoordination == -3: self.athleticsCoordination = 0
            if num == -1: self.athleticsCoordination += 1
            if num != -1: self.athleticsCoordination = num
        if skill == 'Athletics (Endurance)':
            if self.athleticsEndurance == -3: self.athleticsEndurance = 0
            if num == -1: self.athleticsEndurance += 1
            if num != -1: self.athleticsEndurance = num
        if skill == 'Athletics (Strength)':
            if self.athleticsStrength == -3: self.athleticsStrength = 0
            if num == -1: self.athleticsStrength += 1
            if num != -1: self.athleticsStrength = num
        if skill == 'Athletics (Flying)':
            if self.athleticsFlying == -3: self.athleticsFlying = 0
            if num == -1: self.athleticsFlying += 1
            if num != -1: self.athleticsFlying = num
        if skill == 'Carouse':
            if self.carouse == -3: self.carouse = 0
            if num == -1: self.carouse += 1
            if num != -1: self.carouse = num
        if skill == 'Deception':
            if self.deception == -3: self.deception = 0
            if num == -1: self.deception += 1
            if num != -1: self.deception = num

        if skill == 'Drive (Any)':
            skill = random.choice(['Drive', 'Drive (Mole)', 'Drive (Tracked)', 'Drive (Wheeled)'])
        if skill == 'Drive':
            if self.drive == -3: self.drive = 0
            if num == -1: self.drive += 1
            if num != -1: self.drive = num
        if skill == 'Drive (Mole)':
            if self.driveMole == -3: self.driveMole = 0
            if num == -1: self.driveMole += 1
            if num != -1: self.driveMole = num
        if skill == 'Drive (Tracked)':
            if self.driveTracked == -3: self.driveTracked = 0
            if num == -1: self.driveTracked += 1
            if num != -1: self.driveTracked = num
        if skill == 'Drive (Wheeled)':
            if self.driveWheeled == -3: self.driveWheeled = 0
            if num == -1: self.driveWheeled += 1
            if num != -1: self.driveWheeled = num

        if skill == 'Engineer (Any)':
            skill = random.choice(['Engineer',
                                   'Engineer (M-Drive)',
                                   'Engineer (J-Drive)',
                                   'Engineer (Electronics)',
                                   'Engineer (Life Support)',
                                   'Engineer (Power)', ])
        if skill == 'Engineer':
            if self.engineer == -3: self.engineer = 0
            if num == -1: self.engineer += 1
            if num != -1: self.engineer = num
        if skill == 'Engineer (M-Drive)':
            if self.engineerMDrive == -3: self.engineerMDrive = 0
            if num == -1: self.engineerMDrive += 1
            if num != -1: self.engineerMDrive = num
        if skill == 'Engineer (J-Drive)':
            if self.engineerJDrive == -3: self.engineerJDrive = 0
            if num == -1: self.engineerJDrive += 1
            if num != -1: self.engineerJDrive = num
        if skill == 'Engineer (Electronics)':
            if self.engineerElectronics == -3: self.engineerElectronics = 0
            if num == -1: self.engineerElectronics += 1
            if num != -1: self.engineerElectronics = num
        if skill == 'Engineer (Life Support)':
            if self.engineerLifeSupport == -3: self.engineerLifeSupport = 0
            if num == -1: self.engineerLifeSupport += 1
            if num != -1: self.engineerLifeSupport = num
        if skill == 'Engineer (Power)':
            if self.engineerPower == -3: self.engineerPower = 0
            if num == -1: self.engineerPower += 1
            if num != -1: self.engineerPower = num

        if skill == 'Gambler':
            if self.gambler == -3: self.gambler = 0
            if num == -1: self.gambler += 1
            if num != -1: self.gambler = num

        if skill == 'Gun Combat (Any)':
            skill = random.choice(
                ['Gun Combat', 'Gun Combat (Slug Rifle)', 'Gun Combat (Slug Pistol)', 'Gun Combat (Shotgun)',
                 'Gun Combat (Energy Rifle)', 'Gun Combat (Energy Pistol)', ])
        if skill == 'Gun Combat':
            if self.gunCombat == -3: self.gunCombat = 0
            if num == -1: self.gunCombat += 1
            if num != -1: self.gunCombat = num
        if skill == 'Gun Combat (Slug Rifle)':
            if self.gunCombatSlugRifle == -3: self.gunCombatSlugRifle = 0
            if num == -1: self.gunCombatSlugRifle += 1
            if num != -1: self.gunCombatSlugRifle = num
        if skill == 'Gun Combat (Slug Pistol)':
            if self.gunCombatSlugPistol == -3: self.gunCombatSlugPistol = 0
            if num == -1: self.gunCombatSlugPistol += 1
            if num != -1: self.gunCombatSlugPistol = num
        if skill == 'Gun Combat (Shotgun)':
            if self.gunCombatShotgun == -3: self.gunCombatShotgun = 0
            if num == -1: self.gunCombatShotgun += 1
            if num != -1: self.gunCombatShotgun = num
        if skill == 'Gun Combat (Energy Rifle)':
            if self.gunCombatEnergyRifle == -3: self.gunCombatEnergyRifle = 0
            if num == -1: self.gunCombatEnergyRifle += 1
            if num != -1: self.gunCombatEnergyRifle = num
        if skill == 'Gun Combat (Energy Pistol)':
            if self.gunCombatEnergyPistol == -3: self.gunCombatEnergyPistol = 0
            if num == -1: self.gunCombatEnergyPistol += 1
            if num != -1: self.gunCombatEnergyPistol = num

        if skill == 'Gunner (Any)':
            skill = random.choice(
                ['Gunner', 'Gunner (Turrets)', 'Gunner (Ortillery)', 'Gunner (Screens)', 'Gunner (Capital Weapons)'])
        if skill == 'Gunner':
            if self.gunner == -3: self.gunner = 0
            if num == -1: self.gunner += 1
            if num != -1: self.gunner = num
        if skill == 'Gunner (Turrets)':
            if self.gunnerTurrets == -3: self.gunnerTurrets = 0
            if num == -1: self.gunnerTurrets += 1
            if num != -1: self.gunnerTurrets = num
        if skill == 'Gunner (Ortillery)':
            if self.gunnerOrtillery == -3: self.gunnerOrtillery = 0
            if num == -1: self.gunnerOrtillery += 1
            if num != -1: self.gunnerOrtillery = num
        if skill == 'Gunner (Screens)':
            if self.gunnerScreens == -3: self.gunnerScreens = 0
            if num == -1: self.gunnerScreens += 1
            if num != -1: self.gunnerScreens = num
        if skill == 'Gunner (Capital Weapons)':
            if self.gunnerCapitalWeapons == -3: self.gunnerCapitalWeapons = 0
            if num == -1: self.gunnerCapitalWeapons += 1
            if num != -1: self.gunnerCapitalWeapons = num

        if skill == 'Heavy Weapons (Any)':
            skill = random.choice(['Heavy Weapons', 'Heavy Weapons (Launchers)', 'Heavy Weapons (MPA)',
                                   'Heavy Weapons (Field Artillery)'])
        if skill == 'Heavy Weapons':
            if self.heavyWeapons == -3: self.heavyWeapons = 0
            if num == -1: self.heavyWeapons += 1
            if num != -1: self.heavyWeapons = num
        if skill == 'Heavy Weapons (Launchers)':
            if self.heavyWeaponsLaunchers == -3: self.heavyWeaponsLaunchers = 0
            if num == -1: self.heavyWeaponsLaunchers += 1
            if num != -1: self.heavyWeaponsLaunchers = num
        if skill == 'Heavy Weapons (MPA)':
            if self.heavyWeaponsMPA == -3: self.heavyWeaponsMPA = 0
            if num == -1: self.heavyWeaponsMPA += 1
            if num != -1: self.heavyWeaponsMPA = num
        if skill == 'Heavy Weapons (Field Artillery)':
            if self.heavyWeaponsFieldArtillery == -3: self.heavyWeaponsFieldArtillery = 0
            if num == -1: self.heavyWeaponsFieldArtillery += 1
            if num != -1: self.heavyWeaponsFieldArtillery = num

        if skill == 'Jack of all Trades':
            if self.jackOfAllTrades == -3: self.jackOfAllTrades = 0
            if num == -1: self.jackOfAllTrades += 1
            if num != -1: self.jackOfAllTrades = num

        if skill == 'Leadership':
            if self.leadership == -3: self.leadership = 0
            if num == -1: self.leadership += 1
            if num != -1: self.leadership = num

        if skill == 'Mechanic':
            if self.mechanic == -3: self.mechanic = 0
            if num == -1: self.mechanic += 1
            if num != -1: self.mechanic = num

        if skill == 'Medic':
            if self.medic == -3: self.medic = 0
            if num == -1: self.medic += 1
            if num != -1: self.medic = num

        if skill == 'Melee (Any)':
            skill = random.choice(['Melee', 'Melee (Unarmed)', 'Melee (Blade)', 'Melee (Bludgeon)', 'Melee (Natural)'])
        if skill == 'Melee':
            if self.melee == -3: self.melee = 0
            if num == -1: self.melee += 1
            if num != -1: self.melee = num
        if skill == 'Melee (Blade)':
            if self.meleeBlade == -3: self.meleeBlade = 0
            if num == -1: self.meleeBlade += 1
            if num != -1: self.meleeBlade = num
        if skill == 'Melee (Unarmed)':
            if self.meleeUnarmed == -3: self.meleeUnarmed = 0
            if num == -1: self.meleeUnarmed += 1
            if num != -1: self.meleeUnarmed = num
        if skill == 'Melee (Bludgeon)':
            if self.meleeBludgeon == -3: self.meleeBludgeon = 0
            if num == -1: self.meleeBludgeon += 1
            if num != -1: self.meleeBludgeon = num
        if skill == 'Melee (Natural)':
            if self.meleeNatural == -3: self.meleeNatural = 0
            if num == -1: self.meleeNatural += 1
            if num != -1: self.meleeNatural = num

        if skill == 'Pilot (Any)':
            skill = random.choice(['Pilot',
                                   'Pilot (Small Craft)',
                                   'Pilot (Spacecraft)',
                                   'Pilot (Capital Ships)'])
        if skill == 'Pilot':
            if self.pilot == -3: self.pilot = 0
            if num == -1: self.pilot += 1
            if num != -1: self.pilot = num
        if skill == 'Pilot (Small Craft)':
            if self.pilotSmallCraft == -3: self.pilotSmallCraft = 0
            if num == -1: self.pilotSmallCraft += 1
            if num != -1: self.pilotSmallCraft = num
        if skill == 'Pilot (Spacecraft)':
            if self.pilotSpacecraft == -3: self.pilotSpacecraft = 0
            if num == -1: self.pilotSpacecraft += 1
            if num != -1: self.pilotSpacecraft = num
        if skill == 'Pilot (Capital Ships)':
            if self.pilotCapitalShips == -3: self.pilotCapitalShips = 0
            if num == -1: self.pilotCapitalShips += 1
            if num != -1: self.pilotCapitalShips = num

        if skill == 'Recon':  # recon issues
            if self.recon == -3: self.recon = 0
            if num == -1: self.recon += 1
            if num != -1: self.recon = num

        if skill == 'Seafarer (Any)': skill = random.choice(
            ['Seafarer', 'Seafarer (Sail)', 'Seafarer (Submarine)', 'Seafarer (Ocean Ships)', 'Seafarer (Motorboats)'])
        if skill == 'Seafarer':
            if self.seafarer == -3: self.seafarer = 0
            if num == -1: self.seafarer += 1
            if num != -1: self.seafarer = num
        if skill == 'Seafarer (Sail)':
            if self.seafarerSail == -3: self.seafarerSail = 0
            if num == -1: self.seafarerSail += 1
            if num != -1: self.seafarerSail = num
        if skill == 'Seafarer (Submarine)':
            if self.seafarerSubmarine == -3: self.seafarerSubmarine = 0
            if num == -1: self.seafarerSubmarine += 1
            if num != -1: self.seafarerSubmarine = num
        if skill == 'Seafarer (Ocean Ships)':
            if self.seafarerOceanShips == -3: self.seafarerOceanShips = 0
            if num == -1: self.seafarerOceanShips += 1
            if num != -1: self.seafarerOceanShips = num
        if skill == 'Seafarer (Motorboats)':
            if self.seafarerMotorboats == -3: self.seafarerMotorboats = 0
            if num == -1: self.seafarerMotorboats += 1
            if num != -1: self.seafarerMotorboats = num

        if skill == 'Stealth':  # streetwise survival mixup check
            if self.stealth == -3: self.stealth = 0
            if num == -1: self.stealth += 1
            if num != -1: self.stealth = num

        if skill == 'Streetwise':
            if self.streetwise == -3: self.streetwise = 0
            if num == -1: self.streetwise += 1
            if num != -1: self.streetwise = num
        if skill == 'Survival':
            if self.survival == -3: self.survival = 0
            if num == -1: self.survival += 1
            if num != -1: self.survival = num

        if skill == 'Vacc Suit':
            if self.vaccSuit == -3: self.vaccSuit = 0
            if num == -1: self.vaccSuit += 1
            if num != -1: self.vaccSuit = num
        if skill == 'Zero-G':
            if self.zeroG == -3: self.zeroG = 0
            if num == -1: self.zeroG += 1
            if num != -1: self.zeroG = num

    def print(self):
        if self.admin >= 0: print('Admin' + ' ' + str(self.admin))
        if self.advocate >= 0: print('Advocate' + ' ' + str(self.advocate))

        if self.animals >= 0: print('Animals' + ' ' + str(self.animals))
        if self.animalRiding >= 0: print('Animals (Riding)' + ' ' + str(self.animalRiding))
        if self.animalVet >= 0: print('Animals (Veterinary)' + ' ' + str(self.animalVet))
        if self.animalTraining >= 0: print('Animal (Training)' + ' ' + str(self.animalTraining))
        if self.animalFarming >= 0: print('Animal (Farming)' + ' ' + str(self.animalFarming))

        if self.athletics >= 0: print('Athletics' + ' ' + str(self.athletics))
        if self.athleticsCoordination >= 0: print('Athletics (Coordination)' + ' ' + str(self.athleticsCoordination))
        if self.athleticsEndurance >= 0: print('Athletics (Endurance)' + ' ' + str(self.athleticsEndurance))
        if self.athleticsStrength >= 0: print('Athletics (Strength)' + ' ' + str(self.athleticsStrength))
        if self.athleticsFlying >= 0: print('Athletics (Flying)' + ' ' + str(self.athleticsFlying))

        if self.art >= 0: print('Art' + ' ' + str(self.art))
        if self.artActing >= 0: print('Art (Acting)' + ' ' + str(self.artActing))
        if self.artDance >= 0: print('Art (Dance)' + ' ' + str(self.artDance))
        if self.artHolography >= 0: print('Art (Holography)' + ' ' + str(self.artHolography))
        if self.artInstrument >= 0: print('Art (Instrument)' + ' ' + str(self.artInstrument))
        if self.artSculpting >= 0: print('Art (Sculpting)' + ' ' + str(self.artSculpting))
        if self.artWriting >= 0: print('Art (Writing)' + ' ' + str(self.artWriting))

        if self.astrogation >= 0: print('Astrogation' + ' ' + str(self.astrogation))
        if self.battleDress >= 0: print('Battle Dress' + ' ' + str(self.battleDress))
        if self.broker >= 0: print('Broker' + ' ' + str(self.broker))
        if self.carouse >= 0: print('Carouse' + ' ' + str(self.carouse))
        if self.comms >= 0: print('Comms' + ' ' + str(self.comms))
        if self.computers >= 0: print('Computers' + ' ' + str(self.computers))
        if self.deception >= 0: print('Deception' + ' ' + str(self.deception))
        if self.diplomat >= 0: print('Diplomat' + ' ' + str(self.diplomat))

        if self.drive >= 0: print('Drive' + ' ' + str(self.drive))
        if self.driveMole >= 0: print('Drive (Mole)' + ' ' + str(self.driveMole))
        if self.driveTracked >= 0: print('Drive (Tracked)' + ' ' + str(self.driveTracked))
        if self.driveWheeled >= 0: print('Drive (Wheeled)' + ' ' + str(self.driveWheeled))

        if self.engineer >= 0: print('Engineer' + ' ' + str(self.engineer))
        if self.engineerMDrive >= 0: print('Engineer (M-Drive)' + ' ' + str(self.engineerMDrive))
        if self.engineerJDrive >= 0: print('Engineer (J-Drive)' + ' ' + str(self.engineerJDrive))
        if self.engineerElectronics >= 0: print('Engineer (Electronics)' + ' ' + str(self.engineerElectronics))
        if self.engineerLifeSupport >= 0: print('Engineer (Life Support)' + ' ' + str(self.engineerLifeSupport))
        if self.engineerPower >= 0: print('Engineer (Power)' + ' ' + str(self.engineerPower))

        if self.explosives >= 0: print('Admin' + ' ' + str(self.admin))

        if self.flyer >= 0: print('Flyer' + ' ' + str(self.flyer))
        if self.flyerGrav >= 0: print('Flyer (Grav)' + ' ' + str(self.flyerGrav))
        if self.flyerRotor >= 0: print('Flyer (Rotor)' + ' ' + str(self.flyerRotor))
        if self.flyerWing >= 0: print('Flyer (Wing)' + ' ' + str(self.flyerWing))

        if self.gambler >= 0: print('Gambler' + ' ' + str(self.gambler))

        if self.gunner >= 0: print('Gunner' + ' ' + str(self.gunner))
        if self.gunnerTurrets >= 0: print('Gunner (Turrets)' + ' ' + str(self.gunnerTurrets))
        if self.gunnerOrtillery >= 0: print('Gunner (Ortillery)' + ' ' + str(self.gunnerOrtillery))
        if self.gunnerScreens >= 0: print('Gunner (Screens)' + ' ' + str(self.gunnerScreens))
        if self.gunnerCapitalWeapons >= 0: print('Gunner (Capital Weapons)' + ' ' + str(self.gunnerCapitalWeapons))

        if self.gunCombat >= 0: print('Gun Combat' + ' ' + str(self.gunCombat))
        if self.gunCombatSlugRifle >= 0: print('Gun Combat (Slug Rifle)' + ' ' + str(self.gunCombatSlugRifle))
        if self.gunCombatSlugPistol >= 0: print('Gun Combat (Slug Pistol)' + ' ' + str(self.gunCombatSlugPistol))
        if self.gunCombatShotgun >= 0: print('Gun Combat (Shotgun)' + ' ' + str(self.gunCombatShotgun))
        if self.gunCombatEnergyRifle >= 0: print('Gun Combat (Energy Rifle)' + ' ' + str(self.gunCombatEnergyRifle))
        if self.gunCombatEnergyPistol >= 0: print('Gun Combat (Energy Pistol)' + ' ' + str(self.gunCombatEnergyPistol))

        if self.heavyWeapons >= 0: print('Heavy Weapons' + ' ' + str(self.heavyWeapons))
        if self.heavyWeaponsLaunchers >= 0: print('Heavy Weapons (Launchers)' + ' ' + str(self.heavyWeaponsLaunchers))
        if self.heavyWeaponsMPA >= 0: print(
            'Heavy Weapons (MPA)' + ' ' + str(self.heavyWeaponsMPA))  # man portable artillery
        if self.heavyWeaponsFieldArtillery >= 0: print(
            'Heavy Weapons (Field Artillery)' + ' ' + str(self.heavyWeaponsFieldArtillery))

        if self.investigate >= 0: print('Investigate' + ' ' + str(self.investigate))
        if self.jackOfAllTrades >= 0: print('Jack of all Trades' + ' ' + str(self.jackOfAllTrades))
        if self.language >= 0: print('Language' + ' ' + str(self.language))  # must be extrapolated
        if self.leadership >= 0: print('Leadership' + ' ' + str(self.leadership))
        if self.mechanic >= 0: print('Mechanic' + ' ' + str(self.mechanic))
        if self.medic >= 0: print('Medic' + ' ' + str(self.medic))

        if self.melee >= 0: print('Melee' + ' ' + str(self.melee))
        if self.meleeUnarmed >= 0: print('Melee (Unarmed)' + ' ' + str(self.meleeUnarmed))
        if self.meleeBlade >= 0: print('Melee (Blade)' + ' ' + str(self.meleeBlade))
        if self.meleeBludgeon >= 0: print('Melee (Bludgeon)' + ' ' + str(self.meleeBludgeon))
        if self.meleeNatural >= 0: print('Melee (Natural)' + ' ' + str(self.meleeNatural))

        if self.navigation >= 0: print('Navigation' + ' ' + str(self.navigation))
        if self.persuade >= 0: print('Persuade' + ' ' + str(self.persuade))

        if self.pilot >= 0: print('Pilot' + ' ' + str(self.pilot))
        if self.pilotSmallCraft >= 0: print('Pilot (Small Craft)' + ' ' + str(self.pilotSmallCraft))
        if self.pilotSpacecraft >= 0: print('Pilot (Spacecraft)' + ' ' + str(self.pilotSpacecraft))
        if self.pilotCapitalShips >= 0: print('Pilot (Capitol Ships)' + ' ' + str(self.pilotCapitalShips))

        if self.recon >= 0: print('Recon' + ' ' + str(self.recon))
        if self.remoteOperation >= 0: print('Admin' + ' ' + str(self.admin))

        if self.physicalScience >= 0: print('Physical Science' + ' ' + str(self.physicalScience))
        if self.physicalSciencePhysics >= 0: print(
            'Physical Science (Physics)' + ' ' + str(self.physicalSciencePhysics))
        if self.physicalScienceChemistry >= 0: print(
            'Physical Science (Chemistry)' + ' ' + str(self.physicalScienceChemistry))
        if self.physicalScienceElectronics >= 0: print(
            'Physical Science (Electronics)' + ' ' + str(self.physicalScienceElectronics))

        if self.lifeScience >= 0: print('Life Science' + ' ' + str(self.lifeScience))
        if self.lifeScienceBiology >= 0: print('Life Science (Biology)' + ' ' + str(self.lifeScienceBiology))
        if self.lifeScienceCybernetics >= 0: print(
            'Life Science (Cybernetics)' + ' ' + str(self.lifeScienceCybernetics))
        if self.lifeScienceGenetics >= 0: print('Life Science (Genetics)' + ' ' + str(self.lifeScienceGenetics))
        if self.lifeSciencePsionicology >= 0: print(
            'Life Science (Psionicology)' + ' ' + str(self.lifeSciencePsionicology))

        if self.socialScience >= 0: print('Admin' + ' ' + str(self.socialScience))
        if self.socialScienceArcheology >= 0: print(
            'Social Science (Archeology)' + ' ' + str(self.socialScienceArcheology))
        if self.socialScienceEconomics >= 0: print(
            'Social Science (Economics)' + ' ' + str(self.socialScienceEconomics))
        if self.socialScienceHistory >= 0: print('Social Science (History)' + ' ' + str(self.socialScienceHistory))
        if self.socialScienceLinguistics >= 0: print(
            'Social Science (Linguistics)' + ' ' + str(self.socialScienceLinguistics))
        if self.socialSciencePhilosophy >= 0: print(
            'Social Science (Philosophy)' + ' ' + str(self.socialSciencePhilosophy))
        if self.socialSciencePsychology >= 0: print(
            'Social Science (Psychology)' + ' ' + str(self.socialSciencePsychology))
        if self.socialScienceSophontology >= 0: print(
            'Social Science (Sophontology)' + ' ' + str(self.socialScienceSophontology))

        if self.spaceScience >= 0: print('Space Science' + ' ' + str(self.spaceScience))
        if self.spaceSciencePlanetology >= 0: print(
            'Space Science (Planetology)' + ' ' + str(self.spaceSciencePlanetology))
        if self.spaceScienceRobotics >= 0: print('Space Science (Robotics)' + ' ' + str(self.spaceScienceRobotics))
        if self.spaceScienceXenology >= 0: print('Space Science (Xenology)' + ' ' + str(self.spaceScienceXenology))

        if self.seafarer >= 0: print('Seafarer' + ' ' + str(self.seafarer))
        if self.seafarerSail >= 0: print('Seafarer (Sail)' + ' ' + str(self.seafarerSail))
        if self.seafarerSubmarine >= 0: print('Seafarer (Submarine)' + ' ' + str(self.seafarerSubmarine))
        if self.seafarerOceanShips >= 0: print('Seafarer (Ocean Ships)' + ' ' + str(self.seafarerOceanShips))
        if self.seafarerMotorboats >= 0: print('Seafarer (Motorboats)' + ' ' + str(self.seafarerMotorboats))

        if self.sensors >= 0: print('Sensors' + ' ' + str(self.sensors))
        if self.stealth >= 0: print('Stealth' + ' ' + str(self.stealth))
        if self.steward >= 0: print('Admin' + ' ' + str(self.admin))
        if self.streetwise >= 0: print('Streetwise' + ' ' + str(self.streetwise))
        if self.survival >= 0: print('Survival' + ' ' + str(self.survival))

        if self.tactics >= 0: print('Tactics' + ' ' + str(self.tactics))
        if self.tacticsMilitary >= 0: print('Tactics (Military)' + ' ' + str(self.tacticsMilitary))
        if self.tacticsNaval >= 0: print('Tactics (Naval)' + ' ' + str(self.tacticsNaval))

        if self.trade >= 0: print('Trade' + ' ' + str(self.trade))
        if self.tradeBiologicals >= 0: print('Trade (Biologicals)' + ' ' + str(self.tradeBiologicals))
        if self.tradeCivilEngineering >= 0: print('Trade (Civil Engineering)' + ' ' + str(self.tradeCivilEngineering))
        if self.tradeSpaceConstruction >= 0: print(
            'Trade (Space Construction)' + ' ' + str(self.tradeSpaceConstruction))
        if self.tradeHydroponics >= 0: print('Trade (Hydroponics)' + ' ' + str(self.tradeHydroponics))
        if self.tradePolymers >= 0: print('Trade (Polymers)' + ' ' + str(self.tradePolymers))

        if self.vaccSuit >= 0: print('Vacc Suit' + ' ' + str(self.vaccSuit))
        if self.zeroG >= 0: print('Zero-G' + ' ' + str(self.zeroG))


# II. CHARACTER

def charMod(score):  # Returns Characteristic (Ability Score) Modifier
    if score == 0: return -3
    if score == 1 or score == 2: return -2
    if score >= 3 and score <= 5: return -1
    if score >= 6 and score <= 8: return 0
    if score >= 9 and score <= 11: return 1
    if score >= 12 and score <= 14: return 2
    if score >= 15: return 3


def generateName():
    first_names = ['John', 'Steven', 'Mark', 'Caitlyn', 'Stella', 'Jessica', 'James', 'Robert', 'Michael', 'David',
                   'William', 'Richard', 'Joseph', 'Thomas', 'Christopher', 'Calvin', 'Mary', 'Patricia',
                   'Jennifer',
                   'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Sarah', 'Karen']
    middle_initial = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    last_names = ['Toast', 'Rock', 'Pan', 'Bell', 'Camp', 'Waterfall', 'Safe', 'Canteen', 'Wheel', 'Time', 'Year',
                  'Man', 'Thing', 'Woman', 'Child', 'State', 'Hand', 'Case', 'Program', 'Money']
    return random.choice(first_names) + ' ' + random.choice(middle_initial) + '. ' + random.choice(last_names)


class travellerCharacter():
    def __init__(self):
        self.name = 'nameErr'
        self.str = 0
        self.dex = 0
        self.end = 0
        self.int = 0
        self.edu = 0
        self.soc = 0
        self.homeworld = 'homeworldErr'
        self.skills = 'skillsErr'
        self.career = 'careerErr'
        self.age = 16 + d(2, 6, 0)
        self.terms = 0

    def rollCharacteristics(self):
        self.str = d(2, 6, 0)
        self.dex = d(2, 6, 0)
        self.end = d(2, 6, 0)
        self.int = d(2, 6, 0)
        self.edu = d(2, 6, 0)
        self.soc = d(2, 6, 0)

    def generate(self, homeworld, skills, career):
        self.name = generateName()
        # self.rollCharacteristics()
        self.homeworld = homeworld
        self.skills = skills
        self.skills.homeworldSkills(self.homeworld)
        self.skills.educationSkills(self)
        self.career = career
        self.career.basicTraining(self)
        while self.career.died == False:
            self.career.termSkills(self)
            self.career.surviveAdvance(self)

    def dossier(self):

        if self.career.rank[1] == 'Nobody':
            print(self.name)
        else:
            print(self.career.rank[1] + ' ' + self.name)

        print(str(self.age) + ' y/o ' + self.career.specialization + ' (Rank ' + str(self.career.rank[0]) + ')')
        print('STR ' + str(self.str))
        print('DEX ' + str(self.dex))
        print('END ' + str(self.end))
        print('INT ' + str(self.int))
        print('EDU ' + str(self.edu))
        print('SOC ' + str(self.soc))
        print(self.homeworld.codes)
        self.skills.print()


# III. CAREER

class career():
    def __init__(self, character, career, specialization, term):
        self.terms = 0
        self.died = False
        self.career = career
        self.specialization = specialization
        if career == 'Random':
            self.career = random.choice(['Army', 'Drifter'])

        if career == 'Draft':
            x = random.randint(1, 4)
            y = d(2, 6, 0)
            if x == 1 and y + character.int >= 6:
                self.career = 'Navy'
                self.specialization = 'Random'
            if x == 2 and y + charMod(character.end) >= 5:
                self.career = 'Army'
                self.specialization = 'Random'
            if x == 3 and y + character.end >= 6:
                self.career = 'Marines'
                self.specialization = 'Random'
            if x == 4 and y + character.int >= 4:
                self.career = 'Merchants'
                self.specialization = 'Merchant Marine'


            if x == 5 and y + character.int >= 5:
                self.career = 'Scouts'
                self.specialization = 'Random'
            if x == 6 and y + character.int >= 6:
                self.career = 'Agent'
                self.specialization = 'Law Enforcement'
            if self.career == 'Draft':
                self.career = 'Drifter'
                self.specialization = 'Random'


        self.personalDevelopment = 'personalDevelopmentErr'
        self.serviceSkills = 'serviceSkillsErr'
        self.advancedEducation = 'advancedEducationErr'
        self.officerSkills = 'officerSkillsErr'
        self.specialistSkills = 'specialistSkillsErr'
        self.qualification = ['abilityErr', 0]
        self.survival = ['abilityErr', 0]
        self.advancement = ['abilityErr', 0]
        self.benefits = [[0, 'benefitErr'],
                         [0, 'benefitErr'],
                         [0, 'benefitErr'],
                         [0, 'benefitErr'],
                         [0, 'benefitErr'],
                         [0, 'benefitErr'],
                         [0, 'benefitErr']]
        self.rank = [0, 'Nobody']
        self.ranks = [['rankTitleErr', 'benefitErr'],
                      ['rankTitleErr', 'benefitErr'],
                      ['rankTitleErr', 'benefitErr'],
                      ['rankTitleErr', 'benefitErr'],
                      ['rankTitleErr', 'benefitErr'],
                      ['rankTitleErr', 'benefitErr'],
                      ['rankTitleErr', 'benefitErr']]
        self.officerRanks = [['rankTitleErr', 'benefitErr'],
                             ['rankTitleErr', 'benefitErr'],
                             ['rankTitleErr', 'benefitErr'],
                             ['rankTitleErr', 'benefitErr'],
                             ['rankTitleErr', 'benefitErr'],
                             ['rankTitleErr', 'benefitErr'],
                             ['rankTitleErr', 'benefitErr']]
        self.commission = ['abilityErr', 0]
        self.commissioned = False

        if self.career == 'Army':
            self.rank = [0, 'armyRankErr']
            self.commission = ['SOC', 8]
            self.qualification = ['END', 5]
            self.personalDevelopment = ['+1 STR', '+1 DEX', '+1 END', 'Gambler', 'Medic', 'Melee (Unarmed)']
            self.serviceSkills = ['Drive (Any)', 'Athletics (Any)', 'Gun Combat (Any)', 'Recon', 'Melee (Any)',
                                  'Heavy Weapons (Any)']
            self.advancedEducation = ['Comms', 'Sensors', 'Navigation', 'Explosives', 'Engineer (Any)', 'Survival']
            self.officerSkills = ['Tactics (Military)', 'Leadership', 'Advocate', 'Diplomat', 'Tactics (Military',
                                  'Admin']
            self.benefits = [[2000, 'Combat Implant'],
                             [5000, '+1 INT'],
                             [10000, '+1 EDU'],
                             [10000, 'Weapon'],
                             [10000, 'Armor'],
                             [20000, 'Combat Implant or +! END'],
                             [30000, 'q+1 SOC']]
            if self.specialization == 'Random':
                self.specialization = random.choice(['Support', 'Infantry', 'Cavalry'])

            if self.specialization == 'Support':
                self.survival = ['END', 5]
                self.advancement = ['EDU', 7]
                self.specialistSkills = ['Mechanic', 'Drive (Any)', 'Flyer (Any)', 'Explosives', 'Comms', 'Medic']

            if self.specialization == 'Infantry':
                self.survival = ['STR', 6]
                self.advancement = ['EDU', 6]
                self.specialistSkills = ['Gun Combat (Any)', 'Melee (Any)', 'Heavy Weapons (Any)', 'Stealth',
                                         'Athletics (Any)', 'Recon']

            if self.specialization == 'Cavalry':
                self.survival = ['DEX', 7]
                self.advancement = ['INT', 5]
                self.specialistSkills = ['Mechanic', 'Drive (Any)', 'Flyer (Any)', 'Recon', 'Gunner (Any)', 'Sensors']

            self.ranks = [['Private', 'Gun Combat (Slug or Energy Rifle) 1'],
                          ['Lance Corporal', 'Recon', 1],
                          ['Corporal', ''],
                          ['Lance Sergeant', 'Leadership', 1],
                          ['Sergeant', ''],
                          ['Gunnery Sergeant', ''],
                          ['Sergeant Major', '']]
            self.officerRanks = [['OFFICER RANK 0 ERROR', 'X'],
                                 ['Lieutenant', 'Leadership', 1],
                                 ['Captain', ''],
                                 ['Major', 'Tactics (Military)', 1],
                                 ['Lieutenant Colonel', ''],
                                 ['Colonel', ''],
                                 ['General', '+1 SOC']]  # or SOC to 10

        if self.career == 'Drifter':
            self.personalDevelopment = ['+1 STR', '+1 END', '+1 DEX', 'Jack of all Trades', '+1 END', '+1 INT']
            self.serviceSkills = ['Athletics (Any)', 'Melee (Unarmed)', 'Recon', 'Streetwise', 'Stealth', 'Survival']
            self.benefits = [[0, 'Contact'],
                             [0, 'Weapon'],
                             [1000, 'Ally'],
                             [2000, 'Weapon'],
                             [3000, '+1 EDU'],
                             [4000, 'Ship Share'],
                             [8000, '2 Ship Shares']]
            if self.specialization == 'Random':
                self.specialization = random.choice(['Barbarian', 'Wanderer', 'Scavenger'])
            if self.specialization == 'Barbarian':
                self.survival = ['END', 7]
                self.advancement = ['STR', 7]
                self.specialistSkills = ['Animals (Any)', 'Carouse', 'Melee (Blade)', 'Stealth', 'Seafarer (Any)',
                                         'Survival']
                self.ranks = [['Nobody', ''],
                              ['Nobody', 'Survival 1'],
                              ['Warrior', 'Melee (Blade) 1'],
                              ['Warrior', ''],
                              ['Chieftain', 'Leadership 1'],
                              ['Chieftain', ''],
                              ['Chieftain', '']]
            if self.specialization == 'Wanderer':
                self.survival = ['END', 7]
                self.advancement = ['INT', 7]
                self.specialistSkills = ['Athletics (Any)', 'Deception', 'Recon', 'Stealth', 'Streetwise', 'Survival']
                self.ranks = [['Nobody', ''],
                              ['Nobody', 'Streetwise 1'],
                              ['Nobody', ''],
                              ['Nobody', 'Deception 1'],
                              ['Nobody', ''],
                              ['Nobody', ''],
                              ['Nobody', '']]
            if self.specialization == 'Scavenger':
                self.survival = ['DEX', 7]
                self.advancement = ['END', 7]
                self.specialistSkills = ['Pilot (Small Craft)', 'Mechanic', 'Astrogation', 'Vacc Suit', 'Zero-G',
                                         'Gun Combat (Any)']
                self.ranks = [['Nobody', ''],
                              ['Nobody', 'Vacc Suit 1'],
                              ['Nobody', ''],
                              ['Nobody', 'Trade (Belter) or Mechanic 1'],
                              ['Nobody', ''],
                              ['Nobody', ''],
                              ['Nobody', '']]

        if self.career == 'Marines':
            self.rank = [0, 'marinesRankErr']
            self.commission = ['SOC', 8]
            self.qualification = ['END', 6]
            self.personalDevelopment = ['+1 STR', '+1 DEX', '+1 END', 'Gambler', 'Melee (Unarmed)', 'Melee(Blade)']
            self.serviceSkills = ['Athletics (Any)', 'Battle Dress', 'Tactics (Any)', 'Heavy Weapons (Any)', 'Gun Combat (Any)', 'Stealth']
            self.advancedEducation = ['Medic', 'Survival', 'Explosives', 'Engineer (Any)', 'Pilot (Any)',
                                      'Medic']
            self.officerSkills = ['Leadership', 'Tactics (Any)', 'Admin', 'Advocate', 'Battle Dress',
                                  'Leadership']
            self.benefits = [[2000, 'Armor'],
                             [5000, '+1 INT'],
                             [5000, '+1 EDU'],
                             [10000, 'Weapon'],
                             [20000, 'TAS Membership'],
                             [30000, "+1 END"], # or armor
                             [40000, '+1 SOC']] # actually +2
            if self.specialization == 'Random':
                self.specialization = random.choice(['Support', 'Star Marines', 'Ground Assault'])

            if self.specialization == 'Support':
                self.survival = ['END', 5]
                self.advancement = ['EDU', 7]
                decidedSkill = random.choice(['Drive (Any)','Flyer (Any)'])
                self.specialistSkills = ['Comms', 'Mechanic', decidedSkill, 'Medic', 'Heavy Weapons (Any)', 'Gun Combat (Any)']

            if self.specialization == 'Star Marines':
                self.survival = ['END', 6]
                self.advancement = ['EDU', 6]
                self.specialistSkills = ['Battle Dress', 'Zero-G', 'Gunner (Any)', 'Melee (Blade)', 'Sensors',
                                         'Gun Combat (Any)']

            if self.specialization == 'Ground Assault':
                self.survival = ['END', 7]
                self.advancement = ['EDU', 5]
                self.specialistSkills = ['Battle Dress', 'Heavy Weapons (Any)', 'Recon', 'Melee (Blade)',
                                         'Tactics (Military)', 'Gun Combat (Any)']

            marineRankBenefit = random.choice(['Melee (Blade)','Gun Combat (Any)'])
            self.ranks = [['Marine', marineRankBenefit],
                          ['Lance Corporal', 'Gun Combat (Any)', 1],
                          ['Corporal', 'X', 1],
                          ['Lance Sergeant', 'Leadership'],
                          ['Sergeant', 'x'],
                          ['Gunnery Sergeant', '+1 END'],
                          ['Sergeant Major', 'X']]
            self.officerRanks = [['OFFICER RANK 0 ERROR', 'X'],
                                 ['Lieutenant', 'Leadership', 1],
                                 ['Captain', 'x', 1],
                                 ['Force Commander', 'Tactics (Any)', 1],
                                 ['Lieutenant Colonel', 'x', 1],
                                 ['Colonel', '+1 SOC'],  # or SOC to 10
                                 ['Brigadier', 'X']]

        if self.career == 'Merchants':
            self.rank = [0, 'merchantsRankErr']

            # no commission
            self.commission = ['SOC',8]
            self.qualification = ['INT', 4]
            self.personalDevelopment = ['+1 STR', '+1 DEX', '+1 END', '+1 INT', 'Streetwise', 'Melee(Blade)']
            self.serviceSkills = ['Drive (Any)', 'Vacc Suit', 'Broker', 'Steward', 'Comms', 'Persuade']
            self.advancedEducation = ['Social Science (Any)', 'Astrogation', 'Computers', 'Pilot (Any)', 'Admin',
                                      'Advocate']
            self.benefits = [[1000, 'Blade'],
                             [5000, '+1 INT'],
                             [10000, '+1 EDU'],
                             [20000, 'Gun'],
                             [20000, 'Ship Share'],
                             [40000, "Free Trader"],
                             [40000, 'Free Trader']]

            if self.specialization == 'Random':
                self.specialization = random.choice(['Merchant Marine', 'Free Trader', 'Broker'])

            if self.specialization == 'Merchant Marine':
                merchantMarineSkill = random.choice(['Pilot (Spacecraft)','Pilot (Capital Ships)'])
                self.survival = ['EDU', 5]
                self.advancement = ['INT', 7]
                self.specialistSkills = [merchantMarineSkill, 'Vacc Suit', 'Zero-G', 'Mechanic', 'Engineer (Any)', 'Gunner (Any)']
                self.ranks = [['Crewman', 'X'],
                              ['Senior Crewman', 'Mechanic', 1],
                              ['4th Officer', 'X', 1],
                              ['3rd Officer', 'X'],
                              ['2nd Officer', 'Pilot (Any)'],
                              ['1st Officer', '+1 SOC'],
                              ['Captain', 'X']]

            if self.specialization == 'Free Trader':
                self.survival = ['DEX', 6]
                self.advancement = ['INT', 6]
                self.specialistSkills = ['Pilot (Spacecraft)', 'Vacc Suit', 'Zero-G', 'Mechanic', 'Engineer (Any)',
                                         'Sensors']
                self.ranks = [['Trader', 'X'],
                              ['Trader', 'Persuade', 1],
                              ['Trader', 'X', 1],
                              ['Experienced Trader', 'Jack of all Trades'],
                              ['Experienced Trader', 'X'],
                              ['Experienced Trader', 'X'],
                              ['Experienced Trader', 'X']]

            if self.specialization == 'Broker':
                self.survival = ['EDU', 7]
                self.advancement = ['INT', 5]
                self.specialistSkills = ['Admin', 'Advocate', 'Broker', 'Streetwise',
                                         'Deception', 'Persuade']
                self.ranks = [['Broker', 'X'],
                              ['Broker', 'Broker', 1],
                              ['Broker', 'X', 1],
                              ['Experienced Broker', 'Streetwise'],
                              ['Experienced Broker', 'X'],
                              ['Experienced Broker', 'X'],
                              ['Experienced Broker', 'X']]



        if self.career == 'Navy':
            self.rank = [0, 'navyRankErr']
            self.commission = ['SOC', 8]
            self.qualification = ['INT', 5]
            self.personalDevelopment = ['+1 STR', '+1 DEX', '+1 END', '+1 INT', '+1 EDU', '+1 SOC']
            self.serviceSkills = ['Pilot (Any)', 'Vacc Suit', 'Zero-G', 'Gunner (Any)', 'Mechanic', 'Gun Combat (Any)']
            self.advancedEducation = ['Remote Operations', 'Astrogation', 'Engineer (Any)', 'Computers', 'Navigation',
                                      'Admin']
            self.officerSkills = ['Leadership', 'Tactics (Naval)', 'Pilot (Any)', 'Melee (Blade)', 'Admin',
                                  'Tactics (Naval)']
            self.benefits = [[1000, 'Air/Raft or 1 Ship Share'],
                             [5000, '+1 INT'],
                             [5000, '+1 EDU'],  # or two ship shares
                             [10000, 'Weapon'],
                             [20000, 'TAS Membership'],
                             [50000, "Ship's Boat or 2 Ship Shares"],
                             [50000, '+1 SOC']]
            if self.specialization == 'Random':
                self.specialization = random.choice(['Line/Crew', 'Eng/Gun', 'Flight'])

            if self.specialization == 'Line/Crew':
                self.survival = ['INT', 5]
                self.advancement = ['EDU', 7]
                self.specialistSkills = ['Comms', 'Mechanic', 'Gun Combat (Any)', 'Sensors', 'Melee (Any)', 'Vacc Suit']

            if self.specialization == 'Eng/Gun':
                self.survival = ['INT', 6]
                self.advancement = ['EDU', 6]
                self.specialistSkills = ['Engineer (Any)', 'Mechanic', 'Sensors', 'Engineer (Any)', 'Gunner (Any)',
                                         'Computers']

            if self.specialization == 'Flight':
                self.survival = ['DEX', 7]
                self.advancement = ['EDU', 5]
                self.specialistSkills = ['Pilot (Any)', 'Flyer (Any)', 'Gunner (Any)', 'Pilot (Small Craft)',
                                         'Astrogation', 'Zero-G']

            self.ranks = [['Crewman', 'X'],
                          ['Able Spacehand', 'Mechanic', 1],
                          ['Petty Officer, 3rd Class', 'Vacc Suit', 1],
                          ['Petty Officer, 2nd Class', ''],
                          ['Petty Officer, 3rd Class', '+1 END'],
                          ['Chief Petty Officer', 'X'],
                          ['Master Chief', 'X']]
            self.officerRanks = [['OFFICER RANK 0 ERROR', 'X'],
                                 ['Ensign', 'Melee', 1],
                                 ['Sublieutenant', 'Leadership', 1],
                                 ['Lieutenant', 'X', 1],
                                 ['Commander', 'Tactics (Naval)', 1],
                                 ['Captain', '+1 SOC'],  # or SOC to 10
                                 ['Admiral', '+1 SOC']]  # or SOC to 12

        self.rank[1] = self.ranks[0][0]

    def basicTraining(self, character):
        if self.career == 'Army' or self.career == 'Navy':
            for i in range(len(self.serviceSkills)):
                character.skills.train(character, self.serviceSkills[i], 0)
        if self.career == 'Drifter':
            for i in range(len(self.specialistSkills)):
                character.skills.train(character, self.specialistSkills[i], 0)

    def termSkills(self, character):  # doesnt always work
        if self.career == 'Army' or self.career == 'Navy':
            x = random.randint(1, 5)
            y = random.randint(0, 5)
            if x == 1:
                character.skills.train(character, self.personalDevelopment[y], -1)
            if x == 2:
                character.skills.train(character, self.serviceSkills[y], -1)
            if x == 3:
                character.skills.train(character, self.specialistSkills[y], -1)
            if x == 4 and character.edu >= 8:
                character.skills.train(character, self.advancedEducation[y], -1)
            if x == 5 and self.commissioned == True:
                character.skills.train(character, self.advancedEducation[y], -1)
            while x == 4 and character.edu < 8: x = random.randint(1, 5)
            while x == 5 and self.commissioned == False: x = random.randint(1, 5)

        if self.career == 'Drifter':
            x = random.randint(1, 3)
            y = random.randint(0, 5)
            if x == 1:
                character.skills.train(character, self.personalDevelopment[y], -1)
            if x == 2:
                character.skills.train(character, self.serviceSkills[y], -1)
            if x == 3:
                character.skills.train(character, self.specialistSkills[y], -1)

    def surviveAdvance(self, character):

        # Adds 4 Year Term Length
        character.age += 4

        # Aging Effects
        if character.age >= 34:
            x = d(2, 6, 0) - self.terms
            if x <= -5:
                character.str -= 2
                character.dex -= 2
                character.end -= 2
                if x <= -6:
                    y = d(1, 3, 0)
                    if y == 1: character.int -= 1
                    if y == 2: character.edu -= 1
                    if y == 3: character.soc -= 1
            if x == -4:
                physicalChars = ['STR', 'DEX', 'INT']
                for i in range(2):
                    char = random.choice(physicalChars)
                    physicalChars.remove(char)
                    if char == 'STR': character.str -= 2
                    if char == 'DEX': character.dex -= 2
                    if char == 'END': character.end -= 2
                if physicalChars[0] == 'STR': character.str -= 1
                if physicalChars[0] == 'DEX': character.dex -= 1
                if physicalChars[0] == 'END': character.end -= 1
            if x == -3:
                physicalChars = ['STR', 'DEX', 'INT']
                char = random.choice(physicalChars)
                physicalChars.remove(char)
                if char == 'STR': character.str -= 2
                if char == 'DEX': character.dex -= 2
                if char == 'END': character.end -= 2
                for i in range(len(physicalChars)):
                    if physicalChars[i] == 'STR': character.str -= 1
                    if physicalChars[i] == 'DEX': character.dex -= 1
                    if physicalChars[i] == 'END': character.end -= 1
            if x <= -2:
                character.str -= 1
                character.dex -= 1
                character.end -= 1
            if x == -1:
                physicalChars = ['STR', 'DEX', 'INT']
                for i in range(2):
                    char = random.choice(physicalChars)
                    physicalChars.remove(char)
                    if char == 'STR': character.str -= 1
                    if char == 'DEX': character.dex -= 1
                    if char == 'END': character.end -= 1
            if x == 0:
                y = d(1, 3, 0)
                if y == 1: character.str -= 1
                if y == 2: character.dex -= 1
                if y == 3: character.end -= 1

            if character.str < 1 or character.dex < 1 or character.end < 1 or character.int < 1 or character.edu < 1 or character.soc < 1:
                self.died = True
                print('Died of Old Age')

        if self.career == 'Army' or self.career == 'Navy' or self.career == 'Marines' or self.career == 'Merchants':
            if self.commission[0] == 'STR': commissionAbility = charMod(character.str)
            if self.commission[0] == 'DEX': commissionAbility = charMod(character.dex)
            if self.commission[0] == 'END': commissionAbility = charMod(character.end)
            if self.commission[0] == 'INT': commissionAbility = charMod(character.int)
            if self.commission[0] == 'EDU': commissionAbility = charMod(character.edu)
            if self.commission[0] == 'SOC': commissionAbility = charMod(character.soc)
            if self.commissioned == False:
                x = d(2, 6, commissionAbility)
                if x >= self.commission[1]:
                    self.commissioned = True
                    if self.rank[0] == 0:
                        self.rank = [1, 'Lance Corporal']
                    # sometimes a private will get commissioned, so technically they
                    # wouldnt be privates  anymore

        if self.survival[0] == 'STR': survivalAbility = charMod(character.str)
        if self.survival[0] == 'DEX': survivalAbility = charMod(character.dex)
        if self.survival[0] == 'END': survivalAbility = charMod(character.end)
        if self.survival[0] == 'INT': survivalAbility = charMod(character.int)
        if self.survival[0] == 'EDU': survivalAbility = charMod(character.edu)
        if self.survival[0] == 'SOC': survivalAbility = charMod(character.soc)
        if self.advancement[0] == 'STR': advancementlAbility = charMod(character.str)
        if self.advancement[0] == 'DEX': advancementlAbility = charMod(character.dex)
        if self.advancement[0] == 'END': advancementlAbility = charMod(character.end)
        if self.advancement[0] == 'INT': advancementlAbility = charMod(character.int)
        if self.advancement[0] == 'EDU': advancementlAbility = charMod(character.edu)
        if self.advancement[0] == 'SOC': advancementlAbility = charMod(character.soc)

        survivalRoll = d(2, 6, survivalAbility)
        advancementRoll = d(2, 6, advancementlAbility)
        if survivalRoll < self.survival[1] and self.died == False:
            self.died = True
            print('Died in the line of duty.')
        if survivalRoll >= self.survival[1]: self.terms += 1

        # Check to see if not dead and rolled high enough for advancement
        if advancementRoll >= self.advancement[1] and self.died == False and self.rank[0] < 6 and self.career != 'Merchants':
            self.rank[0] += 1
            n = self.rank[0]
            if n >= 6: n = 6
            if self.commissioned == False:
                self.rank[1] = self.ranks[n][0]  # list index out of range
            if self.commissioned == True:
                self.rank[1] = self.officerRanks[n][0]
            character.skills.train(character, self.ranks[self.rank[0]][1], 1)  # list index out of range


# IV. MAIN LOOP
loops = 0
while loops <= 50:
    loops += 1
    nickCarl = travellerCharacter()
    nickCarl.rollCharacteristics()
    hallowsbelt = planet()
    hallowsbelt.generateCodes()
    skillsPackage = travellerSkills()
    careerPackage = career(nickCarl, 'Draft', 'Random', 0)
    nickCarl.generate(hallowsbelt, skillsPackage, careerPackage)
    nickCarl.dossier()

    print()