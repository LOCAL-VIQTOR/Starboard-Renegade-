from SRcharacters import *
from SRskills import *

# TODO: ADD ENEMIES
    #   VERIFY ALL SKILL STRINGS
    #   CONSIDER LOWING AMOUNT OF SKILLS TRAINED (CURRENTLY 40) // LINE 37

class occupation():
    def __init__(self):
        self.role = ''
        self.occupation = ''
        self.monthsWorked = 0
        self.lifeEvents = []
    
    def aptitudeTest(self,character):
        classesList = ['Rockerboy', 'Solo', 'Netrunner', 'Techie', 'Medtechie', 'Cop', 'Corporate', 'Fixer', 'Nomad']
        if character.intel > 7:
            classesList.append('Netrunner')
            classesList.append('Corporate')
        if character.reflex > 7:
            classesList.append('Solo')
            classesList.append('Nomad')
            classesList.append('Rockerboy')
        if character.ingen > 7:
            classesList.append('Techie')
            classesList.append('Medtechie')
        if character.grit > 7:
            classesList.append('Solo')
            classesList.append('Nomad')
            classesList.append('Rocker')
            classesList.append('Fixer')
        if character.emp > 7:
            classesList.append('Media')
            classesList.append('Rockerboy')
        if character.muscle > 7:
            classesList.append('Solo')
            classesList.append('Rockerboy')
            classesList.append('Nomad')
        role = random.choice(classesList)
        self.role = role

    # rolling class skills now in the character
    def rollSkills(self,character):
        grog = True
        classSkills = []
        if grog == True:
            skillDistribution = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(39):
                x = random.randint(0, len(skillDistribution) - 1)
                while skillDistribution[x] >= 10: x = random.randint(0, len(skillDistribution) - 1)
                skillDistribution[x] += 1
                
            if self.role == 'Solo':
                gunAmmo = random.choice(['Energy ','Slug'])
                handgun = gunAmmo + 'Pistol'
                rifle = gunAmmo + 'Rifle'
                classSkills = ['Combat Sense',
                               'Awareness/Notice',
                               handgun,
                               'Martial Arts (any)',
                               'Brawling',
                               'Weaponsmith',
                               rifle,
                               'Athletics',
                               'Submachinegun', # The eternal question. . . Should I include E. Submachine guns?
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
                gunAmmo = random.choice(['Energy ','Slug'])
                rifle = gunAmmo + 'Rifle'
                classSkills = ['Family',
                               'Awareness/Notice',
                               'Endurance',
                               'Melee',
                               rifle,
                               'Driving',
                               'Basic Tech',
                               'Survival',
                               'Brawling',
                               'Athletics']
            if self.role == 'Techie': # Replace "Techie Skills" with Basic Tech, Mechanic, and Engineering Skills
                #techieSkills = ['Aero Tech',
                #                'Vector Thrust Tech',
                #                'Cryotank',
                #                'Cyberdeck Design',
                #                'Demolitions',
                #                'Disguise',
                #                'Electronic Security',
                #                'First Aid',
                #                'Forgery',
                #                'Gyro Tech',
                #                'Paint or Draw',
                #                'Photo & Film',
                #                'Pharmaceuticals',
                #                'Pick Lock',
                #                'Pick Pocket',
                #                'Instrument',
                #                'Weaponsmith']
                
                # NEW Techie Skills
                techieSkills = ['Demolitions','Engineer','M-Drive','J-Drive','Life Support','Power',
                                'Cryotank','Cyberdeck Design','Explosives','Weaponsmith',
                                'Mechanic','Aero Tech','Vector Thrust Tech','Electronic Security','Gyro Tech']

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
                               'Persuade',
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
                gunAmmo = random.choice(['Energy ','Slug '])
                handgun = gunAmmo + 'Pistol'
                classSkills = ['Streetdeal',
                               'Awareness/Notice',
                               'Forgery',
                               handgun,
                               'Brawling',
                               'Melee',
                               'Pick Lock',
                               'Pick Pocket',
                               'Intimidate',
                               'Persuade']
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
                gunAmmo = random.choice(['Energy ','Slug '])
                handgun = gunAmmo + 'Pistol'
                classSkills = ['Authority',
                               'Awareness/Notice',
                               handgun,
                               'Human Perception',
                               'Athletics',
                               'Education',
                               'Brawling',
                               'Melee',
                               'Interrogation',
                               'Streetwise']

            # Train the skills as their random distribution
            for i in range(len(skillDistribution)):
                character.skills.train(self,classSkills[i],skillDistribution[i]) # OOR

            # ROLL PICKUP SKILLS
            # MASTER SKILLS LIST NEEDS TO BE UPDATED
            # OR ELSE PICKUP SKILLS MUST BE REWRITTEN    
            masterSkillsList = ['Personal Grooming','Wardrobe & Style','Endurance','Strength','Swimming','Interrogation','Intimidate','Oratory','Resist Torture & Drugs','Streetwise','Human Perception','Interview','Leadership','Seduction','Social','Persuasion','Performance','Accounting','Anthropology','Awareness/Notice','Biology','Botany','Chemistry','Composition','Diagnose Illness','Education','Expert','Gamble','Hide/Evade','History','Language','Library Search','Math','Physics','Programming','Shadow/Track','Stock Market','System Knowledge','Teaching','Survival','Zoology','Archery','Athletics','Brawling','Dancing','Dodge/Escape','Driving','Fencing','Handgun','Heavy Weapons','Aikido','Animal Kung Fu','Boxing','Capoeria','Choi Li Fut','Judo','Karate','Tae Kwon Do','Thai Kick Boxing','Wresling','Melee','Moorcycle','Heavy Machinery','Gyro','Fixed Wing','Dirigible','Vector Thrust','Rifle','Stealth','Submachinegun','Aero Tech','Vector Thrust Tech','Basic Tech','Cryotank','Cyberdeck Design','Cyber Tech','Demolitions','Disguise','Electronics','Electronic Security','First Aid','Forgery','Gyro Tech','Paint or Draw','Photo & Film','Pharmaceuticals','Pick Lock','Pick Pocket','Instrument','Weaponsmith']
            skillsList = []
            for i in range(len(masterSkillsList)):
                if masterSkillsList[i] not in classSkills: skillsList.append(masterSkillsList[i])
            pointsAvailable = character.intel + character.reflex
            numSkills = random.randint(1,pointsAvailable)
            pickupSkills = []
            pickupDistribution = []
            for i in range(numSkills):
                pickupDistribution.append(0)
                x = random.randint(1,len(skillsList)-1)
                pickupSkills.append(skillsList[x])
                skillsList.remove(skillsList[x])
            for i in range(pointsAvailable):
                if len(pickupDistribution) <= 1: x = 1
                if len(pickupDistribution) > 1:x = random.randint(1,len(pickupDistribution)-1) # EMPTY RANGE
                while pickupDistribution[x] >= 10: x = random.randint(1,len(pickupDistribution)-1)
                pickupDistribution[x] += 1
            for i in range(len(pickupDistribution)):
                character.skills.train(character,pickupSkills[i],pickupDistribution[i])

    def occupationTable(self,character):
        # Returns occupation from CP2020 p.58 'Occupation Table'.
        # Rocker
        if self.role == 'Rockerboy':
            if character.skills.charismaticLeadership <= 5: self.occupation = ['Desperate for gigs', 1000]
            if character.skills.charismaticLeadership == 6: self.occupation = ['Regular Club Jobs', 1500]
            if character.skills.charismaticLeadership == 7: self.occupation = ['Play the Big Clubs', 2000]
            if character.skills.charismaticLeadership == 8: self.occupation = ["You've got a Contract", 5000]
            if character.skills.charismaticLeadership == 9: self.occupation = ['Concert Band', 8000]
            if character.skills.charismaticLeadership == 10: self.occupation = ['Major Act', 12000]
        # Solo
        if self.role == 'Solo':
            if character.skills.combatSense <= 5: self.occupation = ['Street Ronin', 2000]
            if character.skills.combatSense == 6: self.occupation = ['Private Enforcer', 3000]
            if character.skills.combatSense == 7: self.occupation = ['Corporate Muscle', 4500]
            if character.skills.combatSense == 8: self.occupation = ['Professional Operative', 7000]
            if character.skills.combatSense == 9: self.occupation = ['Major League Hitter', 9000]
            if character.skills.combatSense == 10: self.occupation = ['Solo Elite', 12000]
        # Cop
        if self.role == 'Cop':
            if character.skills.authority <= 5: self.occupation = ['Private Guard', 1000]
            if character.skills.authority == 6: self.occupation = ['City Cop', 1200]
            if character.skills.authority == 7: self.occupation = ['Corporate Guard/Detective', 3000]
            if character.skills.authority == 8: self.occupation = ['Corporate Secutiry/Psycho Squad', 5000]
            if character.skills.authority == 9: self.occupation = ['Enforcement Team Leader', 7000]
            if character.skills.authority == 10: self.occupation = ['Security Head/Police Chief', 9000]
        # Corporate
        if self.role == 'Corporate':
            if character.skills.resources <= 5: self.occupation = ['Assistant', 1500]
            if character.skills.resources == 6: self.occupation = ['Manager', 3000]
            if character.skills.resources == 7: self.occupation = ['Junior Executive', 5000]
            if character.skills.resources == 8: self.occupation = ['Executive', 7000]
            if character.skills.resources == 9: self.occupation = ['Department Head', 9000]
            if character.skills.resources == 10: self.occupation = ['Division Head', 12000]
        # Media
        if self.role == 'Media':
            if character.skills.credibility <= 5: self.occupation = ['Stringer Reporter', 1000]
            if character.skills.credibility == 6: self.occupation = ['Staff Reporter', 1200]
            if character.skills.credibility == 7: self.occupation = ['Section Editor', 3000]
            if character.skills.credibility == 8: self.occupation = ['Producer/Managing Editor', 5000]
            if character.skills.credibility == 9: self.occupation = ['Local Media Personality', 7000]
            if character.skills.credibility == 10: self.occupation = ['National Media Personality', 10000]
        # Fixer
        if self.role == 'Fixer':
            if character.skills.streetdeal <= 5: self.occupation = ['Street Punk', 1500]
            if character.skills.streetdeal == 6: self.occupation = ['Gang Leader', 3000]
            if character.skills.streetdeal == 7: self.occupation = ['Enforcer', 5000]
            if character.skills.streetdeal == 8: self.occupation = ['Sub-Lieutenant', 7000]
            if character.skills.streetdeal == 9: self.occupation = ['Lieutenant', 8000]
            if character.skills.streetdeal == 10: self.occupation = ['Crime Boss', 10000]
        # Techie
        if self.role == 'Techie':
            if character.skills.juryRig <= 5: self.occupation = ['Local Fixit Man', 1000]
            if character.skills.juryRig == 6: self.occupation = ['Private Operator', 2000]
            if character.skills.juryRig == 7: self.occupation = ['Corporate Tech', 3000]
            if character.skills.juryRig == 8: self.occupation = ['Junior Engineer', 4000]
            if character.skills.juryRig == 9: self.occupation = ['Engineer', 5000]
            if character.skills.juryRig == 10: self.occupation = ['Senior Engineer', 8000]
        # Netrunner
        if self.role == 'Netrunner':
            if character.skills.interface <= 5: self.occupation = ['Weefle Runner', 1000]
            if character.skills.interface == 6: self.occupation = ['Hacker', 2000]
            if character.skills.interface == 7: self.occupation = ['Bit Jockey', 3000]
            if character.skills.interface == 8: self.occupation = ['Net Cowboy', 5000]
            if character.skills.interface == 9: self.occupation = ['Deckslinger', 7000]
            if character.skills.interface == 10: self.occupation = ['Sysop', 10000]
        # Medtechie
        if self.role == 'Medtechie':
            if character.skills.medicalTech <= 5: self.occupation = ['Patchman', 1600]
            if character.skills.medicalTech == 6: self.occupation = ['Medical Technician', 3000]
            if character.skills.medicalTech == 7: self.occupation = ['RipperDoc', 5000]
            if character.skills.medicalTech == 8: self.occupation = ['Trauma Team Medic', 7000]
            if character.skills.medicalTech == 9: self.occupation = ['General Practitioner', 10000]
            if character.skills.medicalTech == 10: self.occupation = ['Specialist Physician', 15000]
        # Nomad
        if self.role == 'Nomad':
            if character.skills.family <= 5: self.occupation = ['Clanmember', 1000]
            if character.skills.family == 6: self.occupation = ['Warrior', 1500]
            if character.skills.family == 7: self.occupation = ['Head of Household', 2000]
            if character.skills.family == 8: self.occupation = ['Scout', 3000]
            if character.skills.family == 9: self.occupation = ['Clan Senior', 4000]
            if character.skills.family == 10: self.occupation = ['Family Head', 5000]

        self.monthsWorked = d(1,6,0) / 3
        character.credits += (self.monthsWorked * self.occupation[1]) // 1

    def bigProblemsBigWins(self,character):
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
                character.credits -= debt
                return ('Financial Loss/Debt: ' + str(debt) + ' Cr.' + ' (' + action + ')')
            if x == 2:
                timeImprisoned = random.randint(1, 10)
                imprisonment = ['imprisoned', 'held hostage']
                return ('You have been ' + random.choice(imprisonment) + ' for ' + str(
                    timeImprisoned) + ' months.' + ' (' + action + ')')
            if x == 3:
                issues = ['an illness', 'a drug habit']
                character.reflex -= 1
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
                    return 'You are disfigured in a horrible accidents (-5 EMP)' + ' (' + action + ')'
                    self.emp = self.emp - 5
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
                    character.reflex -= 1
                    return 'You suffer some kind of nervous disorder, probably from bioplague (-1 REF)' + ' (' + action + ')'
                if y >= 4 and y <= 7:
                    character.grit -= 1
                    return 'You suffer from anxiety attacks and phobias (-1 GRIT)' + ' (' + action + ')'
                if y > 8:
                    character.reflex -= 1
                    character.grit -= 1
                    return 'You suffer from a major psychosis and hear voices, are irrational, violent, depressive (-1 CL -1 REF)' + ' (' + action + ')'

        # YOU GET LUCKY
        if oddResult == False:
            x = d(1,10,0)

            if x == 1:
                connections = ['Police Department', "District Attorney's Office", "Mayor's Office"]
                return 'Make a powerful connection in the ' + random.choice(connections)

            if x == 2:
                windfall = d(1,10,0) * 100
                character.credits += windfall
                return 'Financial Windfall: +' + str(windfall) + ' Cr.'

            if x == 3:
                yourCut = d(1,10,0) * 100
                character.credits += yourCut
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
                character.skills.train(character,martialArt,1)
                character.skills.train(character,martialArt,-1)
                return 'You find ' + martialArt + ' Sensei'

            if x == 5:
                intSkills = ['Accounting', 'Anthropology', 'Awareness/Notice', 'Biology',
                             'Botany', 'Chemistry', 'Composition', 'Diagnose Illness', 'Education',
                             'Expert', 'Gamble', 'Hide/Evade', 'History', 'Language', 'Library Search',
                             'Mathematics', 'Physics', 'Programming', 'Shadow/Track', 'Stock Market',
                             'System Knowledge', 'Teaching', 'Wilderness Survival', 'Zoology']
                intSkill = random.choice(intSkills)
                character.skills.train(character,intSkill,1)
                character.skills.train(character,intSkill,-1)
                return 'You find a legendary ' + intSkill + ' teacher.'

            if x == 6:
                character.skills.executiveFavor = True
                return 'Powerful corporate exec owes you one favor'
            if x == 7:
                character.skills.befriendedNomad = True
                return 'Befriended Nomad Pack: Family +2 1/mo.'
            if x == 8:
                character.skills.befriendedPolice = True
                return 'Befriend Police Force Member: +2 Streetwise with Police Business'
            if x == 9:
                character.skills.befriendedGang = True
                return 'Befriended Local Boostergang: Family +2 1/mo.'

            if x == 10:
                combatSkills = ['Dodge/Escape', 'Fencing', 'Handgun', 'Heavy Weapons', 'Melee', 'Rifle',
                                'Submachinegun']
                chosenSkill = random.choice(combatSkills)
                character.skills.train(character,chosenSkill,1)
                character.skills.train(character,chosenSkill,-1)
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

    def lifeEventsGenerator(self,character):
        self.lifeEvents = []
        character.age = d(2,6,16)
        yearsToRoll = character.age - 16
        for i in range(yearsToRoll):
            x = d(1,10,0)
            if x < 4:
                self.lifeEvents.append(self.bigProblemsBigWins(character))
            if x >= 4 and x < 7: self.lifeEvents.append(self.friendsAndEnemies())
            if x == 7 or x == 8:
                self.lifeEvents.append(self.romanticLife())
            if x > 8: self.lifeEvents.append('Nothing Happened')
