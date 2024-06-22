from SRtools import *
from SRskills import *
from SRcharacters import *

def injure(character,mus,ref,grit):
    character.muscle -= mus
    character.reflex -= ref
    character.grit -= grit

class lifepath():
    def __init__(self):
        self.career = 'CarErr'
        self.specialization = 'SpecErr'
        
        self.careerAge = 0
        self.term = 0
        self.firstCareer = True
        self.survival = [7,'GRIT']
        self.advancement = [7,'GRIT']

        self.qualifyMod = 0
        self.benefitMod = []
        
        self.personalDevelopment = []
        self.serviceSkills = []
        self.specialistSkills = []
        self.advancedEducation = []
        self.officerSkills = []

        self.commission = False
        self.advEducation = 0

        self.mishaps = []
        self.events = []

        self.rank = 0
        self.ranks = []
        self.benefits = []
        
        self.cashBenefits = []
        self.otherBenefits = []
        self.ejected = False

    # Roll for qualification. If not qualified, just move on to the next. 
    # If this is the first career, have them go through basic training and add 1 to age
    
        # If not, just pick a single skill? double check this
    # roll to see if you survive or if you are ejected
    # add 1 to term
    # if you survive, pick valid skill tables
    # from valid skill tables, pick a skill to train
    # roll to see if you advance in rank
        # award title and rank benefits





    def performTerm(self,character):
        mod = 0
        if self.survival == 'GRIT': mod = amod(character.grit)

        self.term += 1

        survival_roll = d(2,6,mod)
        if survival_roll >= self.survival[0]:
            # when you survive
            skillTables = [self.personalDevelopment,self.serviceSkills,self.specialistSkills]
            if character.intel >= self.advEducationDC and self.advancedEducation != []: skillTables.append(self.advancedEducation)
            if self.commission == True and self.officerSkills != []: skillTables.append(self.officerSkills)
            skillTrained = random.choice(random.choice(skillTables))
            character.skills.train(character,skillTrained,-1)

            event = self.eventHandler(d(2,6,0))


    def eventHandler(self,character,result):
        if self.career == 'Drifter':
            if result == 2:
                injury = injury_table(character,d(1,6,0))
                event = 'Disaster! You receive an injury but are not ejected. ' + injury
            if result == 3:
                event = 'A patron offers you a chance at a job. If you accept, gain +4 to your next qualification roll but you owe them one favor.'
                self.qualifyMod += 4
            if result == 4:
                skill = random.choice(['Jack of all Trades','Survival','Streetwise','Melee (Any)'])
                event = 'You pick up a few skills: '+self.skill+'.'
                character.skills.train(character,skill,-1)
            if result == 5:
                event = 'You manage to scavenge something of use. +1DM to any 1 benefit roll.'
                self.benefitMod.append(1)
            if result == 6:
                event = 'You encounter something unusual. Go to the life events table and have an unusual event.'
                # life events
            if result == 7:
                event = 'Life events. Roll on the life events table.'
                # life events
            if result == 8:
                event = 'You are attacked by enemies. Gain an enemy if you do not have one already. Roll either Melee (Any) 8+, Gun Combat (Any) 8+, or Stalth 8+ to avoid an injury on the injury table.'
                # choose which skill to roll and then add the injury table
            if result == 9:
                
                y = random.randint(1,3)
                if y == 1:
                    outcome = injury_table(character,d(1,6,0))
                if y == 2: outcome = 'No Reward'
                if y == 3:
                    outcome = '+4 to one Benefit Roll'
                    self.benefitMod.append(4)
                event = 'You are offered a chance to take part in a risky but rewarding adventure. if you accept, '+outcome
            if result == 10:
                event = 'life on the edge hones your abilities. Increase any skill you already have by 1.'
                # how would I check to see what kind of skills I already have?
            if result == 11:
                event = 'You are forcibly drafted. Join the draft next term.'
                # on pause until draft is up
            if result == 12:
                event = 'You thrive on adversity. You are automatically promoted.'
                self.rank += 1
                # rank upgrade services

        return event
            


    def injury_table(self, character, x):
        if x == 0:
            x = random.randint(1, 6)
        if x == 1:
            ability_loss = ['Mus', 'Ref', 'Grit']
            ability_lost = random.choice(ability_loss)
            loss_amount = random.randint(1, 6)
            y = random.randint(1, 2)
            if y == 1:
                if ability_lost == 'Mus':
                    injure(character,loss_amount,2,2)
                    return 'Nearly Killed. (Mus -' + str(loss_amount) + ' Ref -2 Grit -2)'
                if ability_lost == 'Ref':
                    injure(character,2,loss_amount,2)
                    return 'Nearly Killed. (Mus -2 Dex -' + str(loss_amount) + ' Grit -2)'
                if ability_lost == 'Grit':
                    injure(character,2,2,loss_amount)
                    return 'Nearly Killed. (Mus -2 Ref -2 Grit - '+ str(loss_amount)+')')
            if y == 2:
                if ability_lost == 'Mus':
                    second_ability = random.choice(['Ref','Grit'])
                    if second_ability == 'Ref': injure(character,loss_amount,4,0)
                    if second_ability == 'Grit': injure(character,loss_amount,0,4)
                    return 'Nearly Killed. (Mus -' + str(loss_amount) + ' '+second_ability+' -4)'
                if ability_lost == 'Grit':
                    second_ability = random.choice(['Ref','Mus'])
                    if second_ability == 'Ref': injure(character,0,4,loss_amount)
                    if second_ability == 'Mus': injure(character,4,0,loss_amount)
                    return 'Nearly Killed. (Grit -' + str(loss_amount) + ' '+second_ability+' -4)'
                if ability_lost == 'Ref':
                    second_ability = random.choice(['Mus','Grit'])
                    if second_ability == 'Mus': injure(character,4,loss_amount,0)
                    if second_ability == 'Grit': injure(character,0,loss_amount,4)
                    return 'Nearly Killed. (Ref -' + str(loss_amount) + ' '+second_ability+' -4)'
        if x == 2:
            y = random.randint(0,2)
            ability_loss = ['Mus', 'Ref', 'Grit']
            ability_lost = ability_loss[y]
            iData = [character,0,0,0]
            iData[y+1] = random.randint(1,6)
            injure(iData[0],iData[1],iData[2],iData[3])
            return 'Severely Injured (' + ability_lost + ' -' + str(iData[y+1]) + ')'
        if x == 3:
            ability_loss = ['Mus', 'Ref']
            ability_lost = random.choice(ability_loss)
            if ability_lost == 'Ref':
                part_lost = ['Missing eye (Ref -2)', 'Missing Arm (Ref -2)']
                injure(charater,0,2,0)
            if ability_lost == 'Mus':
                part_lost = ['Missing Leg (Mus -2)', 'Missing Arm (Mus -2)']
                injure(character,2,0,0)
            injury = random.choice(part_lost)
            return injury
        if x == 4:
            y = random.randint(0,2)
            ability_loss = ['Mus', 'Ref', 'Grit']
            ability_lost = ability_loss[y]
            iData = [character,0,0,0]
            iData[y+1] = 2
            injure(iData[0],iData[1],iData[2],iData[3])
            return 'Scarred (' + ability_lost + ' -2)'
        if x == 5:
            y = random.randint(0,2)
            ability_loss = ['Mus', 'Ref', 'Grit']
            ability_lost = ability_loss[y]
            iData = [character,0,0,0]
            iData[y+1] = 1
            injure(iData[0],iData[1],iData[2],iData[3])
            return 'Injured (' + ability_lost + ' -1)'
        if x == 6: return 'Lightly Injured: No permanent effect'



    def careerSetup(self,character):
        if self.career == 'Drifter':
            self.personalDevelopment = ['MUS','GRIT','REF','Jack of all Trades','GRIT','INT']
            self.serviceSkills = ['Athletics (Any)','Melee (Unarmed)','Recon','Streetwise','Stealth','Survival']
            if self.specialization == 'Barbarian':
                self.specialistSkills = ['Animals (any)', 'Carouse (any)', 'Melee (Blade)', 'Stealth', 'Seafarer (any)', 'Survival']
                self.ranks = [['',''],['','Survival'],['Warrior','Melee (Blade)'],['Warrior',''],['Chieftan','Leadership'],['Chieftan',''],['Chieftan','']]
        

    def drifter_career_check(self,character):
        if self.career == 'Drifter':
            self.personalDevelopment = ['MUS','GRIT','REF','Jack of all Trades','GRIT','INT']
            self.serviceSkills = ['Athletics (Any)','Melee (Unarmed)','Recon','Streetwise','Stealth','Survival']
            assignments = ['Barbarian', 'Wanderer', 'Scavenger']
            self.specialization = random.choice(assignments)
            if self.specialization == 'Barbarian':
                self.specialistSkills = ['Animals (any)', 'Carouse (any)', 'Melee (Blade)', 'Stealth', 'Seafarer (any)', 'Survival']
                self.ranks = ['','','Warrior','','Chieftan','','']
                self.benefits = ['','Survival','Melee (Blade)','','Leadership','','']
            if self.specialization == 'Wanderer':
                self.specialistSkills = ['Athletics (any)', 'Deception', 'Recon', 'Stealth', 'Streetwise', 'Survival']
                self.ranks = ['','','','','','','']
                self.benefits = ['','Streetwise','','Deception','','']
            if self.specialization == 'Scavenger':
                self.specialistSkills = ['Pilot (Small Craft)', 'Mechanic', 'Astrogation', 'Vacc Suit', 'Zero-G', 'Gun Combat (any)']
                self.ranks = ['','','','','','','']
                scavSkill = random.chaoice(['Trade (Belter)','Mechanic'])
                self.benefits = ['','Vacc Suit','',scavSkill,'','']
            self.events.append('Aquired '+self.specialization+' skills.')
            if self.firstCareer == False: character.skills.train(character,random.choice(self.specialistSkills),1)
            if self.firstCareer == True:
                for i in range(len(self.serviceSkills)): character.skills.train(character,self.specialistSkills[i],1)
                self.firstCareer = False
            self.cashBenefits = [0,0,1000,2000,3000,4000,8000]
            self.otherBenefits = ['Contact','Weapon','Ally','Weapon','ING','Ship Share','2 Ship Shares']
            

    def drifter_term(self,character):
        survival_mod = 0
        mishap = False
        mishap_event = ''
        if self.specialization == 'Barbarian': survival_mod = self.grit
        s_roll = d(2,6,amod(survival_mod))
        if s_roll < 7: mishap = True
        if mishap == True:
            x = d(1,6,0)
            if x == 1:
                mishap_event
        if perished == False:
            trainedSkill = random.choice(random.choice([self.personalDevelopment,self.serviceSkills,self.specialistSkills]))
            return trainedSkill
            character.skills.train(character,trainedSkill,-1)
