import random
from SRtools import *

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
