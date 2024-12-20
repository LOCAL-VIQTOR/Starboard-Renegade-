# Starboard, Renegade! v0.3
`Pygame-based` `Version 0.3` **Starboard, Renegade!** ***(SBRG/SR)*** is a *space opera roleplaying game (SORPG)* coding project written in Python. The first code was probably written circa the `Summer of 2009`.

## Goals in Version 0.3
1) Have a workable system of motion, complete with the following:
    - "Mirror" jump-border system, that will follow the player's position and initiate a parsec jump when it comes into contact.
    - Correct loading of a "new area" when jumping (a new planet is loaded in the center)
    - Correct player position and velocity when entering a new area
2) Have a working freight trading system, complete with the following:
    - Working wallet system for buying and selling different freight.
    - Ability to store freight in inventory based on player's cargo tonnage.
    - Ability to buy and sell freight to a planet for profit.
3) Implement a Win Condition:
    - Survive to a certain hex on the map as your final destination.
    - Make enough money to buy something, like your freedom or paying off the ship's mortgage.
    - Aquire enough of a particular cargo to complete a personal mission, like getting nuclear material for your burdgeoning homeworld.
4) Implement fuel purchase, refinement, and consumption.
5) Create basic ship sprites for each configuration and *optionally* planet sprites for each trade code.

### `FORBIDDEN PROGRAMMING` Self-Policing Guidelinges
These are things I am trying to avoid as a programmer:
```
x) YOU MAY THINK THAT INCLUDING THESE WILL MAKE THE GAME BETTER. YOU ARE WRONG.
x) YOU ARE TRYING TO COMPLETE AN ALPHA, NOT RELEASE A FULL GAME IN A WEEK.
x) YOU ARE GOING TO CLEAN UP AND REWRITE THE CODE ANYWAY. THIS IS NOT AN EXCUSE.
```
1) Do not try to make other celestial objects besides the planet in the center of the parsec.
2) Do not try to make bot logic for any thing.
3) Do not attempt to implement gravity.
4) Do not attempt to implement advanced collision math or "impacts".
5) Do not Use your cat's image as a 'holding sprite'
6) Do not Work on any sprites or models that aren't planets or the ship.
7) Do not work on any character-related files
8) Do not work on any equipment related files beyond computers and hardpoints for vessels.
