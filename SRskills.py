# SR skillsheet
import random
from SRtools import *

def skillCalc(skill, num):
    x = skill
    if x == -3: x = 0               # Set to 0 if at -3 for Traveller
    if num <= -1: x += (num * -1)   # If num < 0, add abs. value of num
    if num > -1: x = num            # If num > 0, set skill to num
    if skill >= x: x = skill        # If skill already greater, leave it
    return x                        # Return for skill setting

class skills():
    def __init__(self,character):
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

        # Favor Bools
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

        #Cancel LOL
        if character.name == 'Traveller':
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

        self.vaccSuit = 0
        self.zeroG = 0
        self.computers = 0
        self.deception = 0
        self.mechanic = 0
        self.recon = 0
        self.astrogation = 0

    def train(self,character,skill,num):
        # Cyberpunk Characteristics (Ability Scores)
        if skill == 'MUS': character.muscle = skillCalc(character.muscle, num)
        if skill == 'REF': character.reflex = skillCalc(character.reflex, num)
        if skill == 'GRIT': character.grit = skillCalc(character.grit, num)
        if skill == 'INT': character.intel = skillCalc(character.intel, num)
        if skill == 'ING': character.ingen = skillCalc(character.ingen, num)
        if skill == 'EMP': character.emp = skillCalc(character.emp, num)
        
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
