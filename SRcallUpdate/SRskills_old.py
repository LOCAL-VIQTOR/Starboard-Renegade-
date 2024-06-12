#starboardRenegadeCharacterGenerator

# Out Of Range (OOR) Fault keeps happening 1196 -cl 3/22
# Sometimes, nothing is printed at all
# Empty Range 1213 -cl 3/22

import random
from SRtools import *

class planet():
    def __init__(self):
        self.codes = []
        self.language = 'languageErr'
        self.name = 'Earth'

    def generateCodes(self):
        homeworldCodes = ['Ag', 'As', 'De', 'Fl', 'Ga', 'Ht', 'Hi', 'IC', 'In', 'Lt', 'Po', 'Ri', 'Wa', 'Va']
        for i in range(len(homeworldCodes)):
            x = random.randint(1, 10)
            if x == 1: self.codes.append(homeworldCodes[i])

def skillCalc(skill, num):
    x = skill
    if x == -3: x = 0               # Set to 0 if at -3 for Traveller
    if num <= -1: x += (num * -1)   # If num < 0, add abs. value of num
    if num > -1: x = num            # If num > 0, set skill to num
    if skill >= x: x = skill        # If skill already greater, leave it
    return x                        # Return for skill setting

def returnEthnics():
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
    ethnicities = [anglo_american, african, japanese_korean, central_european_soviet, pacific_islander,
                   chinese_southeast_asian, future_punk, hispanic_american, central_south_american, european]
    ethnicity = random.choice(ethnicities)
    if ethnicity == anglo_american:
        ethnicity = 'Anglo-American'
        language = random.choice(anglo_american)
    if ethnicity == african:
        ethnicity = 'African'
        language = random.choice(african)
    if ethnicity == japanese_korean:
        ethnicity = 'Japanese/Korean'
        language = random.choice(japanese_korean)
    if ethnicity == central_european_soviet:
        ethnicity = 'Central European/Soviet'
        language = random.choice(central_european_soviet)
    if ethnicity == pacific_islander:
        ethnicity = 'Pacific Islander'
        language = random.choice(pacific_islander)
    if ethnicity == chinese_southeast_asian:
        ethnicity = 'Chinese/Southeast Asian'
        language = random.choice(chinese_southeast_asian)
    if ethnicity == future_punk:
        ethnicity = 'Future-Punk'
        language = random.choice(future_punk)
    if ethnicity == hispanic_american:
        ethnicity = 'Hispanic American'
        language = random.choice(hispanic_american)
    if ethnicity == central_south_american:
        ethnicity = 'Central/South American'
        language = random.choice(central_south_american)
    if ethnicity == european:
        ethnicity = 'European'
        language = random.choice(european)
    return [ethnicity,language]
    

class skills():
    def __init__(self,character):
        if character.ttrpg == 'Cyberpunk':
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

            self.befriendedPolice = False
            self.befriendedNomad = False
            self.befriendedGang = False
            self.executiveFavor = False

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

        if character.ttrpg == 'Traveller':
            self.admin = -3
            self.advocate = -3

            self.animals = -3
            self.animalRiding = -3
            self.veterinary = -3
            self.animalTraining = -3
            self.animalFarming = -3

            self.athletics = -3
            self.coordination = -3
            self.endurance = -3
            self.strength = -3
            self.flying = -3

            self.art = -3
            self.acting = -3
            self.dance = -3
            self.holography = -3
            self.instrument = -3
            self.sculpting = -3
            self.writing = -3

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
            self.mDrive = -3
            self.jDrive = -3
            self.electricalEngineer = -3
            self.lifeSupport = -3
            self.power = -3
            self.explosives = -3

            self.flyer = -3
            self.grav = -3
            self.rotor = -3
            self.wing = -3

            self.gambler = -3

            self.gunner = -3
            self.turrets = -3
            self.ortillery = -3
            self.screens = -3
            self.capitalWeapons = -3

            self.gunCombat = -3
            self.slugRifle = -3
            self.slugPistol = -3
            self.shotgun = -3
            self.energyRifle = -3
            self.energyPistol = -3

            self.heavyWeapons = -3
            self.launchers = -3
            self.MPA = -3  # man portable artillery
            self.fieldArtillery = -3

            self.investigate = -3
            self.jackOfAllTrades = -3
            self.language = -3  # must be extrapolated
            self.leadership = -3
            self.mechanic = -3
            self.medic = -3

            self.melee = -3
            self.unarmed = -3
            self.blade = -3
            self.bludgeon = -3
            self.naturalWeapon = -3

            self.navigation = -3
            self.persuade = -3

            self.pilot = -3
            self.smallCraft = -3
            self.spacecraft = -3
            self.capitalShips = -3

            self.recon = -3
            self.remoteOperation = -3

            self.physicalScience = -3
            self.physics = -3
            self.chemistry = -3
            self.electronicScience = -3

            self.lifeScience = -3
            self.biology = -3
            self.cybernetics = -3
            self.genetics = -3
            self.psionicology = -3

            self.socialScience = -3
            self.archeology = -3
            self.economics = -3
            self.history = -3
            self.linguistics = -3
            self.philosophy = -3
            self.psychology = -3
            self.sophontology = -3

            self.spaceScience = -3
            self.planetology = -3
            self.robotics = -3
            self.xenology = -3

            self.seafarer = -3
            self.sail = -3
            self.submarine = -3
            self.oceanShips = -3
            self.motorboats = -3

            self.sensors = -3
            self.stealth = -3
            self.steward = -3
            self.streetwise = -3
            self.survival = -3

            self.tactics = -3
            self.militaryTactics = -3
            self.navalTactics = -3

            self.trade = -3
            self.tradeBiologicals = -3
            self.tradeCivilEngineering = -3
            self.tradeSpaceConstruction = -3
            self.tradeHydroponics = -3
            self.tradePolymers = -3

            self.vaccSuit = -3
            self.zeroG = -3

    def train(self, character, skill, num):

        # Cyberpunk Characteristics (Ability Scores)
        if skill == 'ATTR': character.attr = skillCalc(character.attr, num)
        if skill == 'REF': character.ref[1] = skillCalc(character.ref[1], num)
        if skill == 'TECH': character.tech = skillCalc(character.tech, num)
        if skill == 'LUCK': character.luck = skillCalc(character.luck, num)
        if skill == 'EMP': character.emp[1] = skillCalc(character.emp[1], num)
        if skill == 'INT': character.int = skillCalc(character.int, num)
        if skill == 'BODY': character.body[1] = skillCalc(character.body[1], num)
        if skill == 'COOL': character.cool = skillCalc(character.cool, num)
        if skill == 'MA': character.ma = skillCalc(character.ma, num)
        # Cyberpunk Class Skills (Special Abilities)
        if skill == 'Authority': self.authority = skillCalc(self.authority,num)
        if skill == 'Charismatic Leadership': self.charismaticLeadership = skillCalc(self.charismaticLeadership,num)
        if skill == 'Combat Sense': self.combatSense = skillCalc(self.combatSense,num)
        if skill == 'Credibility': self.credibility = skillCalc(self.credibility,num)
        if skill == 'Family': self.family = skillCalc(self.family,num)
        if skill == 'Interface': self.interface = skillCalc(self.interface,num)
        if skill == 'Jury Rig': self.juryRig = skillCalc(self.juryRig,num)
        if skill == 'Medical Tech': self.medicalTech = skillCalc(self.medicalTech,num)
        if skill == 'Resources': self.resources = skillCalc(self.resources,num)
        if skill == 'Streetdeal': self.streetdeal = skillCalc(self.streetdeal,num)

        # Traveller Skills Lists
        # Animals
        if skill == 'Animals (Any)':
            if self.animals == -3: skill = 'Animals'
            if self.animals > -3:
                skill = random.choice(['Animals',
                                       'Animal Riding',
                                       'Veterinary',
                                       'Animal Training',
                                       'Animal Farming'])
        # Art
        if skill == 'Art (Any)':
            if self.art == -3: skill = 'Art'
            if self.art > -3:
                skill = random.choice(['Art',
                                       'Acting',
                                       'Dancing',
                                       'Holography',
                                       'Instrument',
                                       'Sculpting',
                                       'Writing'])
        # Athletics
        if skill == 'Athletics (Any)':
            if self.athletics == -3: skill = 'Athletics'
            if self.athletics > -3:
                skill = random.choice(['Athletics',
                                       'Coordination',
                                       'Endurance',
                                       'Strength Feat',
                                       'Flying',])

        # Cyberpunk Skill Lists
        # Martial Arts
        if skill == 'Martial Arts (Any)':
            skill = random.choice(['Aikido',
                                   'Animal Kung Fu',
                                   'Boxing',
                                   'Capoeria',
                                   'Choi Li Fut',
                                   'Judo',
                                   'Karate',
                                   'Tae Kwon Do',
                                   'Thai Kick Boxing',
                                   'Wrestling'])
        # Combat Skills
        if skill == 'Combat Skills (Any)':
            skill = random.choice(['Aikido',
                                   'Animal Kung Fu',
                                   'Boxing',
                                   'Capoeria',
                                   'Choi Li Fut',
                                   'Judo',
                                   'Karate',
                                   'Tae Kwon Do',
                                   'Thai Kick Boxing',
                                   'Wrestling'])
        ############# Technical Skills
        if skill == 'Techie Skills':
            skill = random.choice(['Aero Tech',
                                   'Vector Thrust Tech',
                                   'Cryotank',
                                   'Cyberdeck Design',
                                   'Demolitions',
                                   'Disguise',
                                   'Electronic Security',
                                   'First Aid',
                                   'Forgery',
                                   'Gyro Tech',
                                   'Paint or Draw',
                                   'Photo & Film',
                                   'Pharmaceuticals',
                                   'Pick Lock',
                                   'Pick Pocket',
                                   'Instrument',
                                   'Weaponsmith'])
        # SKILL (ANY) LISTS

        #A
        if skill == 'Accounting': self.accounting = skillCalc(self.accounting,num) # INT
        if skill == 'Acting': self.acting = skillCalc(self.acting, num) # TV; ART
        if skill == 'Admin': self.admin = skillCalc(self.admin, num) # TV
        if skill == 'Advocate': self.advocate = skillCalc(self.advocate, num) # TV
        if skill == 'Aero Tech': self.aeroTech = skillCalc(self.aeroTech,num) # TECH
        if skill == 'Aikido': self.aikido = skillCalc(self.aikido,num) # REF
        if skill == 'Animal Farming': self.animalFarming = skillCalc(self.animalFarming, num) # TV; ANIMALS
        if skill == 'Animal Kung Fu': self.animalKungFu = skillCalc(self.animalKungFu,num) # REF
        if skill == 'Animal Riding': self.animalRiding = skillCalc(self.animalRiding, num) # TV; ANIMALS
        if skill == 'Animal Training': self.animalTraining = skillCalc(self.animalTraining, num) # TV; ANIMALS
        if skill == 'Animals': self.animals = skillCalc(self.animals, num) # TV; ANIMALS
        if skill == 'Anthropology': self.anthropology = skillCalc(self.anthropology,num) # INT
        if skill == 'Archery': self.archery = skillCalc(self.archery,num) # REF
        if skill == 'Art': self.art = skillCalc(self.art, num) # TV; ART
        if skill == 'Astrogation': self.astrogation = skillCalc(self.astrogation, num) # TV
        if skill == 'Athletics': self.math = skillCalc(self.math,num) # REF
        if skill == 'Awareness/Notice': self.awarenessNotice = skillCalc(self.awarenessNotice,num) # INT
        #B
        if skill == 'Basic Tech': self.basicTech = skillCalc(self.basicTech,num) # TECH
        if skill == 'Battle Dress': self.battleDress = skillCalc(self.battleDress, num) # TV
        if skill == 'Biology': self.biology = skillCalc(self.biology,num) # INT
        if skill == 'Botany': self.botany = skillCalc(self.botany,num) # INT
        if skill == 'Boxing': self.boxing = skillCalc(self.boxing,num) # REF
        if skill == 'Brawling': self.brawling = skillCalc(self.brawling,num) # REF
        if skill == 'Broker': self.broker = skillCalc(self.broker, num) # TV
        #C
        if skill == 'Capital Weapons': self.capitalWeapons = skillCalc(self.capitalWeapons, num) # TV; GUNNER
        if skill == 'Capoeria': self.capoeria = skillCalc(self.capoeria,num) # REF
        if skill == 'Carouse': self.carouse = skillCalc(self.carouse, num) # TV
        if skill == 'Chemistry': self.chemistry = skillCalc(self.chemistry,num) # INT
        if skill == 'Choi Li Fut': self.choiLiFut = skillCalc(self.choiLiFut,num) # REF
        if skill == 'Comms': self.comms = skillCalc(self.comms, num) # TV
        if skill == 'Composition': self.composition = skillCalc(self.composition,num) # INT
        if skill == 'Computers': self.computers = skillCalc(self.computers, num) # TV
        if skill == 'Coordination': self.coordination = skillCalc(self.coordination, num) # TV; ATHLETICS
        if skill == 'Cryotank': self.cryotank = skillCalc(self.cryotank,num) # TECH
        if skill == 'Cyberdeck Design': self.cyberdeckDesign = skillCalc(self.cyberdeckDesign,num) # TECH
        if skill == 'Cyber Tech': self.cyberTech = skillCalc(self.cyberTech,num) # TECH
        #D
        if skill == 'Dancing': self.dancing = skillCalc(self.dancing,num) # REF
        if skill == 'Dance': self.dance = skillCalc(self.dance, num) # TV; ART
        if skill == 'Deception': self.deception = skillCalc(self.deception, num) # TV
        if skill == 'Demolitions': self.demolitions = skillCalc(self.demolitions,num) # TECH
        if skill == 'Diagnose Illness': self.diagnoseIllness = skillCalc(self.diagnoseIllness,num) # INT
        if skill == 'Diplomat': self.diplomat = skillCalc(self.diplomat, num) # TV
        if skill == 'Dirigible': self.dirigible = skillCalc(self.dirigible,num) # REF; PILOT
        if skill == 'Disguise': self.disguise = skillCalc(self.disguise,num) # TECH
        if skill == 'Dodge/Escape': self.dodgeEscape = skillCalc(self.dodgeEscape,num) # REF
        if skill == 'Drive': self.drive = skillCalc(self.drive, num) # TV; DRIVE
        if skill == 'Drive Mole': self.driveMole = skillCalc(self.driveMole, num) # TV; DRIVE
        if skill == 'Drive Tracked': self.driveTracked = skillCalc(self.driveTracked, num) # TV; DRIVE
        if skill == 'Drive Wheeled': self.driveWheeled = skillCalc(self.driveWheeled, num) # TV; DRIVE
        if skill == 'Driving': self.driving = skillCalc(self.driving,num) # REF
        #E
        if skill == 'Education': self.education = skillCalc(self.education,num) # INT
        if skill == 'Elcetrical Engineer': self.electricalEngineer = skillCalc(self.electricalEngineer, num) # TV; ENGINEER
        if skill == 'Electronics': self.electronics = skillCalc(self.electronics,num) # TECH
        if skill == 'Electronic Security': self.electronicSecurity = skillCalc(self.electronicSecurity,num) # TECH
        if skill == 'Endurance': self.endurance = skillCalc(self.endurance,num) # BODY
        if skill == 'Engineer': self.engineer = skillCalc(self.engineer, num) # TV; ENGINEER
        if skill == 'Expert': self.expert = skillCalc(self.expert,num) # INT
        if skill == 'Explosives': self.explosives = skillCalc(self.explosives, num) # TV
        #F
        if skill == 'Fencing': self.fencing = skillCalc(self.fencing,num) # REF
        if skill == 'First Aid': self.firstAid = skillCalc(self.firstAid,num) # TECH
        if skill == 'Fixed Wing': self.fixedWing = skillCalc(self.fixedWing,num) # REF; PILOT
            ###
        if skill == 'Wing': self.wing = skillCalc(self.wing, num) # TV; FLYER
        if skill == 'Flyer': self.flyer = skillCalc(self.flyer, num) # TV FLYER
        if skill == 'Flying': self.flying = skillCalc(self.flying, num) # TV; ATHLETICS
        if skill == 'Forgery': self.forgery = skillCalc(self.forgery,num) # TECH
        #G
        if skill == 'Gamble': self.gamble = skillCalc(self.gamble,num) # INT
        #if skill == 'Gambler': self.gambler = skillCalc(self.gambler, num) # TV
        if skill == 'Grav': self.grav = skillCalc(self.grav, num) # TV; FLYER
        if skill == 'Gun Combat': self.gunCombat = skillCalc(self.gunCombat, num) # TV; GUN COMBAT
        if skill == 'Gunner': self.gunner = skillCalc(self.gunner, num) # TV; GUNNER
        if skill == 'Gyro': self.gyro = skillCalc(self.gyro,num) # REF; PILOT
        if skill == 'Gyro Tech': self.gyroTech = skillCalc(self.gyroTech,num) # TECH
        #H
        if skill == 'Handgun': self.handgun = skillCalc(self.handgun,num) # REF
        if skill == 'Heavy Machinery': self.heavyMachinery = skillCalc(self.heavyMachinery,num) # REF
        if skill == 'Heavy Weapons': self.heavyWeapons = skillCalc(self.heavyWeapons,num) # REF
        if skill == 'Hide/Evade': self.hideEvade = skillCalc(self.hideEvade,num) # INT
        if skill == 'History': self.history = skillCalc(self.history,num) # INT
        if skill == 'Holography': self.holography = skillCalc(self.holography, num) # TV; ART
        if skill == 'Human Perception': self.humanPerception = skillCalc(self.humanPerception,num) # EMP
        #I
        if skill == 'Instrument': self.instrument = skillCalc(self.instrument,num) # TECH // TV; ART
        if skill == 'Interrogation': self.interrogation = skillCalc(self.interrogation,num) # COOL
        if skill == 'Interview': self.interview = skillCalc(self.interview,num) # EMP
        if skill == 'Indimidate': self.intimidate = skillCalc(self.intimidation,num) # COOL
        #J
        if skill == 'J-Drive': self.jDrive = skillCalc(self.jDrive, num) # TV; ENGINEER
        if skill == 'Judo': self.judo = skillCalc(self.judo,num) # REF
        #K
        if skill == 'Karate': self.karate = skillCalc(self.karate,num) # REF
        #L
        if skill == 'Language': self.language = skillCalc(self.language,num) # INT
        if skill == 'Leadership': self.leadership = skillCalc(self.leadership,num) # EMP
        if skill == 'Library Search': self.librarySearch = skillCalc(self.librarySearch,num) # INT
        if skill == 'Life Support': self.lifeSupport = skillCalc(self.lifeSupport, num) # TV; ENGINEERING
        #M
        if skill == 'M-Drive': self.mDrive = skillCalc(self.mDrive, num) # TV; ENGINEER
        if skill == 'Math': self.math = skillCalc(self.math,num) # INT
        if skill == 'Melee': self.melee = skillCalc(self.melee,num) # REF
        if skill == 'Motorcycle': self.motorcycle = skillCalc(self.motorcycle,num) # REF
        #N
        #O
        if skill == 'Oratory': self.oratory = skillCalc(self.oratory,num) # COOL
        if skill == 'Ortillery': self.ortillery = skillCalc(self.ortillery, num) # TV; GUNNER
        #P
        if skill == 'Paint or Draw': self.paintDraw = skillCalc(self.paintDraw,num) # TECH
        if skill == 'Performance': self.performance = skillCalc(self.performance,num) # EMP
        if skill == 'Personal Grooming': self.personalGrooming = skillCalc(self.personalGrooming,num) # ATTR
        if skill == 'Persuasion': self.persuasion = skillCalc(self.persuasion,num) # EMP
        if skill == 'Pick Lock': self.pickLock = skillCalc(self.rifle,num) # TECH
        if skill == 'Pick Pocket': self.pickPocket = skillCalc(self.pickLock,num) # TECH
        if skill == 'Pharmaceuticals': self.pharmaceuticals = skillCalc(self.pharmaceuticals,num) # TECH
        if skill == 'Photo & Film': self.photoFilm = skillCalc(self.photoFilm,num) # TECH
        if skill == 'Physics': self.physics = skillCalc(self.physics,num) # INT
        if skill == 'Power': self.power = skillCalc(self.power, num) # TV; ENGINEERING
        if skill == 'Programming': self.programming = skillCalc(self.programming,num) # INT
        #Q
        #R
        if skill == 'Resist Torture & Drugs': self.resistTortureDrugs = skillCalc(self.resistTortureDrugs,num) # COOL
        if skill == 'Rifle': self.rifle = skillCalc(self.rifle,num) # REF
        if skill == 'Rotor': self.rotor = skillCalc(self.rotor, num) # TV; FLYER
        #S
        if skill == 'Screens': self.screens = skillCalc(self.screens, num) # TV; GUNNER
        if skill == 'Sculpting': self.sculpting = skillCalc(self.sculpting, num) # TV; ART
        if skill == 'Seduction': self.seduction = skillCalc(self.seduction,num) # EMP
        if skill == 'Shadow/Track': self.shadowTrack = skillCalc(self.shadowTrack,num) # INT
        if skill == 'Social': self.social = skillCalc(self.social,num) # EMP
        if skill == 'Stealth': self.stealth = skillCalc(self.stealth,num) # REF
        if skill == 'Stock Market': self.stockMarket = skillCalc(self.stockMarket,num) # INT
        if skill == 'Streetwise': self.streetwise = skillCalc(self.streetwise,num) # COOL
        if skill == 'Strength': self.strength = skillCalc(self.strength, num) # TV; ATHLETICS
        if skill == 'Strength Feat': self.strengthFeat = skillCalc(self.strengthFeat,num) # BODY
        if skill == 'Submachinegun': self.submachinegun = skillCalc(self.submachinegun,num) # REF
        if skill == 'Survival': self.survival = skillCalc(self.survival,num) # INT
        if skill == 'Swimming': self.swimming = skillCalc(self.swimming,num) # BODY
        if skill == 'System Knowledge': self.systemKnowledge = skillCalc(self.systemKnowledge,num) # INT
        #T
        if skill == 'Tae Kwon Do': self.taeKwonDo = skillCalc(self.taeKwonDo,num) # REF
        if skill == 'Teaching': self.teaching = skillCalc(self.teaching,num) # INT
        if skill == 'Thai Kick Boxing': self.thaiKickBoxing = skillCalc(self.thaiKickBoxing,num) # REF
        if skill == 'Turrets': self.turrets = skillCalc(self.turrets, num) # TV; GUNNER
        #U
        #V
        if skill == 'Vector Thrust': self.vectorThrust = skillCalc(self.vectorThrust,num) # REF; PILOT
        if skill == 'Vector Thrust Tech': self.vectorThrustTech = skillCalc(self.vectorThrustTech,num) # TECH
        if skill == 'Veterinary': self.veterinary = skillCalc(self.veterinary, num) # TV; ANIMALS
        #W
        if skill == 'Wardrobe & Style': self.wardrobeStyle = skillCalc(self.wardrobeStyle,num) # ATTR
        if skill == 'Weaponsmith': self.weaponsmith = skillCalc(self.weaponsmith,num) # TECH
        if skill == 'Wrestling': self.wrestling = skillCalc(self.wrestling,num) # REF
        if skill == 'Writing': self.writing = skillCalc(self.writing, num) # TV; ART
        #X
        #Y
        #Z
        if skill == 'Zoology': self.zoology = skillCalc(self.zoology,num) # INT

        

        
        
        
        
        

        
        if skill == 'Slug Rifle': self.slugRifle = skillCalc(self.slugRifle, num)
        if skill == 'Slug Pistol': self.slugPistol = skillCalc(self.slugPistol, num)
        if skill == 'Shotgun': self.shotgun = skillCalc(self.shotgun, num)
        if skill == 'Energy Rifle': self.energyRifle = skillCalc(self.energyRifle, num)
        if skill == 'Energy Pistol': self.energyPistol = skillCalc(self.energyPistol, num)

        if skill == 'Heavy Weapons': self.heavyWeapons = skillCalc(self.heavyWeapons, num)
        if skill == 'Launchers': self.launchers = skillCalc(self.launchers, num)
        if skill == 'MPA': self.MPA = skillCalc(self.MPA, num)
        if skill == 'Field Artillery': self.fieldArtillery = skillCalc(self.fieldArtillery, num)

        if skill == 'Investigate': self.investigate = skillCalc(self.investigate, num)
        if skill == 'Jack Of All Trades': self.jackOfAllTrades = skillCalc(self.jackOfAllTrades, num)
        if skill == 'Language': self.language = skillCalc(self.language, num)
        if skill == 'Leadership': self.leadership = skillCalc(self.leadership, num)
        if skill == 'Mechanic': self.mechanic = skillCalc(self.mechanic, num)
        if skill == 'Medic': self.medic = skillCalc(self.medic, num)

        if skill == 'Melee': self.melee = skillCalc(self.melee, num)
        if skill == 'Unarmed': self.unarmed = skillCalc(self.unarmed, num)
        if skill == 'Blade': self.blade = skillCalc(self.blade, num)
        if skill == 'Bludgeon': self.bludgeon = skillCalc(self.bludgeon, num)
        if skill == 'Natural Weapon': self.naturalWeapon = skillCalc(self.naturalWeapon, num)

        if skill == 'Navigation': self.navigation = skillCalc(self.navigation, num)
        if skill == 'Persuade': self.persuade = skillCalc(self.persuade, num)

        if skill == 'Pilot': self.pilot = skillCalc(self.pilot, num)
        if skill == 'Small Craft': self.smallCraft = skillCalc(self.smallCraft, num)
        if skill == 'Spacecraft': self.spacecraft = skillCalc(self.spacecraft, num)
        if skill == 'Capital Ships': self.capitalShips = skillCalc(self.capitalShips, num)

        if skill == 'Recon': self.recon = skillCalc(self.recon, num)
        if skill == 'Remote Operation': self.remoteOperation = skillCalc(self.remoteOperation, num)

        if skill == 'Physical Science': self.physicalScience = skillCalc(self.physicalScience, num)
        if skill == 'Physics': self.physics = skillCalc(self.physics, num)
        #if skill == 'Chemistry': self.recon = skillCalc(self.recon, num)
        if skill == 'Electronic Science': self.electronicScience = skillCalc(self.electronicScience, num)

        if skill == 'Life Science': self.lifeScience = skillCalc(self.lifeScience, num)
        #if skill == 'Biology': self.recon = skillCalc(self.recon, num)
        if skill == 'Cybernetics': self.cybernetics = skillCalc(self.cybernetics, num)
        if skill == 'Genetics': self.genetics = skillCalc(self.genetics, num)
        if skill == 'Psionicology': self.psionicology = skillCalc(self.psionicology, num)

        if skill == 'Social Science': self.socialScience = skillCalc(self.socialScience, num)
        if skill == 'Archeology': self.archeology = skillCalc(self.archeology, num)
        if skill == 'Economics': self.economics = skillCalc(self.economics, num)
        if skill == 'History': self.history = skillCalc(self.history, num)
        if skill == 'Linguistics': self.linguistics = skillCalc(self.linguistics, num)
        if skill == 'Philosophy': self.philosophy = skillCalc(self.philosophy, num)
        if skill == 'Psychology': self.psychology = skillCalc(self.psychology, num)
        if skill == 'Sophontology': self.sophontology = skillCalc(self.sophontology, num)

        if skill == 'Space Science': self.spaceScience = skillCalc(self.spaceScience, num)
        if skill == 'Planetology': self.planetology = skillCalc(self.planetology, num)
        if skill == 'Robotics': self.robotics = skillCalc(self.robotics, num)
        if skill == 'Xenology': self.xenology = skillCalc(self.xenology, num)

        if skill == 'Seafarer': self.seafarer = skillCalc(self.history, num)
        if skill == 'Sail': self.sail = skillCalc(self.history, num)
        if skill == 'Submarine': self.submarine = skillCalc(self.history, num)
        if skill == 'Ocean Ships': self.oceanShips = skillCalc(self.history, num)
        if skill == 'Motorboats': self.motorboats = skillCalc(self.history, num)

        if skill == 'Sensors': self.sensors = skillCalc(self.sensors, num)
        if skill == 'Stealth': self.stealth = skillCalc(self.stealth, num)
        if skill == 'Steward': self.steward = skillCalc(self.steward, num)
        #if skill == 'Streetwise': self.sail = skillCalc(self.history, num)
        if skill == 'Survival': self.survival = skillCalc(self.survival, num)

        if skill == 'Tactics': self.tactics = skillCalc(self.tactics, num)
        if skill == 'Military Tactis': self.militaryTactics = skillCalc(self.militaryTactics, num)
        if skill == 'Naval Tactics': self.navalTactics = skillCalc(self.navalTactics, num)

        if skill == 'Trade': self.trade = skillCalc(self.trade, num)
        if skill == 'Trade Biologicals': self.tradeBiologicals = skillCalc(self.tradeBiologicals, num)
        if skill == 'Trade Civil Engineering': self.tradeCivilEngineering = skillCalc(self.tradeCivilEngineering, num)
        if skill == 'Trade Space Construction': self.tradeSpaceConstruction = skillCalc(self.tradeSpaceConstruction, num)
        if skill == 'Trade Hydroponics': self.tradeHydroponics = skillCalc(self.tradeHydroponics, num)
        if skill == 'Trade Polymers': self.tradePolymers = skillCalc(self.tradePolymers, num)

        if skill == 'Vacc Suit': self.vaccSuit = skillCalc(self.vaccSuit, num)
        if skill == 'Zero-G': self.zeroG = skillCalc(self.zeroG, num)
        

    def printSkills(self,ttrpg):
        if ttrpg == 'Cyberpunk':
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
            if self.befriendedGang == True: print('Family (+2 Booster Gang; 1/mo)')
            if self.befriendedNomad == True: print('Family (+2 Nomad Pack; 1/mo)')
            if self.executiveFavor == True: print('Resources (8 Executive Favor; Once)')

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
            if self.befriendedPolice == True: print('Streetwise (+2 Police Business)')

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

            if self.awarenessNotice > 0:
                if self.awarenessNotice == 1: print('Awareness/Notice (' + str(self.awarenessNotice) + ') Deaf Rat')
                if self.awarenessNotice == 2: print('Awareness/Notice (' + str(self.awarenessNotice) + ') Senile Mole')
                if self.awarenessNotice == 3: print('Awareness/Notice (' + str(self.awarenessNotice) + ') Squinting Newt')
                if self.awarenessNotice == 4: print('Awareness/Notice (' + str(self.awarenessNotice) + ') Unsuspecting Trout')
                if self.awarenessNotice == 5: print('Awareness/Notice (' + str(self.awarenessNotice) + ') Wary Trout')
                if self.awarenessNotice == 6: print('Awareness/Notice (' + str(self.awarenessNotice) + ') Alert Coyote')
                if self.awarenessNotice == 7: print('Awareness/Notice (' + str(self.awarenessNotice) + ') Big-Eyed Tiger')
                if self.awarenessNotice == 8: print('Awareness/Notice (' + str(self.awarenessNotice) + ') Monocled Falcon')
                if self.awarenessNotice == 9: print('Awareness/Notice (' + str(self.awarenessNotice) + ') Sniper Hawk')
                if self.awarenessNotice == 10: print('Awareness/Notice (' + str(self.awarenessNotice) + ') Eagle with Telescope')

            if self.biology > 0: print('Biology (' + str(self.biology) + ')')
            if self.botany > 0: print('Botany (' + str(self.botany) + ')')
            if self.chemistry > 0: print('Chemistry (' + str(self.chemistry) + ')')
            if self.composition > 0: print('Composition (' + str(self.composition) + ')')
            if self.diagnoseIllness > 0: print('Diagnose Illness (' + str(self.diagnoseIllness) + ')')

            if self.education > 0: #print('Education (' + str(self.education) + ')')
                if self.education == 1 or self.education == 2: print('Education (' + str(self.education) + ') Certificate')
                if self.education == 3 or self.education == 4: print('Education (' + str(self.education) + ') Associates')
                if self.education == 5 or self.education == 6: print('Education (' + str(self.education) + ') Bachelors')
                if self.education == 7 or self.education == 8: print('Education (' + str(self.education) + ') Masters')
                if self.education == 9 or self.education == 10: print('Education (' + str(self.education) + ') PhD')


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

def statRoll(): #cyberpunk stat roll math
    x = d(2,6,0)
    while x > 10: x = d(2,6,0)
    return x
                
class character():
    def __init__(self,ttrpg):
        self.ttrpg = ttrpg
        if self.ttrpg == 'Cyberpunk':
            self.name = 'Odysseus'
            self.role = 'Solo'
            self.scoreSum = [18, 'Average']
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
            self.languages = []

        if self.ttrpg == 'Traveller':
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
        if self.ttrpg == 'Cyberpunk':
            self.int = statRoll()
            self.ref[0] = statRoll()
            self.ref[1] = self.ref[0]
            self.tech = statRoll()
            self.cool = statRoll()
            self.attr = statRoll()
            self.luck = statRoll()
            self.ma = statRoll()
            self.body[0] = statRoll()
            self.emp[0] = statRoll()
            self.emp[1] = self.emp[0]
            # Determine Movement
            self.run = self.ma * 3
            self.leap = self.run // 4
            self.lift = 40 * self.body[0]
            self.save = self.body[0]
            # Body Type Categorization
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
        if self.ttrpg == 'Traveller':
            self.str = d(2, 6, 0)
            self.dex = d(2, 6, 0)
            self.end = d(2, 6, 0)
            self.int = d(2, 6, 0)
            self.edu = d(2, 6, 0)
            self.soc = d(2, 6, 0)
            

    def scoreSumCalculator(self): # Cyberpunk Score Sum Calculator
        self.scoreSum[0] = self.int + self.ref[1] + self.tech + self.cool + self.attr + self.luck + self.ma + \
                            self.body[0] + self.emp[1]
        if self.scoreSum[0] < 40: self.scoreSum[1] = 'Bullet Fodder'
        if self.scoreSum[0] >= 40 and self.scoreSum[0] < 50: self.scoreSum[1] = 'Film Extra'
        if self.scoreSum[0] >= 50 and self.scoreSum[0] < 60: self.scoreSum[1] = 'Background Character'
        if self.scoreSum[0] >= 60 and self.scoreSum[0] < 70: self.scoreSum[1] = 'Minor Supporting Character'
        if self.scoreSum[0] >= 70 and self.scoreSum[0] < 75: self.scoreSum[1] = 'Major Supporting Character'
        if self.scoreSum[0] >= 75 and self.scoreSum[0] < 80: self.scoreSum[1] = 'Minor Hero'
        if self.scoreSum[0] >= 80 and self.scoreSum[0] < 90: self.scoreSum[1] = 'Major Hero'
        if self.scoreSum[0] == 90: self.scoreSum[1] = 'Impossibility'

    def siblingGenerator(self, sibling_num):
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

    # TODO // CHANGE TO camelCase
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
        if x <= 7: self.siblingGenerator(x)
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

    def personalStylist(self):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = random.randint(1, 10)
        if x == 1: self.clothes = 'Biker Leathers'
        if x == 2: self.clothes = 'Blue Jeans'
        if x == 3: self.clothes = 'Corporate Suits'
        if x == 4: self.clothes = 'Jumpsuits'
        if x == 5: self.clothes = 'Miniskirts'
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

# ORIGIN AND PERSONAL STYLE (CYBERPUNK)
# CHILDHOOD
# MOTIVATIONS

    def aptitudeTest(self):
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

    # rolling class skills now in the character
    def rollSkills(self):
        classSkills = []
        if self.ttrpg == 'Cyberpunk':
            skillDistribution = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(39):
                x = random.randint(0, len(skillDistribution) - 1)
                while skillDistribution[x] >= 10: x = random.randint(0, len(skillDistribution) - 1)
                skillDistribution[x] += 1
                
            if self.role == 'Solo':
                classSkills = ['Combat Sense',
                               'Awareness/Notice',
                               'Handgun',
                               'Martial Arts (Any)',
                               'Brawling',
                               'Weaponsmith',
                               'Rifle',
                               'Athletics',
                               'Submachinegun',
                               'Stealth']
            if self.role == 'Corporate':
                classSkills = ['Resources',
                               'Awareness/Notice',
                               'Human Perception',
                               'Education',
                               'Library Search',
                               'Social',
                               'Persuasion',
                               'Stock Market',
                               'Wardrobe & Style',
                               'Personal Grooming']
            if self.role == 'Media':
                classSkills = ['Credibility',
                               'Awareness/Notice',
                               'Composition',
                               'Education',
                               'Persuasion',
                               'Human Perception',
                               'Social',
                               'Streetwise',
                               'Photo & Film',
                               'Interview']
            if self.role == 'Nomad':
                classSkills = ['Family',
                               'Awareness/Notice',
                               'Endurance',
                               'Melee',
                               'Rifle',
                               'Driving',
                               'Basic Tech',
                               'Survival',
                               'Brawling',
                               'Athletics']
            if self.role == 'Techie':
                techieSkills = ['Aero Tech',
                                'Vector Thrust Tech',
                                'Cryotank',
                                'Cyberdeck Design',
                                'Demolitions',
                                'Disguise',
                                'Electronic Security',
                                'First Aid',
                                'Forgery',
                                'Gyro Tech',
                                'Paint or Draw',
                                'Photo & Film',
                                'Pharmaceuticals',
                                'Pick Lock',
                                'Pick Pocket',
                                'Instrument',
                                'Weaponsmith']
                skillOne = random.choice(techieSkills)
                techieSkills.remove(skillOne)
                skillTwo = random.choice(techieSkills)
                techieSkills.remove(skillTwo)
                skillThree = random.choice(techieSkills)
                techieSkills.remove(skillThree)
                classSkills = ['Jury Rig',
                               'Awareness/Notice',
                               'Basic Tech',
                               'Cyber Tech',
                               'Teaching',
                               'Education',
                               'Electronics',
                               skillOne,
                               skillTwo,
                               skillThree]
            if self.role == 'Rockerboy':
                classSkills = ['Charismatic Leadership',
                               'Awareness/Notice',
                               'Performance',
                               'Wardrobe & Style',
                               'Composition',
                               'Brawling',
                               'Instrument',
                               'Streetwise',
                               'Persuation',
                               'Seduction']
            if self.role == 'Medtechie':
                classSkills = ['Medical Tech',
                               'Awareness/Notice',
                               'Basic Tech',
                               'Diagnose Illness',
                               'Education',
                               'Cryotank',
                               'Library Search',
                               'Pharmaceuticals',
                               'Zoology',
                               'Human Perception']
            if self.role == 'Fixer':
                classSkills = ['Streetdeal',
                               'Awareness/Notice',
                               'Forgery',
                               'Handgun',
                               'Brawling',
                               'Melee',
                               'Pick Lock',
                               'Pick Pocket',
                               'Intimidate',
                               'Persuasion']
            if self.role == 'Netrunner':
                classSkills = ['Interface',
                               'Awareness/Notice',
                               'Basic Tech',
                               'Education',
                               'System Knowledge',
                               'Cyber Tech',
                               'Cyberdeck Design',
                               'Composition',
                               'Electronics',
                               'Programming']
            if self.role == 'Cop':
                classSkills = ['Authority',
                               'Awareness/Notice',
                               'Handgun',
                               'Human Perception',
                               'Athletics',
                               'Education',
                               'Brawling',
                               'Melee',
                               'Interrogation',
                               'Streetwise']

            # Train the skills as their random distribution
            for i in range(len(skillDistribution)):
                self.skills.train(self,classSkills[i],skillDistribution[i]) # OOR

            # ROLL PICKUP SKILLS
            masterSkillsList = ['Personal Grooming','Wardrobe & Style','Endurance','Strength Feat','Swimming','Interrogation','Intimidate','Oratory','Resist Torture & Drugs','Streetwise','Human Perception','Interview','Leadership','Seduction','Social','Persuasion','Performance','Accounting','Anthropology','Awareness/Notice','Biology','Botany','Chemistry','Composition','Diagnose Illness','Education','Expert','Gamble','Hide/Evade','History','Language','Library Search','Math','Physics','Programming','Shadow/Track','Stock Market','System Knowledge','Teaching','Survival','Zoology','Archery','Athletics','Brawling','Dancing','Dodge/Escape','Driving','Fencing','Handgun','Heavy Weapons','Aikido','Animal Kung Fu','Boxing','Capoeria','Choi Li Fut','Judo','Karate','Tae Kwon Do','Thai Kick Boxing','Wresling','Melee','Moorcycle','Heavy Machinery','Gyro','Fixed Wing','Dirigible','Vector Thrust','Rifle','Stealth','Submachinegun','Aero Tech','Vector Thrust Tech','Basic Tech','Cryotank','Cyberdeck Design','Cyber Tech','Demolitions','Disguise','Electronics','Electronic Security','First Aid','Forgery','Gyro Tech','Paint or Draw','Photo & Film','Pharmaceuticals','Pick Lock','Pick Pocket','Instrument','Weaponsmith']
            skillsList = []
            for i in range(len(masterSkillsList)):
                if masterSkillsList[i] not in classSkills: skillsList.append(masterSkillsList[i])
            pointsAvailable = self.int + self.ref[1]
            numSkills = random.randint(1,pointsAvailable)
            pickupSkills = []
            pickupDistribution = []
            for i in range(numSkills):
                pickupDistribution.append(0)
                x = random.randint(1,len(skillsList)-1)
                pickupSkills.append(skillsList[x])
                skillsList.remove(skillsList[x])
            for i in range(pointsAvailable):
                x = random.randint(1,len(pickupDistribution)-1) # EMPTY RANGE
                while pickupDistribution[x] >= 10: x = random.randint(1,len(pickupDistribution)-1)
                pickupDistribution[x] += 1
            for i in range(len(pickupDistribution)):
                self.skills.train(self,pickupSkills[i],pickupDistribution[i])

        if self.ttrpg == 'Traveller':
            print()
            print('Traveller Character Identified')

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
                    self.attr = self.attr - 5
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
                y = d(1,9,0)
                if y == 1: martialArt = 'an Aikido'
                if y == 2: martialArt = 'an Animal Kung Fu'
                if y == 3: martialArt = 'a Capoeria'
                if y == 4: martialArt = 'a Choi Li Fut'
                if y == 5: martialArt = 'a Judo'
                if y == 6: martialArt = 'a Karate'
                if y == 7: martialArt = 'a Tae Kwon Do'
                if y == 8: martialArt = 'a Thai Kick Boxing'
                if y == 9: martialArt = 'a Wrestling'
                self.skills.train(self,martialArt,1)
                self.skills.train(self,martialArt,-1)
                return 'You find ' + martialArt + ' Sensei'

            if x == 5:
                intSkills = ['Accounting', 'Anthropology', 'Awareness/Notice', 'Biology',
                             'Botany', 'Chemistry', 'Composition', 'Diagnose Illness', 'Education',
                             'Expert', 'Gamble', 'Hide/Evade', 'History', 'Language', 'Library Search',
                             'Mathematics', 'Physics', 'Programming', 'Shadow/Track', 'Stock Market',
                             'System Knowledge', 'Teaching', 'Wilderness Survival', 'Zoology']
                intSkill = random.choice(intSkills)
                self.skills.train(self,intSkill,1)
                self.skills.train(self,intSkill,-1)
                return 'You find a legendary ' + intSkill + ' teacher.'

            if x == 6:
                self.skills.executiveFavor = True
                return 'Powerful corporate exec owes you one favor'
            if x == 7:
                self.skills.befriendedNomad = True
                return 'Befriended Nomad Pack: Family +2 1/mo.'
            if x == 8:
                self.skills.befriendedPolice = True
                return 'Befriend Police Force Member: +2 Streetwise with Police Business'
            if x == 9:
                self.skills.befriendedGang = True
                return 'Befriended Local Boostergang: Family +2 1/mo.'

            if x == 10:
                combatSkills = ['Dodge/Escape', 'Fencing', 'Handgun', 'Heavy Weapons', 'Melee', 'Rifle',
                                'Submachinegun']
                chosenSkill = random.choice(combatSkills)
                self.skills.train(self,chosenSkill,1)
                self.skills.train(self,chosenSkill,-1)
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

    def characterNiche(self):
        stockRegion = self.languages[0][0]
        firstLanguage = self.languages[0][1]
        occupation = self.occupation[0]
        if stockRegion == 'Hispanic American': firstLanguage = 'Mexican'
        if self.role == 'Rockerboy': occupation = "Rockerboy: " + occupation
        if stockRegion == 'African': firstLanguage = 'African'
        if firstLanguage == 'Mandarin': firstLanguage = 'Chinese'
        if stockRegion == 'Anglo-American': firstLanguage = 'American'
        if firstLanguage == 'Lingua Astra': firstLanguage = 'Starcitizen'
        if firstLanguage == 'Alien Language': firstLanguage = 'Alien'
        print(self.personality+' '+firstLanguage + ' ' + occupation)

    def appearance(self):
        hair = self.hairstyle
        if hair != 'Bald' and hair != 'Mohawk': hair = hair + ' hair'
        clothes = self.clothes
        if clothes == 'Nude': clothes = 'a Nudist disposition'
        affect = self.affectations
        print(hair+', '+clothes+' and '+affect)

    def vitomatic(self):
        if self.int == 1: print('INT 1 Sub-Brick')
        if self.int == 2: print('INT 2 Vegetable')
        if self.int == 3: print('INT 3 Cretin')
        if self.int == 4: print('INT 4 Knucklehead')
        if self.int == 5: print('INT 5 Knowledgeable')
        if self.int == 6: print('INT 6 Gifted')
        if self.int == 7: print('INT 7 Smartypants')
        if self.int == 8: print('INT 8 Know-It-All')
        if self.int == 9: print('INT 9 Genius')
        if self.int == 10: print('INT 10 Omniscient')
        if self.int > 10: print('INT '+str(self.int))

        if self.ref[0] == 1: print('REF [1/'+str(self.ref[1])+'] Walking Disaster')
        if self.ref[0] == 2: print('REF [2/'+str(self.ref[1])+'] Accident Prone')
        if self.ref[0] == 3: print('REF [3/'+str(self.ref[1])+'] Oaf')
        if self.ref[0] == 4: print('REF [4/'+str(self.ref[1])+'] Butterfingers')
        if self.ref[0] == 5: print('REF [5/'+str(self.ref[1])+'] Under Control')
        if self.ref[0] == 6: print('REF [6/'+str(self.ref[1])+'] Catlike')
        if self.ref[0] == 7: print('REF [7/'+str(self.ref[1])+'] Knife Thrower')
        if self.ref[0] == 8: print('REF [8/'+str(self.ref[1])+'] Knife Catcher')
        if self.ref[0] == 9: print('REF [9/'+str(self.ref[1])+'] Acrobatic Marvel')
        if self.ref[0] == 10: print('REF [10/'+str(self.ref[1])+'] Water Walker')
        if self.ref[0] > 10: print('REF ['+str(self.ref[0])+'/'+str(self.ref[1])+']')

        if self.tech == 1: print('TECH 1 Caveman')
        if self.tech == 2: print('TECH 2 Grandma')
        if self.tech == 3: print('TECH 3 Analog')
        if self.tech == 4: print('TECH 4 Outdated')
        if self.tech == 5: print('TECH 5 Computer Literate')
        if self.tech == 6: print('TECH 6 Repairman')
        if self.tech == 7: print('TECH 7 Technician')
        if self.tech == 8: print('TECH 8 Programmer')
        if self.tech == 9: print('TECH 9 Hacker')
        if self.tech == 10: print('TECH 10 Tech Wizard')
        if self.tech > 10: print('TECH '+str(self.tech))

        if self.cool == 1: print('COOL 1 Diaper-Worthy')
        if self.cool == 2: print('COOL 2 Deserter')
        if self.cool == 3: print('COOL 3 Coward')
        if self.cool == 4: print('COOL 4 Scaredy-Cat')
        if self.cool == 5: print('COOL 5 Average Joe')
        if self.cool == 6: print('COOL 6 Soldier')
        if self.cool == 7: print('COOL 7 Brave Hero')
        if self.cool == 8: print('COOL 8 John Wick')
        if self.cool == 9: print('COOL 9 Masterchief')
        if self.cool == 10: print('COOL 10 Mary-Sue')
        if self.cool > 10: print('COOL '+str(self.cool))
        
        if self.attr == 1: print('ATTR 1 Paper Bag')
        if self.attr == 2: print('ATTR 2 Disfigured')
        if self.attr == 3: print('ATTR 3 Phantom')
        if self.attr == 4: print('ATTR 4 Butterface')
        if self.attr == 5: print('ATTR 5 Average Looks')
        if self.attr == 6: print('ATTR 6 Frontman')
        if self.attr == 7: print('ATTR 7 C-List Model')
        if self.attr == 8: print('ATTR 8 Model')
        if self.attr == 9: print('ATTR 9 Supermodel')
        if self.attr == 10: print('ATTR 10 Divine Beauty')
        if self.attr > 10: print('ATTR '+str(self.attr))

        if self.luck == 1: print('LUCK 1 13 Pitch-Black Cats')
        if self.luck == 2: print('LUCK 2 Broken Gypsy Mirror')
        if self.luck == 3: print('LUCK 3 Sickly Albatross')
        if self.luck == 4: print('LUCK 4 Spilled Salt')
        if self.luck == 5: print('LUCK 5 Coin Flip')
        if self.luck == 6: print('LUCK 6 Stacked Deck')
        if self.luck == 7: print('LUCK 7 Lucky 7')
        if self.luck == 8: print("LUCK 8 Leprechaun's Foot")
        if self.luck == 9: print('LUCK 9 21-Leaf Clover')
        if self.luck == 10: print('LUCK 10 Two-Headed Coin Flip')
        if self.luck > 10: print('LUCK '+str(self.luck))

        print('MA '+str(self.ma)+' ('+str(self.run)+'m/'+str(self.leap)+'m/'+str(self.lift)+'kg)')

        if self.body[0] == 1: print('BODY 1 Basically Dead')
        if self.body[0] == 2: print('BODY 2 Crumbly')
        if self.body[0] == 3: print('BODY 3 Do Not Bend')
        if self.body[0] == 4: print('BODY 4 Handle With Care')
        if self.body[0] == 5: print('BODY 5 Stain-Resistant')
        if self.body[0] == 6: print('BODY 6 Hardy')
        if self.body[0] == 7: print('BODY 7 Tough-As-Nails')
        if self.body[0] == 8: print('BODY 8 Flame Retardant')
        if self.body[0] == 9: print('BODY 9 Bulletproof')
        if self.body[0] == 10: print('BODY 10 Unstoppable')
        if self.body[0] > 10: print('BODY '+str(self.body[0]))

        if self.emp[0] == 1: print('EMP [1/'+str(self.emp[1])+'] Misanthrope')
        if self.emp[0] == 2: print('EMP [2/'+str(self.emp[1])+'] Old Hermit')
        if self.emp[0] == 3: print('EMP [3/'+str(self.emp[1])+'] Creepy Undertaker')
        if self.emp[0] == 4: print('EMP [4/'+str(self.emp[1])+'] Basement Dweller')
        if self.emp[0] == 5: print('EMP [5/'+str(self.emp[1])+'] Substitute Teacher')
        if self.emp[0] == 6: print('EMP [6/'+str(self.emp[1])+'] Cheery Salesman')
        if self.emp[0] == 7: print('EMP [7/'+str(self.emp[1])+'] Local Newsman')
        if self.emp[0] == 8: print('EMP [8/'+str(self.emp[1])+'] Diplomat')
        if self.emp[0] == 9: print('EMP [9/'+str(self.emp[1])+'] Denmother')
        if self.emp[0] == 10: print('EMP [10/'+str(self.emp[1])+'] Cult Leader')
        if self.emp[0] > 10: print('EMP ['+str(self.emp[0])+'/'+str(self.emp[1])+']')

    def dossier(self):
        if self.ttrpg == 'Cyberpunk':
            print('Name: '+self.name)
            self.characterNiche()
            self.appearance()
            print()
            self.vitomatic()
            print()
            self.skills.printSkills(self.ttrpg)
            print()
            print('Life Events:')
            for i in range(len(self.lifeEvents)):
                if isinstance(self.lifeEvents[i], str): print(str(17 + i) + ' y/o: ' + self.lifeEvents[i])

        if self.ttrpg == 'Traveller':
            print('Name: '+self.name)
            print('Homeworld: '+self.homeworld.name)
            print(self.homeworld.codes)
            print('STR ' + str(self.str))
            print('DEX ' + str(self.dex))
            print('END ' + str(self.end))
            print('INT ' + str(self.int))
            print('EDU ' + str(self.edu))
            print('SOC ' + str(self.soc))

    def generate(self,homeworld):
        if self.ttrpg == 'Cyberpunk':
            self.name = generateName()
            self.rollStats()
            self.scoreSumCalculator()
            self.languages.append(returnEthnics())
            self.personalStylist()
            self.childhood()
            self.motivations()
            self.aptitudeTest()
            skillPackage = skills(self)
            self.skills = skillPackage
            self.rollSkills()
            self.occupationTable()
            self.lifeEventsGenerator() # TODO // WRITE 'ENEMIES' SUBSECTION
            self.ref[0] = self.ref[1]
            self.emp[0] = self.emp[1]

        if self.ttrpg == 'Traveller':
            self.name = generateName()
            self.rollStats()
            self.homeworld = homeworld
            skillPackage = skills(self)
            self.skills = skillPackage
            self.rollSkills()# homeworld and education
            #careerPackage = career()
            #self.career = careerPackage
            #self.career.basicTraining()
            #while self.career.died == False:
            #    self.career.termSkills(self)
            #    self.career.surviveAdvance(self)

# Main Loop

hallowsbelt = planet()
hallowsbelt.language = returnEthnics()
hallowsbelt.generateCodes()

odysseus = character('Cyberpunk')
odysseus.generate('none')
odysseus.dossier()

silverhand = character('Traveller')
silverhand.generate(hallowsbelt)
silverhand.dossier()
