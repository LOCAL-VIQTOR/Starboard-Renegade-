import random
from SRcomputers import *
from SRcyberpunk import *
from SRequipment import *
from SRfirearms import *
from SRfreight import *
from SRpatrons import *
from SRplanets import *
from SRtools import *
from SRtraveller import *
from SRvessels import *

#  __________  ____  __  ______  __    ___________ __  ______  ____  ___________   ________
# /_  __/ __ \/ __ \/ / / / __ )/ /   / ____/ ___// / / / __ \/ __ \/_  __/  _/ | / / ____/
#  / / / /_/ / / / / / / / __  / /   / __/  \__ \/ /_/ / / / / / / / / /  / //  |/ / / __
# / / / _, _/ /_/ / /_/ / /_/ / /___/ /___ ___/ / __  / /_/ / /_/ / / / _/ // /|  / /_/ /
# /_/ /_/ |_|\____/\____/_____/_____/_____//____/_/ /_/\____/\____/ /_/ /___/_/ |_/\____/
# FUNCTIONS WITH THE INTENT TO FIGURE OUT WHAT THE HELL IS GOING ON

def tl_printer(planet):
    if planet.uwp[7] <= 3: print('Primitive Tech')
    if planet.uwp[7] >= 4 and planet.uwp[7] <= 6: print('Industrial Tech')
    if planet.uwp[7] >= 7 and planet.uwp[7] <= 9: print('Pre-Stellar Tech')
    if planet.uwp[7] >= 10 and planet.uwp[7] <= 11: print('Early Stellar Tech')
    if planet.uwp[7] >= 12 and planet.uwp[7] <= 14: print('Average Stellar Tech')
    if planet.uwp[7] >= 15: print('High Stellar Tech')
    if planet.uwp[7] == 0: print('No Tech')
    if planet.uwp[7] == 1: print('Bronze/Iron Age')
    if planet.uwp[7] == 2: print('Renaissance')
    if planet.uwp[7] == 3:
        print('Steam Power, 19th Century')
        print('Antique Pistol/Rifle')
    if planet.uwp[7] == 4:
        print('Industrial Revolution, 19th/20th Century')
        print('Shotgun')
    if planet.uwp[7] == 5:
        print('Electrification, mid-20th Century')
        print('Revolver, Rifle')
    if planet.uwp[7] == 6:
        print('Fission Power / Dawn of Space Age')
        print('Autopistol, Autorifle')
    if planet.uwp[7] == 7:
        print('Satellites / Computers')
        print('Assault Rifle')
    if planet.uwp[7] == 8:
        print('Reach Other Worlds')
        print('Snub / Body Pistol, Stunner I')
    if planet.uwp[7] == 9:
        print('Gravity Manipulation / Colonies')
        print('Accelerator Rifle, Laser Pistol / Carbine / Rifle I')
    if planet.uwp[7] == 10:
        print('Jump Drive')
        print('Advanced Combat Rifle, Stunner II')
    if planet.uwp[7] == 11:
        print('AI / Jump-2')
        print('Laser Pistol /Carbine / Rifle II')
    if planet.uwp[7] == 12:
        print('Weather Control / Plasma Weaponry / J-3')
        print('Gauss Rifle, Stunner III')
    if planet.uwp[7] == 13:
        print('Battle Dress / Human Cloning / J-4')
        print('Gauss Pistol')
    if planet.uwp[7] == 14: print('Fusion Weaponry / J-5')
    if planet.uwp[7] == 15: print('Black Globe Generators / J-6')
    if planet.uwp[7] == 16: print('Plasma Rifle')


def generate_traveller_npc(jean_luc, hallowsbelt, noble):
    if noble == True:
        while jean_luc.soc < 11: jean_luc.roll_scores()
    if noble == False: jean_luc.roll_scores()
    jean_luc.homeworld = hallowsbelt.codes
    jean_luc.homeworld_skills()
    jean_luc.education_skills()
    jean_luc.draft()
    jean_luc.drifter_career_check()
    jean_luc.any_skill_determinism()
    jean_luc.skill_compiler()
    jean_luc.print()
    print()


def navy_progression(nick_carl, naval):
    term_desc = 'TermDescErr'
    print(nick_carl.specialization)
    naval.gain_skill(nick_carl)
    if nick_carl.specialization == 'Line/Crew':
        survival_roll = d(2,6,characteristic_modifier(nick_carl.int))
        advancement_roll = d(2,6,characteristic_modifier(nick_carl.edu))
        print(survival_roll, advancement_roll)
        if survival_roll >= 5:
            term_desc = naval.events()
            if advancement_roll >= 7: print('Advanced!')
        if survival_roll < 5:
            term_desc = naval.mishap()
            naval.ejected = True
        print(term_desc)
    if nick_carl.specialization == 'Engineering/Gunner':  # NOT KICKED OUT ERR COUNT 1
        survival_roll = d(2,6,characteristic_modifier(nick_carl.int))  # ERR COUNT 1
        advancement_roll = d(2,6,characteristic_modifier(nick_carl.edu))
        print(survival_roll, advancement_roll)
        if survival_roll >= 6:
            term_desc = naval.events()
            if advancement_roll >= 6: print('Advanced!')
        if survival_roll < 6:
            term_desc = naval.mishap()
            naval.ejected = True
        print(term_desc)
    if nick_carl.specialization == 'Flight':
        survival_roll = d(2,6,characteristic_modifier(nick_carl.dex))
        advancement_roll = d(2,6,characteristic_modifier(nick_carl.edu))
        print(survival_roll, advancement_roll)
        if survival_roll >= 7:
            term_desc = naval.events()
            if advancement_roll >= 5: print('Advanced!')
        if survival_roll < 7:
            term_desc = naval.mishap()
            naval.ejected = True
        print(term_desc)
        if naval.ejected == True: print('You have been ejected from the Navy.')


#    __  ______    _____   __   __    ____  ____  ____
#   /  |/  /   |  /  _/ | / /  / /   / __ \/ __ \/ __ \
#  / /|_/ / /| |  / //  |/ /  / /   / / / / / / / /_/ /
# / /  / / ___ |_/ // /|  /  / /___/ /_/ / /_/ / ____/
#/_/  /_/_/  |_/___/_/ |_/  /_____/\____/\____/_/
# THIS IS WHERE THE MAGIC HAPPENS, BABE!

galaxy = defaultGalaxy()
menuChoice = 0
terminalRunning = True
print('Starboard, Renegade! by Calvin L.')
print('Build 2024.01.26')
print()
print('Welcome to the terminal.')
while terminalRunning == True:

    # Placeholder Terminal Locations
    if menuChoice == -2:
        print('Vessel Terminal')
        print()
        print('<<< Returning to Terminal ')
        menuChoice = 0

    if menuChoice == -3:
        print('Character Terminal')
        print()
        print('<<< Returning to Terminal ')
        menuChoice = 0

    if menuChoice == -4:
        print('Equiment Terminal')
        print()
        print('<<< Returning to Terminal ')
        menuChoice = 0

    # 0.0 Main Terminal
    if menuChoice == 0:
        print('Please enter one of the following integers: ')
        print('1. Galaxy Terminal')
        print('2. Vessel Terminal')
        print('3. Character Terminal (B)')
        print('4. Equipment Terminal (X)')
        print('99. Exit Program')
        menuChoice = int(input('>>: '))

    # 1 Galaxy Terminal
    if menuChoice == 1:
        galaxyTerminal = 0
        while galaxyTerminal < 7:

            # 1.0 Galaxy Terminal Main Menu
            if galaxyTerminal == 0:
                print('Galaxy Terminal')
                print('1. Print Current Galaxy')
                print('2. Generate New Galaxy')
                print('3. Construct Planet')
                print('4. Print Planet Details')
                print('5. Edit Planet Details')
                print('6. Generate New Freight')
                print('99. Back to Terminal.')
                galaxyTerminal = int(input('>>>: '))

            # 1.1 Print Current Galaxy
            if galaxyTerminal == 1:
                print()
                print('---> CURRENT GALAXY <---')
                for i in range(len(galaxy)):
                    print(
                        galaxy[i].return_tagline() + '| ' + galaxy[i].government + ' | ' + galaxy[i].culture + ' | ' +
                        galaxy[i].climate[2] + ' | Factions: ' + str(len(galaxy[i].factions)))
                print('<<< Returning to Terminal')
                print()
                galaxyTerminal = 0

            # 1.2 Generate New Galaxy
            if galaxyTerminal == 2:
                print()
                print('Rows and columns multiply for the total possible hexes.')
                print('Each hex has a 50% chance of containing a planet.')
                rows = int(input('How many rows of hexes? '))
                columns = int(input('How many columns? '))
                galaxy = generateGalaxy(rows, columns)
                generateFreight(galaxy)
                print('New Galaxy Successfully Generated')
                print()
                print('<<< Returning to Terminal ')
                galaxyTerminal = 0

            # 1.3 Create Planet
            if galaxyTerminal == 3:
                print()
                print('Welcome to the Planet Construction Interface (PCI).')
                print('Here, you will input data to create a planet.')
                hallowsbelt = planet()
                hallowsbelt.hex = input('What hex is your planet located in? >>: ')
                hallowsbelt.name = input("What is your planet's name? >>: ")

                # Starport
                print('What is the Quality of the Starport?')
                print('A = Excellent, B = Good, C = Routine, D = Poor, E = Frontier, X = None')
                starport_choice = input('>>: ')
                if starport_choice == 'A': hallowsbelt.generateStarport(10)
                if starport_choice == 'B': hallowsbelt.generateStarport(8)
                if starport_choice == 'C': hallowsbelt.generateStarport(6)
                if starport_choice == 'D': hallowsbelt.generateStarport(4)
                if starport_choice == 'E': hallowsbelt.generateStarport(2)
                if starport_choice == 'X': hallowsbelt.generateStarport(0)

                # Size
                print('Enter diameter of planet in kilometers.')
                size_choice = int(input('>>: '))
                size_choice = size_choice // 1600
                hallowsbelt.generateSize(int(size_choice))

                # Atmosphere
                print("What is the planet's atmosphere?")
                print('0 = None, 1 = Trace, 2 = Very Thin,')
                print('3 = Very Thin + Tainted, 4 = Thin, 5 = Thin + Tainted,')
                print('6 = Standard, 7 = Standard + Tainted, 8 = Dense,')
                print('9 = Dense + Tainted, 10 = Exotic, 11 = Corrosive,')
                print('12 = Insidious, 13 = Dense + High, 14 = Thin + Low,')
                print('15 = Unusual.')
                hallowsbelt.generateAtmosphere(int(input('>>: ')))

                # Climate
                print("What is the planet's climate?")
                print('1 = Frozen, 2 = Cold, 3 = Temperate, 4 = Hot, 5 = Roasting')
                climate = int(input('>>: '))
                if climate == 1: hallowsbelt.climate = [-100, -51, 'Frozen']
                if climate == 2: hallowsbelt.climate = [-51, 0, 'Cold']
                if climate == 3: hallowsbelt.climate = [0, 30, 'Temperate']
                if climate == 4: hallowsbelt.climate = [31, 80, 'Hot']
                if climate == 5: hallowsbelt.climate = [81, 100, 'Roasting']

                # Print & Exit
                hallowsbelt.print()
                print()
                print('<<< Returning to Terminal ')
                galaxyTerminal = 0

            # 1.4 Print Planet Details & Freight
            if galaxyTerminal == 4:
                print()
                planetFound = False
                print('Will print out details and freight.')
                planetFocus = input('Enter planet hex: ')
                for i in range(len(galaxy)):
                    if galaxy[i].hex == planetFocus:
                        galaxy[i].print()
                        for x in range(len(galaxy[i].goods)):
                            galaxy[i].goods[x].info()
                        print()
                        planetFound = True
                if planetFound == False:
                    print()
                    print('Planet not found.')
                    print()
                print('<<< Returning to Terminal ')
                galaxyTerminal = 0

            # 1.5 Edit Planet Details
            if galaxyTerminal == 5:
                print()
                print('FEATURE NOT YET AVAILABLE')
                print()
                print('<<< Returning to Terminal ')
                galaxyTerminal = 0

            # 1.6 Generate New Freight
            if galaxyTerminal == 6:
                print()
                generateFreight(galaxy)
                print('New Galaxy Freight Successfully Generated')
                print()
                print('<<< Returning to Terminal ')
                galaxyTerminal = 0

        # Galaxy Terminal Return to Main Terminal
        print()
        print('<<< Returning to Terminal ')
        menuChoice = 0

    # 2. Vessel Terminal
    if menuChoice == 2:
        vesselTerminal = 0
        while vesselTerminal < 3:

            # 2.0 Main Vessel Terminal
            if vesselTerminal == 0:
                print()
                print('Vessel Terminal')
                print('1. Generate Random Vessel')
                print('2. Design Vessel')
                vesselTerminal = int(input('>>>: '))

            # 2.1 Generate Random Vessel
            if vesselTerminal == 1:
                print()
                print('Generated Space Vessel: ')
                enterprise = vessel()
                constructVessel(enterprise)
                print()
                print('<<< Returning to Terminal ')
                vesselTerminal = 0

            # 2.2 Design Vessel
            if vesselTerminal == 2:
                print()
                print('Designing Vessels is currently unavailable')
                print()
                print('<<< Returning to Terminal ')
                vesselTerminal = 0

        # Vessel Terminal Return to Main Terminal
        print()
        print('<<< Returning to Terminal ')
        menuChoice = 0

    # 3. Character Terminal
    if menuChoice == 3:
        characterTerminal = 0
        while characterTerminal < 6:

            # 3.0 Main Character Terminal
            if characterTerminal == 0:
                print()
                print('Vessel Terminal')
                print('1. Traveller (LP)')
                print('2. Traveller (FDE)')
                print('3. Cyberpunk (LP)')
                print('4. Cyberpunk (FDE)')
                print('2. Design Character')
                print('6. Draft Generator')
                print('99. Return to Terminal')
                characterTerminal = int(input('>>>: '))

            # 3.1 Traveller NPC with Lifepath
            if characterTerminal == 1:
                print()
                print('For now, please use the draft generator. ')
                print()
                print('<<< Returning to Terminal ')
                characterTerminal = 0

            # 3.2 Traveller NPC without Lifepath
            if characterTerminal == 2:
                print()
                print('This feature is currently unavailable')
                print()
                print('<<< Returning to Terminal ')
                characterTerminal = 0

            # 3.3 Cyberpunk NPC with Lifepath
            if characterTerminal == 3:
                print()
                print('This feature is currently unavailable')
                print()
                print('<<< Returning to Terminal ')
                characterTerminal = 0

            # 3.4 Cyberpunk NPC without Lifepath
            if characterTerminal == 4:
                print()
                x = int(input('How many FDEs? >>: '))
                for i in range(x):
                    silverhand = cyberpunk_npc()
                    silverhand.generate()
                print()
                print('<<< Returning to Terminal ')
                characterTerminal = 0

            # 3.5 Design Character
            if characterTerminal == 5:
                print()
                print('This feature  is currently unavailable')
                print()
                print('<<< Returning to Terminal ')
                characterTerminal = 0

            # 3.6 Draft Generator
            if characterTerminal == 6:
                print()
                for i in range(int(input('How many draftees? >>: '))):
                    homeworld = random.choice(galaxy)
                    print('Homeworld: ' + homeworld.return_tagline())
                    # ^^^^^ ADDED
                    nick_carl = traveller_npc()
                    print('chk1')
                    nick_carl.generate(homeworld)
                    while nick_carl.career == 'Drifter': nick_carl.generate(homeworld)
                    naval = navy_career()
                    terms = []
                    # terms.append(naval.events())
                    # terms.append(naval.mishap())

                    navy_progression(nick_carl, naval)
                    print()
                    # for i in range(len(terms)):
                    # print(terms[i])
                print()
                print('<<< Returning to Terminal ')
                characterTerminal = 0

        # Character Terminal Return to Main Terminal
        print()
        print('<<< Returning to Terminal ')
        menuChoice = 0

    if menuChoice == 4:
        answer = 100
        while answer != 99:
            print('1. Print Equipment')
            print('2. Random Prototech')
            print('3. Generate by TL')
            print('4. Firearm Registration')
            print('5. Return to terminal')
            answer = int(input('?: '))
            print()

            # ________________________________
            # 1. Print Equipment
            if answer == 1:
                for i in range(len(equipment_list)):
                    to_print_list = equipment_list[i]
                    for n in range(len(to_print_list)):
                        to_print_list[n].info()

            # ________________________________
            # 2. Random Prototech (Defunct)
            if answer == 2:
                x = random.choice(equipment_list)
                while x == []:
                    x = random.choice(equipment_list)
                y = random.choice(x)
                y.prototech()
                y.info()

            # ________________________________
            # 3. Generate by TL
            if answer == 3:
                planet_tl = int(input('Planetary TL: '))
                products = []
                for i in range(len(equipment_list)):
                    tl_check_list = equipment_list[i]
                    for n in range(len(tl_check_list)):
                        tl_check_item = tl_check_list[n]
                        if tl_check_item.tl == planet_tl:
                            products.append(tl_check_item)
                        if tl_check_item.tl == planet_tl + 1:
                            tl_check_item.prototech(1)
                            products.append(tl_check_item)
                        if tl_check_item.tl == planet_tl + 2:
                            tl_check_item.prototech(2)
                            products.append(tl_check_item)
                        if tl_check_item.tl <= planet_tl - 1:
                            tl_check_item.retrotech(planet_tl)
                            products.append(tl_check_item)
                for i in range(len(products)):
                    products[i].print()

            # ________________________________
            # Firearms Registration
            if answer == 4:
                for i in range(len(weapons_list)):
                    homeworld = input('Planet of Origin: ')
                    if homeworld == 'random':
                        placeHolder = random.choice(galaxy)
                        homeworld = placeHolder.name
                    name = input('Model Name: ')
                    weapons_list[i].designate(homeworld, name)
                    print('FIREARM REGISTRATION COMPLETE')
                    print('-----------------------------------------------------------')
                    weapons_list[i].print()
                    print('-----------------------------------------------------------')

            if answer == 5:
                menuChoice = 0
                answer = 99

    if menuChoice == 5:
        haspJamesT = cyberpunkCharacter()
        haspJamesT.cyberpunkCharacterGenerator()
        menuChoice = 0

    if menuChoice >= 99:
        print('Closing program. . . Goodbye! Click OK on the popup window to close this window.')
        exit()

    if menuChoice < 99 and menuChoice > 6:
        print('Incorrect integer choice, returning to terminal.')
        menuChoice = 0

