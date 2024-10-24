# PROGRAM       SRvessels 
# AUTHOR        LOCAL-VIQTOR
# DATE CREATED  Unknown; Relocated 10/17/2024 | 10/20/2024
from SRtools import *
#import random
# Vessel Class
# Hardpoint Class
# Vessel Paperwork part of vessel class?
# Will have to re-do computers maybe? just keep them in this class till we re-do computers maybe?

class TitlePapers():
    def __init__(self,vessel,_random=True):
        self.vessel = vessel
        if _random == True:
            self.architect = generateName()
            self.builder = 'General Space Engineering Systems (GSES)'
            self.shipyard = 'GSES Construction Hanger No.89109'
            self.no_lien = ''
            self.lien = '10/20/06'
            self.hijacked = ''
            self.principal = vessel.stats.cost
            apyten = random.randint(50,150)
            self.apy = apyten / 10
            self.lease_months = random.randint(24,120)
            self.interest = int(self.principal * (self.apy/100) * (self.lease_months/12))
            self.with_interest = self.principal + self.interest
            self.borrower = generateName()
            self.borrower_group = 'the Scavenger Union ch.38A7b'
            self.lien_holder = generateName()
            self.lien_holder_group = 'the Federal Galactic Bank'
            self.borrower_date = self.lien
            self.lien_holder_date = self.lien
            self.owner = self.borrower
            self.payment_location = 'any FGB Terminal'
            self.payment_amount = int(self.with_interest/self.lease_months)
            self.financial_agreement = self.make_agreement()

    def make_agreement(self):
        lien_blurb = 'I, '+self.borrower+' of '+self.borrower_group+', will pay '+self.lien_holder+' of '+self.lien_holder_group+' CR '+str(self.payment_amount)+' for '+str(self.lease_months)+' months. \nPayment is due on the first day of each month and is to be presented at '+self.payment_location+'.'
        return lien_blurb

    def print(self):
        print()
        print(' --- VESSEL TITLE PAPERS --- ')
        print('Name:             '+self.vessel.designation)
        print('Class:            '+self.vessel.hull.num)
        #if self.vessel.hullMass // 100 == 1: scopeTag = 'craft'
        #if self.vessel.hullMass // 100 > 1: scopeTag = 'ship'
        #print('Type:             '+self.vessel.scope+scopeTag)
        print('Cost:             '+str(self.vessel.stats.cost))
        print('Architect:        '+self.architect)
        print('Builder:          '+self.builder)
        print('Shipyard:         '+self.shipyard)
        print()
        print(' ---        OWNER        --- ')
        print('Owner:            '+self.owner)
        print()
        print(' ---        LIEN         --- ')
        print('No Lien:          '+self.no_lien)
        print('Lien:             '+self.lien)
        print('Hijacked:         '+self.hijacked)
        print('Principal:        '+str(self.principal))
        print('APY:              '+str(self.apy)+'%')
        print(self.financial_agreement)
        print('Borrower:         '+self.borrower)
        print('Date:             '+self.borrower_date)
        print('Lien Holder:      '+self.lien_holder)
        print('Lien Holder Date: '+self.lien_holder_date)

class Spec():
    def __init__(self,num=0,spec='None',tons=0,cost=0,tons_per=0,cost_per=0):
        self.num = num              # Use this for various hull and drive classes, as well as quantities
        self.spec = spec            # like ship configuration or drive type
        self.tons = tons            # Keep to tons instead of mass
        self.cost = cost            # Keep to cost instead of price
        self.tons_per = tons_per
        self.cost_per = cost_per

    def _cost(self):
        if self.cost > 0: return self.cost
        if self.cost_per > 0: return self.cost_per*self.num
        else:
            print('No Cost Return (Spec)')
            return 0

    def _tons(self):
        if self.tons > 0: return self.tons
        if self.tons_per > 0: return self.tons_per*self.num
        else: return 0

    def print(self):
        print('Num: '+str(self.num))
        print('Spec: '+str(self.spec))
        print('Tons: '+str(self.tons))
        print('Cost: '+str(self.cost))
        print('Tons per: '+str(self.tons_per))
        print('Cost per: '+str(self.cost_per))

class VesselStats():
    def __init__(self,hull,armor):
        hull_struct = hull.tons // 50
        self.hull = hull_struct
        self.structure = hull_struct
        self.armor = armor.num
        self.tl = armor.tl
        self.tons = hull.tons
        self.cost = int(hull.cost + armor.cost)

    def upd_tl(self,num):
        if num > self.tl: self.tl = num

    def print(self):
        print('BASIC STATS:')
        print('Hull:   '+str(self.hull))
        print('Struct: '+str(self.structure))
        print('Armor:  '+str(self.armor))
        print('TL:     '+str(self.tl))
        print('Tons:   '+str(self.tons))

class Hull(Spec):
    def __init__(self,config='Wedge',hull_class='4',_random=False):
        standard = ['Wedge', 'Cone', 'Sphere', 'Cylinder']
        streamlined = ['Wing', 'Disc', 'Other Lifting Body']
        if _random == True:
            config = random.choice([*standard,*streamlined,'Distributed'])
            hull_class = random.randint(1,20)
        if isinstance(hull_class,int) == True: hull_class = hexSwitch(hull_class)
        hull_prices = {'1':2,'2':8,'3':12,'4':16,'5':32,'6':48,'7':64,'8':80,'9':90,'A':100,'B':110,'C':120,'D':130,'E':140,'F':150,'G':160,'H':170,'J':180,'K':190,'L':200}
        hull_price = hull_prices[hull_class]
        self.body = config
        self.configuration = 'Distributed'
        if config in standard: self.configuration = 'Standard'
        if config in streamlined:
            self.configuration = 'Streamlined'
            hull_price = hull_price * 1.1
        if self.configuration == 'Distributed':
            hull_price = hull_price * 0.9
            self.body = 'Distributed'
        super().__init__(num=hull_class,spec=self.configuration,cost=int(hull_price*1000000),tons=int(hexSwitch(hull_class)*100))

class Armor():
    def __init__(self,hull,titanium_steel=0,crystaliron=0,bonded_superdense=0,reflec=False,self_sealing=False,stealth=False,_random=False):
        if _random == True:
            titanium_steel = random.randint(0,2)
            crystaliron = random.randint(0,2)
            bonded_superdense = random.randint(0,2)
            reflec = random.choice([True,False])
            self_sealing = random.choice([True,False])
            stealth = random.choice([True,False])
        self.tl = 0
        c = hull.cost
        t = int(hull.tons)
        armor_weight = t * 0.05
        if titanium_steel > 0: self.tl = 7
        if self_sealing == True:
            self.self_sealing = Spec(num=1,cost=t*10000)
            self.tl = 9
        else: self.self_sealing = Spec(cost=t*10000)
        if reflec == True:
            self.reflec = Spec(num=1,cost=t*100000)
            self.tl = 10
        else: self.reflec = Spec(cost=t*100000)
        if crystaliron > 0: self.tl = 10
        if stealth == True:
            self.stealth = Spec(cost=10000)
            self.tl = 11
        else: self.stealth = Spec(cost=10000)
        if bonded_superdense > 0: self.tl = 14
        self.titanium_steel = Spec(num=titanium_steel,tons_per=armor_weight,cost_per=c*0.05)
        self.crystaliron = Spec(num=crystaliron,tons_per=armor_weight,cost_per=c*0.2)
        self.bonded_superdense = Spec(num=bonded_superdense,tons_per=armor_weight,cost_per=c*0.5)
        self.num = titanium_steel * 2 + crystaliron * 4 + bonded_superdense * 6
        self.tons = self.reflec._tons() + self.self_sealing._tons() + self.stealth._tons() + self.titanium_steel._tons() + self.crystaliron._tons() + self.bonded_superdense._tons()
        self.cost = self.reflec._cost() + self.self_sealing._cost() + self.stealth._cost() + self.titanium_steel._cost() + self.crystaliron._cost() + self.bonded_superdense._cost()

    def print(self):
        if self.titanium_steel.num > 0: print('Titanium Steel: '+str(self.titanium_steel.num))
        if self.crystaliron.num > 0: print('Crystaliron: '+str(self.crystaliron.num))
        if self.bonded_superdense.num > 0: print('Bonded Superdense: '+str(self.bonded_superdense.num))
        if self.reflec.num == 1: print('Reflec')
        if self.self_sealing.num == 1: print('Self-Sealing')
        if self.stealth.num == 1: print('Stealth')
        
class Drive(Spec):
    def __init__(self,vessel,thrust=-1,jump=-1,power=-1):
        self.hull_code = hexSwitch(vessel.hull.num)
        hc = self.hull_code
        if thrust > -1:
            self.drive_type = 'M-Drive'
            self.thrust = thrust
            if hc > 1: d_tons = hc*2-1
            else: d_tons = hc*2
            d_cost = hc*4
            self.fuel = 0
            d_code = self.scope(thrust)
        if jump > -1:
            self.drive_type = 'J-Drive'
            self.jump = jump
            d_tons = hc*5+5
            d_cost = hc*10
            self.fuel = vessel.hull.tons // 10
            d_code = self.scope(jump)
        if power > -1:
            self.drive_type = 'P-Plant'
            d_tons = (hc-1)*3+4
            d_cost = hc*8
            self.fuel = power*2
            d_code = power
        super().__init__(num=d_code,tons=d_tons,cost=d_cost)

    def scope(self,desired_rating,troubleshooting=False):
        drive_performance = [{1:1},{1:2,2:4,3:6},
                             {1:1,2:2,3:3,4:4,5:5,6:6},
                             {2:1,3:2,4:2,5:3,6:4,7:4,8:5,9:6},
                             {2:1,3:1,4:2,5:2,6:3,7:3,8:4,9:4,10:5,11:5,12:6,13:6},
                             {3:1,4:1,5:2,6:2,7:2,8:3,9:3,10:4,11:4,12:4,13:5,14:5,15:6,16:6,17:6},
                             {3:1,4:1,5:2,6:3,7:3,8:2,9:3,10:3,11:3,12:4,13:4,14:4,15:5,16:5,17:5,18:6,19:6,20:6},
                             {4:1,5:1,6:1,7:2,8:2,9:2,10:3,11:3,12:3,13:4,14:4,15:4,16:5,17:5,18:5,19:6,20:6,21:6,22:6,23:6,24:6},
                             {4:1,5:1,6:1,7:2,8:2,9:2,10:3,11:3,12:3,13:4,14:4,15:4,16:5,17:5,18:5,19:5,20:6,21:6,22:6,23:6,24:6},
                             {5:1,6:1,7:1,8:2,9:2,10:2,11:3,12:3,13:3,14:4,15:4,16:4,17:5,18:5,19:5,20:5,21:6,22:6,23:6,24:6},
                             {5:1,6:1,7:1,8:2,9:2,10:2,11:3,12:3,13:3,14:4,15:4,16:4,17:5,18:5,19:5,20:5,21:5,22:6,23:6,24:6},
                             {6:1,7:1,8:1,9:1,10:2,11:2,12:2,13:3,14:3,15:3,16:4,17:4,18:4,19:4,20:5,21:5,22:5,23:5,24:5},
                             {7:1,8:1,9:1,10:2,11:2,12:2,13:3,14:3,15:3,16:4,17:4,18:4,19:4,20:5,21:5,22:5,23:5,24:5},
                             {8:1,9:1,10:1,11:2,12:2,13:2,14:3,15:3,16:3,17:4,18:4,19:4,20:4,21:4,22:5,23:5,24:5},
                             {9:1,10:1,11:1,12:2,13:2,14:2,15:3,16:3,17:3,18:4,19:4,20:4,21:4,22:4,23:4,24:5},
                             {10:1,11:1,12:2,13:2,14:2,15:3,16:3,17:3,18:4,19:4,20:4,21:4,22:4,23:4,24:5}]
        range_tool = [[1,1],[1,3],[1,6],[2,9],[2,13],[3,17],[3,20],[4,24],[4,24],[5,24],[5,24],[6,24],[7,24],[8,24],[9,24]]
        if self.hull_code > 9: hc = ((self.hull_code - 9) // 2) + 9
        else: hc = self.hull_code
        result = 0
        ret_result = 0
        if troubleshooting:
            print('Troubleshooting scope('+str(desired_rating)+')')
            print('Hull Class: '+str(self.hull_code)+' | hc: '+str(hc))
            print(drive_performance[hc])
        for i in range(24):
            if range_tool[hc][0] <= i <= range_tool[hc][1]: # OOR: IX
                result = drive_performance[hc][i]
                if result >= desired_rating and ret_result == 0: ret_result = i
                if troubleshooting:
                    print('i:'+str(i)+', result:'+str(result)+' ret_r:'+str(ret_result))
        if ret_result != 0:
            if troubleshooting: print('Returned result: '+str(ret_result))
            return ret_result
        else:
            print('SCOPE ISSUE!!!')
            return ret_result

class Turret(Spec):
    def __init__(self,turret,troubleshooting=False):
        if troubleshooting: print(turret)
        self.ammo = 'None'
        self.weapon_range = 'None'
        self.damage = 'None'
        self.tl = 0
        cost = 0
        if turret == 'Pulse Laser':
            self.tl = 7
            self.weapon_range = 'Short'
            self.damage = '1d6'
            cost = 500000
        if turret == 'Beam Laser':
            self.tl = 7
            self.weapon_range = 'Medium'
            self.damage = '2d6'
            cost = 500000
        if turret == 'Particle Beam':
            self.tl = 8
            self.weapon_range = 'Long'
            self.damage = '3d6 + crew hit'
            cost = 500000
        if turret == 'Missile Rack':
            self.tl = 6
            self.weapon_range = 'Special'
            self.damage = 'Missile-Dependant'
            cost = 500000
            self.ammo = 'Missiles'
        if turret == 'Sandcaster':
            self.tl = 7
            self.weapon_range = 'Special'
            self.damage = 'Special'
            cost = 500000
            self.ammo = 'Sand Barrels'
        if turret == 'Empty': turret = 'Empty'
        super().__init__(spec=turret,cost=cost)

class SensorSuite(Spec):
    def __init__(self,spec):
        if spec == 'Random': spec = random.choice(['Standard','Basic Civilian','Basic Military','Advanced','Very Advanced'])
        if spec == 'Standard': s = [8, -4, ['Radar', 'Lidar'], 0, 0]
        if spec == 'Basic Civilian': s = [9, -2, ['Radar', 'Lidar'], 1, 50000]
        if spec == 'Basic Military': s = [10, 0, ['Radar', 'Lidar', 'Jammers'], 2, 1000000]
        if spec == 'Advanced': s = [11, 1, ['Radar', 'Lidar', 'Densitometer', 'Jammers'], 3, 2000000]
        if spec == 'Very Advanced': s = [12, 2, ['Radar', 'Lidar', 'Densitometer', 'Jammers', 'Neural Activity Sensor'], 5, 4000000]
        self.tl = s[0]
        self.mod = s[1]
        self.equipment = s[2]
        super().__init__(num=1,spec=spec,tons=s[3],cost=s[4])

    def print(self):
        print(self.spec+' Sensors (TL'+str(self.tl)+')')
        print(self.equipment,'Mod:',self.mod)

class Hardpoint(Spec):  # WILL HAE TO CHANGE RANGE INTO A NUMBER INSTEAD OF RELATIVE
    def __init__(self,turrets=-1,bay='No Bay',screen='No Screen',popup=False,fixed=False,_random=False,_random_turret=False):
        turrets_list = ['Pulse Laser','Beam Laser','Particle Beam','Missile Rack','Sandcaster']
        bays_list = ['Missile Bank','Particle Beam','Fusion Gun','Meson Gun']
        screens_list = ['Nuclear Damper','Meson Screen']
        if _random:
            x = d(1,10,0)
            if x < 5: turrets = [random.choice(turrets_list)]
            if 5 <= x <= 7: turrets = [random.choice(turrets_list),random.choice(turrets_list)]
            if 7 < x <= 9: turrets = [random.choice(turrets_list),random.choice(turrets_list),random.choice(turrets_list)]
            if x == 10:
                y = d(1,2,0)
                if y == 1: bay = random.choice(bays_list)
                if y == 2: screen = random.choice(screens_list)
        if _random_turret: turrets = [random.choice(turrets_list)]

        if isinstance(turrets,list) == True:
            turret_options = turrets
            turrets = len(turrets)
        self.tl = 0
        self.weapon_range = 'None'
        self.damage = 'None'
        self.ammo = 'None'
        
        if bay != 'No Bay':
            spec = bay
            tons = 51
            if spec == 'Missile Bank':
                self.tl = 6
                self.weapon_range = 'Special'
                self.damage = 'Launch 12 Missiles'
                cost = 12000000
                self.ammo = 'Missiles'
            if spec == 'Particle Beam':
                self.tl = 8
                self.weapon_range = 'Long'
                self.damage = '6d6 + crew hit'
                cost = 20000000
            if spec == 'Fusion Gun':
                self.tl = 12
                self.weapon_range = 'Medium'
                self.damage = '5d6'
                cost = 8000000
            if spec == 'Meson Gun':
                self.tl = 11
                self.weapon_range = 'Long'
                self.damage = '5d6 + crew hit'
                cost = 50000000
        elif screen != 'No Screen':
            spec = screen
            tons = 50
            self.tl = 12
            if spec == 'Nuclear Damper': cost = 50000000
            if spec == 'Meson Screen': cost = 60000000
        else:
            self.turrets = []
            tons = 1
            if turrets < 0:
                spec = 'No Hardpoint Installed'
                cost = 0
                tons = 0
            if turrets == 0:
                spec = 'Empty'
                cost = 0
                tons = 0
            if turrets == 1:
                spec = 'Single'
                cost = 200000
                self.tl = 7
            if turrets == 2:
                spec = 'Double'
                cost = 500000
                self.tl = 8
            if turrets == 3:
                spec = 'Triple'
                cost = 1000000
                self.tl = 9
            if turrets > 0:
                if fixed:
                    spec = 'Fixed-Mount '+spec
                    self.tons -= 1
                    cost = cost // 2
                if popup:
                    spec = spec + ' Pop-up'
                    self.tl = 10
                    tons += 1
                    cost += 1000000
            spec = spec + ' Turret'
            for turret in turret_options:
                new_turret = Turret(turret)
                self.turrets.append(new_turret)
                cost += new_turret.cost
        super().__init__(num=1,spec=spec,cost=cost,tons=tons)

    def print(self):
        #print('HARDPOINT:')
        if 'Turret' in self.spec:
            turret_string = self.spec + ' ('
            for i in range(len(self.turrets)):
                turret_string = turret_string+self.turrets[i].spec
                if i < len(self.turrets)-1: turret_string = turret_string + '/'
            turret_string = turret_string + ')'
            print(turret_string)
        else:
            print(self.spec)
        #print(self.cost)

class SpaceVessel():
    def __init__(self,_random=True,hardpoint_budget=3):
        self.designation = 'Test Vessel'
        self.license = self.return_license()
        self.hull = Hull(_random=_random)
        self.armor = Armor(self.hull,_random=_random)
        self.stats = VesselStats(self.hull,self.armor)
        self.mdrive = Drive(self,thrust=3)
        self.jdrive = Drive(self,jump=1)
        power = self.mdrive.num
        if power < self.jdrive.num: power = self.jdrive.num
        self.pplant = Drive(self,power=power)
        #self.title_papers = TitlePapers(self)
        self.fuel = [0,self.jdrive.fuel*self.jdrive.jump+self.pplant.fuel]
        self.available_hull = self.hull.tons - (self.armor.tons+self.mdrive._tons()+self.jdrive._tons()+self.pplant._tons()+self.fuel[1])

        # How do we decide how much will go in weapons vs. hull vs. options?
        HARDPOINTS = self.hull.tons // 100
        HP_TONS_BUDGET = self.available_hull // hardpoint_budget
        self.hardpoints = []

        self.sensors = SensorSuite('Random')
        self.stats.cost += self.sensors.cost
        self.available_hull -= self.sensors.tons
        self.stats.upd_tl(self.sensors.tl)

        for i in range(HARDPOINTS):
            if 50 >= HP_TONS_BUDGET > 15:
                new_hardpoint = Hardpoint(_random_turret=True)
                self.hardpoints.append(new_hardpoint)
                HP_TONS_BUDGET -= new_hardpoint.tons
                self.stats.upd_tl(new_hardpoint.tl)
            elif HP_TONS_BUDGET > 50:
                new_hardpoint = Hardpoint(_random=True)
                self.hardpoints.append(new_hardpoint)
                HP_TONS_BUDGET -= new_hardpoint.tons
                self.stats.upd_tl(new_hardpoint.tl)
            
        
        for hp in self.hardpoints:
            self.stats.cost += hp.cost
            self.available_hull -= hp.tons

        

        self.title_papers = TitlePapers(self)
        

    def return_license(self):
        lic = ''
        for i in range(3): lic = lic + alphaSwitch(random.randint(1,26))
        lic = lic + '-'
        for i in range(4): lic = lic  + str(random.randint(0,9))
        return lic

    def print(self):
        print(self.designation+' ('+self.license+')')
        print('Owner: '+self.title_papers.owner)
        print('Class '+self.hull.num+' '+self.hull.body+' ('+hexSwitch(self.mdrive.num)+'-'+hexSwitch(self.jdrive.num)+'-'+hexSwitch(self.pplant.num)+')')
        print('Fuel Tank: '+str(self.fuel[1]))
        print(str(self.stats.cost)+' CR @ '+str(self.title_papers.apy)+'% APY')
        print(str(self.title_papers.payment_amount)+' CR / mo. for '+str(self.title_papers.lease_months)+' months')
        self.stats.print()
        print('Available: '+str(self.available_hull)+' tons')
        self.armor.print()
        for weapon in self.hardpoints:
            weapon.print()
        self.sensors.print()

for i in range(3):
    print()
    b_bertha = SpaceVessel()
    while b_bertha.stats.tl > 9: b_bertha = SpaceVessel()
    b_bertha.print()
    
