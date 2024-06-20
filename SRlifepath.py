from SRtools import *
from SRskillsheet import *
from SRcharacters import *

class lifepath():
    def __init__(self):
        self.career = 'CarErr'
        self.specialization = 'SpecErr'
        self.careerAge = 0
        self.rank = 0
        self.term = 0
        self.firstCareer = True
        self.events = []
        self.personalDevelopment = []
        self.serviceSkills = []
        self.specialistSkills = []
        self.ranks = []
        self.benefits = []
        self.cashBenefits = []
        self.otherBenefits = []

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
                for i in range(len(service_skills)): character.skills.train(character,self.specialistSkills[i],1)
                self.firstCareer = False
            self.cashBenefits = [0,0,1000,2000,3000,4000,8000]
            self.otherBenefits = ['Contact','Weapon','Ally','Weapon','ING','Ship Share','2 Ship Shares']
            

    def drifter_term(self,character):
        if self.specialization == 'Barbarian':
            s_roll = d(2,6,amod(character.grit))
            if s_roll >= 7:
                trainedSkill = random.choice(random.choice([self.personalDevelopment,self.serviceSkills,self.specialistSkills]))
                print(trainedSkill)
                character.skills.train(character,trainedSkill,-1)
