from SRcomputers import *

#    __________  __  __________  __  __________   ________
#   / ____/ __ \/ / / /  _/ __ \/  |/  / ____/ | / /_  __/
#  / __/ / / / / / / // // /_/ / /|_/ / __/ /  |/ / / /
# / /___/ /_/ / /_/ // // ____/ /  / / /___/ /|  / / /
# /_____/\___\_\____/___/_/   /_/  /_/_____/_/ |_/ /_/
# ITEMS, TOOLS, DRUGS, ANYTHING BUT COMPUTERS AND GUNS.

class equipment():
    def __init__(self, name, skill, description, tl, mass, cost):
        self.name = name
        self.skill = skill
        self.description = description
        self.tl = tl
        self.mass = mass
        self.cost = cost
        self.computerInstalled = False
        self.computer = 0

    def installComputer(self, computerToInstall):
        self.computerInstalled = True
        self.computer = computerToInstall

    def info(self):
        print(self.name + ' | TL ' + str(self.tl))
        print(self.description)
        print(str(self.mass) + ' kg | ' + str(self.cost) + ' Cr.')
        print('Skill for use: ' + self.skill)
        if self.computerInstalled == True:
            self.computer.info(True)

    # Communications

    # Bugs


tl5_bug = equipment('Bug', 'Recon', 'Audio Surveillance Device', 5, 3, 50)
tl7_bug = equipment('Bug', 'Recon', 'Audio or Visual', 7, 2, 50)
tl9_bug = equipment('Bug', 'Recon', 'Audio or visual or Data', 9, 1, 50)
tl11_bug = equipment('Bug', 'Recon', 'Audio/Visual/Data', 11, 0.1, 50)
tl13_bug = equipment('Bug', 'Recon', 'Audio/Visual/Data/Bioscan', 13, 0.01, 50)
tl15_bug = equipment('Bug', 'Recon', 'Audio/Visual/Data/Bioscan', 15, 0, 50)
tl15_bug.installComputer(tl8_computer1)

bugs_list = [tl5_bug, tl7_bug, tl9_bug, tl11_bug, tl13_bug, tl15_bug, tl15_bug]

# Tranceivers
tl5_radio_tranceiver = equipment('Radio Tranceiver', 'Comms', 'Range: 5 km', 5, 20, 50)
tl8_radio_tranceiver = equipment('Radio Tranceiver', 'Comms', 'Range: 5 km', 8, 2, 100)
tl9_radio_tranceiver = equipment('Radio Tranceiver', 'Comms', 'Range: 50 km', 9, 1, 250)
tl9_radio_tranceiver.installComputer(computer0)
tl12_radio_tranceiver = equipment('Radio Tranceiver', 'Comms', 'Range: 500 km', 12, 1, 500)
tl12_radio_tranceiver.installComputer(computer0)
tl13_radio_tranceiver = equipment('Radio Tranceiver', 'Comms', 'Range: 5000 km', 13, 1, 1000)
tl13_radio_tranceiver.installComputer(tl8_computer1)
tl9_laser_tranceiver = equipment('Laser Tranceiver', 'Comms', 'Range: 500 km', 9, 1.5, 100)
tl11_laser_tranceiver = equipment('Laser Tranceiver', 'Comms', 'Range: 500 km', 11, 0.5, 250)
tl11_laser_tranceiver.installComputer(computer0)
tl13_laser_tranceiver = equipment('Laser Tranceiver', 'Comms', 'Range: 500 km', 13, 0, 500)
tl13_laser_tranceiver.installComputer(tl8_computer1)

tranceivers_list = [tl5_radio_tranceiver, tl8_radio_tranceiver, tl9_radio_tranceiver, tl12_radio_tranceiver,
                    tl13_radio_tranceiver, tl9_laser_tranceiver, tl11_laser_tranceiver, tl13_laser_tranceiver]

# Comms
tl6_comm = equipment('Comm', 'Comms', 'Audio Only', 6, 1, 50)
tl8_comm = equipment('Comm', 'Comms', 'Audio and Visual', 8, 1, 150)
tl8_comm.installComputer(computer0)
tl10_comm = equipment('Comm', 'Comms', 'Multiple forms of data', 10, 1, 500)
tl10_comm.installComputer(tl8_computer1)

comms_list = [tl6_comm, tl8_comm, tl10_comm]

# Options
data_display_recorder = equipment('Data Display/Recorder', 'unknown', 'HUD Headpiece', 13, 1, 5000)
data_wafer = equipment('Data Wafer', 'n/a', 'Info Storage', 10, 0, 5)

computersEquipmentList = [data_display_recorder, data_wafer]

# ________________________________
# Medical Supplies

cryoberth = equipment('Cryoberth', 'Cryotech', 'Medical Cryogenics Contrainer', 10, 200, 50000)

# Medikits
tl8_medikit = equipment('Medikit', 'Medic', 'Advanced Medical Kit', 8, 8, 1000)
tl10_medikit = equipment('Medikit', 'Medic', 'Advanced Medical Kit', 10, 8, 1500)
tl12_medikit = equipment('Medikit', 'Medic', 'Advanced Medical Kit', 12, 8, 5000)
tl14_medikit = equipment('Medikit', 'Medic', 'Advanced Medical Kit', 14, 8, 10000)

# Drugs
medicinal_drugs = equipment('Medicinal Drugs', 'Medic', 'Basic Medicinal Drugs', 5, 2, 10)
panaceas = equipment('Panaceas', 'Medic', 'Wide-Spectrum Medicinal Drug Dose', 8, 1, 200)
antirad_drugs = equipment('Anto-Rad Drugs', 'Medic', 'Anti-Radiation Drugs', 8, 1, 1000)
stim_drugs = equipment('Stim Drugs', 'Medic', 'Reduce Fatigue at a Cost', 8, 1, 50)
metabolic_accelerator = equipment('Metabolic Accelerator', 'Medic', 'Slow Drug', 10, 1, 500)
combat_drug = equipment('Combat Drug', 'Medic', 'Adds initiative and extra dodge', 10, 1, 1000)
medicinal_slow = equipment('Medicinal Slow', 'Medic', 'Medical-Grade Metabolic Accelerator', 11, 1, 500)
fast_drug = equipment('Fast Drug', 'Medic', 'Suspended Animation Drug', 10, 1, 200)
anagathics = equipment('Anagathics', 'Medic', 'anti-Aging Drugs', 15, 1, 2000)

medical_supplies_list = [cryoberth, tl8_medikit, tl10_medikit, tl12_medikit, tl14_medikit, medicinal_drugs,
                         panaceas, antirad_drugs, stim_drugs, metabolic_accelerator, combat_drug, medicinal_slow,
                         fast_drug, anagathics]

# ________________________________
# Robots and Drones
cargo_robot = equipment('Cargo Robot', 'unknown', 'Simple heavy-Duty Robotics', 11, 500, 75000)
repair_robot = equipment('Repair Robot', 'unknown', 'Crab-Shaped Machine', 11, 10, 10000)
personal_drone = equipment('Personal Drone', 'unknown', 'Personal Holo-Projector', 11, 0.2, 2000)
probe_drone = equipment('Probe Drone', 'unkown', 'Hardened Personal Remote', 11, 6, 15000)
autodoc = equipment('Autodoc', 'unknown', 'Robot Doctor', 12, 100, 40000)
combat_drone = equipment('Combat Drone', 'unknown', 'Flying Guns', 12, 6, 90000)
servitor = equipment('Servitor', 'unknown', 'Robot Butler', 13, 9, 120000)

robots_list = [cargo_robot, repair_robot, personal_drone, probe_drone, autodoc, combat_drone, servitor]

# ________________________________
# Sensors
tl3_binoculars = equipment('Binoculars', 'Recon', 'Basic Pair of Binoculars', 3, 1, 75)
tl8_binoculars = equipment('Binoculars', 'Recon', 'Image Capture and Light Intenification', 8, 1, 750)
tl12_binoculars = equipment('Portable Radiation Imaging System', 'Sensors', 'EM-Spectrum Binoculars', 12, 2, 3500)
geiger_counter = equipment('Geiger Counter', 'Sensors', 'Detects radiation.', 5, 1, 250)
ir_goggles = equipment('IR Goggles', 'Recon', 'See Heat Signatures', 6, 1, 500)
tl7_li_goggles = equipment('Light-Intensifying Goggles', 'Recon', 'Night-Vision Goggles', 7, 1, 500)
tl9_li_goggles = equipment('Light-Intensifying Goggles', 'Recon', 'Night-Vision Goggles', 9, 1, 1250)
tl7_motion_sensor = equipment('Motion Sensor', 'Sensors', 'Detects Movement', 7, 4, 500)
tl9_motion_sensor = equipment('Motion Sensor', 'Sensors', 'Reports shape, size, duration', 9, 3, 1000)
electromagnetic_probe = equipment('Electromagnetic Probe', 'Sensors/Investigation', 'Detects EM Emissions', 10, 0.5,
                                  1000)
densitometer = equipment('Densitometer', 'Sensors', 'Measures density inside and out', 14, 5, 20000)
bioscanner = equipment('Bioscanner', 'Sensors/Life Sciences (Biology)', 'Analyzes biological matter', 15, 3.5, 350000)
nas = equipment('N.A.S.', 'Life Sciences (Biology)/Social Sciences (Sophontology)', 'Scans for neural activity', 15, 10,
                35000)

sensors_list = [tl3_binoculars, tl8_binoculars, tl12_binoculars, geiger_counter, ir_goggles, tl7_li_goggles,
                tl9_li_goggles, tl7_motion_sensor, tl9_motion_sensor, electromagnetic_probe, densitometer,
                bioscanner, nas]

# ________________________________
# Survival Gear and Supplies
tl3_tent = equipment('Tent', 'Survival', 'Basic Shelter for 2', 3, 3, 200)
tl7_tent = equipment('Tent', 'Survival', 'Pressurized Shelter for 2', 7, 5, 2000)
rebreather = equipment('Rebreather', 'n/a', 'Six hours of breathable atmosphere', 6, 10, 250)
tl6_respirator = equipment('Respirator', 'n/a', 'Oxygen Concentration', 6, 0.5, 100)
tl10_respirator = equipment('Respirator', 'n/a', 'Oxygen Concentration', 10, 0.1, 2000)
tl7_filter = equipment('Filter', 'n/a', 'Filters air', 7, 0.5, 100)
tl10_filter = equipment('Filter', 'n/a', 'Filters air', 10, 0.1, 2000)
breather_mask = equipment('Breather Mask', 'n/a', 'Filter + Respirator', 8, 0.5, 150)
artificial_gill = equipment('Artificial Gill', 'n/a', 'Extracts ocygen from water', 8, 4, 4000)
env_suit = equipment('Environment Suit', 'n/a', 'Protects against elements', 8, 3, 500)
tl8_habitat_mod = equipment('Habitat Module', 'n/a', 'Pop-up Living Quarters', 8, 15, 10000)
tl10_habitat_mod = equipment('Habitat Module', 'n/a', 'Pop-up Living Quarters', 10, 12, 20000)
rescue_bubble = equipment('Rescue Bubble', 'n/a', 'Lifeboat', 9, 1, 600)
tl9_thruster_pack = equipment('Thruster Pack', 'Zero-G', 'Jetpack', 9, 8, 2000)
tl12_thruster_pack = equipment('Thruster Pack', 'Zero-G', 'Jetpack', 12, 10, 14000)
tl14_thruster_pack = equipment('Thruster Pack', 'Zero-G', 'Jetpack', 14, 5, 20000)
portable_generator = equipment('Portable Generator', 'n/a', 'Fusion Generator', 10, 30, 500000)

survival_list = [tl3_tent, tl7_tent,
                 rebreather,
                 tl6_respirator, tl10_respirator,
                 tl7_filter, tl10_filter,
                 breather_mask, artificial_gill, env_suit,
                 tl8_habitat_mod, tl10_habitat_mod,
                 rescue_bubble,
                 tl9_thruster_pack, tl12_thruster_pack, tl14_thruster_pack,
                 portable_generator]

# ________________________________
# Toolkits
engineer_toolkit = equipment('Engineering Toolkit', 'Engineer (any)', 'Required for repairs or installation', 7, 12,
                             1000)
forensics_toolkit = equipment('Forensics Toolkit', 'Investigation', 'Required for testing samples and crime scenes', 7,
                              12, 1000)
mechanical_toolkit = equipment('Mechanical Toolkit', 'Mechanic', 'Required for repairs or construction', 7, 12, 1000)
scientific_toolkit = equipment('Scientific Toolkit', 'Science', 'Required for scientific testing', 7, 12, 1000)
surveying_toolkit = equipment('Surveying Toolkit', 'Space Science (any)', 'Required for planetary surveys', 7, 12, 1000)

toolkits_list = [mechanical_toolkit, forensics_toolkit, engineer_toolkit, scientific_toolkit, surveying_toolkit]

# Putting it all together
equipment_list = [bugs_list, tranceivers_list, comms_list, computersEquipmentList, medical_supplies_list, robots_list,
                  sensors_list, survival_list, toolkits_list]

class armor():
    def __init__(self,name,sp,slot,hard,ev,cost):
        self.name = name
        self.sp = sp
        self.slot = slot
        self.hard = hard
        self.ev = ev
        self.cost = cost

kevlarT = armor('Kevlar T-shirt',10,['Torso'],False,0,90)
kevlarVest = armor('Kevlar Vest',10,['Torso'],False,0,90)
steelHelmet = armor('Steel Helmet',14,['Head'],True,0,20)
lgtArmorJacket = armor('Light Armor Jacket',14,['Torso','Arms'],False,0,150)
medArmorJacket = armor('Medium Armor Jacket',18,['Torso','Arms'],False,1,200)
flakVest = armor('Flak Vest',20,['Torso'],True,1,200)
flakPants = armor('Flak Pants',20,['Legs'],True,1,200)
nylonHelmet = armor('Nylon Helmet',20,['Head'],True,0,100)
hvyArmorJacket = armor('Heavy Armor Jacket',20,['Torso','Arms'],False,2,250)
doorGunnerVest = armor("Door Gunner's Vest",25,['Torso'],False,3,250)
metalGear = armor('MetalGear(TM)',25,['Whole Body'],True,2,600)

