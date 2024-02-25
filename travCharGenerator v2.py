# Traveller Character Generator v2 (2024-02-16)

# Part 1: Setup
# Imports, dice rolls, and planet skeleton code.

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


# Part 2: Skills
# The extra skill classes are more trouble than they are worth. . .

class animalSkills():
    def __init__(self):
        self.riding = -3
        self.vet = -3
        self.training = -3
        self.farming = -3


class athleticSkills():
    def __init__(self):
        self.coordination = -3
        self.endurance = -3
        self.strength = -3
        self.flying = -3


class artSkills():
    def __init__(self):
        self.acting = -3
        self.dance = -3
        self.holography = -3
        self.instrument = -3  # Can extrapolate into instrument subclass
        self.sculpting = -3
        self.writing = -3


class driveSkills():
    def __init__(self):
        self.mole = -3
        self.tracked = -3
        self.wheeled = -3


class engineerSkills():
    def __init__(self):
        self.mDrive = -3
        self.jDrive = -3
        self.electronics = -3
        self.lifeSupport = -3
        self.power = -3


class flyerSkills():
    def __init__(self):
        self.grav = -3
        self.rotor = -3
        self.wing = -3


class gunSkills():
    def __init__(self):
        self.slugRifle = -3
        self.slugPistol = -3
        self.shotgun = -3
        self.energyRifle = -3
        self.energyPistol = -3


class heavyWeaponSkills():
    def __init__(self):
        self.launchers = -3
        self.mpa = -3
        self.fieldArtillery = -3


class meleeSkills():
    def __init__(self):
        self.unarmed = -3
        self.blade = -3
        self.bludgeon = -3
        self.natural = -3


class pilotSkills():
    def __init__(self):
        self.smallCraft = -3
        self.spacecraft = -3
        self.capitalShips = -3


class physicalSciences():
    def __init__(self):
        self.physics = -3
        self.chemistry = -3
        self.electronics = -3


class lifeSciences():
    def __init__(self):
        self.biology = -3
        self.cybernetics = -3
        self.genetics = -3
        self.psionology = -3


class socialSciences():
    def __init__(self):
        self.archeology = -3
        self.economics = -3
        self.history = -3
        self.linguistics = -3
        self.philosophy = -3
        self.sophontology = -3


class spaceSciences():
    def __init__(self):
        self.planetology = -3
        self.robotics = -3
        self.xenology = -3


class sciences():
    def __init__(self, physicalSciences, lifeSciences, socioalSciences, spaceSciences):
        self.physical = physicalSciences
        self.life = lifeSciences
        self.social = socialSciences
        self.space = spaceSciences,


class tacticSkills():
    def __init__(self):
        self.military = -3
        self.naval = -3


class tradeSkills():
    def __init__(self):
        self.biologicals = -3
        self.civilEngineering = -3
        self.spaceConstruction = -3
        self.hydroponics = -3
        self.polymers = -3


# Math for travellerSkills.train()
# Positive to make AT LEAST num
# Negative to ADD TO skill
def skillCalc(skill, num):
    x = skill
    if x == -3: x = 0
    if num <= -1: x += (num * -1)
    if num > -1: x = num
    if skill >= num: x = skill
    return x


class travellerSkills():
    def __init__(self, skillPackages):
        self.admin = -3
        self.advocate = -3
        self.animals = -3
        self.animalSkills = skillPackages[0]
        self.athletics = -3
        self.athleticSkills = skillPackages[1]
        self.art = -3
        self.artSkills = skillPackages[2]
        self.astrogation = -3
        self.battleDress = -3
        self.broker = -3
        self.carouse = -3
        self.comms = -3
        self.computers = -3
        self.deception = -3
        self.diplomat = -3
        self.drive = -3
        self.driveSkills = skillPackages[3]
        self.engineer = -3
        self.engineerSkills = skillPackages[4]
        self.explosives = -3
        self.flyer = -3
        self.flyerSkills = skillPackages[5]
        self.gambler = -3
        self.gunCombat = -3
        self.gunSkills = skillPackages[6]
        self.heavyWeapons = -3
        self.heavyWeaponSkills = skillPackages[7]
        self.investigate = -3
        self.jackOfAllTrades = -3
        self.language = -3  # must be extrapolated
        self.leadership = -3
        self.mechanic = -3
        self.medic = -3
        self.melee = -3
        self.meleeSkills = skillPackages[8]
        self.navigation = -3
        self.persuade = -3
        self.pilot = -3
        self.pilotSkills = skillPackages[9]
        self.recon = -3
        self.remoteOperation = -3
        self.sciences = skillPackages[10]
        self.sensors = -3
        self.stealth = -3
        self.steward = -3
        self.streetwise = -3
        self.survival = -3
        self.tactics = -3
        self.tacticSkills = skillPackages[11]
        self.trade = -3
        self.tradeSkills = skillPackages[12]
        self.vaccSuit = -3
        self.zeroG = -3

    def train(self, character, skillString, num):

        # Ability Score Additions
        if skill == 'STR': character.str = skillCalc(character.str, num)
        if skill == 'DEX': character.str = skillCalc(character.str, num)
        if skill == 'CON': character.str = skillCalc(character.str, num)
        if skill == 'INT': character.str = skillCalc(character.str, num)
        if skill == 'WIS': character.str = skillCalc(character.str, num)
        if skill == 'CHA': character.str = skillCalc(character.str, num)

        # Skill Training Additions
        if skill == 'Admin': self.admin = skillCalc(self.admin, num)
        if skill == 'Advocate': self.advocate = skillCalc(self.advocate, num)

        # Animals
        if skill == 'Animals (Any)':
            if self.animals == -3: skill = 'Animals'
            if self.animals > -3:
                skill = random.choice(['Animals',
                                       'Animals (Riding)',
                                       'Animals (Vet)',
                                       'Animals (Training)',
                                       'Animals (Farming)'])
        if skill == 'Animals': self.animals = skillCalc(self.animals, num)
        if skill == 'Animals (Riding)': self.animalSkills.riding = skillCalc(self.animalSkills.riding, num)
        if skill == 'Animals (Vet)': self.animalSkills.vet = skillCalc(self.animalSkills.riding, num)
        if skill == 'Animals (Training)': self.animalSkills.training = skillCalc(self.animalSkills.riding, num)
        if skill == 'Animals (Farming)': self.animalSkills.farming = skillCalc(self.animalSkills.riding, num)

        # Art
        if skill == 'Art (Any)':
            if self.art == -3: skill = 'Art'
            if self.art > -3:
                skill = random.choice(['Art',
                                       'Art (Acting)',
                                       'Art (Dance)',
                                       'Art (Holography)',
                                       'Art (Instrument)',
                                       'Art (Sculpting)',
                                       'Art (Writing)'])
        if skill == 'Art': self.art = skillCalc(self.animals, num)
        if skill == 'Art (Acting)': self.artSkills.acting = skillCalc(self.artSkills.acting, num)
        if skill == 'Art (Dance)': self.artSkills.dance = skillCalc(self.artSkills.dance, num)
        if skill == 'Art (Holography)': self.artSkills.holography = skillCalc(self.artSkills.holography, num)
        if skill == 'Art (Instrument)': self.artSkills.instrument = skillCalc(self.artSkills.instrument, num)
        if skill == 'Art (Sculpting)': self.artSkills.sculpting = skillCalc(self.artSkills.sculpting, num)
        if skill == 'Art (Writing)': self.artSkills.writing = skillCalc(self.artSkills.writing, num)

        if skill == 'Astrogation': self.astrogation = skillCalc(self.astrogation, num)

        # Athletics
        if skill == 'Athletics (Any)':
            if self.athletics == -3: skill = 'Athletics'
            if self.athletics > -3:
                skill = random.choice(['Athletics',
                                       'Athletics (Coordination)',
                                       'Athletics (Endurance)',
                                       'Athletics (Strength)',
                                       'Athletics (Flying)'])
        if skill == 'Athletics': self.athletics = skillCalc(self.athletics, num)
        if skill == 'Athletics (Coordination)': self.athleticSkills.coordination = skillCalc(
            self.athleticSkills.coordination, num)
        if skill == 'Athletics (Endurance)': self.athleticSkills.endurance = skillCalc(self.athleticSkills.endurance,
                                                                                       num)
        if skill == 'Athletics (Strength)': self.athleticSkills.strength = skillCalc(self.athleticSkills.strength, num)
        if skill == 'Athletics (Flying)': self.athleticSkills.flying = skillCalc(self.athleticSkills.flying, num)


# Returns a list of all skills at -3
def setupTravellerSkills():
    animalSkillPackage = animalSkills()
    athleticSkillPackage = athleticSkills()
    artSkillPackage = artSkills()
    driveSkillPackage = driveSkills()
    engineerSkillPackage = engineerSkills()
    flyerSkillPackage = flyerSkills()
    gunSkillPackage = gunSkills()
    heavyWeaponSkillPackage = heavyWeaponSkills()
    meleeSkillPackage = meleeSkills()
    pilotSkillPackage = pilotSkills()
    physicalSciencesPackage = physicalSciences()
    lifeSciencesPackage = lifeSciences()
    socialSciencesPackage = socialSciences()
    spaceSciencesPackage = spaceSciences()
    sciencePackage = sciences(physicalSciencesPackage, lifeSciencesPackage,
                              socialSciencesPackage, spaceSciencesPackage)
    tacticSkillPackage = tacticSkills()
    tradeSkillPackage = tradeSkills()
    return [animalSkillPackage, athleticSkillPackage, artSkillPackage,
            driveSkillPackage, gunSkillPackage, engineerSkillPackage,
            flyerSkillPackage, heavyWeaponSkillPackage,
            meleeSkillPackage, pilotSkillPackage, sciencePackage,
            tacticSkillPackage, tradeSkillPackage]


# 3. Character

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
        self.homeworldSkills = []
        self.educationSkills = []
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

    # Skills from Homeworld
    def homeworldSkills(self, homeworld):
        if 'Ag' in homeworld.codes or 'Ga' in homeworld.codes or 'Po' in homeworld.codes: self.skills.train(self,
                                                                                                            'Animals',
                                                                                                            0)
        if 'As' in homeworld.codes: self.skills.train(self, 'Zero-G', 0)
        if 'De' in homeworld.codes or 'Lt' in homeworld.codes: self.skills.train(self, 'Survival', 0)
        if 'Fl' in homeworld.codes or 'Wa' in homeworld.codes: self.skills.train(self, 'Seafarer (Any)', 0)
        if 'Ht' in homeworld.codes: self.skills.train(self, 'Computer', 0)
        if 'Hi' in homeworld.codes: self.skills.train(self, 'Streetwise', 0)
        if 'IC' in homeworld.codes or 'Va' in homeworld.codes: self.skills.train(self, 'Vacc Suit', 0)
        if 'In' in homeworld.codes: self.skills.train(self, 'Trade (Any)', 0)
        if 'Ri' in homeworld.codes: self.skills.train(self, 'Carouse', 0)

    def educationSkills(self):
        studies = ['Admin', 'Advocate', 'Art (Any)', 'Carouse', 'Comms', 'Computers',
                   'Drive (Any)', 'Engineer (Any)', 'Language', 'Medic', 'Physical Science (Any)',
                   'Social Science (Any)', 'Space Science (Any)', 'Trade (Any)']
        eduSkillNum = 3 + charMod(character.edu)
        for i in range(eduSkillNum):
            skill = random.choice(studies)
            studies.remove(skill)
            self.skills.train(self, skill, 0)

    def generate(self, homeworld, skills, career):
        self.name = generateName()
        self.rollCharacteristics()
        self.homeworld = homeworld
        self.skills = skills
        self.skills.homeworldSkills(homeworld)
        self.skills.educationSkills()

    def dossier(self):
        print(self.name)
        print(self.str)


# 4. Career


# 5. Main Loop

# travellerSkills() Setup
skillPackage = travellerSkills(setupTravellerSkills())
hallowsbelt = planet()
hallowsbelt.generateCodes()
nickCarl = travellerCharacter()
nickCarl.generate(hallowsbelt, skillPackage, 'careerErr')

