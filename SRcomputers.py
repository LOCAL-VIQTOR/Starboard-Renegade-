import random
from SRtools import d

#   _____ ____  _____________       _____    ____  ______
#  / ___// __ \/ ____/_  __/ |     / /   |  / __ \/ ____/
#  \__ \/ / / / /_    / /  | | /| / / /| | / /_/ / __/
# ___/ / /_/ / __/   / /   | |/ |/ / ___ |/ _, _/ /___
# /____/\____/_/     /_/    |__/|__/_/  |_/_/ |_/_____/
# SOFTWARE FOR PERSONAL AND SHIP COMPUTERS

class program():
    def __init__(self, name, shipSoftware, tl, rating, cost, description):
        self.name = name
        self.shipSoftware = name
        self.tl = tl
        self.rating = rating
        self.skill = 'none'
        self.dm = -3
        self.cost = cost
        self.description = description

    def setSkill(self, skill, dm):
        self.skill = skill
        self.dm = dm

    def info(self):
        print(self.name + ': ' + self.description)

    # Manoeuvre Software


manoeuvre0 = program('Manoeuvre/0', True, 8, 9, 0, 'Allows basic control of ship')

# Voice Command Software
intellect = program('Intellect', True, 11, 10, 1, 'Allows verbal commands.')

# Jump Drive Control Software
jumpControl1 = program('Jump Control/1', True, 9, 5, 100000, 'Allows Auto-Jump/1')
jumpControl2 = program('Jump Control/2', True, 11, 10, 200000, 'Allows Auto-Jump/2')
jumpControl3 = program('Jump Control/3', True, 12, 15, 300000, 'Allows Auto-Jump/3')
jumpControl4 = program('Jump Control/4', True, 13, 20, 400000, 'Allows Auto-Jump/4')
jumpControl5 = program('Jump Control/5', True, 14, 25, 500000, 'Allows Auto-Jump/5')
jumpControl6 = program('Jump Control/6', True, 15, 30, 600000, 'Allows Auto-Jump/6')

# Evasive Manoeuvre Software
evade1 = program('Evade/1', True, 9, 10, 1000000, 'Auto-Evade, 1 Dodge, -1 DM')
evade2 = program('Evade/2', True, 11, 15, 2000000, 'Auto-Evade, 2 Dodges, -1 DM')
evade3 = program('Evade/3', True, 13, 25, 3000000, 'Auto-Evade, 3 Dodges, -1 DM')

# Fire Control Software
fireControl1 = program('Fire Control/1', True, 9, 5, 2000000, 'Fire 1 weapon or give +1 DM')
fireControl2 = program('Fire Control/2', True, 10, 10, 4000000, 'Fire 2 weapons or give +2 DM')
fireControl3 = program('Fire Control/3', True, 10, 15, 6000000, 'Fire 3 weapons or give +3 DM')
fireControl4 = program('Fire Control/4', True, 10, 20, 8000000, 'Fire 4 weapons or give +4 DM')
fireControl5 = program('Fire Control/5', True, 10, 25, 10000000, 'Fire 5 weapons or give +5 DM')

# Repair Drone Software
autoRepair1 = program('Auto-Repair/1', 1, 10, 10, 5000000, '1 Repair Attempt or give +1 DM')
autoRepair2 = program('Auto-Repair/2', 2, 12, 20, 10000000, '2 Repair Attempts or give +2 DM')

# Database Software
library = program('Library', 0, 8, 0, 0, 'Contains a wealth of knowledge')

jumpControlSoftware = [jumpControl1, jumpControl2, jumpControl3, jumpControl4, jumpControl5, jumpControl6]
evadeSoftware = [evade1, evade2, evade3]
fireControlSoftware = [fireControl1, fireControl2, fireControl3, fireControl4, fireControl5]
autoRepairSoftware = [autoRepair1, autoRepair2]

# Database Software
database = program('Database', False, 7, 0, random.randint(10, 10000),
                   'Store of information, can be checked with agent.')

# Human-Machine Interface Software
interface = program('Interface', False, 7, 0, 0, 'Displays data.')

# Security Software
security0 = program('Security/0', False, 7, 0, 0, 'Average +0 Security Program')
security1 = program('Security/1', False, 9, 1, 200, 'Difficult -2 Security Program')
security2 = program('Security/2', False, 11, 2, 1000, 'Very Difficult -4 Security Program')
security3 = program('Security/3', False, 12, 3, 20000, 'Formidible -6 Security Program')

# Translation Software
translator0 = program('Translator/0', False, 9, 0, 50, 'Near real-time specialized language program')
translator1 = program('Translator/1', False, 10, 1, 500, 'Real-time specialized language program')

# Intrusion Software
intrusion1 = program('Intrusion/1', False, 10, 1, 1000, 'Level 1 Hacking Program')
intrusion2 = program('Intrusion/2', False, 11, 2, 10000, 'Level 2 Hacking Program')
intrusion3 = program('Intrusion/3', False, 13, 3, 100000, 'Level 3 Hacking Program')
intrusion4 = program('Intrusion/4', False, 15, 4, -1, 'Level 4 Hacking Program')

# Vocal and Human-Controlled Expert Programming
intelligentInterface = program('Intelligent Interface', False, 11, 1, 100, 'Voice Control and Intelligent Data Display')

# Skill Programming
expert1 = program('Expert/1', False, 11, 1, 1000, 'Skill-based Expert Program')
expert2 = program('Expert/2', False, 12, 2, 10000, 'Skill-based Expert Program')
expert3 = program('Expert/3', False, 13, 3, 100000, 'Skill-based Expert Program')

# Computer-Controlled Computer Programming
agent0 = program('Agent/0', False, 11, 0, 500, 'AI with Computer 0')
agent1 = program('Agent/1', False, 12, 1, 2000, 'AI with Computer 1')
agent2 = program('Agent/2', False, 13, 2, 100000, 'AI with Computer 2')
agent3 = program('Agent/3', False, 14, 3, 250000, 'AI with Computer 3')

# Computer-Controlled Expert Programming
intellect1 = program('Intellect/1', False, 12, 1, 2000, 'AI for Expert Programming')
intellect2 = program('Intellect/2', False, 13, 2, 50000, 'AI for Expert Programming')
intellect3 = program('Intellect/3', False, 14, 3, -1, 'AI for Expert Programming')

computerSoftwareList = [[database],
                        [interface],
                        [security0, security1, security2, security3],
                        [translator0, translator1],
                        [intrusion1, intrusion2, intrusion3, intrusion4],
                        [intelligentInterface],
                        [expert1, expert2, expert3],
                        [agent0, agent1, agent2, agent3],
                        [intellect1, intellect2, intellect3]]


#   __________  __  _______  __  __________________  _____
#  / ____/ __ \/  |/  / __ \/ / / /_  __/ ____/ __ \/ ___/
# / /   / / / / /|_/ / /_/ / / / / / / / __/ / /_/ /\__ \
# / /___/ /_/ / /  / / ____/ /_/ / / / / /___/ _, _/___/ /
# \____/\____/_/  /_/_/    \____/ /_/ /_____/_/ |_|/____/
# SHIP AND PERSONAL COMPUTATIONAL DEVICES

class computer():
    def __init__(self, name, shipComputer, tl, power, mass, cost):
        self.name = name
        self.shipComputer = shipComputer
        self.bis = False
        self.fib = False
        self.tl = tl
        self.power = power
        self.programs = []
        self.softwareCost = 0
        self.mass = mass
        self.cost = cost

    def prototech(self, homeworld_tl):
        tlBelow = self.tl - homeworld_tl
        if tlBelow > 0 and tlBelow <= 2:
            self.name = 'Prototech ' + self.name
            self.tl -= tlBelow
            if tlBelow == 1:
                self.mass = self.mass * 10
                self.cost = self.cost * 10
            if tlBelow == 2:
                self.mass = self.mass * 100
                self.cost = self.cost * 100
        if tlBelow <= 0 or tlBelow > 2:
            print('prototech() TL error')

    def retrotech(self, homeworld_tl):
        self.name = 'Retrotech ' + self.name
        tl_difference = homeworld_tl - self.tl
        self.tl = homeworld_tl
        for i in range(tl_difference):
            self.mass = self.mass / 2
            self.cost = self.cost / 2

    def techShift(self, homeworld_tl):  # Determines proto- or retrotech level
        if homeworld_tl < self.tl:  # to apply to computer technology.
            if self.tl - homeworld_tl <= 2:
                self.prototech(homeworld_tl)
            if self.tl - homeworld_tl > 2:
                self.prototech(self.tl + 2)
        if homeworld_tl > self.tl:
            self.retrotech(homeworld_tl)

    def install(self, program):
        self.programs.append(program)
        self.softwareCost += program.cost

    def shipComputerOptions(self, option):
        self.bis = False
        self.fib = False
        if option == 'bis':
            self.bis = True
            self.cost = self.cost * 1.5
        if option == 'fib':
            self.fib = True
            self.cost += 1000000
        if option == 'both':
            self.bis = True
            self.fib = True
            self.cost = self.cost * 2

    def initializeShipSoftware(self, vessel, programTheme):
        self.programs = []

        self.install(library)
        self.install(manoeuvre0)
        

        if programTheme == 'random':
            x = d(2,6,0)
            if x > 8: self.install(intellect)

        jumpCapacity = vessel.jumpDrive[1]
        if self.bis == True: jumpCapacity += 5
        if jumpCapacity == 6: self.install(jumpControl6)
        if jumpCapacity == 5: self.install(jumpControl5)
        if jumpCapacity == 4: self.install(jumpControl4)
        if jumpCapacity == 3: self.install(jumpControl3)
        if jumpCapacity == 2: self.install(jumpControl2)
        if jumpCapacity == 1: self.install(jumpControl1)

        if programTheme == 'random':
            x = d(2,6,0)
            if x > 8: self.install(random.choice(evadeSoftware))

        if programTheme == 'random':
            x = d(2,6,0)
            if x > 8: self.install(random.choice(fireControlSoftware))

        # Library is installed with autoRepair in vessel vehicle options

    def info(self, fromEquipment):
        if self.shipComputer == False:
            if fromEquipment == False: print(self.name + ' | TL ' + str(self.tl))
            if fromEquipment == True: print(self.name)
            if fromEquipment == False:
                if self.mass >= 1: print(str(self.mass) + ' kg | ' + str(self.cost) + ' Cr.')
                if self.mass < 1: print(str(self.mass * 1000) + ' g | ' + str(self.cost) + ' Cr.')

            if self.programs == []: print('No programs loaded on this device')
            if self.programs != []:
                for i in range(len(self.programs)):
                    print(self.programs[i].name)
            if fromEquipment == False: print('Software Cost: ' + str(self.softwareCost) + ' Cr.')


model1 = computer('Model 1', True, 7, 5, 0, 30000)
model2 = computer('Model 2', True, 9, 10, 0, 160000)
model3 = computer('Model 3', True, 11, 15, 0, 2000000)
model4 = computer('Model 4', True, 12, 20, 0, 5000000)
model5 = computer('Model 5', True, 13, 25, 0, 10000000)
model6 = computer('Model 6', True, 14, 30, 0, 20000000)
model7 = computer('Model 7', True, 15, 35, 0, 30000000)

shipComputersList = [model1, model2, model3, model4, model5, model6, model7]

computer0 = computer('Computer/0', False, 7, 0, 10, 50)
tl8_computer1 = computer('Computer/1', False, 8, 1, 5, 250)
tl9_computer1 = computer('Computer/1', False, 9, 1, 5, 100)
tl10_computer2 = computer('Computer/2', False, 10, 2, 1, 500)
tl11_computer2 = computer('Computer/2', False, 11, 2, 1, 350)
computer3 = computer('Computer/3', False, 12, 3, 0.5, 1000)
computer4 = computer('Computer/4', False, 13, 4, 0.5, 1500)
computer5 = computer('Computer/5', False, 14, 5, 0.5, 5000)

computerTerminal = computer('Computer Terminal', False, 7, 0, 3, 200)

tl7_handComputer = computer('Hand Computer/0', False, 7, 0, 5, 100)
tl8_handComputer = computer('Hand Computer/1', False, 8, 1, 2.5, 500)
tl9_handComputer = computer('Hand Computer/1', False, 9, 1, 2.5, 200)
tl10_handComputer = computer('Hand Computer/2', False, 10, 2, 0.5, 1000)
tl11_handComputer = computer('Hand Computer/2', False, 11, 2, 0.5, 700)
tl12_handComputer = computer('hand Computer/3', False, 12, 3, 0.25, 2000)
tl13_handComputer = computer('Hand Computer/4', False, 13, 4, 0.25, 3000)
tl14_handComputer = computer('Hand Computer/5', False, 14, 5, 0.25, 10000)

computersList = [[computer0, tl8_computer1, tl9_computer1, tl10_computer2,
                  tl11_computer2, computer3, computer4, computer5],
                 [computerTerminal],
                 [tl7_handComputer, tl8_handComputer, tl9_handComputer, tl10_handComputer,
                  tl11_handComputer, tl12_handComputer, tl13_handComputer, tl14_handComputer]]
