# Starboard Renegade Tools
# Basic Functions: Dice rolling, integer and letter switching.
import random

def d(dice,base,mod):   # Dice Roller, 2D6+1 = d(2,6,1)
    result = mod
    for i in range(dice):
        result += random.randint(1,base)
    return result

def dsixtysix(tens_modifier, ones_modifier):  # Rolls D66 with a modifier to 10s and 1s places
    return (random.randint(1, 6) * 10) + random.randint(1, 6) + (tens_modifier * 10) + ones_modifier

def hexSwitch(number):  # Takes a decimal and returns a hexadecimal string
    if isinstance(number,int)==True:
        if number < 10: return str(number)
        if 10 <= number <= 20:
            to_letter = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:'J',19:'K',20:'L'}
            return to_letter[number]
        else: print('Error: hexSwitch above 20')
    if isinstance(number,str)==True:
        if number == 'A': return 10
        if number == 'B': return 11
        if number == 'C': return 12
        if number == 'D': return 13
        if number == 'E': return 14
        if number == 'F': return 15
        if number == 'G': return 16
        if number == 'H': return 17
        if number == 'J': return 18
        if number == 'K': return 19
        if number == 'L': return 20
        else: return int(number)
    else: print('hexSwitch not number or letter.')
        

def alphaSwitch(numLet):  # Takes either a number or a
    if str(numLet).isdigit() == True:  # letter and returns the inverse
        if numLet == 1: return 'A'
        if numLet == 2: return 'B'
        if numLet == 3: return 'C'
        if numLet == 4: return 'D'
        if numLet == 5: return 'E'
        if numLet == 6: return 'F'
        if numLet == 7: return 'G'
        if numLet == 8: return 'H'
        if numLet == 9: return 'I'
        if numLet == 10: return 'J'
        if numLet == 11: return 'K'
        if numLet == 12: return 'L'
        if numLet == 13: return 'M'
        if numLet == 14: return 'N'
        if numLet == 15: return 'O'
        if numLet == 16: return 'P'
        if numLet == 17: return 'Q'
        if numLet == 18: return 'R'
        if numLet == 19: return 'S'
        if numLet == 20: return 'T'
        if numLet == 21: return 'U'
        if numLet == 22: return 'V'
        if numLet == 23: return 'W'
        if numLet == 24: return 'X'
        if numLet == 25: return 'Y'
        if numLet == 26: return 'Z'
    if str(numLet).isdigit() == False:
        if numLet == 'A': return 1
        if numLet == 'B': return 2
        if numLet == 'C': return 3
        if numLet == 'D': return 4
        if numLet == 'E': return 5
        if numLet == 'F': return 6
        if numLet == 'G': return 7
        if numLet == 'H': return 8
        if numLet == 'I': return 9
        if numLet == 'J': return 10
        if numLet == 'K': return 11
        if numLet == 'L': return 12
        if numLet == 'M': return 13
        if numLet == 'N': return 14
        if numLet == 'O': return 15
        if numLet == 'P': return 16
        if numLet == 'Q': return 17
        if numLet == 'R': return 18
        if numLet == 'S': return 19
        if numLet == 'T': return 20
        if numLet == 'U': return 21
        if numLet == 'V': return 22
        if numLet == 'W': return 23
        if numLet == 'X': return 24
        if numLet == 'Y': return 25
        if numLet == 'Z': return 26

def generateName(): # List of first names, middle names as letters, and nouns as last name (See: Toast of London)
    first_names = ['John', 'Steven', 'Mark', 'Caitlyn', 'Stella', 'Jessica', 'James', 'Robert', 'Michael', 'David',
                   'William', 'Richard', 'Joseph', 'Thomas', 'Christopher', 'Calvin', 'Mary', 'Patricia',
                   'Jennifer', 'Henry', 'Elijah', 'Charles', 'Tobias', 'Philomena', 'Phillip', 'Patrick', 'Stewart',
                   'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Sarah', 'Karen', 'Gillian', 'William']
    middle_initial = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'RR']
    last_names = ['Toast', 'Rock', 'Pan', 'Bell', 'Camp', 'Waterfall', 'Safe', 'Canteen', 'Wheel', 'Time', 'Year',
                  'Man', 'Thing', 'Woman', 'Child', 'State', 'Hand', 'Case', 'Program', 'Money', 'Cordycepts', 'Tongs',
                  'Camera', 'Flower', 'Orchid', 'Rose', 'Boiler', 'Oven', 'Drum', 'Letter', 'Library', 'Brick', 'Corn',
                  'Whiskey', 'Rogers', 'Bedford', 'Lowe', 'Pistol', 'Revolver', 'Can', 'Van', 'Sedan', 'Armoire',
                  'Knife', 'Switchblade', 'Basket', 'Harpoon', 'Harpsichord', 'Taco', 'Burrito', 'Sock', 'Branch',
                  'Cane', 'Driftwood', 'Woods', 'Processor', 'Candlestick', 'Blunderbuss']
    return random.choice(first_names) + ' ' + random.choice(middle_initial) + '. ' + random.choice(last_names)
