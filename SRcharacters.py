import random
from SRtools import *
from SRplanets import *
from SRskills import *
from SRbackstory import *
from SRoccupation import *
from SRlifepath import *

# Returns a modifier based on a character's ability score
def characteristic_modifier(score):
    if score == 0: return -3
    if score == 1 or score == 2: return -2
    if score >= 3 and score <= 5: return -1
    if score >= 6 and score <= 8: return 0
    if score >= 9 and score <= 11: return 1
    if score >= 12 and score <= 14: return 2
    if score >= 15: return 3

def amod(score):
    if score == 0: return -3
    if score == 1 or score == 2: return -2
    if score >= 3 and score <= 4: return -1
    if score >= 5 and score <= 6: return 0
    if score >= 7 and score <= 8: return 1
    if score >= 9 and score <= 10: return 2
    if score >= 11: return 3

class character():
    def __init__(self):
        self.name = 'nameErr'
        self.muscle = 0
        self.reflex = 0
        self.grit = 0
        self.intel = 0
        self.ingen = 0
        self.emp = 0
        self.age = 16
        self.homeworld = 'homeworldErr'
        self.childhood = 'childhoodErr'
        self.equipped = 'equipErr'
        self.inventory = []
        self.clothes = ''
        self.hairstyle = ''
        self.affectations = ''
        self.occupation = 'roleErr'
        self.skills = 'skillErr'
        self.armor = ''
        self.credits = 0
        self.lifepath = 'lifepathErr'

    def roll_stats(self):
        self.muscle = d(2,6,0)
        self.grit = d(2,6,0)
        self.ingen = d(2,6,0)
        self.reflex = d(2,6,0)
        self.emp = d(2,6,0)
        self.intel = d(2,6,0)

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

    def generate(self,homeworld):
        self.name = generateName()                                                  # Generate a name for the character.
        self.roll_stats()                                                           # Roll the character's ability scores.
        self.homeworld = homeworld                                                  # Set the included planet as the homeworld.
        history = backstory()                                                       # Create an instance of the backstory() class.
        history.generateBackstory(homeworld.uwp[7])                                 # Generate a backstory in the created instance.
        self.backstory = history                                                    # Sets the character's backstory as the created backstory.
        home_skill = self.backstory.homeworld_skills(self)                          # Creates a variable containing the 'homeworld skill'.
        tiein = generateName()                                                      # Generates a name for a tie-in character.
        self.backstory.valuedPerson = tiein+' ('+self.backstory.valuedPerson+')'    # Sets the tie-in for our main character's most valued person.
        self.personalStylist()                                                      # Sets the character's hair, clothing, and affectations.
        p_occupy = occupation()                                                     # Creates an instance of the occupation() class.
        self.occupation = p_occupy                                                  # Sets the character's occupation as the created instance.
        self.occupation.aptitudeTest(self)                                          # Decides the character's sabatical job based on ability scores.
        p_skills = skills(self)                                                     # Creates an instance of the skills() class.
        self.skills = p_skills                                                      # Set the character's skills as the instance.
        self.skills.train(self,home_skill[0],home_skill[1])                         # Trains the character in their native homeworld skill.
        self.occupation.rollSkills(self)                                            # Rolls the character's occupation skills.
        self.occupation.occupationTable(self)                                       # Gives the character a job for initial funds.
        self.occupation.lifeEventsGenerator(self)                                   # Generates a number of life events to apply to the character.
        
        self.age = self.age + len(self.occupation.lifeEvents)                       # Sets character age to 16 plus the number of life events.
        p_lifepath = lifepath()                                                     # Creates an instance of the lifepath() class.
        self.lifepath = p_lifepath                                                  # Sets the character's lifepath as the instance. 
        self.lifepath.careerAge = self.age                                          # Sets the starting age for your lifepath as the current age. 

        self.lifepath.career = 'Drifter'                                            # Sets the career path as 'Drifter' for troubleshooting purposes.
        self.lifepath.drifter_career_check(self)                                    # Performs a 'career check'. I don't know what that means. (Hello, God? Are you there?)
        
        
    def characterNiche(self):
        stockRegion = self.homeworld.stock
        firstLanguage = self.homeworld.language
        occupation = self.occupation.occupation[0]
        if stockRegion == 'Hispanic American': firstLanguage = 'Mexican'
        if self.occupation.role == 'Rockerboy': occupation = "Rockerboy: " + occupation
        if stockRegion == 'African': firstLanguage = 'African'
        if firstLanguage == 'Mandarin': firstLanguage = 'Chinese'
        if stockRegion == 'Anglo-American': firstLanguage = 'American'
        if firstLanguage == 'Lingua Astra': firstLanguage = 'Starcitizen'
        if firstLanguage == 'Alien Language': firstLanguage = 'Alien'
        print(self.backstory.personality+' '+firstLanguage + ' ' + occupation)

    def appearance(self):
        hair = self.hairstyle
        if hair != 'Bald' and hair != 'Mohawk': hair = hair + ' hair'
        clothes = self.clothes
        if clothes == 'Nude': clothes = 'a Nudist disposition'
        affect = self.affectations
        print(hair+', '+clothes+' and '+affect)

    def print(self):
        print('Name: ' + str(self.name))
        self.characterNiche()
        self.appearance()
        print('Homeworld: ' + str(self.homeworld.name))
        print('Credits: '+str(self.credits))
        print('Muscles: ' + str(self.muscle))
        print('Grit: ' + str(self.grit))
        print('Ingenuity: ' + str(self.ingen))
        print('Reflexes: ' + str(self.reflex))
        print('Empathy: ' + str(self.emp))
        print('Intellect: ' + str(self.intel))
        
        print('V. Person: ' + self.backstory.valuedPerson)
        print('Virtue: ' + self.backstory.virtue)
        print('Disposition: ' + self.backstory.disposition)
        print('V. Possession: ' + self.backstory.valuedPossession)
        print('Parents: ' + self.backstory.parents)
        print('F. Status: ' + str(self.backstory.family_status))
        print('Tragedy: ' + self.backstory.tragedy)
        print('Childhood Env.: ' + self.backstory.childhood_env)
        print('Siblings: ')
        print(self.backstory.siblings)
        self.skills.printSkills()
        for i in range(len(self.occupation.lifeEvents)):
            print(str(16+i)+': '+self.occupation.lifeEvents[i])

        print(self.lifepath.career)
        print(self.lifepath.specialization)
        for i in range(len(self.lifepath.events)):
            print(self.lifepath.events[i])

def ctest(): # For testing character generation.
    home = planet()
    home.generate(['0505'],True)
    diana = character()
    
    diana.generate(home)
    diana.print()
