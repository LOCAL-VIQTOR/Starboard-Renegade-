# PROGRAM   Starboard, Renegade! Pilot Simulator v0.1
# AUTHOR    LOCAL VIQTOR
# DATE      7/12/24

from SRplanets import *
from SRvessels import *
from distutils import command # comes from setuptools
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import turtle as t

# THIS INTERFACE IS SEPARATED INTO SIX SECTIONS
# 1. VESSEL HARDWARE
#   - VESSEL CONFIGURATION AND NAMEPLATE INFORMATION
#   - VESSEL HARDPOINTS AND WEAPONRY INFORMATION
# 2. BRIDGE CONTROL
#   - SHIP COMPUTER
#   - VESSEL CONTROL
# 3. PLANETARY INFORMATION
#   - STARPORT, GEOGRAPHICAL, AND SOCIOECONOMIC DATA
#   - PLANET FREIGHT AVAILABLE


def printHardpoints(vessel):
    hardpoint_strings = []
    for i in range(len(vessel.hardpoints)):
        if i >= 9: spacer = '    '
        if i < 9: spacer = '     '
        turretWeapons = ''
        if vessel.hardpoints[i].turrets > 0: turretWeapons = vessel.hardpoints[i].turretOne[0]
        if vessel.hardpoints[i].turrets > 1: turretWeapons = vessel.hardpoints[i].turretOne[0] + '/' + \
                                                           vessel.hardpoints[i].turretTwo[0]
        if vessel.hardpoints[i].turrets > 2: turretWeapons = vessel.hardpoints[i].turretOne[0] + '/' + \
                                                           vessel.hardpoints[i].turretTwo[0] + '/' + \
                                                           vessel.hardpoints[i].turretThree[0]
        if vessel.hardpoints[i].isTurret == True:
            if vessel.hardpoints[i].designation != 'Empty Turret':
                hardpoint_strings.append('Hardpoint #' + str(i + 1) + '  ' + spacer + vessel.hardpoints[i].designation + ' (' + turretWeapons + ')')
            if vessel.hardpoints[i].designation == 'Empty Turret':
                hardpoint_strings.append('Hardpoint #' + str(i + 1) + '  ' + spacer + 'Empty Turret')
        if vessel.hardpoints[i].isBay == True:
            hardpoint_strings.append('Hardpoint #' + str(i + 1) + '  ' + spacer + 'Weapon Bay (' + vessel.hardpoints[i].designation + ')')
        if vessel.hardpoints[i].isScreen == True:
            hardpoint_strings.append('Hardpoint #' + str(i + 1) + '  ' + spacer + 'Screen (' + vessel.hardpoints[i].designation + ')')
        if vessel.hardpoints[i].isTurret == False and vessel.hardpoints[i].isBay == False and vessel.hardpoints[i].isScreen == False:
            hardpoint_strings.append('Hardpoint #' + str(i + 1) + '  ' + spacer + 'Empty')
    return hardpoint_strings

class vstate():
    def __init__(self,vessel,galaxy,startHex):
        self.vessel = vessel
        self.galaxy = galaxy
        self.location = int(startHex)
        self.credits = 1000000
        self.planet = 'vstate planet error'
        self.docked = False
        self.processingFuel = False

    # Search for a planet by its hex.
    # Returns a string if no planet found.
    def search(self,find):
        planet_found = False
        for i in range(len(self.galaxy)):
            if int(self.galaxy[i].hex) == int(find):
                planet_found = True
                return self.galaxy[i]
        if planet_found == False:
            return 'NO PLANET'
        
    # Scans for planet
    def scan(self):
        self.planet = self.search(self.location)
        
    # 'closeby' search 6 closest neighbors
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
    
    # refuel
    def refuel(self):
        # must be docked to do this
        # 500 for refined, 100 for unrefined
        if self.planet.uwp[0] == 'A' or self.planet.uwp[0] == 'B':
            refuel_amount = self.vessel.fuel[1] - self.vessel.fuel[0]
            refuel_cost = refuel_amount * 500
            print(str(refuel_amount) + ' | ' + str(refuel_cost))
            self.vessel.fuel[0] = self.vessel.fuel[1]
            self.credits -= refuel_cost
        if self.planet.uwp[0] == 'C' or self.planet.uwp[0] == 'D':
            print('CD FUEL CHECK')
            refuel_amount = self.vessel.fuel[1] - self.vessel.fuel[0]
            refuel_cost = refuel_amount * 100
            self.fuelProcessing == True
            print(self.fuelProcessing)
            print(str(refuel_amount) + ' | ' + str(refuel_cost))
            #self.vessel.fuel[0] = self.vessel.fuel[1]
            self.credits -= refuel_cost
        print('UWP CHECK' + self.planet.uwp[0])
        if self.planet.uwp[0] != 'A' and self.planet.uwp[0] != 'B' and self.planet.uwp[0] != 'C' or self.planet.uwp[0] != 'D':
            print('No refined fuel available.')
            
    # move
    def move(self,direction,distance):
        jump_cost = self.vessel.jumpFuel[0] * distance
        if jump_cost > self.vessel.fuel[0]: print('You do not have enough fuel for the jump.')
        if jump_cost <= self.vessel.fuel[0]:
            for i in range(distance):
                topStart = False
                x = self.location // 100
                if x % 2 == 1: topStart = True
                if direction == 'N': self.location -= 1
                if direction == 'S': self.location += 1
                if direction == 'NW':
                    if topStart == True: self.location -= 101
                    if topStart == False: self.location -= 100
                if direction == 'NE':
                    if topStart == True: self.location += 99
                    if topStart == False: self.location += 100
                if direction == 'SW':
                    if topStart == True: self.location -= 100
                    if topStart == False: self.location -= 99
                if direction == 'SE':
                    if topStart == True: self.location += 100
                    if topStart == False: self.location += 101
                    if self.location < 100: self.location = 101
                print('You are now in hex '+str(self.location))
                self.vessel.fuel[0] -= jump_cost
                print('You have '+str(self.vessel.fuel[0])+' tons of fuel remaining.')
    
    # docking
    def dock(self):
        takeoff = False
        if self.docked == True:
            print('You take off.')
            takeoff = True
            self.docked = False
        if self.docked == False and takeoff == False:
            if isinstance(self.planet,str) == True: print('No planet to land on.')
            if isinstance(self.planet,str) == False:
                self.credits -= self.planet.berthingCost
                print('You land for '+str(self.planet.berthingCost)+' Cr.')
                self.docked = True
    
    # takeoff (docking reverse)
    def takeoff(state):
        state.docked = False

    # simulation setup
def simSetup(v):
    x = vessel()
    if v == 'M': constructMallard(x)
    if v == 'R': constructVessel(x)
    x.fuel[0] = x.fuel[1]
    y = generateGalaxy(25,25)
    startingLocation = random.choice(y)
    startHex = startingLocation.hex
    return [x,y,startHex]

def returnCodeString(code):
    if code == 'Ag': return ['Agricultural','Dedicated to farming and food production.']
    if code == 'As': return ['Asteroid','This is a floating rock in space.']
    if code == 'Ba': return ['Barren','Uncolonized and empty.']
    if code == 'De': return ['Desert','Dry and barely inhabitable.']
    if code == 'Fl': return ['Fluid Oceans','Oceans are not water.']
    if code == 'Ga': return ['Garden','Earth-like landscape.']
    if code == 'Hi': return ['High Population','Population exceeds a billion.']
    if code == 'Ht': return [' High Technology','Technologically advanced society.']
    if code == 'IC': return ['Ice-Capped','Water mostly frozen in polar ice caps; cold and dry.']
    if code == 'In': return ['Industrial','Dominated in factories and cities.']
    if code == 'Lo': return ['Low Population','Population fewer than a few thousand.']
    if code == 'Lt': return ['Low Technology','Society is pre-industrial.']
    if code == 'Na': return ['Non-Agricultural','Cannot grow enough food to support population.']
    if code == 'NI': return ['Non-Industrial','Population cannot maintain industrial base.']
    if code == 'Po': return ['Poor','Lack resources to exceed as a marginal colony.']
    if code == 'Ri': return ['Rich','Blessed as an economic powerhouse.']
    if code == 'Va': return ['Vacuum','There is no atmosphere.']
    if code == 'Wa': return ['Water World','Planet is almost entirely ocean.']

game_start = simSetup('R')
game = vstate(game_start[0],game_start[1],game_start[2])
print('Welcome to SRpilot!')
t.up
root = Tk()
root.title('Starboard, Renegade!')

# Vessel Specs
vessel_header =  Label(root,text='VESSEL INFORMATION',width=60,fg='black',bg='red3',font='Helvetica 12')
hull_mass_label = Label(root,text='HULL MASS',fg='white',bg='black',font='Helvetica 10')
configuration_label = Label(root,text='CONFIGURATION',fg='white',bg='black',font='Helvetica 10')
armor_type_label = Label(root,text='ARMOR TYPE',fg='white',bg='black',font='Helvetica 10')
hull_stats_label = Label(root,text='STATISTICS',fg='white',bg='black',font='Helvetica 10')
hull_options_label = Label(root,text='HULL OPTION',fg='white',bg='black',font='Helvetica 10')

mDrive_label = Label(root,text='MANOEUVRE DRIVE',fg='white',bg='black',font='Helvetica 10')
jDrive_label = Label(root,text='JUMP DRIVE',fg='white',bg='black',font='Helvetica 10')
pPlant_label = Label(root,text='POWER PLANT',fg='white',bg='black',font='Helvetica 10')

staterooms_label = Label(root,text='STATEROOMS',fg='white',bg='black',font='Helvetica 10')
low_berths_label = Label(root,text='LOW BERTHS',fg='white',bg='black',font='Helvetica 10')
extras_label = Label(root,text='Extras:',fg='white',bg='black',font='Helvetica 10') 
extras_body = Label(root,text='EXTRAS',fg='white',bg='black',justify='left',font='Helvetica 10') 
maintenance_label = Label(root,text='MAINTENANCE COST',fg='white',bg='black',font='Helvetica 10') 
mortgage_label = Label(root,text='MORTGAGE',fg='white',bg='black',font='Helvetica 10') 
vessel_price_label = Label(root,text='COST',fg='white',bg='black',font='Helvetica 10') 

# Armaments
arms_header = Label(root,text='Hardpoints / Armaments',width=60,fg='black',bg='red3',font='Helvetica 12')
hardpoint_strings = printHardpoints(game.vessel)
armament_list = []
for i in range(len(hardpoint_strings)):
    x = Label(root,text='HARDPOINT',fg='white',bg='black',font='Helvetica 10')
    armament_list.append(x)

# Bridge Control
bridge_header = Label(root,text='Bridge Control 控制甲板',width=30,fg='white',bg='blue',font='Helvetica 12')
computer_label = Label(root,text='COMPUTER',fg='white',bg='black',font='Helvetica 10')
sensors_label = Label(root,text='SENSORS',fg='white',bg='black',font='Helvetica 10')
software_label = Label(root,text='Software:',fg='white',bg='black',font='Helvetica 10')
software_list = []
for i in range(len(game.vessel.computer.programs)):
    x = Label(root,text='SOFTWARE',fg='white',bg='black',font='Helvetica 10')
    software_list.append(x)
scan_button = Button(root,text='SCAN',fg='white',bg='black',width=10,font='Helvetica 12', command=lambda:game.scan())
dock_button = Button(root,text='DOCK',fg='white',bg='black',width=10,font='Helvetica 12', command=lambda:game.dock())
refuel_button = Button(root,text='REFUEL',fg='white',bg='black',width=10,font='Helvetica 12', command=lambda:game.refuel())

#zhepad
hexloc = Label(root,text=str(game.location),fg='black',bg='white',height=2,width=6,font='Helvetica 12')
moveNW = Button(root,text='NW',fg='white',bg='black',height=1,width=3,font='Helvetica 12', command=lambda:game.move('NW',1))
moveN = Button(root,text='N',fg='white',bg='black',height=1,width=3,font='Helvetica 12', command=lambda:game.move('N',1))
moveNE = Button(root,text='NE',fg='white',bg='black',height=1,width=3,font='Helvetica 12', command=lambda:game.move('NE',1))
moveSW = Button(root,text='SW',fg='white',bg='black',height=1,width=3,font='Helvetica 12', command=lambda:game.move('SW',1))
moveS = Button(root,text='S',fg='white',bg='black',height=1,width=3,font='Helvetica 12', command=lambda:game.move('S',1))
moveSE = Button(root,text='SE',fg='white',bg='black',height=1,width=3,font='Helvetica 12', command=lambda:game.move('SE',1))

# Cargo Bay


# Planet: Starport
starport_header = Label(root,text='Planet Starport',width=66,fg='white',bg='green',font='Helvetica 12')
starport_quality_label = Label(root,text='STARPORT QUALITY',fg='white',bg='black',font='Helvetica 10')
planet_size_label = Label(root,text='PLANET SIZE',fg='white',bg='black',font='Helvetica 10')
high_gravity_label = Label(root,text='HIGH GRAVITY',fg='white',bg='gray',width=14,font='Helvetica 10')
low_gravity_label = Label(root,text='LOW GRAVITY',fg='white',bg='gray',width=14,font='Helvetica 10')
atmosphere_label = Label(root,text='ATMOSPHERE',fg='white',bg='black',font='Helvetica 10')
hydrosphere_label = Label(root,text='HYDROSPHERE',fg='white',bg='black',font='Helvetica 10')
climate_label = Label(root,text='CLIMATE',fg='white',bg='black',font='Helvetica 10')
government_label = Label(root,text='GOVERNMENT',fg='white',bg='black',font='Helvetica 10')
population_label = Label(root,text='POPULATION',fg='white',bg='black',font='Helvetica 10')
stock_label = Label(root,text='STOCK',fg='white',bg='black',font='Helvetica 10')

vaccSuit_label = Label(root,text='VACC SUIT',fg='white',bg='gray',width=14,font='Helvetica 10')
respirator_label = Label(root,text='RESPIRATOR',fg='white',bg='gray',width=14,font='Helvetica 10')
filter_label = Label(root,text='FILTER',fg='white',bg='gray',width=14,font='Helvetica 10')
airSupply_label = Label(root,text='AIR SUPPLY',fg='white',bg='gray',width=14,font='Helvetica 10')
ppeVaries_label = Label(root,text='PPE VARIES',fg='white',bg='gray',width=14,font='Helvetica 10')

blw = 12
naval_label = Label(root,text='Naval',fg='white',bg='gray',width=blw,font='Helvetica 12')
scout_label = Label(root,text='Scout',fg='white',bg='gray',width=blw,font='Helvetica 12')
research_label = Label(root,text='Research',fg='white',bg='gray',width=blw,font='Helvetica 12')
tas_label = Label(root,text='TAS',fg='white',bg='gray',width=blw,font='Helvetica 12')
consulate_label = Label(root,text='Consulate',fg='white',bg='gray',width=blw,font='Helvetica 12')
pirate_label = Label(root,text='Pirate',fg='white',bg='gray',width=blw,font='Helvetica 12')

# FREIGHT
freight_header = Label(root,text='Freight',width=66,fg='white',bg='green',font='Helvetica 12')


def hmi():        # Represents main() for tkinter
    root.config(background='black')
    root.title = 'SRterminal'
    root.geometry('1400x700')
    root.bind('q',lambda event: root.destroy()) # Bind 'q' to quit

    # Vessel Specs
    vsx = 0
    vsy = 0
    vsx = [vsx,
           vsx + 50]
    vsy = [vsy,
           vsy + 25,
           vsy + 45,
           vsy + 65,
           vsy + 85,
           vsy + 105,
           vsy + 125,
           vsy + 145,
           vsy + 165,
           vsy + 185,
           vsy + 205,
           vsy + 225,
           vsy + 245,
           vsy + 265,
           vsy + 285,
           vsy + 305,
           vsy + 325,
           vsy + 345,
           vsy + 365,
           vsy + 385,
           vsy + 405,
           vsy + 425]
    vessel_header.place(anchor=NW,x=vsx[0],y=vsy[0])
    hull_mass_label.place(anchor=NW,x=vsx[0],y=vsy[1])
    configuration_label.place(anchor=NW,x=vsx[0],y=vsy[2])
    armor_type_label.place(anchor=NW,x=vsx[0],y=vsy[3])
    hull_stats_label.place(anchor=NW,x=vsx[0],y=vsy[4])
    hull_options_label.place(anchor=NW,x=vsx[0],y=vsy[5])
    mDrive_label.place(anchor=NW,x=vsx[0],y=vsy[6])
    jDrive_label.place(anchor=NW,x=vsx[0],y=vsy[7])
    pPlant_label.place(anchor=NW,x=vsx[0],y=vsy[8])
    staterooms_label.place(anchor=NW,x=vsx[0],y=vsy[9])
    low_berths_label.place(anchor=NW,x=vsx[0],y=vsy[10])
    extras_label.place(anchor=NW,x=vsx[0],y=vsy[11])
    extras_body.place(anchor=NW,x=vsx[1],y=vsy[11])
    new_row = len(game.vessel.options)
    if game.vessel.fuelScoops == True: new_row += 2
    if new_row == 0: new_row += 1
    maintenance_label.place(anchor=NW,x=vsx[0],y=vsy[new_row+11])
    mortgage_label.place(anchor=NW,x=vsx[0],y=vsy[new_row+12])
    vessel_price_label.place(anchor=NW,x=vsx[0],y=vsy[new_row+13])

    # Armaments
    arx = 0
    ary = vsy[new_row+15] + 5
    arx = [arx]
    ary = [ary,
           ary + 25,
           ary + 45,
           ary + 65,
           ary + 85,
           ary + 105,
           ary + 125,
           ary + 145,
           ary + 165,
           ary + 185,
           ary + 205,
           ary + 225,
           ary + 245,
           ary + 265,
           ary + 285,
           ary + 305,
           ary + 325,
           ary + 345,
           ary + 365,
           ary + 385,
           ary + 405,
           ary + 425,
           ary + 445]
    arms_header.place(anchor=NW,x=arx[0],y=ary[0])
    for i in range(len(armament_list)):
        armament_list[i].place(anchor=NW,x=arx[0],y=ary[i+1])
    
    # Bridge Control
    bcx = 545
    bcy = 0
    bcx = [bcx,
           bcx + 60,
           bcx + 120]
    bcy = [bcy,
           bcy + 25,
           bcy + 45,
           bcy + 65,
           bcy + 85,
           bcy + 105,
           bcy + 125,
           bcy + 145,
           bcy + 165,
           bcy + 185,
           bcy + 205,
           bcy + 225,
           bcy + 245,
           bcy + 265,
           bcy + 285,
           bcy + 305,
           bcy + 325,
           bcy + 345,
           bcy + 365,
           bcy + 385,
           bcy + 405,
           bcy + 425,
           bcy + 445]
    bridge_header.place(anchor=NW,x=bcx[0],y=bcy[0])
    computer_label.place(anchor=NW,x=bcx[0],y=bcy[1])
    sensors_label.place(anchor=NW,x=bcx[0],y=bcy[2])
    software_label.place(anchor=NW,x=bcx[0],y=bcy[3])
    s = len(software_list)
    for i in range(s):
        software_list[i].place(anchor=NW,x=bcx[1],y=bcy[i+3])
    scan_button.place(anchor=NW,x=bcx[0]+22,y=bcy[s+4]-15)
    dock_button.place(anchor=NW,x=bcx[2]+7,y=bcy[s+4]-15)
    refuel_button.place(anchor=NW,x=bcx[0]+22,y=bcy[s+6]-15)

    # Zhepad
    zhex = bcx[0] + 110
    zhey = bcy[10] + 300
    hexloc.place(anchor=NW,x=zhex-10,y=zhey-5)
    moveNW.place(anchor=NW,x=zhex-85,y=zhey-35)
    moveN.place(anchor=NW,x=zhex,y=zhey-60)
    moveNE.place(anchor=NW,x=zhex+85,y=zhey-35)
    moveSW.place(anchor=NW,x=zhex-85,y=zhey+35)
    moveS.place(anchor=NW,x=zhex,y=zhey+60)
    moveSE.place(anchor=NW,x=zhex+85,y=zhey+35)
    
    # Cargo Bay
    cbx = 0
    cby = 0

    # Planet: (Star)port
    ppx = 800
    ppy = 0
    ppx = [ppx,
           ppx + 400,
           ppx + 500]
    ppy = [ppy,
           ppy + 25,
           ppy + 45,
           ppy + 65,
           ppy + 85,
           ppy + 105,
           ppy + 125,
           ppy + 145,
           ppy + 165,
           ppy + 185,
           ppy + 205,
           ppy + 225,
           ppy + 245,
           ppy + 265,
           ppy + 285,
           ppy + 305,
           ppy + 325,
           ppy + 345,
           ppy + 365,
           ppy + 385,
           ppy + 405,
           ppy + 425,
           ppy + 445]
    starport_header.place(anchor=NW,x=ppx[0],y=ppy[0])
    starport_quality_label.place(anchor=NW,x=ppx[0],y=ppy[1])
    planet_size_label.place(anchor=NW,x=ppx[0],y=ppy[2])
    atmosphere_label.place(anchor=NW,x=ppx[0],y=ppy[3])
    hydrosphere_label.place(anchor=NW,x=ppx[0],y=ppy[4])
    climate_label.place(anchor=NW,x=ppx[0],y=ppy[5])

    government_label.place(anchor=NW,x=ppx[0],y=ppy[6])
    population_label.place(anchor=NW,x=ppx[0],y=ppy[7])
    stock_label.place(anchor=NW,x=ppx[0],y=ppy[8])

    # status indicators
    six = 1150
    siy = ppy[2] + 5
    six = [six,
           six + 120]
    siy = [siy,
           siy + 25,
           siy + 50,
           siy + 75]
    
    high_gravity_label.place(anchor=NW,x=six[0],y=siy[0])
    low_gravity_label.place(anchor=NW,x=six[1],y=siy[0])
    vaccSuit_label.place(anchor=NW,x=six[0],y=siy[1])
    respirator_label.place(anchor=NW,x=six[1],y=siy[1])
    filter_label.place(anchor=NW,x=six[0],y=siy[2])
    airSupply_label.place(anchor=NW,x=six[1],y=siy[2])
    ppeVaries_label.place(anchor=NW,x=six[0],y=siy[3])

    # Bases Indicators
    basex = ppx[0] + 120
    basey = ppy[9] + 10
    basex = [basex,
             basex + 120,
             basex + 240]
    basey = [basey,
             basey + 30]
    naval_label.place(anchor=NW,x=basex[0],y=basey[0])
    scout_label.place(anchor=NW,x=basex[0],y=basey[1])
    research_label.place(anchor=NW,x=basex[1],y=basey[0])
    tas_label.place(anchor=NW,x=basex[1],y=basey[1])
    consulate_label.place(anchor=NW,x=basex[2],y=basey[0])
    pirate_label.place(anchor=NW,x=basex[2],y=basey[1])

    # Freight
    freightx = ppx[0]
    freighty = ppy[0] + 260
    freightx = [freightx]
    freighty = [freighty,
                freighty + 25,
                freighty + 45,
                freighty + 65]
    freight_header.place(anchor=NW,x=freightx[0],y=freighty[0])
    #codes_label.place(anchor=NW,x=freightx[0],y=freighty[1])
    
    
    # Planet: Geographical
    pgx = 0
    pgy = 0
    # Planet: Socioeconomic
    psx = 0
    psy = 0

    root.after(1000,update_value)   # Call updater and show our window
    root.mainloop()                 # Leave this line and root.after at end of
                                    # main().

def update_value():

    # Vessel Specs
    vessel_header['text'] = 'Vessel 太空飞船: '+game.vessel.designation
    if game.vessel.hullMass // 100 == 1: scopeTag = 'craft'
    if game.vessel.hullMass // 100 > 1: scopeTag = 'ship'
    hull_mass_label['text'] = 'Class ' + game.vessel.hullCode + ' ' + game.vessel.scope + scopeTag + ' (' + str(game.vessel.hullMass) + ' tons)'
    configuration_label['text'] = 'Configuration: '+game.vessel.config2
    if game.vessel.armorType == '': game.vessel.armorType = 'None'
    armor_type_label['text'] = 'Armor: ' + game.vessel.armorType
    hullStats = 'Hull ' + str(game.vessel.hull) + ' | Structure ' +str(game.vessel.structure) + ' | Armor ' + str(game.vessel.armor)
    hull_stats_label['text'] = hullStats
    armopts = 'Options: '
    if game.vessel.reflec == True: armopts = armopts + 'Reflec '
    if game.vessel.selfSealing == True: armopts = armopts + 'Self-Sealing '
    if game.vessel.stealth == True: armopts = armopts + 'Stealth '
    if game.vessel.reflec == False and game.vessel.selfSealing == False and game.vessel.stealth == False: armopts = 'No Armor Options'
    hull_options_label['text'] = armopts
    if game.vessel.mannyDrive[0] != 'N/A': mDrive_label['text'] = 'Manoeuvre Drive ' + game.vessel.mannyDrive[0] + ' | Thrust ' + str(game.vessel.mannyDrive[1])
    if game.vessel.mannyDrive[0] == 'N/A':
        mDrive_label['text'] = 'No Manoeuvre Drive'
        mDrive_label['fg'] = 'gray'
    if game.vessel.jumpDrive[0] != 'N/A': jDrive_label['text'] = 'Jump Drive ' + game.vessel.jumpDrive[0] + ' | Jump ' + str(game.vessel.jumpDrive[1])
    if game.vessel.jumpDrive[0] == 'N/A':
        jDrive_label['text'] = 'No Jump Drive'
        jDrive_label['fg'] = 'gray'
    pPlant_label['text'] = 'Power Plant ' + game.vessel.powerPlant[0] + ' | Fuel per 2 weeks: ' + str(game.vessel.powerPlant[1])
    if isinstance(game.vessel.staterooms,int) == False: staterooms_label['text'] = 'Staterooms: ' + str(game.vessel.staterooms[0] + game.vessel.staterooms[1])
    if isinstance(game.vessel.staterooms,int) == True: staterooms_label['text'] = 'Staterooms: ' + str(game.vessel.staterooms)
    low_berths_label['text'] = 'Low Berths: ' + str(game.vessel.lowBerths)
    extras_string = ''
    if game.vessel.fuelScoops == True: extras_string = '- Fuel Scoops \n- ' + str(game.vessel.fuelProcessors) + ' Fuel Processors \n'
    for i in range(len(game.vessel.options)):
        extras_string = extras_string + '- ' + game.vessel.options[i][0] + '\n'
        if game.vessel.fuelScoops == False and len(game.vessel.options) == 0: extras_string = 'None'
    extras_body['text'] = extras_string
    maintenance_label['text'] = 'Maintenance: ' + str(int(game.vessel.maintenance)) + ' Cr./mo'
    mortgage_label['text'] = 'Mortgage: ' + str(int(game.vessel.mortgage)) + ' Cr./mo'
    vessel_price_label['text'] = 'Value: ' + str(int(game.vessel.price)) + ' Cr.'
    
    # Armaments
    for i in range(len(armament_list)):
        armament_list[i]['text'] = hardpoint_strings[i]
    
    # Bridge Control
    computer_label['text'] = 'Computer ' + game.vessel.computer.name + ' | Rating ' + str(game.vessel.computer.power)
    sensors_label['text'] = game.vessel.sensorsSuite[0] + ' Sensor Suite'
    for i in range(len(software_list)):
        software_list[i]['text'] = '- ' + game.vessel.computer.programs[i].name
    if game.docked == True: dock_button['text'] = 'TAKEOFF'
    if game.docked == False: dock_button['text'] = 'DOCK'

    # Zhepad
    if isinstance(game.planet,str) == False: hexloc['text'] = 'HEX\n' + str(game.location)
    if isinstance(game.planet,str) == True: hexloc['text'] = 'HEX\n???'
    neighbors = game.closeby()

    #moveNW = neighbors[0]
    if isinstance(neighbors[0],str) == True: moveNW['bg'] = 'black'
    if isinstance(neighbors[0],str) == False:
        if neighbors[0].uwp[0] == 'A' or neighbors[0].uwp[0] == 'B': moveNW['bg'] = 'green'
        if neighbors[0].uwp[0] == 'C' or neighbors[0].uwp[0] == 'D': moveNW['bg'] = 'orange'
        if neighbors[0].uwp[0] == 'E' or neighbors[0].uwp[0] == 'X': moveNW['bg'] = 'red'

    #moveN = neighbors[1]
    if isinstance(neighbors[1],str) == True: moveN['bg'] = 'black'
    if isinstance(neighbors[1],str) == False:
        if neighbors[1].uwp[0] == 'A' or neighbors[1].uwp[0] == 'B': moveN['bg'] = 'green'
        if neighbors[1].uwp[0] == 'C' or neighbors[1].uwp[0] == 'D': moveN['bg'] = 'orange'
        if neighbors[1].uwp[0] == 'E' or neighbors[1].uwp[0] == 'X': moveN['bg'] = 'red'

    #moveNE = neighbors[2]
    if isinstance(neighbors[2],str) == True: moveNE['bg'] = 'black'
    if isinstance(neighbors[2],str) == False:
        if neighbors[2].uwp[0] == 'A' or neighbors[2].uwp[0] == 'B': moveNE['bg'] = 'green'
        if neighbors[2].uwp[0] == 'C' or neighbors[2].uwp[0] == 'D': moveNE['bg'] = 'orange'
        if neighbors[2].uwp[0] == 'E' or neighbors[2].uwp[0] == 'X': moveNE['bg'] = 'red'

    #moveSW = neighbors[3]
    if isinstance(neighbors[3],str) == True: moveSW['bg'] = 'black'
    if isinstance(neighbors[3],str) == False:
        if neighbors[3].uwp[0] == 'A' or neighbors[3].uwp[0] == 'B': moveSW['bg'] = 'green'
        if neighbors[3].uwp[0] == 'C' or neighbors[3].uwp[0] == 'D': moveSW['bg'] = 'orange'
        if neighbors[3].uwp[0] == 'E' or neighbors[3].uwp[0] == 'X': moveSW['bg'] = 'red'

    #moveS = neighbors[4]
    if isinstance(neighbors[4],str) == True: moveS['bg'] = 'black'
    if isinstance(neighbors[4],str) == False:
        if neighbors[4].uwp[0] == 'A' or neighbors[4].uwp[0] == 'B': moveS['bg'] = 'green'
        if neighbors[4].uwp[0] == 'C' or neighbors[4].uwp[0] == 'D': moveS['bg'] = 'orange'
        if neighbors[4].uwp[0] == 'E' or neighbors[4].uwp[0] == 'X': moveS['bg'] = 'red'


    if isinstance(neighbors[5],str) == True: moveSE['bg'] = 'black'
    if isinstance(neighbors[5],str) == False:
        if neighbors[5].uwp[0] == 'A' or neighbors[5].uwp[0] == 'B': moveSE['bg'] = 'green'
        if neighbors[5].uwp[0] == 'C' or neighbors[5].uwp[0] == 'D': moveSE['bg'] = 'orange'
        if neighbors[5].uwp[0] == 'E' or neighbors[5].uwp[0] == 'X': moveSE['bg'] = 'red'

    
    
    # Cargo Bay

    # Planet starPort
    if isinstance(game.planet,str) == False:
        
        planetUWP = game.planet.return_uwp()
        starport_header['text'] = 'Current Planet 当前行星: ' + game.planet.name + ' [' + planetUWP + ']'
        if game.planet.starportQuality != 'No': starport_quality_label['text'] = game.planet.starportQuality + ' Quality Starport (' + str(game.planet.berthingCost) + ' Cr. Berth | ' + game.planet.fuel + ' | ' + game.planet.facilities + ')'
        if game.planet.starportQuality == 'No': starport_quality_label['text'] = game.planet.starportQuality + ' Starport Present'
        planet_size_label['text'] = 'Planet Diameter: ' + str(game.planet.size) + ' km (' + str(game.planet.surfaceGravity) + 'gs)'
        if game.planet.highGravity == True: high_gravity_label['bg'] = 'red3'
        if game.planet.highGravity == False: high_gravity_label['bg'] = 'gray'
        if game.planet.lowGravity == True: low_gravity_label['bg'] = 'red3'
        if game.planet.lowGravity == False: low_gravity_label['bg'] = 'gray'
        atmosphereString = game.planet.atmosphere
        if game.planet.taintedAtmosphere == True: atmosphereString = atmosphereString + ', tainted'
        atmosphere_label['text'] = atmosphereString + ' atmosphere'
        hydrosphereString = 'Landmass is ' + str(game.planet.hydrosphere) + '% Covered by Water'
        hydrosphere_label['text'] = hydrosphereString
        if game.planet.vaccSuit == True: vaccSuit_label['bg'] = 'red3'
        if game.planet.vaccSuit == False: vaccSuit_label['bg'] = 'gray'
        if game.planet.respirator == True: respirator_label['bg'] = 'red3'
        if game.planet.respirator == False: respirator_label['bg'] = 'gray'
        if game.planet.filter == True: filter_label['bg'] = 'red3'
        if game.planet.filter == False: filter_label['bg'] = 'gray'
        if game.planet.airSupply == True: airSupply_label['bg'] = 'red3'
        if game.planet.airSupply == False: airSupply_label['bg'] = 'gray'
        if game.planet.ppeVaries == True: ppeVaries_label['bg'] = 'red3'
        if game.planet.ppeVaries == False: ppeVaries_label['bg'] = 'gray'
        climateString = game.planet.climate[2] + ' Climate | ' + str(game.planet.climate[0]) + '°C - ' + str(game.planet.climate[1]) + '°C'
        if game.planet.temperatureSwings == True: climateString = 'Temperature varies with Circadian Rhythm'
        climate_label['text'] = climateString
        governmentString = game.planet.government + ' | ' + game.planet.culture + ' | Law ' + str(game.planet.uwp[6])
        government_label['text'] = governmentString
        populationString = 'Population: ' + str(game.planet.population) + ' | ' + str(game.planet.population_density) + ' people per sqkm'
        population_label['text'] = populationString
        stock_label['text'] = game.planet.stock + ' Descendants | Language: ' + game.planet.language

        # The following is an attempt at appropriately updating the number of trade
        # code spaces needed to show all available trade codes. At the moment, it
        # just continues to make new labels and place them on top of each other. This
        # is not a problem now, although I am concerned that it is going to become
        # one once play lasts longer than just troubleshooting. As information about
        # labels is lost through updating the list, it becomes difficult, dare I say
        # impossible, to access or change the information stored in the labels that
        # do not have an appropriate variable name. 

        #codeString = 'Travel Codes: '
        #for i in range(len(game.planet.codes)):
        #    codeString = codeString + game.planet.codes[i] + ' '
        #codes_label['text'] = codeString

        freightx = [800,920]
        freighty = [285,305,325,345,365]

        codes_list = []
        code_descriptions = []

        # Writes black line over the previous planet codes
        for i in range(4):
            x = Label(root,text='',fg='white',bg='black',width=400,font='Helvetica 10')
            x.place(anchor=NW,x=freightx[0],y=freighty[0+i])

        # Creates a label and adds it to the list
        for i in range(len(game.planet.codes)):
            label = returnCodeString(game.planet.codes[i])
            x = Label(root,text=label[0],fg='white',bg='black',font='Helvetica 10')
            codes_list.append(x)

        # Places label and adds description to another list
        for i in range(len(codes_list)):
            codes_list[i].place(anchor=NW,x=freightx[0],y=freighty[0+i])
            desc = returnCodeString(game.planet.codes[i])
            x = Label(root,text=desc[1],fg='white',bg='black',font='Helvetica 10')
            code_descriptions.append(x)

        # Places descriptions
        for i in range(len(code_descriptions)):
            code_descriptions[i].place(anchor=NW,x=freightx[1],y=freighty[0+i])

        # Update colors of 'Bases Present' indicators
        if 'Naval' in game.planet.bases: naval_label['bg'] = 'blue'
        if 'Naval' not in game.planet.bases: naval_label['bg'] = 'gray'
        if 'Scout' in game.planet.bases: scout_label['bg'] = 'blue'
        if 'Scout' not in game.planet.bases: scout_label['bg'] = 'gray'
        if 'Research' in game.planet.bases: research_label['bg'] = 'blue'
        if 'Research' not in game.planet.bases: research_label['bg'] = 'gray'
        if 'TAS' in game.planet.bases: tas_label['bg'] = 'blue'
        if 'TAS' not in game.planet.bases: tas_label['bg'] = 'gray'
        if 'Imperial Consulate' in game.planet.bases: consulate_label['bg'] = 'blue'
        if 'Imperial Consulate' not in game.planet.bases: consulate_label['bg'] = 'gray'
        if 'Pirate' in game.planet.bases: pirate_label['bg'] = 'red'
        if 'Pirate' not in game.planet.bases: pirate_label['bg'] = 'gray'
    
    # Planet Geography
    # Planet Anthropology

    root.after(500, update_value) # Leave at end of update_value()

if __name__ == '__main__':
    hmi()
