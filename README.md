# Starboard, Renegade!
Set in the far-off future year of 2006, *Starboard, Renegade!* is a programming project and ostensive roleplaying "game". Drawn with hefty inspiration from *Cyberpunk 2020*, *Mongoose Traveller*, and *GAMMAWORLD*, it is meant as a storytelling device that seeks to quickly determine worldbuilding details and alleviate some of the headache involved in having to consistently generate new ideas by hand for objects or locations which will reasonably never be explored. Unfortunately, there is an extremely fun *'one-shot'* aspect to the program, watching characters continue to develop until they die in the process, sometimes at over 100 years old. Watch out, Conway's *Game of Life*, there's a new 0-player game in town.

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
