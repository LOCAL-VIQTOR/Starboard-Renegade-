import random
from SRtools import d

class Equipment():
    def __init__(self,name,tl,mass,cost,skill='No Skill',desc='No Description',computer=False,make='Generic',model='Generic',origin='Unknown'):
        self.name = name
        self.skill = skill
        self.description = desc
        self.tl = tl
        self.mass = mass
        self.cost = cost
        self.computer = computer
        self.make = make
        self.model = model
        self.origin = origin

    def manufacturer(make='Sierra Galactic Shipping & Supply Co.',model='',origin='SIER Production Facility #8911'):
        self.make = make
        if model == '': self.model = 'TL' + str(self.tl) + ' ' + self.name
        else: self.model = model
        self.origin = origin

class Armor(Equipment):
    def __init__(self,name,slot,sp,hard,cost,ev=0,desc='',tl=0,mass=0):
        self.sp = sp
        self.slot = slot
        self.hard = hard
        self.ev = ev
        if desc == '': desc = slot + ' Armor'
        super().__init__(name,tl,mass,cost,desc=desc)

class Firearm(Equipment):
    def __init__(self, name, gunType, subtype, tl, accuracy, damageBase, damageDice, damageModifier, ammunition,
                 automaticFire, clipSize, rateOfFire, reliability, cost, gunRange, mass, desc=''):
        self.type = gunType
        self.weight = subtype
        self.accuracy = accuracy
        self.damage = [damageBase,damageDice,damageMod]
        self.ammo = ammo
        self.auto = automaticFire
        self.clip = clipSize
        self.rof = rateOfFire
        self.reliability = reliability
        self.range = gunRange
        if desc == '': desc = self.weight + ' ' + self.type
        super().__init__(name,tl,mass,cost,desc=desc)

class Computer(Equipment):
    def __init__(self,name,tl,power,mass,cost,ship_computer=False,fib=False,bis=False):
        self.ship_computer = ship_computer
        self.bis = bis
        self.fib = fib
        self.power = power
        self.programs = []
        self.software_cost = 0
        super().__init__(name,tl,mass,cost)

# Ships' Computers
model1 = Computer('Model 1',7,5,0,30000,ship_computer=True)
model2 = Computer('Model 2',9,10,0,160000,ship_computer=True)
model3 = Computer('Model 3',11,15,0,300000,ship_computer=True)
model4 = Computer('Model 4',12,20,0,500000,ship_computer=True)
model5 = Computer('Model 5',13,25,0,1000000,ship_computer=True)
model6 = Computer('Model 6',14,30,0,2000000,ship_computer=True)
model7 = Computer('Model 7',15,35,0,3000000,ship_computer=True)
ship_computers = [model1,model2,model3,model4,model5,model6,model7]

class Program(Equipment):
    def __init__(self,name,tl,cost,rating,ship_software=False,desc='',dm=-3,skill='No Skill'):
        self.rating = rating
        self.ship_software = ship_software
        self.dm = dm
        if desc == '': desc = self.name + ' Program'
        super().__init__(bname,tl,mass,cost,desc=desc,skill=skill)
