from SRcharacters import *

class relationships():
    def __init__(self):
        self.friends = []
        self.enemies = []
        self.rivals = []
        self.contacts = []
        self.patrons = []

    def add(self,name,occupation,charType):
        npc = character()
        npc.roll_stats()
        npc.personalStylist()
        npc.name = name
        npc.occupation = occupation
        if charType == 'friend': self.friends.append(npc)
        if charType == 'enemy': self.enemies.append(npc)
        if charType == 'rival': self.rivals.append(npc)
        if charType == 'contact': self.contacts.append(npc)
        if charType == 'patron': self.patrons.append(npc)
        
