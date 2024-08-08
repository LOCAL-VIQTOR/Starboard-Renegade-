# SR skillsheet
#___________             __       ________.__  __     ___ ___      ___.     _________               .__.__          __   
#\_   _____/_ __   ____ |  | __  /  _____/|__|/  |_  /   |   \ __ _\_ |__   \_   ___ \  ____ ______ |__|  |   _____/  |_ 
# |    __)|  |  \_/ ___\|  |/ / /   \  ___|  \   __\/    ~    \  |  \ __ \  /    \  \/ /  _ \\____ \|  |  |  /  _ \   __\
# |     \ |  |  /\  \___|    <  \    \_\  \  ||  |  \    Y    /  |  / \_\ \ \     \___(  <_> )  |_> >  |  |_(  <_> )  |  
# \___  / |____/  \___  >__|_ \  \______  /__||__|   \___|_  /|____/|___  /  \______  /\____/|   __/|__|____/\____/|__|  
#     \/              \/     \/         \/                 \/           \/          \/       |__|                        - lv 8/6/24
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
        n = -3

        # Special Abilities
        self.authority = n              # Cop
        self.charismaticLeadership = n  # Rockerboy
        self.combatSense = n            # Solo
        self.credibility = n            # Media
        self.family = n                 # Nomad
        self.interface = n              # Netrunner
        self.juryRig = n                # Techie
        self.medicalTech = n            # Medtechie
        self.resources = n              # Corporate
        self.streetdeal = n             # Fixer

        # Favor Bools
        self.befriendedPolice = False
        self.befriendedNomad = False
        self.befriendedGang = False
        self.executiveFavor = False

        # MASTER SKILLS LIST
        # Arranged alphabetically by parent tag.
        # Animals, Art, Athletics, Combat Skills, Heavy Weapons, Driving, Engineer Flyer, Gunner, 
        # Melee, Martial Arts, Pilot, Gunner, Gun Combat, Seafarer, Sciences, Tactics, Technical Skills,
        # Trade, Optionally Languages
        #
        # >> ADD GUERILLA TACTICS
        # >> MAYBE PACK/PUNK TACTICS?

        #    Tag                                # Name of Tag               Source  Ability Note:

        # A - A
        self.accounting = n                     # Accounting                CP      INT
        self.admin = n                          # Admin                     TV
        self.advocate = n                       # Advocate                  TV              Consider removing
        self.astrogation = n                    # Astrogation               TV              
        self.awarenessNotice = n                # Awareness/Notice          CP      INT     Classic "Perception"

        #   Animals
        self.animals = n                        # Animals                   TV
        self.animalRiding = n                   # Animal Riding             TV
        self.veterinary = n                     # Veterinary                TV
        self.animalTraining = n                 # Animal Training           TV
        self.animalFarming = n                  # Animal Farming            TV
        
        #   Art - Self Expression or Pastiche
        self.performance = n                    # Performance               CP      EMP
        self.composition = n                    # Composition               CP      INT
        self.dancing = n                        # Dancing                   CP/TV   REF     Traveller listed as 'Dance'
        self.disguise = n                       # Disguise                  CP      TECH    Fool others (person)
        self.forgery = n                        # Forgery                   CP      TECH    Fool others (object)
        self.instrument = n                     # Instrument                CP/TV   TECH    Requires extrapolation
        self.paintDraw = n                      # Paint or Draw             CP      TECH    Consider separating
        self.photoFilm = n                      # Photo & Film              CP      TECH    Consider renaming "Camera"
        self.art = n                            # Art                       TV
        self.acting = n                         # Acting                    TV              
        self.holography = n                     # Holography                TV
        self.sculpting = n                      # Sculpting                 TV
        self.writing = n                        # Writing                   TV
        
        #   Athletics
        self.athletics = n                      # Athletics                 CP      REF
        self.endurance = n                      # Endurance                 CP/TV   BODY
        self.coordination = n                   # Coordination              TV
        self.strength = n                       # Strength                  CP/TV   BODY    Cyberpunk listed 'Strength Feat'
        self.flying = n                         # Flying                    TV              Only for characters with wings
        self.swimming = n                       # Swimming                  CP      BODY

        # A - C
        self.battleDress = n                    # Battle Dress              TV
        self.blade = n                          # Blade                     TV
        self.bludgeon = n                       # Bludgeon                  TV
        self.brawling = n                       # Brawling                  CP      REF
        self.broker = n                         # Broker                    TV
        self.carouse = n                        # Carouse                   TV
        
        
        # Combat Skills - Tool-Oriented Missile Weapons
        self.archery = n                        # Archery                   CP      REF
        self.fencing = n                        # Fencing                   CP      REF
        self.submachinegun = n                  # Submachinegun             CP      REF
        self.gunCombat = n                      # Gun Combat                TV
        self.slugRifle = n                      # Slug Rife                 TV/CP   REF     Cyberpunk referred 'rifle'
        self.slugPistol = n                     # Slug Pistol               TV/CP   REF     Cyberpunk referred 'handgun'
        self.shotgun = n                        # Shotgun                   TV
        self.energyRifle = n                    # Energy Rifle              TV
        self.energyPistol = n                   # Energy Pistol             TV
        
        # Heavy Weapons - Listed underneath combat skills for unknown reasons
        self.heavyWeapons = n                   # Heavy Weapons             CP/TV   REF
        self.launchers = n                      # Launchers                 TV  
        self.MPA = n                            # MPA                       TV              Man-Portable Artillery
        self.fieldArtillery = n                 # Field Artillery           TV
        
        # C - D
        self.comms = n                          # Comms                     TV
        self.computers = n                      # Computers                 TV
        self.deception = n                      # Deception                 TV
        self.diplomat = n                       # Diplomat                  TV
        self.diagnoseIllness = n                # Diagnose Illness          CP      INT
        self.dodgeEscape = n                    # Dodge/Escape              CP      REF
        
        # Driving - On or Below Surface Transportation Schemes
        self.driving = n                        # Driving                   CP      REF     Traveller refers as "Drive"
        self.motorcycle = n                     # Motorcycle                CP      REF
        self.heavyMachinery = n                 # Heavy Machinery           CP      REF 
        self.driveMole = n                      # Drive Mole                TV
        self.driveTracked = n                   # Drive Tracked             TV
        self.driveWheeled = n                   # Drive Wheeled             TV

        # D - E
        self.education = n                      # Education                 CP      INT
        
        # Engineer
        self.engineer = n                       # Engineer                  TV
        self.mDrive = n                         # M-Drive                   TV
        self.jDrive = n                         # J-Drive                   TV
        self.electricalEngineer = n             # Electrical Engineer       TV
        self.lifeSupport = n                    # Life Support              TV              Life Support Systems
        self.power = n                          # Power                     TV              Power Plants
        self.explosives = n                     # Explosives                TV              Consider Merging with Demolitions

        # E - F
        self.expert = n                         # Expert                    CP      INT
        
        # Flyer - In-Atmosphere Flying Schemes
        self.fixedWing = n                      # Fixed Wing                CP/TV   REF     Traveller referred 'Wing'
        self.dirigible = n                      # Dirigible                 CP      REF     For Airships / Blimps
        self.vectorThrust = n                   # Vector Thrust             CP      REF 
        self.flyer = n                          # Flyer                     TV              For piloting in-atmosphere craft
        self.grav = n                           # Grav                      TV              For crafts with anti-gravity propulsion
        self.rotor = n                          # Rotor                     TV/CP   REF     Cyberpunk referred 'Gyro'

        # F - G
        self.gamble = n                         # Gamble                    CP/TV   INT     Traveller referred 'Gambler'
        
        # Gunner - On-Board Weaponry
        self.gunner = n                         # Gunner                    TV              Ship Weaponry Familiarity
        self.turrets = n                        # Turrets                   TV              Mounted Turret Weapons
        self.ortillery = n                      # Ortillery                 TV              Orbital Artillery
        self.screens = n                        # Screens                   TV              Ship Weapons: Screens
        self.capitalWeapons = n                 # Capital Weapons           TV              Massive weapons on ships 5k tons and up

        # G - M
        self.hideEvade = n                      # Hide/Evade                CP      INT
        self.humanPerception = n                # Human Perception          CP      EMP
        self.interrogation = n                  # Interrogation             CP      COOL
        self.interview = n                      # Interview                 CP      EMP
        self.intimidate = n                     # Intimidate                CP      COOL
        self.investigate = n                    # Investigate               TV
        self.jackOfAllTrades = n                # Jack of all Trades        TV              Consider Removal
        self.language = n                       # Language                  CP/TV   INT     Requires Extrapolation
        self.leadership = n                     # Leadership                CP/TV   EMP
        self.librarySearch = n                  # Library Search            CP      INT

        #   Martial Arts - No Brawling, Melee, or Crude Fighting Styles
        self.aikido = n                         # Aikido                    CP      REF
        self.animalKungFu = n                   # Animal Kung Fu            CP      REF   
        self.boxing = n                         # Boxing                    CP      REF
        self.capoeria = n                       # Capoeria                  CP      REF
        self.choiLiFut = n                      # Choi Li Fut               CP      REF
        self.judo = n                           # Judo                      CP      REF
        self.karate = n                         # Karate                    CP      REF
        self.taeKwonDo = n                      # Tae Kwon Do               CP      REF
        self.thaiKickBoxing = n                 # Thai Kick Boxing          CP      REF
        self.wrestling = n                      # Wrestling                 CP      REF

        # M - P
        self.melee = n                          # Melee                     CP/TV   REF
        self.naturalWeapon = n                  # Natural Weapon            TV              Only for characters with claws etc.
        self.navigation = n                     # Navigation                TV
        self.oratory = n                        # Oratory                   CP      COOL
        self.personalGrooming = n               # Personal Grooming         CP      ATTR
        self.persuasion = n                     # Persuasion                CP      EMP

        # Pilot
        self.pilot = n                          # Pilot                     TV              x = ship tonnage
        self.smallCraft = n                     # Small Craft               TV              x<100t
        self.spacecraft = n                     # Spacecraft                TV              100t<x<5kt
        self.capitalShips = n                   # Capital Ships             TV              x>5kt

        self.persuade = n                       # Persuade                  TV
        self.programming = n                    # Programming               CP      INT
        self.recon = n                          # Recon                     TV
        self.remoteOperation = n                # Remote Operation          TV
        self.resistTortureDrugs = n             # Resist Torture & Drugs    CP      COOL
        
        #   Seafarer
        self.seafarer = n
        self.sail = n
        self.submarine = n
        self.oceanShips = n
        self.motorboats = n


        #   Sciences / Studies
        # Physical Science
        self.physicalScience = n                # Physical Science
        self.physics = n                        # Physics                   CP/TV   INT
        self.chemistry = n                      # Chemistry                 CP      INT 
        self.electronicScience = n              # Electronic Science             
        self.math = n                           # Math                      CP      INT
        # Life Science
        self.lifeScience = n                    # Life Science
        self.biology = n                        # Biology                   CP/TV   INT
        self.botany = n                         # Botony                    CP      INT
        self.cybernetics = n                    # Cybernetics
        self.genetics = n                       # Genetics
        self.psionicology = n                   # Psionicology
        self.pharmaceuticals = n                # Pharmaceuticals           CP      TECH
        self.zoology = n                        # Zoology                   CP      INT
        # Social Science
        self.socialScience = n                  # Social Science
        self.anthropology = n                   # Anthropology              CP      INT
        self.archeology = n                     # Archaeology
        self.economics = n                      # Economics
        self.history = n                        # History                   CP/TV   INT
        self.linguistics = n                    # Linguistics
        self.philosophy = n                     # Philosophy
        self.psychology = n                     # Psychology
        self.sophontology = n                   # Sophontology
        # Space Science
        self.spaceScience = n                   # Space Science
        self.planetology = n                    # Planetology
        self.robotics = n                       # Robotics
        self.xenology = n                       # Xenology

        # S - T
        self.seduction = n                      # Seduction                 CP      EMP
        self.sensors = n                        # Sensors                   TV      
        self.shadowTrack = n                    # Shadow/Track              CP      INT
        self.social = n                         # Social                    CP      EMP
        self.stealth = n                        # Stealth                   CP/TV   REF
        self.steward = n                        # Steward                   TV
        self.stockMarket = n                    # Stock Market              CP      INT
        self.streetwise = n                     # Streetwise                CP/TV   COOL
        self.survival = n                       # Survival                  CP/TV   INT
        self.systemKnowledge = n                # System Knowledge          CP      INT  

        # Tactics
        self.tactics = n                        # Tactics                   TV
        self.militaryTactics = n                # Military Tactics          TV
        self.navalTactics = n                   # Naval Tactics             TV
        
        # T - T
        self.teaching = n                       # Teaching                  CP      INT

        #   Technical Skills
        self.aeroTech = n                       # Aero Tech                 CP      TECH
        self.vectorThrustTech = n               # Vector Thrust Tech        CP      TECH
        self.basicTech = n  #                   # Basic Tech                CP      TECH
        self.cryotank = n                       # Cryotank                  CP      TECH
        self.cyberdeckDesign = n                # Cyberdeck Design          CP      TECH
        self.cyberTech = n  #                   # Cyber Tech                CP      TECH
        self.demolitions = n                    # Demolitions               CP      TECH
        self.electronics = n  #                 # Electronics               CP      TECH
        self.electronicSecurity = n             # Electronic Security       CP      TECH
        self.firstAid = n                       # First Aid                 CP/TV   TECH    Traveller Refers 'Medic'
        self.gyroTech = n                       # Gyro Tech                 CP      TECH
        self.pickLock = n                       # Pick Lock                 CP      TECH
        self.pickPocket = n                     # Pick Pocket               CP      TECH
        self.weaponsmith = n                    # Weaponsmith               CP      TECH
        self.mechanic = n                       # Mechanic                  TV

        # Trade: will probably attempt to add one per freight entry (LOTS)
        self.trade = n                          # Trade                     TV
        self.tradeBiologicals = n               # Trade Biologicals         TV
        self.tradeCivilEngineering = n          # Trade Civil Engineering   TV
        self.tradeSpaceConstruction = n         # Trade Space Construction  TV
        self.tradeHydroponics = n               # Trade Hydroponics         TV
        self.tradePolymers = n                  # Trade Polymers            TV
        
        # T - Z
        self.unarmed = n                        # Unarmed                   TV
        self.vaccSuit = n                       # Vacc Suit                 TV
        self.wardrobeStyle = n                  # Wardrobe & Style          CP      ATTR
        self.zeroG = n                          # Zero-G                    TV

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
        if skill == 'Archeology': self.archeology = skillCalc(self.archeology, num)
        if skill == 'Art': self.art = skillCalc(self.art, num) # TV; ART
        if skill == 'Astrogation': self.astrogation = skillCalc(self.astrogation, num) # TV
        if skill == 'Athletics': self.math = skillCalc(self.math,num) # REF
        if skill == 'Awareness/Notice': self.awarenessNotice = skillCalc(self.awarenessNotice,num) # INT
        
        #B
        if skill == 'Basic Tech': self.basicTech = skillCalc(self.basicTech,num) # TECH
        if skill == 'Battle Dress': self.battleDress = skillCalc(self.battleDress, num) # TV
        if skill == 'Biology': self.biology = skillCalc(self.biology,num) # INT
        if skill == 'Blade': self.blade = skillCalc(self.blade, num)
        if skill == 'Bludgeon': self.bludgeon = skillCalc(self.bludgeon, num)
        if skill == 'Botany': self.botany = skillCalc(self.botany,num) # INT
        if skill == 'Boxing': self.boxing = skillCalc(self.boxing,num) # REF
        if skill == 'Brawling': self.brawling = skillCalc(self.brawling,num) # REF
        if skill == 'Broker': self.broker = skillCalc(self.broker, num) # TV
        
        #C
        if skill == 'Capital Ships': self.capitalShips = skillCalc(self.capitalShips, num)
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
        if skill == 'Cybernetics': self.cybernetics = skillCalc(self.cybernetics, num)
        if skill == 'Cyber Tech': self.cyberTech = skillCalc(self.cyberTech,num) # TECH
        
        #D
        if skill == 'Dancing': self.dancing = skillCalc(self.dancing,num) # REF
        if skill == 'Deception': self.deception = skillCalc(self.deception, num) # TV
        if skill == 'Demolitions': self.demolitions = skillCalc(self.demolitions,num) # TECH
        if skill == 'Diagnose Illness': self.diagnoseIllness = skillCalc(self.diagnoseIllness,num) # INT
        if skill == 'Diplomat': self.diplomat = skillCalc(self.diplomat, num) # TV
        if skill == 'Dirigible': self.dirigible = skillCalc(self.dirigible,num) # REF; PILOT
        if skill == 'Disguise': self.disguise = skillCalc(self.disguise,num) # TECH
        if skill == 'Dodge/Escape': self.dodgeEscape = skillCalc(self.dodgeEscape,num) # REF
        if skill == 'Drive Mole': self.driveMole = skillCalc(self.driveMole, num) # TV; DRIVE
        if skill == 'Drive Tracked': self.driveTracked = skillCalc(self.driveTracked, num) # TV; DRIVE
        if skill == 'Drive Wheeled': self.driveWheeled = skillCalc(self.driveWheeled, num) # TV; DRIVE
        if skill == 'Driving': self.driving = skillCalc(self.driving,num) # REF
        
        #E
        if skill == 'Economics': self.economics = skillCalc(self.economics, num) # Consider merging with stock market
        if skill == 'Education': self.education = skillCalc(self.education,num) # INT
        if skill == 'Electrical Engineer': self.electricalEngineer = skillCalc(self.electricalEngineer, num) # TV; ENGINEER
        if skill == 'Electronics': self.electronics = skillCalc(self.electronics,num) # TECH
        if skill == 'Electronic Science': self.electronicScience = skillCalc(self.electronicScience, num)
        if skill == 'Electronic Security': self.electronicSecurity = skillCalc(self.electronicSecurity,num) # TECH
        if skill == 'Energy Pistol': self.energyPistol = skillCalc(self.energyPistol, num)
        if skill == 'Energy Rifle': self.energyRifle = skillCalc(self.energyRifle, num)
        if skill == 'Endurance': self.endurance = skillCalc(self.endurance,num) # BODY
        if skill == 'Engineer': self.engineer = skillCalc(self.engineer, num) # TV; ENGINEER
        if skill == 'Expert': self.expert = skillCalc(self.expert,num) # INT
        if skill == 'Explosives': self.explosives = skillCalc(self.explosives, num) # TV
        
        #F
        if skill == 'Fencing': self.fencing = skillCalc(self.fencing,num) # REF
        if skill == 'Field Artillery': self.fieldArtillery = skillCalc(self.fieldArtillery, num)
        if skill == 'First Aid': self.firstAid = skillCalc(self.firstAid,num) # TECH
        if skill == 'Fixed Wing': self.fixedWing = skillCalc(self.fixedWing,num) # REF; PILOT
        if skill == 'Flyer': self.flyer = skillCalc(self.flyer, num) # TV FLYER
        if skill == 'Flying': self.flying = skillCalc(self.flying, num) # TV; ATHLETICS
        if skill == 'Forgery': self.forgery = skillCalc(self.forgery,num) # TECH
        
        #G
        if skill == 'Gamble': self.gamble = skillCalc(self.gamble,num) # INT
        if skill == 'Genetics': self.genetics = skillCalc(self.genetics, num)
        if skill == 'Grav': self.grav = skillCalc(self.grav, num) # TV; FLYER
        if skill == 'Gun Combat': self.gunCombat = skillCalc(self.gunCombat, num) # TV; GUN COMBAT
        if skill == 'Gunner': self.gunner = skillCalc(self.gunner, num) # TV; GUNNER
        #if skill == 'Gyro': self.gyro = skillCalc(self.gyro,num) # REF; PILOT // REPLACED WITH ROTOR
        if skill == 'Gyro Tech': self.gyroTech = skillCalc(self.gyroTech,num) # TECH
       
        #H
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
        if skill == 'Intimidate': self.intimidate = skillCalc(self.intimidation,num) # COOL
        if skill == 'Investigate': self.investigate = skillCalc(self.investigate, num)
        
        #J
        if skill == 'J-Drive': self.jDrive = skillCalc(self.jDrive, num) # TV; ENGINEER
        if skill == 'Jack Of All Trades': self.jackOfAllTrades = skillCalc(self.jackOfAllTrades, num)
        if skill == 'Judo': self.judo = skillCalc(self.judo,num) # REF
        
        #K
        if skill == 'Karate': self.karate = skillCalc(self.karate,num) # REF
        
        #L
        if skill == 'Language': self.language = skillCalc(self.language,num) # INT
        if skill == 'Launchers': self.launchers = skillCalc(self.launchers, num)
        if skill == 'Leadership': self.leadership = skillCalc(self.leadership,num) # EMP
        if skill == 'Library Search': self.librarySearch = skillCalc(self.librarySearch,num) # INT
        if skill == 'Life Science': self.lifeScience = skillCalc(self.lifeScience, num)
        if skill == 'Life Support': self.lifeSupport = skillCalc(self.lifeSupport, num) # TV; ENGINEERING
        if skill == 'Linguistics': self.linguistics = skillCalc(self.linguistics, num)
        
        #M
        if skill == 'M-Drive': self.mDrive = skillCalc(self.mDrive, num) # TV; ENGINEER
        if skill == 'Math': self.math = skillCalc(self.math,num) # INT
        if skill == 'Mechanic': self.mechanic = skillCalc(self.mechanic, num)
        if skill == 'Melee': self.melee = skillCalc(self.melee,num) # REF
        if skill == 'Military Tactics': self.militaryTactics = skillCalc(self.militaryTactics, num)
        if skill == 'Motorboats': self.motorboats = skillCalc(self.history, num)
        if skill == 'Motorcycle': self.motorcycle = skillCalc(self.motorcycle,num) # REF
        if skill == 'MPA': self.MPA = skillCalc(self.MPA, num)
        
        #N
        if skill == 'Natural Weapon': self.naturalWeapon = skillCalc(self.naturalWeapon, num)
        if skill == 'Naval Tactics': self.navalTactics = skillCalc(self.navalTactics, num)
        if skill == 'Navigation': self.navigation = skillCalc(self.navigation, num)
        
        #O
        if skill == 'Ocean Ships': self.oceanShips = skillCalc(self.history, num)
        if skill == 'Oratory': self.oratory = skillCalc(self.oratory,num) # COOL
        if skill == 'Ortillery': self.ortillery = skillCalc(self.ortillery, num) # TV; GUNNER
        
        #P
        if skill == 'Paint or Draw': self.paintDraw = skillCalc(self.paintDraw,num) # TECH
        if skill == 'Performance': self.performance = skillCalc(self.performance,num) # EMP
        if skill == 'Personal Grooming': self.personalGrooming = skillCalc(self.personalGrooming,num) # ATTR
        if skill == 'Persuade': self.persuade = skillCalc(self.persuade, num) # EMP
        if skill == 'Pharmaceuticals': self.pharmaceuticals = skillCalc(self.pharmaceuticals,num) # TECH
        if skill == 'Philosophy': self.philosophy = skillCalc(self.philosophy, num)
        if skill == 'Photo & Film': self.photoFilm = skillCalc(self.photoFilm,num) # TECH
        if skill == 'Physical Science': self.physicalScience = skillCalc(self.physicalScience, num)
        if skill == 'Physics': self.physics = skillCalc(self.physics,num) # INT
        if skill == 'Pick Lock': self.pickLock = skillCalc(self.rifle,num) # TECH
        if skill == 'Pick Pocket': self.pickPocket = skillCalc(self.pickLock,num) # TECH
        if skill == 'Pilot': self.pilot = skillCalc(self.pilot, num)
        if skill == 'Planetology': self.planetology = skillCalc(self.planetology, num)
        if skill == 'Power': self.power = skillCalc(self.power, num) # TV; ENGINEERING
        if skill == 'Programming': self.programming = skillCalc(self.programming,num) # INT
        if skill == 'Psionicology': self.psionicology = skillCalc(self.psionicology, num)
        if skill == 'Psychology': self.psychology = skillCalc(self.psychology, num)
        
        # NO Q SKILLS
       
        #R
        if skill == 'Recon': self.recon = skillCalc(self.recon, num)
        if skill == 'Remote Operation': self.remoteOperation = skillCalc(self.remoteOperation, num)
        if skill == 'Resist Torture & Drugs': self.resistTortureDrugs = skillCalc(self.resistTortureDrugs,num) # COOL
        if skill == 'Robotics': self.robotics = skillCalc(self.robotics, num)
        if skill == 'Rotor': self.rotor = skillCalc(self.rotor, num) # TV; FLYER
        
        #S
        if skill == 'Sail': self.sail = skillCalc(self.history, num)
        if skill == 'Seafarer': self.seafarer = skillCalc(self.history, num)
        if skill == 'Sensors': self.sensors = skillCalc(self.sensors, num)
        if skill == 'Screens': self.screens = skillCalc(self.screens, num) # TV; GUNNER
        if skill == 'Sculpting': self.sculpting = skillCalc(self.sculpting, num) # TV; ART
        if skill == 'Seduction': self.seduction = skillCalc(self.seduction,num) # EMP
        if skill == 'Shadow/Track': self.shadowTrack = skillCalc(self.shadowTrack,num) # INT
        if skill == 'Shotgun': self.shotgun = skillCalc(self.shotgun, num)
        if skill == 'Slug Pistol': self.slugPistol = skillCalc(self.slugPistol, num)
        if skill == 'Slug Rifle': self.slugRifle = skillCalc(self.slugRifle, num)
        if skill == 'Small Craft': self.smallCraft = skillCalc(self.smallCraft, num)
        if skill == 'Social': self.social = skillCalc(self.social,num) # EMP
        if skill == 'Social Science': self.socialScience = skillCalc(self.socialScience, num)
        if skill == 'Sophontology': self.sophontology = skillCalc(self.sophontology, num)
        if skill == 'Spacecraft': self.spacecraft = skillCalc(self.spacecraft, num)
        if skill == 'Space Science': self.spaceScience = skillCalc(self.spaceScience, num)
        if skill == 'Stealth': self.stealth = skillCalc(self.stealth,num) # REF
        if skill == 'Steward': self.steward = skillCalc(self.steward, num)
        if skill == 'Stock Market': self.stockMarket = skillCalc(self.stockMarket,num) # INT
        if skill == 'Streetwise': self.streetwise = skillCalc(self.streetwise,num) # COOL
        if skill == 'Strength': self.strength = skillCalc(self.strength, num) # TV; ATHLETICS; BODY
        if skill == 'Submachinegun': self.submachinegun = skillCalc(self.submachinegun,num) # REF
        if skill == 'Submarine': self.submarine = skillCalc(self.history, num)
        if skill == 'Survival': self.survival = skillCalc(self.survival,num) # INT
        if skill == 'Swimming': self.swimming = skillCalc(self.swimming,num) # BODY
        if skill == 'System Knowledge': self.systemKnowledge = skillCalc(self.systemKnowledge,num) # INT
        
        #T
        if skill == 'Tae Kwon Do': self.taeKwonDo = skillCalc(self.taeKwonDo,num) # REF
        if skill == 'Teaching': self.teaching = skillCalc(self.teaching,num) # INT
        if skill == 'Tactics': self.tactics = skillCalc(self.tactics, num)
        if skill == 'Thai Kick Boxing': self.thaiKickBoxing = skillCalc(self.thaiKickBoxing,num) # REF
        if skill == 'Trade': self.trade = skillCalc(self.trade, num)
        if skill == 'Trade Biologicals': self.tradeBiologicals = skillCalc(self.tradeBiologicals, num)
        if skill == 'Trade Civil Engineering': self.tradeCivilEngineering = skillCalc(self.tradeCivilEngineering, num)
        if skill == 'Trade Space Construction': self.tradeSpaceConstruction = skillCalc(self.tradeSpaceConstruction, num)
        if skill == 'Trade Hydroponics': self.tradeHydroponics = skillCalc(self.tradeHydroponics, num)
        if skill == 'Trade Polymers': self.tradePolymers = skillCalc(self.tradePolymers, num)
        if skill == 'Turrets': self.turrets = skillCalc(self.turrets, num) # TV; GUNNER
        
        #U
        if skill == 'Unarmed': self.unarmed = skillCalc(self.unarmed, num)
        
        #V
        if skill == 'Vacc Suit': self.vaccSuit = skillCalc(self.vaccSuit, num)
        if skill == 'Vector Thrust': self.vectorThrust = skillCalc(self.vectorThrust,num) # REF; PILOT
        if skill == 'Vector Thrust Tech': self.vectorThrustTech = skillCalc(self.vectorThrustTech,num) # TECH
        if skill == 'Veterinary': self.veterinary = skillCalc(self.veterinary, num) # TV; ANIMALS
        
        #W
        if skill == 'Wardrobe & Style': self.wardrobeStyle = skillCalc(self.wardrobeStyle,num) # ATTR
        if skill == 'Weaponsmith': self.weaponsmith = skillCalc(self.weaponsmith,num) # TECH
        if skill == 'Wrestling': self.wrestling = skillCalc(self.wrestling,num) # REF
        if skill == 'Writing': self.writing = skillCalc(self.writing, num) # TV; ART
        
        #X
        if skill == 'Xenology': self.xenology = skillCalc(self.xenology, num)
        
        # NO Y SKILLS
        
        #Z
        if skill == 'Zero-G': self.zeroG = skillCalc(self.zeroG, num)
        if skill == 'Zoology': self.zoology = skillCalc(self.zoology,num) # INT       

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
