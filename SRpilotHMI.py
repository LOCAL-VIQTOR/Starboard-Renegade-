# PROGRAM   Starboard Renegade Pilot HMI
# AUTHOR    LOCALVIQ
# DATE      6/26/24

from SRpilot import *

# Password protects the program
#print("Welcome to LOCALVIQ's HMI Framework.")
#password = input('Password: ')
#if password != 'User1': quit()

import os
from pylogix import PLC
from distutils import command # comes from setuptools
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

from winsound import Beep
def blip(): Beep(300,300)   # Incorrect Buzzer (不对)
def bep(): Beep(400,300)    # Correct Bell (对)

import datetime
def returnTime():           # Returns time (点)
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    return timestamp

# Creates a logfile with the date for storing commands
now = datetime.datetime.now()
timestamp = now.strftime("%Y%m%d")
logFileName = timestamp+'_hmiLogfile.txt'
#logFile = open(logFileName,'a')
#logFile.close

# Used to print things to the terminal and to the logfile
# won't print path to terminal as a sneaky move
def spit(logFileName,toPrint):
    #logFile = open(logFileName,'a')
    #logFile.write(toPrint+'\n')
    if 'PATH:' not in toPrint: print(toPrint)
    #logFile.close



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
root.title('Terminal HMI')

#   _____ _____  ______       _______ ______   ______ _      ______ __  __ ______ _   _ _______ _____ 
#  / ____|  __ \|  ____|   /\|__   __|  ____| |  ____| |    |  ____|  \/  |  ____| \ | |__   __/ ____|
# | |    | |__) | |__     /  \  | |  | |__    | |__  | |    | |__  | \  / | |__  |  \| |  | | | (___  
# | |    |  _  /|  __|   / /\ \ | |  |  __|   |  __| | |    |  __| | |\/| |  __| | . ` |  | |  \___ \ 
# | |____| | \ \| |____ / ____ \| |  | |____  | |____| |____| |____| |  | | |____| |\  |  | |  ____) |
#  \_____|_|  \_\______/_/    \_\_|  |______| |______|______|______|_|  |_|______|_| \_|  |_| |_____/ 
# CREATE GUI ELEMENTS & CONTROLS SO THAT YOU CAN PLACE THEM ON SCREEN FURTHER DOWN

# EXAMPLE:
#cc210_label = Label(root, text='CC210',fg='white',bg='black',width=8,font='Helvetica 12')
#cc210_st = Button(root,text='START',fg='white',bg='black',width=8,font='Helvetica 12', command=lambda: receiving.start())

fuel_label = Label(root,text='FUEL LABEL ERROR',fg='black',bg='white',font='Helvetica 12')

hexloc = Label(root,text=str(game.location),fg='black',bg='white',height=2,width=6,font='Helvetica 12')
moveNW = Button(root,text='NW',fg='white',bg='black',height=3,width=8,font='Helvetica 12', command=lambda:move(game,'NW',1))
moveN = Button(root,text='N',fg='white',bg='black',height=3,width=8,font='Helvetica 12')
moveNE = Button(root,text='NE',fg='white',bg='black',height=3,width=8,font='Helvetica 12')
moveSW = Button(root,text='SW',fg='white',bg='black',height=3,width=8,font='Helvetica 12')
moveS = Button(root,text='S',fg='white',bg='black',height=3,width=8,font='Helvetica 12')
moveSE = Button(root,text='SE',fg='white',bg='black',height=3,width=8,font='Helvetica 12')

def hmi():        # Represents main() for tkinter
    root.config(background='black')
    root.title = 'Terminal HMI'
    root.geometry('1000x600')
    root.bind('q',lambda event: root.destroy()) # Bind 'q' to quit

    #  _____  _               _____ ______   ______ _      ______ __  __ ______ _   _ _______ _____ 
    # |  __ \| |        /\   / ____|  ____| |  ____| |    |  ____|  \/  |  ____| \ | |__   __/ ____|
    # | |__) | |       /  \ | |    | |__    | |__  | |    | |__  | \  / | |__  |  \| |  | | | (___  
    # |  ___/| |      / /\ \| |    |  __|   |  __| | |    |  __| | |\/| |  __| | . ` |  | |  \___ \ 
    # | |    | |____ / ____ \ |____| |____  | |____| |____| |____| |  | | |____| |\  |  | |  ____) |
    # |_|    |______/_/    \_\_____|______| |______|______|______|_|  |_|______|_| \_|  |_| |_____/ 
    # PLACE ALL ELEMENTS HERE WITH TKINTER AND X,Y COORDINATES

    # COLUMNS PLACEMENT
    c1 = 50
    c2 = 100
    # ROWS PLACEMENT
    r1 = 50
    r2 = 100

    # EXAMPLE:
    #cc210_label.place(anchor=NW,x=c1,y=r1)
    #cc210_st.place(anchor=NW, x=c2, y=r2)
    zhex = 800
    zhey = 440

    zhe_labelx = zhex-85
    zhe_labely = zhey-90

    fuel_label.place(anchor=NW,x=zhe_labelx,y=zhe_labely)

    hexloc.place(anchor=NW,x=zhex+10,y=zhey+12)
    moveNW.place(anchor=NW,x=zhex-85,y=zhey-35)
    moveN.place(anchor=NW,x=zhex,y=zhey-60)
    moveNE.place(anchor=NW,x=zhex+85,y=zhey-35)
    moveSW.place(anchor=NW,x=zhex-85,y=zhey+35)
    moveS.place(anchor=NW,x=zhex,y=zhey+60)
    moveSE.place(anchor=NW,x=zhex+85,y=zhey+35)

    root.after(1000,update_value)   # Call updater and show our window
    root.mainloop()                 # Leave this line and root.after at end of
                                    # main().

def update_value():

    # EXAMPLE
    tag_updates = ['TAG_1',
                   'TAG_2']
    #tag_values = ccPLC.Read(tag_updates).Value

    #  _    _ _____  _____       _______ ______ 
    # | |  | |  __ \|  __ \   /\|__   __|  ____|
    # | |  | | |__) | |  | | /  \  | |  | |__   
    # | |  | |  ___/| |  | |/ /\ \ | |  |  __|  
    # | |__| | |    | |__| / ____ \| |  | |____ 
    #  \____/|_|    |_____/_/    \_\_|  |______|
    # UPDATE TKINTER PACKAGES HERE

    # EXAMPLE
    #if receiving_values[0].Value == True: cc210_st['bg'] = 'black'
    #if receiving_values[0].Value == False: cc210_st['bg'] = 'green'
    hexloc['text'] = str(game.location)
    fuel_label['text'] = 'Fuel: '+str(game.vessel.fuel[0])+' / '+str(game.vessel.fuel[1])
    if game.vessel.jumpFuel[0] > game.vessel.fuel[0]: fuel_label['fg'] = 'red'

    root.after(500, update_value) # Leave at end of update_value()

if __name__ == '__main__':
    hmi()
