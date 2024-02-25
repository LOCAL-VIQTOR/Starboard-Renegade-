# Friday Night Firefight (FNFF) coding exercise
# Ripped from Mike Pondsmith's Cyberpunk 2020 TTRPG
# Meant for inclusion in Starboard, Renegade!

# Imports
import random
from time import sleep

# Basic Functions
def d(numDice,diceType,mod):   # Dice Roller 2D6+1 = d(2,6,1)
    result = mod
    for i in range(numDice):
        result += random.randint(1,diceType)
    return result

#    ______________  _________    ____  __  ________
#   / ____/  _/ __ \/ ____/   |  / __ \/  |/  / ___/
#  / /_   / // /_/ / __/ / /| | / /_/ / /|_/ /\__ \
# / __/ _/ // _, _/ /___/ ___ |/ _, _/ /  / /___/ /
# /_/   /___/_/ |_/_____/_/  |_/_/ |_/_/  /_//____/
# GUNS, GUNS, GUNS, GUNS, GUNS

class firearm():
    def __init__(self, gunType, subtype, tl, accuracy, numDice, damageDie, damageModifier, ammunition,
                 automaticFire, clipSize, rateOfFire, reliability, cost, gunRange, mass):
        self.origin = 'OriginErr'
        self.name = 'NameErr'
        self.type = gunType
        self.subtype = subtype
        self.tl = tl
        self.accuracy = accuracy
        self.numDice = numDice
        self.damageDie = damageDie
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

    def fire(self, character, distance):

        # Determine hit number based on firearm range
        hitNumber = 0
        if distance <= 5: hitNumber = 10
        if distance > 5 and distance <= self.range / 4: hitNumber = 15
        if distance > self.range / 4 and distance <= self.range / 2: hitNumber = 20
        if distance > self.range / 2 and distance <= self.range: hitNumber = 25
        if distance > self.range and distance <= self.range * 2: hitNumber = 30

        # Determine relevant skill
        if self.type == 'Autopistol': skillMod = character.skills.handgun
        if self.type == 'Submachinegun': skillMod = character.skills.submachinegun
        if self.type == 'Assault Rifle': skillMod = character.skills.rifle
        if self.type == 'Shotgun': skillMod = character.skills.shotgun
        if self.type == 'Heavy Weapon': skillMod = character.skills.heavyWeapons

        # Make an accuracy roll 1d10+skill+ref
        attackRoll = d(1, 10, skillMod + character.ref[0])

        self.clip[0] -= 1  # remove the fired shot

        print('Accuracy Roll: ' + str(attackRoll))  # please remove me 2/6

        # If hit, return damage roll, if not hit return 0
        if attackRoll >= hitNumber:
            damage = d(self.numDice, self.damageDie, self.damageMod)
            return damage
        if attackRoll < hitNumber: return 0

    def reload(self): # Reset the clip to full capacity
        self.clip[0] = self.clip[1]

    def info(self):
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


class fde():
    def __init__(self):
        self.name = 'James T. Hasp'
        self.ref = [7, 7]
        self.body = [7, 'Average']
        self.btm = -2
        self.headSP = 0
        self.torsoSP = 0
        self.rightArmSP = 0
        self.leftArmSP = 0
        self.rightLegSP = 0
        self.leftLegSP = 0
        self.damageTaken = 0
        self.stunned = False
        self.wound = 'Light'
        self.mortallyWounded = False
        self.dead = False
        self.gunSkill = 2
        self.firearm = 'firearmErr'
        # light
        # serious -2 ref
        # critical ref int cool 1/2
        # mortal ref int cool 1/3

    def setAbilities(self):
        if self.body[0] <= 2:
            self.body[1] = 'Very Weak'
            self.btm = 0
        if self.body[0] >= 3 and self.body[0] <= 4:
            self.body[1] = 'Weak'
            self.btm = -1
        if self.body[0] >= 5 and self.body[0] <= 7:
            self.body[1] = 'Average'
            self.btm = -2
        if self.body[0] == 8 or self.body[0] == 9:
            self.body[1] = 'Strong'
            self.btm = -3
        if self.body[0] == 10:
            self.body[1] = 'Very Strong'
            self.btm = -5

    def hollywoodOveracting(self):
        x = random.randint(1, 6)
        if x == 1: return 'screams, windmills arms, falls'
        if x == 2: return 'crumples like a rag doll'
        if x == 3: return 'spins around in place, falls'
        if x == 4: return 'clutches wound, staggers and falls'
        if x == 5: return 'stares stupidly at wound, then falls'
        if x == 6: return 'slumps to ground, moaning'

    def hitDamage(self, damage):
        locationHit = d(1,10,0)
        if locationHit == 1:
            print(self.name + ' hit in the head.')
            if self.headSP > 0:
                if self.headSP > damage: damage = 0
                if self.headSP <= damage:
                    damage -= self.headSP
                    self.headSP -= 1
            if self.headSP < 0: self.headSP = 0

        if locationHit >= 2 and locationHit <= 4:
            print(self.name + ' hit in the torso.')
            if self.torsoSP > 0:
                if self.torsoSP > damage: damage = 0
                if self.torsoSP <= damage:
                    damage -= self.torsoSP
                    self.torsoSP -= 1
            if self.torsoSP < 0: self.torsoSP = 0

        if locationHit == 5:
            print(self.name + ' hit in the right arm.')
            if self.rightArmSP > 0:
                if self.rightArmSP > damage: damage = 0
                if self.rightArmSP <= damage:
                    damage -= self.rightArmSP
                    self.rightArmSP -= 1
            if self.rightArmSP < 0: self.rightArmSP = 0

        if locationHit == 6:
            print(self.name + ' hit in the left arm.')
            if self.leftArmSP > 0:
                if self.leftArmSP > damage: damage = 0
                if self.leftArmSP <= damage:
                    damage -= self.leftArmSP
                    self.leftArmSP -= 1
            if self.leftArmSP < 0: self.leftArmSP = 0

        if locationHit == 7 or locationHit == 8:
            print(self.name + ' hit in the right leg.')
            if self.rightLegSP > 0:
                if self.rightLegSP > damage: damage = 0
                if self.rightLegSP <= damage:
                    damage -= self.rightLegSP
                    self.rightLegSP -= 1
            if self.rightLegSP < 0: self.rightLegSP = 0

        if locationHit == 9 or locationHit == 10:
            print(self.name + ' hit in the left leg.')
            if self.leftLegSP > 0:
                if self.leftLegSP > damage: damage = 0
                if self.leftLegSP <= damage:
                    damage -= self.leftLegSP
                    self.leftLegSP -= 1
            if self.leftLegSP < 0: self.leftLegSP = 0

        damage += self.btm
        if damage <= 0: damage = 1
        if damage > 0:
            print(self.name + ' takes ' + str(damage) + ' damage.')
            self.damageTaken += damage
            self.stunSave()

    def stunSave(self):
        print(self.name + ' Stun Save!')
        woundLevel = self.damageTaken // 4
        if woundLevel == 0: self.wound = 'Light'
        if woundLevel == 1:
            self.wound = 'Serious'
            self.ref[0] -= 2
        if woundLevel == 2:
            self.wound = 'Critical'
        if woundLevel > 2: self.mortallyWounded = True
        if woundLevel == 3: self.wound = 'Mortal0'
        if woundLevel == 4: self.wound = 'Mortal1'
        if woundLevel == 5: self.wound = 'Mortal2'
        if woundLevel == 6: self.wound = 'Mortal3'
        if woundLevel == 7: self.wound = 'Mortal4'
        if woundLevel == 8: self.wound = 'Mortal5'
        if woundLevel == 9: self.wound = 'Mortal6'
        print(self.wound)
        stunRoll = d(1,10,self.btm)
        stunSave = self.body[0] - woundLevel
        if stunRoll < stunSave: print(self.name + ' Stun Save Passed')
        if stunRoll >= stunSave:
            print(self.name + ' Stun Save Failed')
            print(self.name + ' ' + self.hollywoodOveracting())
            self.stunned = True

    def deathSave(self):
        woundLevel = self.damageTaken // 4
        if woundLevel == 0: self.wound = 'Light'
        if woundLevel == 1: self.wound = 'Serious'
        if woundLevel == 2: self.wound = 'Critical'
        if woundLevel == 3: self.wound = 'Mortal0'
        if woundLevel == 4: self.wound = 'Mortal1'
        if woundLevel == 5: self.wound = 'Mortal2'
        if woundLevel == 6: self.wound = 'Mortal3'
        if woundLevel == 7: self.wound = 'Mortal4'
        if woundLevel == 8: self.wound = 'Mortal5'
        if woundLevel == 9: self.wound = 'Mortal6'
        deathRoll = d(1,10,self.btm)
        deathSave = self.body[0] - woundLevel
        if deathRoll < deathSave: print(self.name + ' Death Save Passed')
        if deathRoll >= deathSave:
            print(self.name + ' Death Save Failed')
            self.dead = True
        if woundLevel < 2: self.mortallyWounded = False

    # Move
    # Attack
    # Dodge, melee only
    # Parry (?)
    # Escape hold/trap
    # Aim
    # Reload / change weapon
    # dis/mount vehicle
    # repair/medical aid
    # perform 'non-combat' tast

    # successive actions act as -3 consecutive after first
    # two attacks get -3 on both
    # backstabs

    # saves = roll equal or under body type
    # damage = damage - btm

    # head 1
    # torso 2-4
    # r.arm 5
    # l arm 6
    # r leg 7-8
    # l leg 9 -0

    # stun -DM = damage taken // 4


# every round is ~~ 3 seconds
# init = 1d10 + ref


player = fde()
player.ref[1] = random.randint(1, 10)
player.ref[0] = player.ref[1]
player.body[0] = random.randint(1, 10)
player.setAbilities()
player.firearm = random.choice(guns)

enemy = fde()
enemy.ref[1] = random.randint(1, 10)
enemy.ref[0] = enemy.ref[1]
enemy.body[0] = random.randint(1, 10)
enemy.setAbilities()
enemy.firearm = random.choice(guns)
while enemy.firearm == player.firearm: enemy.firearm = random.choice(guns)
enemy.name = 'Enemy'

print(player.name + ' | Ref ' + str(player.ref[0]) + ' BTM ' + str(player.btm) + ' | ' + player.firearm.name)
print(enemy.name + ' | Ref ' + str(enemy.ref[0]) + ' BTM ' + str(enemy.btm) + ' | ' + enemy.firearm.name)
print()

while player.stunned == False and enemy.stunned == False:
    playerFired = False
    enemyFired = False

    sleep(3)
    print('PLAYER SHOT')

    if player.firearm.clip[0] >= player.firearm.rof:
        playerFired = True
        for i in range(player.firearm.rof):
            damage = player.firearm.fire(player, 10)
            if damage > 0:
                enemy.hitDamage(damage)
            else:
                print('Shot Missed')
            print()
            sleep(1)

    if player.firearm.clip[0] < player.firearm.rof and playerFired == False:
        print('Reload')
        player.firearm.reload()

    print()
    sleep(3)
    print('ENEMY SHOT')

    if enemy.firearm.clip[0] >= enemy.firearm.rof:
        enemyFired = True
        for i in range(enemy.firearm.rof):
            damage = enemy.firearm.fire(player, 10)
            if damage > 0:
                player.hitDamage(damage)
            else:
                print('Enemy Shot Missed')
            print()
            sleep(1)

    if enemy.firearm.clip[0] < enemy.firearm.rof and enemyFired == False:
        print('Reload')
        enemy.firearm.reload()

    print()

if player.stunned == True: print('Enemy Win')
if enemy.stunned == True: print('Player Win')
print()
print(player.name + ' ' + str(player.damageTaken))
print(enemy.name + ' ' + str(enemy.damageTaken))

