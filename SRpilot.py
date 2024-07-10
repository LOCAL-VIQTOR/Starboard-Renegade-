# PROGRAM:  STARBOARD, RENEGADE! PILOT SIMULATOR v0
# AUTHOR:   LOCAL VIQTOR
# DATE:     7/5/2024

from SRplanets import *
from SRvessels import *

class vstate():
    def __init__(self,vessel,galaxy,startHex):
        self.vessel = vessel
        self.galaxy = galaxy
        self.location = int(startHex)
        self.credits = 1000000
        self.planet = None
        self.docked = False

    def scan(self):
        planet_found = False
        for i in range(len(self.galaxy)):
            if int(self.galaxy[i].hex) == self.location:
                self.galaxy[i].print()
                self.planet = self.galaxy[i]
                planet_found = True
        if planet_found == False:
            print('No plante found in this location.')
            self.planet = 'No Planet'

    def search(self,find):
        planet_found = False
        for i in range(len(self.galaxy)):
            if int(self.galaxy[i].hex) == find:
                planet_found = True
                return self.galaxy[i]
        if planet_found == False:
            return 'NO PLANET'

    def closeby(self):
        topStart = False
        x = self.location // 100
        if x % 2 == 1: topStart = True
        neighbors = ['NW', 'N', 'NE', 'SW', 'S', 'SE']
        neighbors[1] = self.search(self.location - 1)
        neighbors[4] = self.search(self.location + 1)
        if topStart == True:
            neighbors[0] = self.search(self.location - 101)
            neighbors[2] = self.search(self.location + 99)
            neighbors[3] = self.search(self.location - 100)
            neighbors[5] = self.search(self.location + 100)
        if topStart == False:
            neighbors[0] = self.search(self.location - 100)
            neighbors[2] = self.search(self.location + 100)
            neighbors[3] = self.search(self.location - 99)
            neighbors[5] = self.search(self.location + 101)
        if self.location < 100: self.location = 101
        return neighbors
    

    def refuel(self):
        # must be docked to do this
        # 500 for refined, 100 for unrefined
        if self.planet.uwp[0] == 'A' or self.planet.uwp[0] == 'B':
            refuel_amount = self.vessel.fuel[1] - self.vessel.fuel[0]
            refuel_cost = refuel_amount * 500
            print(str(refuel_amount) + ' | ' + str(refuel_cost))
            self.vessel.fuel[0] = self.vessel.fuel[1]
            self.credits -= refuel_cost
        if self.planet.uwp[0] != 'A' and self.planet.uwp[0] != 'B':
            print('No refined fuel available.')

def simSetup():
    x = vessel()
    #constructMallard(x)
    constructVessel(x)
    x.fuel[0] = x.fuel[1]
    y = generateGalaxy(50,50)
    startingLocation = random.choice(y)
    startHex = startingLocation.hex
    return [x,y,startHex]

def move(state,direction,distance):
    jump_cost = state.vessel.jumpFuel[0] * distance
    if jump_cost > state.vessel.fuel[0]: print('You do not have enough fuel for the jump.')
    if jump_cost <= state.vessel.fuel[0]:
        for i in range(distance):
            topStart = False
            x = state.location // 100
            if x % 2 == 1: topStart = True
            if direction == 'N': state.location -= 1
            if direction == 'S': state.location += 1
            if direction == 'NW':
                if topStart == True: state.location -= 101
                if topStart == False: state.location -= 100
            if direction == 'NE':
                if topStart == True: state.location += 99
                if topStart == False: state.location += 100
            if direction == 'SW':
                if topStart == True: state.location -= 100
                if topStart == False: state.location -= 99
            if direction == 'SE':
                if topStart == True: state.location += 100
                if topStart == False: state.location += 101
                if state.location < 100: state.location = 101
            print('You are now in hex '+str(state.location))
            state.vessel.fuel[0] -= jump_cost
            print('You have '+str(state.vessel.fuel[0])+' tons of fuel remaining.')

def dock(state):
    if state.docked == True: print('You are already docked.')
    if state.docked == False:
        if state.planet is None: print('No planet to land on.')
        if state.planet is not None:
            state.credits -= state.planet.berthingCost
            print('You land for '+str(state.planet.berthingCost)+' Cr.')

def takeoff(state):
    state.docked = False


    
    
    

game_start = simSetup()
game = vstate(game_start[0],game_start[1],game_start[2])
print("Welcome to SRpilot!")


    
