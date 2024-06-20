import random
from SRtools import *

#    ____  ___  __________  ____  _   _______
#   / __ \/   |/_  __/ __ \/ __ \/ | / / ___/
#  / /_/ / /| | / / / /_/ / / / /  |/ /\__ \
# / ____/ ___ |/ / / _, _/ /_/ / /|  /___/ /
# /_/   /_/  |_/_/ /_/ |_|\____/_/ |_//____/
# MISSION PATRONS AND MISSION STATEMENTS

class patron():
    def __init__(self):
        self.name = 'patronNameErr'
        self.type = 'patronTypeErr'
        self.occupation = 'patronOccupationErr'
        self.mission = 'missionErr'
        self.missionTarget = 'missionTargetErr'
        self.opposition = 'missionOppositionErr'

    def randomOccupation(self):
        patronTypes = ['Criminal', 'Local Leader', 'High Society',
                       'Commercial', 'Spacer', 'Unusual']
        self.type = random.choice(patronTypes)
        if self.type == 'Criminal': self.occupation = random.choice([
            'Assassin', 'Smuggler', 'Terrorist', 'Embezzler',
            'Thief', 'Revolutionary'])
        if self.type == 'Local Leader': self.occupation = random.choice([
            'Clerk', 'Administrator', 'Mayor', 'Minor Noble', 'Physician', 'Tribal Leader'])
        if self.type == 'High Society': self.occupation = random.choice([
            'Diplomat', 'Courier', 'Spy', 'Ambassador', 'Noble', 'Police Officer'])
        if self.type == 'Commercial': self.occupation = random.choice([
            'Merchant', 'Free Trader', 'Broker', 'Corporate Executive', 'Corporate Agent', 'Financier'])
        if self.type == 'Spacer': self.occupation = random.choice([
            'Belter', 'Researcher', 'Naval Officer', 'Pilot', 'Starport Administrator', 'Scout'])
        if self.type == 'Unusual': self.occupation = random.choice([
            'Alien', 'Playboy', 'Stowaway', 'Family Relative',
            'Agent of a Foreign Power', 'Imperial Agent'])

    def randomMission(self):
        missions = ['Assassinate a target', 'Frame a target', 'Destroy a target',
                    'Steal from a target', 'Aid in a burglary', 'Stop a burglary',
                    'Retrieve data or an object from a secure facility', 'Discredit a target',
                    'Find a lost cargo', 'Find a lost person', 'Deceive a target',
                    'Sabotage a target', 'Transport goods', 'Transport a person',
                    'Transport data', 'Transport goods secretly',
                    'Transport goods quickly', 'Transport dangerous goods',
                    'Investigate a crime', 'Investigate a theft', 'Investigate a murder',
                    'Investigate a mystery', 'Investigate a target', 'Investigate an event',
                    'Join an expidition', 'Survey a planet', 'Explore a new system',
                    'Explore a ruin', 'Salvage a ship', 'Capture a creature',
                    'Hijack a ship', 'Entertain a noble', 'Protect a target',
                    'Save a target', 'Aid a target', "It's a trap by the patron"]
        self.mission = random.choice(missions)

    def randomMissionTarget(self):
        targetTypes = ['Trade Goods', 'Objects', 'Places', 'NPCs',
                       'Organizations', 'Vessels']
        typeChosen = random.choice(targetTypes)
        if typeChosen == 'Trade Goods': self.missionTarget = random.choice([
            'Common Trade Goods', 'Random Trade Goods', 'Illegal Trade Goods'])
        if typeChosen == 'Objects': self.missionTarget = random.choice([
            'Computer Data', 'Alien Artifact', 'Personal Effects', 'Work of Art',
            'Historical Artifact', 'Weapon'])
        if typeChosen == 'Places': self.missionTarget = random.choice([
            'Starport', 'Asteroid Base', 'City', 'Research Station',
            'Bar or Nightclub', 'Medical Facility'])
        if typeChosen == 'NPCs':
            self.missionTarget = random.choice(['Random Patron', 'Random Opposition'])
            placeHolder = patron()
            placeHolder.randomOccupation()
            placeHolder.randomOpposition()
            placeHolder.name = generateName()
            if self.missionTarget == 'Random Patron':
                self.missionTarget = placeHolder.name + ', ' + placeHolder.occupation
            if self.missionTarget == 'Random Opposition':
                self.missionTarget = placeHolder.opposition
        if typeChosen == 'Organizations':
            self.missionTarget = random.choice(['Local Government', 'Planetary Government',
                                                'Corporation', 'Imperial Intelligence',
                                                'Criminal Syndicate', 'Criminal Gang'])
        if typeChosen == 'Vessels':
            self.missionTarget = random.choice(['Free Trader', 'Yacht', 'Cargo Hauler',
                                                'Police Cutter', 'Space Station', 'Warship'])

    def randomOpposition(self):
        oppositions = ['Low Tech', 'Average Tech', 'High Tech', 'Environmental',
                       'Technology', 'Social']
        typeChosen = random.choice(oppositions)
        if typeChosen == 'Low Tech': self.opposition = random.choice([
            'Animals', 'Large Animals', 'Bandits & Thieves', 'Fearful Peasants', 'Local Lord'])
        if typeChosen == 'Average Tech': self.opposition = random.choice([
            'Crminals (Thugs/Corsairs]', 'Criminals (Thieves/Sabateurs)', 'Police (Ordinary Security)',
            'Police (Inspectors/Detectives', 'Corporate Agents', 'Corporate Legal'])
        if typeChosen == 'High Tech': self.opposition = random.choice([
            'Starport Security', 'Imperial Marines', 'Interstellar Corporation', 'Alien Private Citizen or Corporation',
            'Alien Government', 'Space Travellers/Rival Ship'])
        if typeChosen == 'Environmental': self.opposition = random.choice([
            'Target in Deep Space', 'Target in Orbit', 'Hostile Weather', 'Dangerous Organisms/Radiation',
            'Target in Dangerous Region', 'Target in Restricted Area'])
        if typeChosen == 'Technology': self.opposition = random.choice([
            'Target under Elec. Observation', 'Hostile Guard Robots/Ships', 'Biometric Identification Needed',
            'Mechanical Failure/Computer Hacking', 'Characters under Surveillance', 'Out of fuel/ammunition'])
        if typeChosen == 'Social': self.opposition = random.choice([
            'Police Investigation', 'Legal Barriers', 'Nobility', 'Government Officials',
            'Target Protected by Third Party', 'Hostages'])

    def info(self):
        print(self.name + ', ' + self.occupation + '.')
        print(self.mission + ' | ' + self.missionTarget)
        print('Opposition: ' + self.opposition)


lydia = patron()
lydia.name = generateName()
lydia.randomOccupation()
lydia.randomMission()
lydia.randomMissionTarget()
lydia.randomOpposition()
lydia.info()
print()
