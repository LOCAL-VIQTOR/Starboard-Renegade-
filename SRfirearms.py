#    ______________  _________    ____  __  ________
#   / ____/  _/ __ \/ ____/   |  / __ \/  |/  / ___/
#  / /_   / // /_/ / __/ / /| | / /_/ / /|_/ /\__ \
# / __/ _/ // _, _/ /___/ ___ |/ _, _/ /  / /___/ /
# /_/   /___/_/ |_/_____/_/  |_/_/ |_/_/  /_//____/
# GUNS, GUNS, GUNS, GUNS, GUNS

class firearm():
    def __init__(self, gunType, subtype, tl, accuracy, damageBase, damageDice, damageModifier, ammunition,
                 automaticFire, clipSize, rateOfFire, reliability, cost, gunRange, mass):
        self.origin = 'OriginErr'
        self.name = 'NameErr'
        self.type = gunType
        self.subtype = subtype
        self.tl = tl
        self.accuracy = accuracy
        self.damageBase = damageBase
        self.damageDice = damageDice
        self.damageMod = damageModifier
        self.ammo = ammunition
        self.auto = automaticFire
        self.clip = clipSize
        self.rof = rateOfFire
        self.reliability = reliability
        self.cost = cost
        self.range = gunRange
        self.mass = mass

    def designate(self, origin, name):
        self.origin = origin
        self.name = name

    def print(self):
        print(self.origin + ' ' + self.name)
        print(self.type + ' (' + self.subtype + ')')
        print('Acc: ' + str(self.accuracy) + ' | TL ' + str(self.tl))
        damage_string = str(self.damageBase) + 'd' + str(self.damageDice) + '+' + str(
            self.damageMod) + ' (' + self.ammo + ')'
        print(damage_string)
        # print(self.auto)
        print('Clip: ' + str(self.clip) + ' (' + str(self.rof) + ')')
        if self.reliability == 1: print('Unreliable')
        if self.reliability == 2: print('Standard Reliability')
        if self.reliability == 3: print('Very Reliable')
        print(str(self.cost) + ' Cr. | ' + str(self.range) + 'm | ' + str(self.mass) + 'kg')


# Sourceless Weapons
sw_combat_magnum = firearm('Revolver', 'Combat Magnum', 5, 1, 2, 6, 3, '.357', False, 6, 2, 3, 125, 50, 0.5)
revolver = firearm('Revolver', 'Medium', 5, -1, 3, 6, -3, 'RevAmmo', False, 6, 1, 2, 200, 50, 1)

# Cyberpunk Weapons
# Masses are 1 until I figure that shit out

# Light Autopistols
budgetArmsC13 = firearm('Autopistol', 'Light', 7, -1, 1, 6, 0, '5mm', False, 8, 2, 1, 75, 50, 0.5)
budgetArmsC13.designate('Earth', 'BudgetArms C-13')
lightAutopistols = [budgetArmsC13]

# Medium Autopistols
militechArmsAvenger = firearm('Autopistol', 'Medium', 7, 0, 2, 6, 1, '9mm', False, 10, 2, 3, 250, 50, 1)
militechArmsAvenger.designate('Earth', 'Militech Arms Avenger')
mediumAutopistols = [militechArmsAvenger]

# Heavy Autopistols
budgetArmsAuto3 = firearm('Autopistol', 'Heavy', 7, -1, 3, 6, 0, '11mm', False, 8, 2, 1, 350, 50, 1)
budgetArmsAuto3.designate('Earth', 'BudgetArms Auto 3')
heavyAutopistols = [budgetArmsAuto3]

# Very Heavy Autopistols
armalite44 = firearm('Autopistol', 'Very Heavy', 7, 0, 4, 6, 1, '11mm', False, 8, 1, 2, 450, 50, 1)
armalite44.designate('Earth', 'Armalite 44')
veryHeavyAutopistols = [armalite44]

# Light Submachineguns
uziMiniauto9 = firearm('Submachinegun', 'Light', 7, 1, 2, 6, 1, '9mm', False, 30, 35, 3, 475, 150, 1)
uziMiniauto9.designate('Earth', 'Uzi Miniauto 9')
lightSubmachineguns = [uziMiniauto9]

# Medium Submachineguns
arasakaMinami10 = firearm('Submachinegun', 'Medium', 7, 0, 2, 6, 3, '10mm', False, 40, 20, 3, 500, 200, 1)
arasakaMinami10.designate('Earth', 'Arasaka Minami 10')
mediumSubmachineguns = [arasakaMinami10]

# Heavy Submachineguns
sternmeyerSMG21 = firearm('Submachinegun', 'Heavy', 7, -1, 3, 6, 0, '11mm', False, 30, 15, 3, 500, 200, 1)
sternmeyerSMG21.designate('Earth', 'Sternmeyer SMG 21')
heavySubmachineguns = [sternmeyerSMG21]

# Light Assault Rifles
militechRoninLightAssault = firearm('Assault Rifle', 'Light', 7, 1, 5, 6, 0, '5.56', False, 35, 30, 3, 450, 400, 1)
militechRoninLightAssault.designate('Earth', 'Militech Ronin Light Assault')
lightAssaultRifles = [militechRoninLightAssault]

# Medium Assault Rifles
akr20MediumAssault = firearm('Assault Rifle', 'Medium', 7, 0, 5, 6, 0, '5.56', False, 30, 30, 2, 500, 400, 1)
akr20MediumAssault.designate('Earth', 'AKR-20 Medium Assault')
mediumAssaultRifles = [akr20MediumAssault]

# Heavy Assault Rifles
fnralHeavyAssaultRifle = firearm('Assault Rifle', 'Heavy', 7, -1, 6, 6, 0, '7.62', False, 30, 30, 3, 600, 400, 1)
fnralHeavyAssaultRifle.designate('Earth', 'AKR-20 Medium Assault')
heavyAssaultRifles = [fnralHeavyAssaultRifle]

# Shotguns
arasakaRapidAssault12 = firearm('Shotgun', 'None', 7, -1, 4, 6, 0, 'Shells', False, 20, 10, 2, 900, 50, 1)
arasakaRapidAssault12.designate('Earth', 'Arasaka Rapid Assault 12')
shotguns = [arasakaRapidAssault12]

# Heavy Weapons
barettArasakaLight20mm = firearm('Heavy Weapon', 'Heavy', 7, 0, 4, 10, 3, '20/9mm', False, 10, 1, 3, 2000, 450, 1)
barettArasakaLight20mm.designate('Earth', 'Barett-Arasaka Light 20mm')
heavyWeapons = [barettArasakaLight20mm]


# weapons_list = [sw_combat_magnum, budgetarms_c13, militech_ronin, revolver]
