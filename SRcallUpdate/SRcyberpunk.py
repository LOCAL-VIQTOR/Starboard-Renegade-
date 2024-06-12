import random
from SRtools import *

#   ________  ______  __________  ____  __  ___   ____ __
#  / ____/\ \/ / __ )/ ____/ __ \/ __ \/ / / / | / / //_/
# / /      \  / __  / __/ / /_/ / /_/ / / / /  |/ / ,<
# / /___    / / /_/ / /___/ _, _/ ____/ /_/ / /|  / /| |
# \____/   /_/_____/_____/_/ |_/_/    \____/_/ |_/_/ |_|
# CYBERPUNK NPC GENERATOR FUNCTIONS
# TO BE REMOVED ONCE THE SKILL HANDLER IS COMPLETE

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
