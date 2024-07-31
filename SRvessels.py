import random
from SRtools import *
from SRcomputers import *

# _    __________________ ________   _____
# | |  / / ____/ ___/ ___// ____/ /  / ___/
# | | / / __/  \__ \\__ \/ __/ / /   \__ \
# | |/ / /___ ___/ /__/ / /___/ /______/ /
# |___/_____//____/____/_____/_____/____/
# SHIP CONSTRUCTION, PILOTING, MOUNTING (LOL)

class hardpoint():
    def __init__(self):
        self.designation = 'Hardpoint 0'
        self.isTurret = False
        self.turrets = 0
        self.isBay = False
        self.bay = []
        self.isScreen = False
        self.screen = []
        self.turretOne = []
        self.turretTwo = []
        self.turretThree = []
        self.tl = 0
        self.tons = 0
        self.price = 0
        self.range = 'None'
        self.damage = 'None'

    def installTurret(self, numTurrets, options):
        self.turrets = numTurrets
        if numTurrets == 0:
            self.designation = 'Empty'
            self.turrets = 0
            self.tl = 0
            self.price = 0
        if numTurrets == 1:
            self.designation = 'Single'
            self.turrets = 1
            self.tl = 7
            self.tons = 1
            self.price = 200000
        if numTurrets == 2:
            self.designation = 'Double'
            self.turrets = 2
            self.tl = 8
            self.tons = 1
            self.price = 500000
        if numTurrets == 3:
            self.designation = 'Triple'
            self.turrets = 3
            self.tl = 9
            self.tons = 1
            self.price = 1000000
        if options == 'popup':
            self.designation = self.designation + ' Pop-Up'
            self.tl = 10
            self.tons = 2
            self.price += 1000000
        if options == 'fixed':
            self.designation = self.designation + ' Fixed-Mount'
            self.tons = 0
            self.price = self.price * 0.5
        if options == 'both':
            self.designation = self.designation + ' Fixed-Mount Pop-Up'
            self.tl = 10
            self.tons = 1
            self.price = 0.5 * self.price + 500000
        self.designation = self.designation + ' Turret'

    def randomTurret(self):
        self.isTurret = True
        self.isBay = False
        self.isScreen = False

        options = ['none', 'popup', 'fixed']
        if random.randint(1, 4) == 4: options.append('both')
        turretRoll = random.randint(0, 3)
        if turretRoll <= 0: turretOption = 'none'
        if turretRoll > 0: turretOption = random.choice(options)
        self.installTurret(turretRoll, turretOption)
        self.installRandomTurretWeapons()

    def installRandomTurretWeapons(self):
        pulseLaser = ['Pulse Laser', 7, 'Short', '1d6', 500000]
        beamLaser = ['Beam Laser', 7, 'Medium', '2d6', 1000000]
        particleBeam = ['Particle Beam', 8, 'Long', '3d6 + crew hit', 4000000]
        missileRack = ['Missile Rack', 6, 'Special', 'Depends on missile', 750000]
        sandcaster = ['Sandcaster', 7, 'Special', 'Special', 250000]
        empty = ['Empty', 0, 'none', 'none', 0]
        turretWeapons = [pulseLaser, beamLaser, particleBeam, missileRack, sandcaster, empty]
        if self.turrets > 0:
            self.turretOne = random.choice(turretWeapons)
            self.price += self.turretOne[4]
        if self.turrets > 1:
            self.turretTwo = random.choice(turretWeapons)
            self.price += self.turretTwo[4]
        if self.turrets > 2:
            self.turretThree = random.choice(turretWeapons)
            self.price += self.turretThree[4]

    def installBay(self, bay):
        self.isTurret = False
        self.isBay = True
        self.isScreen = False

        missileBank = ['Missile Bank', 6, 'Special', 'Launch 12 Missiles', 12000000]
        particleBeam = ['Particle Beam', 8, 'Long', '6d6 + crew hit', 20000000]
        fusionGun = ['Fusion Gun', 12, 'Medium', '5d6', 8000000]
        mesonGun = ['Meson Gun', 11, 'Long', '5d6 + crew hit', 50000000]
        bays = [missileBank, particleBeam, fusionGun, mesonGun]
        if bay == 'missile': bayChoice = missileBank
        if bay == 'particle': bayChoice = particleBeam
        if bay == 'fusion': bayChoice = fusionGun
        if bay == 'meson': bayChoice = mesonGun
        if bay == 'random': bayChoice = random.choice(bays)
        self.designation = bayChoice[0]
        self.tl = bayChoice[1]
        self.range = bayChoice[2]
        self.damage = bayChoice[3]
        self.price = bayChoice[4]
        self.tons = 51

    def installScreen(self, screen):
        self.isTurret = False
        self.isBay = False
        self.isScreen = True

        nuclearDamper = ['Nuclear Damper', 12, 50, 50000000]
        mesonScreen = ['Meson Screen', 12, 50, 60000000]
        screens = [nuclearDamper, mesonScreen]
        if screen == 'nuclear': screenChoice = nuclearDamper
        if screen == 'meson': screenChoice = mesonScreen
        if screen == 'random': screenChoice = random.choice(screens)
        self.designation = screenChoice[0]
        self.tl = screenChoice[1]
        self.tons = screenChoice[2]
        self.price = screenChoice[3]

def name_vessel():
    #prefix = ['Kes','Pen','Ost','Casso','Ea','Ha','Mall','Du']
    #suffix = ['trel','guin','rich','wary','gle','wk','ard','ck']
    #vessel_name = random.choice(prefix)+random.choice(suffix)
    anatidae = ['Dendrocygna', # combines the Ancient Greek dendron meaning "tree" with the genus name Cygnus Bechstein, 1803, meaning "swan" in Latin
                'Thalassornis',
                'Cereopsis',
                'Branta', # Latinised form of Old Norse brandgás, "burnt (black) goose".
                'Anser', # Latin anser, "goose"
                'Coscoroba', # Has a loud trumpet-like call ‘cos-cor-oo’ the first syllable being longer and higher in pitch. Female’s calls are higher in pitch than those of the male. The species’ name is derived from the call.
                'Cygnus',
                'Stictonetta',
                'Hymenolaimus',
                'Tachyeres',
                'Merganetta',
                'Plectropterus',
                'Sarkidiornis',
                'Cyanochen',
                'Alopochen',
                'Neochen',
                'Chloephaga',
                'Radjah',
                'Tadorna',
                'Malacorhynchus',
                'Salvadorina',
                'Cairina',
                'Asarcornis',
                'Aix',
                'Chenonetta',
                'Nettapus',
                'Amazonetta',
                'Callonetta',
                'Lophonetta',
                'Speculanas',
                'Sibirionetta',
                'Spatula',
                'Mareca',
                'Anas',
                'Marmaronetta',
                'Rhodonessa',
                'Netta', # Means 'Duck'
                'Athya',
                'Polysticta', # from polus "many" and stiktos "spotted"
                'Somateria',
                'Histrionicus',
                'Camptorhynchus',
                'Melanitta',
                'Clangula',
                'Bucephala',
                'Mergellus',
                'Lophodytes',
                'Mergus',
                'Heteronetta', # "Same Duck", black-headed brood theives
                'Nomonyx',
                'Oxyura',
                'Biziura']
    vessel_name = random.choice(anatidae)
    return vessel_name
    
class vessel():
    def __init__(self):
        self.designation = 'Test Vessel'

        # Hull
        self.hullCode = 0  # Letter Code for Hull Mass
        self.hullMass = 0  # Mass of Hull in Tons
        self.config1 = 'config1Err'  # Hull Configuration Setting 1
        self.config2 = 'config2Err'  # Hull Configuration Setting 2
        self.armorType = ''  # Armor Configuration
        self.reflec = False  # Reflec Option
        self.selfSealing = False  # Self-Sealing Option
        self.stealth = False  # Stealth Option

        # Basic Stats
        self.hull = 0  # Hull Points
        self.structure = 0  # Structure Points
        self.armor = 0  # Armor Points

        # Engineering
        self.scope = 'scopeErr'  # Scope of Vessel's Drive Capability
        self.mannyDrive = ['<A', 0]  # Manoeuvre Drive Code, Thrust Rating
        self.jumpDrive = ['<A', 0]  # Jump Drive Code, Jump Rating
        self.jumpFuel = 0  # Amount of Fuel Used in Maximum Jump
        self.powerPlant = ['<A', 0]  # Power Plant Code and Fuel per 2 Weeks
        self.fuel = [0, 10]  # Current Fuel and Max Fuel Tank
        self.driveTons = [0, 0, 0]  # Tonnage of M-Drive, J-Drive, and Power Plant

        # Electronics
        self.computer = 'emptyShipComputer'  # Ship's Computer
        self.bis = False  # Jump Control Specialization
        self.fib = False  # EMP Defence Wiring
        self.sensorsSuite = []  # Sensors Installed in Ship

        # Hardpoints
        self.hardpoints = []  # Hardpoints Installed on Ship

        # Amenities
        self.passengers = 0  # Number of Planned Passengers
        self.staterooms = [0, 0, 0]  # Crew Staterooms, Passenger Staterooms, Low Berths
        self.lowBerths = 0  # Low Berths

        # Options & Cargo
        self.options = []  # Options Installed on Ship
        self.fuelScoops = False  # Fuel Scoops Installed on Hull
        self.fuelProcessors = 0  # Number of Fuel Processors Installed
        self.repairDrones = 0  # Tons of Repair Drones Onboard
        self.cargo = 0  # Tons of Cargo Space for Freight

        # Math Objects
        self.availableHull = 0  # Hull Left Available for Installations
        self.price = 0  # Price of the Ship
        self.mortgage = 0  # Mortgage to Buy Ship

    def constructHull(self, hullCode):
        if isinstance(hullCode,int) == False:
            if hullCode == 'random': self.hullCode = random.randint(1, 20)
            if hullCode != 'random': print("randomHull() Error: hullCode not 'random'")
        if isinstance(hullCode,int) == True: self.hullCode = hullCode
        self.hullMass = self.hullCode * 100
        self.availableHull = self.hullMass
        if self.hullCode == 1: self.price = 2000000
        if self.hullCode == 2: self.price = 8000000
        if self.hullCode == 3: self.price = 12000000
        if self.hullCode == 4: self.price = 16000000
        if self.hullCode == 5: self.price = 32000000
        if self.hullCode == 6: self.price = 48000000
        if self.hullCode == 7: self.price = 64000000
        if self.hullCode > 7: self.price = self.hullCode * 1000000
        self.hullCode = hexSwitch(self.hullCode)

    def determineHullStructure(self):
        points = int(self.hullMass // 50)
        self.hull = points
        self.structure = points

    def assignConfiguration(self, configuration):
        standard = ['Wedge', 'Cone', 'Sphere', 'Cylinder']
        streamlined = ['Wing', 'Disc', 'Other Lifting Body']
        distributed = ['Distributed']
        configurations = [standard, streamlined, distributed]
        self.config2 = configuration
        if configuration == 'random': self.config2 = random.choice(random.choice(configurations))
        if self.config2 in standard: self.config1 = 'Standard'
        if self.config2 in streamlined:
            self.config1 = 'Streamlined'
            self.price = self.price * 1.1
            self.fuelScoops = True
        if self.config2 == 'Distributed':
            self.config1 = 'Distributed'
            self.price = self.price * 0.9

    def installArmor(self, tit, cry, bon, randomSetting):

        # Determines the amount of mass the armor will take up
        if randomSetting == True: armorCount = random.randint(0, 4)
        if randomSetting == False: armorCount = tit + cry + bon
        fivePerc = self.hullMass * 0.05
        self.availableHull = self.availableHull - (armorCount * fivePerc)

        # Sets Values of the different Armors
        titanium = ['Titanium Steel', 2, 0.05]
        crystal = ['Crystaliron', 4, 0.2]
        bonded = ['Bonded Superdense', 6, 0.5]
        armorCost = 0

        if randomSetting == True:
            tit = 0
            cry = 0
            bon = 0

        # Adds price of the armor to the total cost
        for i in range(armorCount):
            if randomSetting == True:
                chosenArmor = random.choice([titanium, crystal, bonded])
                if chosenArmor[0] == 'Titanium Steel': tit += 1
                if chosenArmor[0] == 'Crystaliron': cry += 1
                if chosenArmor[0] == 'Bonded Superdense': bon += 1
                self.armor += chosenArmor[1]
                costPerc = self.price * chosenArmor[2]
                armorCost += costPerc
        if randomSetting == False:
            for i in range(tit):
                armorCost += self.price * titanium[2]
                self.armor += titanium[1]
            for i in range(cry):
                armorCost += self.price * crystal[2]
                self.armor += titanium[1]
            for i in range(bon):
                armorCost += self.price * bonded[2]
                self.armor += titanium[1]
        self.price += armorCost

        # Sets up string to print for terminal

        if tit > 0:
            titString = 'Titanium Steel'
            if cry > 0 or bon > 0:
                if tit == 1: titString = titString + ', '
            if tit > 1:
                titString = titString + ' '
                for i in range(tit):
                    titString = titString + 'I'
                if cry > 0 or bon > 0: titString = titString + ', '
            self.armorType = titString

        if cry > 0:
            cryString = 'Crystaliron'
            if bon > 0:
                if cry == 1: cryString = cryString + ', '
            if cry > 1:
                cryString = cryString + ' '
                for i in range(cry):
                    cryString = cryString + 'I'
                if bon > 0: cryString = cryString + ', '
            self.armorType = self.armorType + cryString

        if bon > 0:
            bonString = 'Bonded Superdense'
            if bon > 1:
                bonString = bonString + ' '
                for i in range(bon):
                    bonString = bonString + 'I'
            self.armorType = self.armorType + bonString

    def installArmorOptions(self, reflec, selfSealing, stealth, randomArmor):
        optionsPrice = self.hullMass * 10000
        if randomArmor == False:
            x = 0
            y = 0
            z = 0
        if randomArmor == True: x = random.randint(1, 10)
        if x == 10 or reflec == True:
            self.reflec = True
            self.price += optionsPrice
        if randomArmor == True: y = random.randint(1, 10)
        if y == 10 or selfSealing == True:
            self.selfSealing = True
            self.price += optionsPrice
        if randomArmor == True: z = random.randint(1, 10)
        if z == 10 or stealth == True:
            self.stealth = True
            self.price += optionsPrice

    # Determines Jump, Manoeuvre Drives, Power Plant Tons and Cost
    def driveCodeTool(self, driveCode):
        jTons = driveCode * 5 + 5
        jCost = driveCode * 10
        if driveCode == 0: mTons = 0
        if driveCode == 1: mTons = 2
        if driveCode > 1: mTons = driveCode * 2 - 1
        mCost = driveCode * 4
        pTons = (driveCode - 1) * 3 + 4
        pCost = driveCode * 8
        return [jTons, jCost, mTons, mCost, pTons, pCost]

    # Determines how drives act based on hull volume
    def drivePerformanceTool(self):
        hullCode = self.hullMass // 100
        drivePerformance = [[1, 1]]
        if hullCode == 1: drivePerformance = [[1, 2], [2, 4], [3, 6]]
        if hullCode == 2: drivePerformance = [[1, 1], [2, 2], [3, 3],
                                              [4, 4], [5, 5], [6, 6]]
        if hullCode == 3: drivePerformance = [[2, 1], [3, 2], [4, 2],
                                              [5, 3], [6, 4], [7, 4],
                                              [8, 5], [9, 6]]
        if hullCode == 4: drivePerformance = [[2, 1], [3, 1], [4, 2],
                                              [5, 2], [6, 3], [7, 3],
                                              [8, 4], [9, 4], [10, 5],
                                              [11, 5], [12, 6], [13, 6]]
        if hullCode == 5: drivePerformance = [[3, 1], [4, 1], [5, 2],
                                              [6, 2], [7, 2], [8, 3],
                                              [9, 3], [10, 4], [11, 4],
                                              [12, 4], [13, 5], [14, 5],
                                              [15, 6], [16, 6], [17, 6]]
        if hullCode == 6: drivePerformance = [[3, 1], [4, 1], [5, 1],
                                              [6, 2], [7, 2], [8, 2],
                                              [9, 3], [10, 3], [11, 3],
                                              [12, 4], [13, 4], [14, 4],
                                              [15, 5], [16, 5], [17, 5],
                                              [18, 6], [19, 6], [20, 6]]
        if hullCode == 7: drivePerformance = [[4, 1], [5, 1], [6, 1],
                                              [7, 2], [8, 2], [9, 2],
                                              [10, 3], [11, 3], [12, 3],
                                              [13, 4], [14, 4], [15, 4],
                                              [16, 5], [17, 5], [18, 5],
                                              [19, 6], [20, 6], [21, 6],
                                              [22, 6], [23, 6], [24, 6]]
        if hullCode == 8: drivePerformance = [[4, 1], [5, 1], [6, 1],
                                              [7, 2], [8, 2], [9, 2],
                                              [10, 3], [11, 3], [12, 3],
                                              [13, 4], [14, 4], [15, 4],
                                              [16, 5], [17, 5], [18, 5],
                                              [19, 5], [20, 6], [21, 6],
                                              [22, 6], [23, 6], [24, 6]]
        if hullCode == 9: drivePerformance = [[5, 1], [6, 1],
                                              [7, 1], [8, 2], [9, 2],
                                              [10, 2], [11, 3], [12, 3],
                                              [13, 3], [14, 4], [15, 4],
                                              [16, 4], [17, 5], [18, 5],
                                              [19, 5], [20, 5], [21, 6],
                                              [22, 6], [23, 6], [24, 6]]
        if hullCode == 10 or hullCode == 11: drivePerformance = [[5, 1], [6, 1],
                                                                 [7, 1], [8, 2], [9, 2],
                                                                 [10, 2], [11, 3], [12, 3],
                                                                 [13, 3], [14, 4], [15, 4],
                                                                 [16, 4], [17, 5], [18, 5],
                                                                 [19, 5], [20, 5], [21, 5],
                                                                 [22, 6], [23, 6], [24, 6]]
        if hullCode == 12 or hullCode == 13: drivePerformance = [[6, 1],
                                                                 [7, 1], [8, 1], [9, 2],
                                                                 [10, 2], [11, 2], [12, 3],
                                                                 [13, 3], [14, 3], [15, 4],
                                                                 [16, 4], [17, 4], [18, 5],
                                                                 [19, 5], [20, 5], [21, 5],
                                                                 [22, 5], [23, 5], [24, 6]]
        if hullCode == 14 or hullCode == 15: drivePerformance = [[7, 1], [8, 1], [9, 1],
                                                                 [10, 2], [11, 2], [12, 2],
                                                                 [13, 3], [14, 3], [15, 3],
                                                                 [16, 4], [17, 4], [18, 4],
                                                                 [19, 4], [20, 5], [21, 5],
                                                                 [22, 5], [23, 5], [24, 5]]
        if hullCode == 16 or hullCode == 17: drivePerformance = [[8, 1], [9, 1],
                                                                 [10, 1], [11, 2], [12, 2],
                                                                 [13, 2], [14, 3], [15, 3],
                                                                 [16, 3], [17, 4], [18, 4],
                                                                 [19, 4], [20, 4], [21, 4],
                                                                 [22, 5], [23, 5], [24, 5]]
        if hullCode == 18 or hullCode == 19: drivePerformance = [[9, 1],
                                                                 [10, 1], [11, 1], [12, 2],
                                                                 [13, 2], [14, 2], [15, 3],
                                                                 [16, 3], [17, 3], [18, 4],
                                                                 [19, 4], [20, 4], [21, 4],
                                                                 [22, 4], [23, 4], [24, 5]]
        if hullCode >= 20: drivePerformance = [[10, 1], [11, 1], [12, 2],
                                               [13, 2], [14, 2], [15, 3],
                                               [16, 3], [17, 3], [18, 4],
                                               [19, 4], [20, 4], [21, 4],
                                               [22, 4], [23, 4], [24, 5]]

        return drivePerformance

    def decideScope(self, scope):
        scopes = ['Station', 'System', 'Jump', 'Star']
        if scope == 'random': self.scope = random.choice(scopes)
        else: self.scope = scope

    def scopeDrives(self):
        drive = random.randint(1, 6)
        jump = random.randint(1, 6)

        if self.scope == 'Station': return [0, 0]
        if self.scope == 'System': return [0, drive]
        if self.scope == 'Jump': return [jump, 0]
        if self.scope == 'Star': return [jump, drive]

    def decideCruisingSpeed(self, thrust):
        print('THRUST:'+str(thrust))
        if self.hullMass // 100 <= 1:
            if thrust < 2: thrust = 2
            if thrust > 2 and thrust <= 4: thrust = 4
            if thrust > 4: thrust = 6
        if self.hullMass // 100 >= 14 and thrust == 6:
            thrust = 5
        drivePerformance = self.drivePerformanceTool()
        driveCode = [0, 0, 0, 0]
        w = 0
        for i in range(len(drivePerformance)):
            if drivePerformance[i][1] == thrust:
                driveCode = self.driveCodeTool(drivePerformance[i][0])
                w = i
        self.availableHull -= driveCode[2]
        self.driveTons[1] = driveCode[2]
        self.price += driveCode[3]
        drivePerformance = drivePerformance[w]

        # Turns drive number into string for drive printing
        drivePerformance[0] = alphaSwitch(drivePerformance[0])
        self.mannyDrive = drivePerformance

        print(self.mannyDrive)
        self.mannyDrive[0] = alphaSwitch(self.mannyDrive[0])
        if thrust == 0: self.mannyDrive = ['N/A', 0]

    def decideJumpDistance(self, jumpDistance):
        if self.hullMass // 100 <= 1:
            if jumpDistance < 2: jumpDistance = 2
            if jumpDistance > 2 and jumpDistance < 4: jumpDistance = 4
            if jumpDistance < 4: jumpDistance = 6
        if self.hullMass // 100 >= 14 and jumpDistance == 6:
            jumpDistance = 5
        drivePerformance = self.drivePerformanceTool()
        driveCode = [0, 0, 0, 0]
        x = 0
        for i in range(len(drivePerformance)):
            if drivePerformance[i][1] == jumpDistance:
                driveCode = self.driveCodeTool(drivePerformance[i][0])
                x = i
        drivePerformance = drivePerformance[x]
        self.availableHull -= driveCode[0]
        self.driveTons[0] = driveCode[0]
        self.price += driveCode[1]
        drivePerformance[0] = alphaSwitch(drivePerformance[0])
        self.jumpDrive = drivePerformance
        if jumpDistance == 0: self.jumpDrive = ['N/A', 0]

    def installPowerPlant(self, driveScope):
        x = 0
        y = 0
        if isinstance(self.jumpDrive[0],int) == True: self.jumpDrive[0] = alphaSwitch(self.jumpDrive[0])
        if isinstance(self.mannyDrive[0],int) == True: self.mannyDrive[0] = alphaSwitch(self.mannyDrive[0])
        if self.jumpDrive[0] != 'N/A': x = alphaSwitch(self.jumpDrive[0])
        if self.jumpDrive[0] == 'N/A': x = 0
        if self.mannyDrive[0] != 'N/A': y = alphaSwitch(self.mannyDrive[0])
        if self.mannyDrive[0] == 'N/A': y = 0
        print('XY CHECK' + str(x) + ' ' + str(y))
        if x < y: x = y
        if x != 0:
            driveCode = self.driveCodeTool(x)
            self.availableHull -= driveCode[4]
            self.driveTons[2] = driveCode[5]
            self.powerPlant = [alphaSwitch(x), x * 2]
        if x == 0: self.powerPlant = ['A', 2]

    def allocateFuelTank(self):
        self.jumpFuel = [int((self.hullMass) // 10), int((self.hullMass * self.jumpDrive[1]) // 10)]
        print(self.jumpDrive)
        print(self.jumpFuel)
        print(self.powerPlant)
        self.fuel[1] = self.powerPlant[1] + self.jumpFuel[1]
        if self.fuelScoops == True:
            self.fuelProcessors = self.fuel[1] // 20
            self.price += self.fuelProcessors * 50000

    def installBridge(self):
        if self.hullMass <= 200: self.availableHull -= 10
        if self.hullMass >= 200: self.availableHull -= 20
        if self.hullMass >= 1000: self.availableHull -= 20
        if self.hullMass >= 2000: self.availableHull -= 20
        self.price += 0.5 * (self.hullMass // 100)

    def installComputer(self, compType, options):
        if options == 'random':
            x = d(2,6,0)
            if x <= 6: option = 'none'
            if x > 6 and x <= 8: option = 'bis'
            if x > 8 and x <= 10: option = 'fib'
            if x > 10: option = 'both'

        if options != 'random': option = options

        # if compType == 'optimal':
        #    compLevel = self.jumpDrive[1]
        #    if options == 'bis' or options == 'both': compLevel = self.jumpDrive[1] - 1
        #    for i in range(len(shipComputersList)):
        #        if shipComputersList[i].power == compLevel:
        #            self.computer = shipComputersList[i]
        #    if self.computer == 'emptyShipComputer':self.computer = random.choice(shipComputersList)

        if compType == 'optimal':
            ratingRequired = self.jumpDrive[1] * 5
            for i in range(len(shipComputersList)):
                if shipComputersList[i].power == ratingRequired:
                    self.computer = shipComputersList[i]
            if self.computer == 'emptyShipComputer':
                print('NO COMPUTER AVAILABLE ERR')
                self.computer = random.choice(shipComputersList)

        if computer == 'model1': self.computer = model1
        if computer == 'model2': self.computer = model2
        if computer == 'model3': self.computer = model3
        if computer == 'model4': self.computer = model4
        if computer == 'model5': self.computer = model5
        if computer == 'model6': self.computer = model6
        if computer == 'model7': self.computer = model7
        if option == 'bis' or option == 'fib' or option == 'both':
            self.computer.shipComputerOptions(option)
        

    def installSensorsSuite(self, sensorsSuite):
        standardElectronics = ['Standard', 8, -4, ['Radar', 'Lidar'], 0, 0]
        civilianElectronics = ['Basic Civilian', 9, -2, ['Radar', 'Lidar'], 1, 50000]
        militaryElectronics = ['Basic Military', 10, 0, ['Radar', 'Lidar', 'Jammers'], 2, 1000000]
        advancedElectronics = ['Advanced', 11, 1, ['Radar', 'Lidar', 'Densitometer', 'Jammers'], 3, 2000000]
        veryAdvancedElectronics = ['Very Advanced', 12, 2,
                                   ['Radar', 'Lidar', 'Densitometer', 'Jammers', 'Neural Activity Sensor'], 5, 4000000]

        sensorsList = [standardElectronics, civilianElectronics, militaryElectronics,
                       advancedElectronics, veryAdvancedElectronics]

        if sensorsSuite == 'random': self.sensorsSuite = random.choice(sensorsList)
        if sensorsSuite == 'standard': self.sensorsSuite = standardElectronics
        if sensorsSuite == 'civilian': self.sensorsSuite = civilianElectronics
        if sensorsSuite == 'military': self.sensorsSuite = militaryElectronics
        if sensorsSuite == 'advanced': self.sensorsSuite = advancedElectronics
        if sensorsSuite == 'very advanced': self.sensorsSuite = veryAdvancedElectronics

    # New themes for hardpoint generation:
    # - pacifist, low-tonnage, stealth, fixed, maxxed, high-tonnage

    def createHardpoints(self):
        hardpoints = self.hullMass // 100
        armaments = []
        for i in range(hardpoints):
            armament = hardpoint()
            if self.availableHull >= 200 or self.availableHull > self.hullMass / 4:
                x = d(2,6,0)
                if x <= 7: armament.randomTurret()
                if x >= 8 and x <= 10: armament.installBay('random')
                if x >= 11: armament.installScreen('random')
            armaments.append(armament)
            self.availableHull -= armament.tons
        self.hardpoints = armaments

    def attachArmaments(self, percent):
        hardpoints = self.hullMass // 100
        armaments = []
        armorBudget = int((self.availableHull // 1) * (percent / 100))
        totalArmaments = 0
        for i in range(hardpoints):
            armament = hardpoint()
            hardpointsRemaining = hardpoints - i
            if armorBudget // hardpointsRemaining < 51 and hardpointsRemaining >= 10:
                armament.randomTurret()
            if armorBudget // hardpointsRemaining >= 51:
                x = d(2,6,0)
                if x <= 7: armament.randomTurret()
                if x >= 8 and x <= 10: armament.installBay('random')
                if x >= 11: armament.installScreen('random')
            armaments.append(armament)
            armorBudget -= armament.tons
            totalArmaments += armament.tons
        self.hardpoints = armaments
        self.availableHull -= totalArmaments

    def compileShipManifest(self, low, work, middle, high, doubleOccupancy, luxuries):
        stewardRequired = ((work + middle) // 5) + (high // 2)
        if luxuries == True:
            luxuriesRequired = stewardRequired
            stewardRequired = 0
        if luxuries == False: luxuriesRequired = 0
        medicRequired = (low + work + middle + high) // 120
        staterooms = stewardRequired + medicRequired
        lowBerths = low
        if doubleOccupancy == False: staterooms = work + middle + high
        if doubleOccupancy == True: staterooms = ((work + middle) // 2) + high
        return [staterooms, lowBerths, luxuriesRequired]

    def determineCrew(self, coverage, manifest, doubleOccupancy):
        if coverage == 'minimum': staterooms = 2
        if coverage == 'average':
            staterooms = 4 + ((self.driveTons[0] + self.driveTons[1]) // 50)

            for i in range(len(self.hardpoints)):
                if self.hardpoints[i].isScreen == False: staterooms += 1
            addExtra = False
            if doubleOccupancy == True:
                if staterooms % 2 == 1: addExtra = True
                staterooms = staterooms // 2
                if addExtra == True: staterooms += 1
            staterooms += manifest[0]
            self.staterooms = staterooms
            self.lowBerts = manifest[1]
            self.availableHull -= self.lowBerths * 0.5
            self.price += self.lowBerths * 50000
            self.availableHull -= self.staterooms * 4
            self.price += self.staterooms * 500000

    # DESPARATE OVERHAUL
    def vehicleOptions(self, option):
        miningDrones = ['Mining Drones', 10, 1000000]
        repairDronesTons = 0.01 * self.hullMass
        repairDrones = ['Repair Drones', repairDronesTons, (repairDronesTons * 200000)]
        probeDrones = ['5 Probe Drones', 1, 500000]
        escapePods = ['Escape Pods', 0.5, 100000]
        lifeBoat = ['Life Boat', 20, 14000000]
        shipsBoat = ["Ship's Boat", 30, 16000000]
        pinnacle = ['Pinnacle', 40, 20000000]
        cutter = ['Cutter', 50, 28000000]
        shuttle = ['Shuttle', 95, 33000000]
        airRaft = ['Air/Raft', 4, 275000]
        atv = ['ATV', 10, 50000]
        options = [miningDrones, repairDrones, probeDrones, escapePods, lifeBoat,
                   shipsBoat, pinnacle, cutter, shuttle, airRaft, atv]
        availableOptions = []
        chosenOption = ['X', 0, 0]
        for i in range(len(options)):
            if self.availableHull > options[i][1]:
                availableOptions.append(options[i])
            if options[i][0] == option: chosenOption = options[i]
        if option == 'random' and availableOptions != []:
            self.options.append(random.choice(availableOptions))
        if option != 'random':
            self.options.append(chosenOption)
        if repairDrones in self.options:
            self.computer.install(random.choice(autoRepairSoftware))
        for i in range(len(self.options)):
            self.availableHull -= self.options[i][1]
            self.price += self.options[i][2]
        

    def technicalData(self):
        if self.hullMass // 100 == 1: scopeTag = 'craft'
        if self.hullMass // 100 > 1: scopeTag = 'ship'
        print('Designation:       ' + self.designation + ' | ' + self.scope + scopeTag)
        print('Hull:              ' + str(self.hullMass) + ' tons | Hull ' + str(self.hull))
        print('                   ' + self.config2 + ' | Structure ' + str(self.structure))
        if self.armor > 0:
            print('Armour:            ' + self.armorType + ' | ' + str(self.armor) + ' points')
        if self.jumpDrive != ['N/A', 0]:
            print('Jump Drive ' + str(self.jumpDrive[0]) + '       Jump ' + str(self.jumpDrive[1]))
        if self.jumpDrive == ['N/A', 0]:
            print('No Jump Drive')
        if self.mannyDrive != ['N/A', 0]:
            print('Manoeuvre Drive ' + str(self.mannyDrive[0]) + '  Thrust ' + str(self.mannyDrive[1]))
        if self.mannyDrive == ['N/A', 0]:
            print('No Manoeuvre Drive')
        print('Power Plant ' + self.powerPlant[0])
        print('Bridge')
        if self.computer.bis == False:
            print('Computer           ' + self.computer.name + ' | Rating: ' + str(self.computer.power))
        if self.computer.bis == True:
            print('Computer           ' + self.computer.name + ' | Rating: ' + str(self.computer.rating) + ' (' + str(
                self.computer.rating + 5) + ' for Jump Control)')
        if self.sensorsSuite[2] >= 0: print(
            'Electronics        ' + self.sensorsSuite[0] + ' | +' + str(self.sensorsSuite[2]) + ' DM')
        if self.sensorsSuite[2] < 0: print(
            'Electronics        ' + self.sensorsSuite[0] + ' | ' + str(self.sensorsSuite[2]) + ' DM')
        print()
        for i in range(len(self.hardpoints)):
            if i >= 9: spacer = '    '
            if i < 9: spacer = '     '
            turretWeapons = ''
            if self.hardpoints[i].turrets > 0: turretWeapons = self.hardpoints[i].turretOne[0]
            if self.hardpoints[i].turrets > 1: turretWeapons = self.hardpoints[i].turretOne[0] + '/' + \
                                                               self.hardpoints[i].turretTwo[0]
            if self.hardpoints[i].turrets > 2: turretWeapons = self.hardpoints[i].turretOne[0] + '/' + \
                                                               self.hardpoints[i].turretTwo[0] + '/' + \
                                                               self.hardpoints[i].turretThree[0]
            if self.hardpoints[i].isTurret == True:
                if self.hardpoints[i].designation != 'Empty Turret':
                    print('Hardpoint #' + str(i + 1) + '  ' + spacer + self.hardpoints[
                        i].designation + ' (' + turretWeapons + ')')
                if self.hardpoints[i].designation == 'Empty Turret':
                    print('Hardpoint #' + str(i + 1) + '  ' + spacer + 'Empty Turret')
            if self.hardpoints[i].isBay == True:
                print(
                    'Hardpoint #' + str(i + 1) + '  ' + spacer + 'Weapon Bay (' + self.hardpoints[i].designation + ')')
            if self.hardpoints[i].isScreen == True:
                print('Hardpoint #' + str(i + 1) + '  ' + spacer + 'Screen (' + self.hardpoints[i].designation + ')')
            if self.hardpoints[i].isTurret == False and self.hardpoints[i].isBay == False and self.hardpoints[
                i].isScreen == False:
                print('Hardpoint #' + str(i + 1) + '  ' + spacer + 'Empty')
        print()
        if self.jumpDrive[0] != 'N/A':
            print('Fuel               ' + str(self.fuel[1]) + ' tons | One Jump-' + str(
                self.jumpDrive[1]) + " and two weeks' operation")
        if self.jumpDrive[0] == 'N/A':
            print('Fuel               ' + str(self.fuel[1]) + " tons |  Two weeks' operation")
        print('Cargo:             ' + str(self.cargo) + ' tons')
        print(str(self.staterooms) + ' Staterooms')
        print(str(self.lowBerths) + ' Low Berths')
        print()
        print("Extras:            Ship's Locker")
        if self.fuelScoops == True: print('                   Fuel Scoops')
        if self.fuelProcessors > 0: print('                   ' + str(self.fuelProcessors) + ' Fuel Processors')
        for i in range(len(self.options)):
            print('                   ' + self.options[i][0])
        print()
        for i in range(len(self.computer.programs)):
            if i == 0:
                print('Software           ' + self.computer.programs[i].name)
            if i > 0:
                print('                   ' + self.computer.programs[i].name)
        print()
        print('Price:             ' + str(round(self.price)) + ' Cr.')
        self.mortgage = self.price // 240
        self.maintenance = self.price // 1000
        print('Mortgage:          ' + str(int(self.mortgage)) + ' Cr./mo.')
        print('Maintenance:       ' + str(int(self.maintenance)) + ' Cr./yr.')


def constructVessel(vessel):
    vessel.designation = name_vessel()
    
    # 1. Choose Hull Mass
    vessel.constructHull('random')
    vessel.determineHullStructure()

    # 2. Choose Hull Configuration
    vessel.assignConfiguration('random')

    # 3. Install Armor
    vessel.installArmor(0, 0, 0, True)

    # 4. Install Hull Options
    vessel.installArmorOptions(False, False, False, True)

    # 5. Decide Ship Scope
    vessel.decideScope('random')
    driveScope = vessel.scopeDrives()
    print(driveScope)

    # 6. Decide Cruising Altitude (Thrust)
    vessel.decideCruisingSpeed(driveScope[1])

    # 7. Decide Jump Rating
    vessel.decideJumpDistance(driveScope[0])

    # 8. Choose Power Plant
    vessel.installPowerPlant(driveScope)

    # 9. Fuel Allocation
    vessel.allocateFuelTank()

    # 10. Install Bridge
    vessel.installBridge()

    # 11. Install Computer
    vessel.installComputer('optimal', 'none')

    # 12. Install Computer Software
    vessel.computer.initializeShipSoftware(vessel, ['random'])

    # 13. Install Sensors
    vessel.installSensorsSuite('random')

    # 16. Hardpoints
    vessel.attachArmaments(50)

    # 14. Staterooms, Low berths, luxuries
    vesselManifest = vessel.compileShipManifest(0, 0, 0, 0, True, False)
    vessel.determineCrew('average', vesselManifest, True)

    # 15. Vehicles / cargo options
    vessel.vehicleOptions('random')

    # 17. Final Cargo space allocation
    vessel.cargo = int(vessel.availableHull)

    # 18. Printing to Terminal
    vessel.technicalData()

def customVessel(vessel):
    # 1. Choose Hull Mass
    x = int(input('Please input hull code: '))
    vessel.constructHull(int(x))
    vessel.determineHullStructure()

    # 2. Choose Hull Configuration
    print('Choose a configuration:')
    print('Wedge, Cone, Sphere, Cylinder,')
    print('Wing, Disc, Other, Distributed')
    x = input('>>> ')
    vessel.assignConfiguration(x)

    # 3. Install Armor
    print('List desired number of armors:')
    x = int(input('Titanium Steel: '))
    y = int(input('Crystaliron: '))
    z = int(input('Bonded Superdense: '))
    vessel.installArmor(x, y, z, False)

    # 4. Install Hull Options
    print('Armor Options: 1 = Yes, 2 = No')
    x = int(input('Install Reflec? >>>: '))
    y = int(input('Install Self-Sealing? >>>: '))
    z = int(input('Install Stealth? >>>: '))
    a = [x,y,z]
    for i in range(len(a)):
        if a[i] == 1: a[i] = True
        else: a[i] = False
    vessel.installArmorOptions(a[0], a[1], a[2], False)

    # 5. Decide Ship Scope
    x = input('Station, System, Jump(ship) or Star(ship)? >>>: ')
    vessel.decideScope(x)
    driveScope = vessel.scopeDrives()
    print(driveScope)

    # 6. Decide Cruising Altitude (Thrust)
    x = int(input('Lateral Gs of thrust? >>>: '))
    vessel.decideCruisingSpeed(x)

    # 7. Decide Jump Rating
    y = int(input('Jump Rating?? >>>: '))
    vessel.decideJumpDistance(driveScope[0])

    # 8. Choose Power Plant
    vessel.installPowerPlant([y,x])

    # 9. Fuel Allocation
    vessel.allocateFuelTank()

    # 10. Install Bridge
    vessel.installBridge()

    # 11. Install Computer
    if y == 1: vessel.computer.install('Jump Control/1')
    if y == 1: vessel.computer.install('Jump Control/1')
    if y == 1: vessel.computer.install('Jump Control/1')
    if y == 1: vessel.computer.install('Jump Control/1')
    if y == 1: vessel.computer.install('Jump Control/1')
    if y == 1: vessel.computer.install('Jump Control/1')
    vessel.installComputer('optimal', 'none')

    # 12. Install Computer Software
    vessel.computer.initializeShipSoftware(vessel, ['random'])

    # 13. Install Sensors
    input('standard, civilian, military, advanced, very advanced')
    vessel.installSensorsSuite('random')

    # 16. Hardpoints
    vessel.attachArmaments(50)

    # 14. Staterooms, Low berths, luxuries
    vesselManifest = vessel.compileShipManifest(0, 0, 0, 0, True, False)
    vessel.determineCrew('average', vesselManifest, True)

    # 15. Vehicles / cargo options
    vessel.vehicleOptions('random')

    # 17. Final Cargo space allocation
    vessel.cargo = int(vessel.availableHull)

    # 18. Printing to Terminal
    vessel.technicalData()

def constructMallard(vessel):
    vessel.designation = 'Mallard 310T'
    vessel.constructHull(3)
    vessel.determineHullStructure()
    vessel.assignConfiguration('Wing')
    vessel.installArmor(2, 0, 0, False)
    vessel.installArmorOptions(False, True, False, False)
    vessel.scope = 'Star'
    #driveScope = vessel.scopeDrives()
    #print(driveScope)
    vessel.decideCruisingSpeed(3)
    vessel.decideJumpDistance(3)
    vessel.installPowerPlant([3,3])
    vessel.allocateFuelTank()

    vessel.installBridge()
    vessel.installComputer('optimal', 'none')
    vessel.computer.initializeShipSoftware(vessel, ['Jump Control/1'])
    vessel.installSensorsSuite('civilian')
    vessel.attachArmaments(20)
    vesselManifest = vessel.compileShipManifest(0, 0, 0, 0, True, False)
    vessel.determineCrew('minimum', vesselManifest, True)
    #vessel.vehicleOptions('random')
    vessel.cargo = int(vessel.availableHull)
    #vessel.technicalData()
