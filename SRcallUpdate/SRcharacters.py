from SRtools import *


class character():
    def __init__(self):
        self.name = 'nameErr'
        self.muscle = 0
        self.grit = 0
        self.knowledge = 0
        self.reflex = 0
        self.emp = 0
        self.intellect = 0

    def roll_stats(self):
        self.muscle = d(2,8,0)
        self.grit = d(2,8,0)
        self.knowledge = d(2,8,0)
        self.reflex = d(2,8,0)
        self.emp = d(2,8,0)
        self.intellect = d(2,8,0)

    def generate(self):
        self.name = generateName()
        self.roll_stats()
        

    def print(self):
        print(self.name)
        print(self.muscle)
        print(self.grit)
        print(self.knowledge)
        print(self.reflex)
        print(self.emp)
        print(self.intellect)
