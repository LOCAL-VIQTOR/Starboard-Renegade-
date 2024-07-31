# Starboard, Renegade!
*An ostensible roleplaying "game" created by LOCAL-VIQTOR.*
### *It is the far-off future year of 2006. The human race has spread its creeping tendrils to the furthest reaches of the stars. The taxation of trade routes to outlying star systems is once again in dispute. . . Code red, we are under attack! Battle stations! Starboard, Renegade!* 
*Starboard, Renegade!* is a programming project and hobby that was started approximately in Spring 2022. Drawn with hefty inspiration from *Cyberpunk 2020*, *Mongoose Traveller*, and *GAMMAWORLD*, it was originally meant as a storytelling device that sought to quickly determine worldbuilding details and alleviate some of the headache involved in having to consistently generate new ideas by hand for objects or locations which will reasonably never be explored. Now, it is expanding to a graphical user interface (**not** pronounced "goo-ey") that covers the areas of planet generation, space vessel construction, freight trade, and getting stranded in the icy depths of space for all eternity. 

Future versions of the game will incorporate player and non-player characters. The original program already has data included about character generation. Unfortunately, there is an extremely fun *'one-shot'* aspect to the program, watching characters continue to develop until they die in the process, sometimes at over 100 years old. Watch out, Conway's *Game of Life*, there's a new 0-player game in town.

## Major Considerations
- Planet Generator
- Equipment (Software & Computers, Firearms, Drugs, Tools, Survival Gear, etc.)
- Vessels (Space or otherwise)
- Character Generator (Childhood & Lifeskills, Education, Sebatical, Career)

## Current Files
- SRbackstory.py | Determines a character's childhood, such as family class & environment, status of parents, number of and relationships with siblings, current family status, and childhood skill selection.
- SRcharacters.py | The main handler for creating characters with SRbackstory, SRoccupation, and SRlifepath.
- SRcomputers.py | Details for handling computers and their connected equipment. Will most likely be merged with SRequipment.
- SRdiana.py | Details surrounding a player character being tested.
- SRequipment.py | Equippable or hands-on items for use by players.
- SRfirearms.py | Document detailing firearms and other general weaponry.
- SRfreight.py | Creates and distributes hands-off trade goods for use with SRplanets.
- SRlifepath.py | Handles Traveller-based character career paths.
- SRmain.py | Outdated main loop from previous branch.
- SRoccupation.py | Handles Cyberpunk-based character career paths.
- SRpatrons.py | Creates random missions and mission patrons.
- SRplanets.py | Generates galactic maps and populates them with detailed planets.
- SRskills.py | Skill handler for use with SRcharacters.
- SRtools.py | Generally called-upon functions, such as d().
- SRvessels.py | Details concerning construction and operation of various vehicles. 
