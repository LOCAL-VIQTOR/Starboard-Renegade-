# SR backstory
import random

class backstory():
    def __init__(self):
        self.personality = ''
        self.valuedPerson = ''
        self.virtue = ''
        self.disposition = ''
        self.valuedPossession = ''
        self.parents = ''
        self.family_status = False
        self.tragedy = ''
        self.childhood_env = ''
        self.siblings = []

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
        if self.family_status == True: self.tragedy = random.choice(family_tragedies)
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

    def generateBackstory(self, homeworldTL):
        self.childhood()
        self.motivations()

    def print(self):
        print(self.personality)
        print(self.valuedPerson)
        print(self.virtue)
        print(self.disposition)
        print(self.valuedPossession)
        print(self.parents)
        print(self.family_status)
        print(self.tragedy)
        print(self.childhood_env)
        print(self.siblings)
        
