# PROGRAM   Starboard Renegade Pilot HMI
# AUTHOR    LOCALVIQ
# DATE      6/26/24

from SRpilot import *
import os
from distutils import command # comes from setuptools
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import datetime
def returnTime():           # Returns time (点)
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    return timestamp

import turtle as t

t.up()

#   _____ _                _____ _____ ______  _____ 
#  / ____| |        /\    / ____/ ____|  ____|/ ____|
# | |    | |       /  \  | (___| (___ | |__  | (___  
# | |    | |      / /\ \  \___ \\___ \|  __|  \___ \ 
# | |____| |____ / ____ \ ____) |___) | |____ ____) |
#  \_____|______/_/    \_\_____/_____/|______|_____/ 
# PUT CUSTOM PLC CLASSES HERE AS AN ADDRESSING FRAMEWORK

# EXAMPLE: 


#           _____  _____  _____  ______  _____ _____ _____ _   _  _____ 
#     /\   |  __ \|  __ \|  __ \|  ____|/ ____/ ____|_   _| \ | |/ ____|
#    /  \  | |  | | |  | | |__) | |__  | (___| (___   | | |  \| | |  __ 
#   / /\ \ | |  | | |  | |  _  /|  __|  \___ \\___ \  | | | . ` | | |_ |
#  / ____ \| |__| | |__| | | \ \| |____ ____) |___) |_| |_| |\  | |__| |
# /_/    \_\_____/|_____/|_|  \_\______|_____/_____/|_____|_| \_|\_____|
# --> PLEASE PLACE PLC IP ADDRESSING AND CLASS ASSIGNMENTS BELOW <--

# EXAMPLE:


# Tells the logfile when the program started and where it is located

#testComms()

root = Tk()
root.title('Starboard, Renegade!')

#   _____ _____  ______       _______ ______   ______ _      ______ __  __ ______ _   _ _______ _____ 
#  / ____|  __ \|  ____|   /\|__   __|  ____| |  ____| |    |  ____|  \/  |  ____| \ | |__   __/ ____|
# | |    | |__) | |__     /  \  | |  | |__    | |__  | |    | |__  | \  / | |__  |  \| |  | | | (___  
# | |    |  _  /|  __|   / /\ \ | |  |  __|   |  __| | |    |  __| | |\/| |  __| | . ` |  | |  \___ \ 
# | |____| | \ \| |____ / ____ \| |  | |____  | |____| |____| |____| |  | | |____| |\  |  | |  ____) |
#  \_____|_|  \_\______/_/    \_\_|  |______| |______|______|______|_|  |_|______|_| \_|  |_| |_____/ 
# CREATE GUI ELEMENTS & CONTROLS SO THAT YOU CAN PLACE THEM ON SCREEN FURTHER DOWN

fuel_label = Label(root,text='FUEL LABEL ERROR',fg='white',bg='black',font='Helvetica 12')
#cargo_label = Label(root,text='CARGO LABEL ERROR',fg='black',bg='white',font='Helvetica 12')
designation_label = Label(root,text='VESSEL DESIG ERROR',fg='white',bg='black',font='Helvetica 12')

vessel_bloc_label = Label(root,text='VESSEL INFORMATION',width=30,fg='black',bg='red3',font='Helvetica 12')
class_label = Label(root,text='CLASS ERROR',fg='white',bg='black',font='Helvetica 12')
hullMass_label = Label(root,text='HULL MASS ERROR',fg='white',bg='black',font='Helvetica 12')
hullConfig_label = Label(root,text='HULL CONFIGURATION ERROR',fg='white',bg='black',font='Helvetica 12')
armor_label = Label(root,text='ARMOR LABEL ERROR',fg='white',bg='black',font='Helvetica 12')
hull_stats_label = Label(root,text='HULL STATS ERROR',fg='white',bg='black',font='Helvetica 12')

armopts = 'Options: '
if game.vessel.reflec == True: armopts = armopts + 'Reflec '
if game.vessel.selfSealing == True: armopts = armopts + 'Self-Sealing '
if game.vessel.stealth == True: armopts = armopts + 'Stealth '
if game.vessel.reflec == False and game.vessel.selfSealing == False and game.vessel.stealth == False: armopts = 'No Armor Options'

armor_options_label = Label(root,text=armopts,fg='white',bg='black',font='Helvetica 12')

computer_type = 'Computer: '+game.vessel.computer.name
if game.vessel.computer.bis == 'True': computer_type = computer_type+'/bis'
if game.vessel.computer.fib == 'True': computer_type = computer_type+'/fib'
ships_computer_label = Label(root,text=computer_type,fg='white',bg='black',font='Helvetica 12')

ship_sensors_label = Label(root,text='Sensors: '+game.vessel.sensorsSuite[0],fg='white',bg='black',font='Helvetica 12')

cargo_label = Label(root,text='Cargo Capacity: '+str(game.vessel.cargo),fg='white',bg='black',font='Helvetica 12')



jump_control_head = Label(root,text='ENGINE CONTROL',fg='black',bg='red3',width=27,font='Helvetica 12')

hexloc = Label(root,text=str(game.location),fg='black',bg='white',height=2,width=6,font='Helvetica 12')
moveNW = Button(root,text='NW',fg='white',bg='black',height=3,width=8,font='Helvetica 12', command=lambda:move(game,'NW',1))
moveN = Button(root,text='N',fg='white',bg='black',height=3,width=8,font='Helvetica 12', command=lambda:move(game,'N',1))
moveNE = Button(root,text='NE',fg='white',bg='black',height=3,width=8,font='Helvetica 12', command=lambda:move(game,'NE',1))
moveSW = Button(root,text='SW',fg='white',bg='black',height=3,width=8,font='Helvetica 12', command=lambda:move(game,'SW',1))
moveS = Button(root,text='S',fg='white',bg='black',height=3,width=8,font='Helvetica 12', command=lambda:move(game,'S',1))
moveSE = Button(root,text='SE',fg='white',bg='black',height=3,width=8,font='Helvetica 12', command=lambda:move(game,'SE',1))

refuel_button = Button(root,text='REFUEL',fg='white',bg='black',font='Helvetica 12', command=lambda:game.refuel())
credits_label = Label(root,text='Credits: '+str(game.credits),fg='white',bg='black',font='Helvetica 12')

x = 'white'
y = 'white'
z = 'white'

mDstring = 'M-DRIVE ' + str(game.vessel.mannyDrive[0]) + ' | Thrust '+str(game.vessel.mannyDrive[1])
if game.vessel.mannyDrive[0] == 'N/A':
    mDstring = 'NO M-DRIVE'
    x = 'gray'
mDrive_label = Label(root,text=mDstring,fg=x,bg='black',font='Helvetica 12')

jDstring = 'J-DRIVE ' + str(game.vessel.jumpDrive[0]) + ' | Jump Rating '+str(game.vessel.jumpDrive[1])
if game.vessel.jumpDrive[0] == 'N/A':
    jDstring = 'NO J-DRIVE'
    y = 'gray'
jDrive_label = Label(root,text=jDstring,fg=y,bg='black',font='Helvetica 12')
jD_gas = Label(root,text='Fuel/parsec: '+str(game.vessel.jumpFuel[0])+'t',fg='gray',bg='black',font='Helvetica 12')

pPstring = 'P-PLANT ' + game.vessel.powerPlant[0]
if game.vessel.powerPlant[0] == 'N/A':
    pPstring = 'NO POWER PLANT'
    z = 'gray'
pPlant_label = Label(root,text=pPstring,fg=z,bg='black',font='Helvetica 12')
pP_gas = Label(root,text='Fuel/2 weeks: '+str(game.vessel.powerPlant[1])+'t',fg='gray',bg='black',font='Helvetica 12')

computer_details_head = Label(root,text='SHIP COMPUTER',width=30,fg='black',bg='red3',font='Helvetica 12')
softlist = 'Software:'
for i in range(len(game.vessel.computer.programs)):
    softlist = softlist + '\n - ' + game.vessel.computer.programs[i].name
ship_computer_software = Label(root,text=softlist,fg='white',bg='black',font='Helvetica 12',justify=(LEFT))

readout = ''
def scan_func(game,readout):
    game.scan()
    t.dot()
    if isinstance(game.planet,str) == False:
        readout = game.planet.return_tagline()
        t.write(game.planet.uwp[0])
    if isinstance(game.planet,str) == True: t.write('_')
    

scan_button = Button(root,text='SCAN',fg='white',bg='black',font='Helvetica 12', command=lambda:scan_func(game,readout))
scan_readout = Label(root,text=readout,fg='white',bg='black',font='Helvetica 12')

blw = 12
naval_label = Label(root,text='Naval',fg='white',bg='gray',width=blw,font='Helvetica 12')
scout_label = Label(root,text='Scout',fg='white',bg='gray',width=blw,font='Helvetica 12')
research_label = Label(root,text='Research',fg='white',bg='gray',width=blw,font='Helvetica 12')
tas_label = Label(root,text='TAS',fg='white',bg='gray',width=blw,font='Helvetica 12')
consulate_label = Label(root,text='Consulate',fg='white',bg='gray',width=blw,font='Helvetica 12')
pirate_label = Label(root,text='Pirate',fg='white',bg='gray',width=blw,font='Helvetica 12')

planet_head = Label(root,text='PLANET DETAILS',fg='white',bg='blue',width=39,font='Helvetica 12')

starport_quality_label = Label(root,text='STARPORT ERROR',fg='white',bg='black',font='Helvetica 12')
starport_fuel_label = Label(root,text='STARPORT ERROR',fg='white',bg='black',font='Helvetica 12')


def hmi():        # Represents main() for tkinter
    root.config(background='black')
    root.title = 'SRterminal'
    root.geometry('1000x600')
    root.bind('q',lambda event: root.destroy()) # Bind 'q' to quit

    #  _____  _               _____ ______   ______ _      ______ __  __ ______ _   _ _______ _____ 
    # |  __ \| |        /\   / ____|  ____| |  ____| |    |  ____|  \/  |  ____| \ | |__   __/ ____|
    # | |__) | |       /  \ | |    | |__    | |__  | |    | |__  | \  / | |__  |  \| |  | | | (___  
    # |  ___/| |      / /\ \| |    |  __|   |  __| | |    |  __| | |\/| |  __| | . ` |  | |  \___ \ 
    # | |    | |____ / ____ \ |____| |____  | |____| |____| |____| |  | | |____| |\  |  | |  ____) |
    # |_|    |______/_/    \_\_____|______| |______|______|______|_|  |_|______|_| \_|  |_| |_____/ 
    # PLACE ALL ELEMENTS HERE WITH TKINTER AND X,Y COORDINATES

    zhex = 800
    zhey = 440

    zhe_labelx = zhex-85
    zhe_labely = zhey-200

    zhel1 = zhe_labely - 100
    zhel2 = zhe_labely - 75
    zhel3 = zhe_labely - 55
    zhel4 = zhe_labely - 35
    zhel5 = zhe_labely - 15
    zhel6 = zhe_labely + 5
    zhel7 = zhe_labely + 25
    

    fuel_label.place(anchor=NW,x=zhe_labelx,y=zhel2)
    #cargo_label.place(anchor=NW,x=zhe_labelx,y=zhe_labely-25)
    jump_control_head.place(anchor=NW,x=zhe_labelx,y=zhel1)
    mDrive_label.place(anchor=NW,x=zhe_labelx,y=zhel3)
    jDrive_label.place(anchor=NW,x=zhe_labelx,y=zhel4)
    jD_gas.place(anchor=NW,x=zhe_labelx,y=zhel5)
    pPlant_label.place(anchor=NW,x=zhe_labelx,y=zhel6)
    pP_gas.place(anchor=NW,x=zhe_labelx,y=zhel7)
    
    

    hexloc.place(anchor=NW,x=zhex+10,y=zhey+12)
    moveNW.place(anchor=NW,x=zhex-85,y=zhey-35)
    moveN.place(anchor=NW,x=zhex,y=zhey-60)
    moveNE.place(anchor=NW,x=zhex+85,y=zhey-35)
    moveSW.place(anchor=NW,x=zhex-85,y=zhey+35)
    moveS.place(anchor=NW,x=zhex,y=zhey+60)
    moveSE.place(anchor=NW,x=zhex+85,y=zhey+35)

    vbloc_x = 10
    vbloc_y = 10
    vbloc_1 = vbloc_y + 25
    vbloc_2 = vbloc_y + 45
    vbloc_3 = vbloc_y + 65
    vbloc_4 = vbloc_y + 85
    vbloc_5 = vbloc_y + 105
    vbloc_6 = vbloc_y + 125
    vbloc_7 = vbloc_y + 145
    vbloc_8 = vbloc_y + 165
    vbloc_9 = vbloc_y + 185
    vbloc_10 = vbloc_y + 205

    vessel_bloc_label.place(anchor=NW,x=vbloc_x,y=vbloc_y)
    designation_label.place(anchor=NW,x=vbloc_x,y=vbloc_1)
    class_label.place(anchor=NW,x=vbloc_x,y=vbloc_2)
    hullMass_label.place(anchor=NW,x=vbloc_x,y=vbloc_3)
    hullConfig_label.place(anchor=NW,x=vbloc_x,y=vbloc_4)
    armor_label.place(anchor=NW,x=vbloc_x,y=vbloc_5)
    hull_stats_label.place(anchor=NW,x=vbloc_x,y=vbloc_6)
    armor_options_label.place(anchor=NW,x=vbloc_x,y=vbloc_7)
    cargo_label.place(anchor=NW,x=vbloc_x,y=vbloc_8)


    cbloc_x = vbloc_x + 280
    cbloc_y = 10
    cbloc_1 = cbloc_y + 25
    cbloc_2 = cbloc_y + 45
    cbloc_3 = cbloc_y + 65
    cbloc_4 = cbloc_y + 85
    cbloc_5 = cbloc_y + 105
    cbloc_6 = cbloc_y + 125
    cbloc_7 = cbloc_y + 145
    cbloc_8 = cbloc_y + 165
    cbloc_9 = cbloc_y + 185
    cbloc_10 = cbloc_y + 205
    
    computer_details_head.place(anchor=NW,x=cbloc_x,y=cbloc_y)
    ships_computer_label.place(anchor=NW,x=cbloc_x,y=cbloc_1)
    ship_sensors_label.place(anchor=NW,x=cbloc_x,y=cbloc_2)

    scanx = 400
    scany = 250
    
    refuel_button.place(anchor=NW,x=scanx,y=scany+35)
    credits_label.place(anchor=NW,x=scanx+80,y=scany+37)

    ship_computer_software.place(anchor=NW,x=cbloc_x,y=cbloc_3)

    # PLANET DETAILS
    planet_x = 10
    planet_y = 335
    
    planet_x = [planet_x,
                planet_x+120,
                planet_x+240]
    planet_y = [planet_y,
                planet_y+30,
                planet_y+65,
                planet_y+95,
                planet_y+120,
                planet_y+140]
    
    planet_head.place(anchor=NW,x=planet_x[0],y=planet_y[0])
    # Scanning Button and Planet Readout
    scan_button.place(anchor=NW,x=planet_x[0],y=planet_y[1])
    scan_readout.place(anchor=NW,x=planet_x[0]+60,y=planet_y[1]+2)
    # Bases Indicators
    naval_label.place(anchor=NW,x=planet_x[0],y=planet_y[2])
    scout_label.place(anchor=NW,x=planet_x[0],y=planet_y[3])
    research_label.place(anchor=NW,x=planet_x[1],y=planet_y[2])
    tas_label.place(anchor=NW,x=planet_x[1],y=planet_y[3])
    consulate_label.place(anchor=NW,x=planet_x[2],y=planet_y[2])
    pirate_label.place(anchor=NW,x=planet_x[2],y=planet_y[3])
    # Starport Information
    starport_quality_label.place(anchor=NW,x=planet_x[0],y=planet_y[4])
    starport_fuel_label.place(anchor=NW,x=planet_x[0],y=planet_y[5])




    root.after(1000,update_value)   # Call updater and show our window
    root.mainloop()                 # Leave this line and root.after at end of
                                    # main().
game.scan()

def update_value():
    #  _    _ _____  _____       _______ ______ 
    # | |  | |  __ \|  __ \   /\|__   __|  ____|
    # | |  | | |__) | |  | | /  \  | |  | |__   
    # | |  | |  ___/| |  | |/ /\ \ | |  |  __|  
    # | |__| | |    | |__| / ____ \| |  | |____ 
    #  \____/|_|    |_____/_/    \_\_|  |______|
    # UPDATE TKINTER PACKAGES HERE

    hexloc['text'] = str(game.location)
    fuel_label['text'] = 'Fuel: '+str(game.vessel.fuel[0])+'t / '+str(game.vessel.fuel[1]) + 't'
    if game.vessel.jumpFuel[0] > game.vessel.fuel[0]: fuel_label['fg'] = 'red'
    if game.vessel.jumpFuel[0] <= game.vessel.fuel[0]: fuel_label['fg'] = 'white'
    designation_label['text'] = 'Model: '+game.vessel.designation
    hullMass_string = 'Hull Code: ' + game.vessel.hullCode + ' (' + str(game.vessel.hullMass) + ' tons)'

    if game.vessel.hullMass // 100 == 1: scopeTag = 'craft'
    if game.vessel.hullMass // 100 > 1: scopeTag = 'ship'
    class_label['text'] = 'Class: '+game.vessel.scope + scopeTag
    
    hullStats = 'Hull ' + str(game.vessel.hull) + ' | Structure ' +str(game.vessel.structure) + ' | Armor ' + str(game.vessel.armor)
    hull_stats_label['text'] = hullStats

    readout = 'Readout Error'
    if isinstance(game.planet,str) == True:
        readout = 'No Planet Detected!'
    if isinstance(game.planet,str) == False:
        readout = game.planet.return_tagline()
    #if isinstance(game.planet,str) == False: readout = 'readout error'
    #if isinstance(readout,str) == True: readout = game.planet.return_tagline()
    #if isinstance(readout,str) == False: readout = 'No Planet Detected!'
    scan_readout['text'] = readout

    credits_label['text'] = 'Credits: '+str(game.credits//1)
    
    hullMass_label['text'] = hullMass_string
    hullConfig = 'Configuration: ' + game.vessel.config2
    hullConfig_label['text'] = hullConfig
    if game.vessel.armorType == '': game.vessel.armorType = 'None'
    armor_label['text'] = 'Armor: ' + game.vessel.armorType

    if game.vessel.fuel[0] > 0: game.vessel.fuel[0] -= 0.01
    game.vessel.fuel[0] = round(game.vessel.fuel[0],2)

    

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

    if isinstance(game.planet,str) == False:
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

        starport_quality_label['text'] = game.planet.starportQuality + ' Starport | Berth ' + str(game.planet.berthingCost)
        starport_fuel_label['text'] = game.planet.fuel +' | '+ game.planet.facilities

    topStart = False
    x = game.location // 100
    if x % 2 == 1: topStart = True
    
    x = game.location // 100
    y = game.location - x * 100
    x = int(x*15)
    y = int(-y*15)
    
    if topStart == True: y += 7

    x -= 410
    y -= -380
    
    t.goto(x,y)
    t.down()




    
    root.after(500, update_value) # Leave at end of update_value()

if __name__ == '__main__':
    hmi()
