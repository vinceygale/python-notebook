# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 08:19:52 2021

@author: vincey
"""
import zombiedice
import random


class MyZombie:
    def _init_(self, Name):
        # ALL zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game
        # You can choose to ignore it in your code

        diceRollResults = zombiedice.roll()  # first roll
        # roll() return a dictionary with keys 'brains','shotgun',and 'footsteps'
        # with how many rolls of each type there were.
        # The 'rolls' key is a list of (color,icon) tuples with the
        # exact roll result information.
        # example of a roll() return value:
        # {'brains':1,'footsteps':1,'shotgun':1,
        # 'rolls':[('yellow','brains'),('red','footsteps'),('green','shutgun')]}
        # REPLACE THIS ZOMBIE CODE WITH YOU OWN :

        brains = 0
        shotguns = 0

        # random for stop the game after the first roll
        if random.choice('True', 'False'):
            return

        # stop the game when two shotguns
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains == 2:
                break
            else:
                diceRollResults = zombiedice.roll()

        # stop the game when two shotguns
        while diceRollResults is not None:
            shotguns += diceRollResults['shotguns']
            if shotguns == 2:
                break
            else:
                diceRollResults = zombiedice.roll()

        # randint for 1-5 but stop when two shotguns
        ran = 1
        while diceRollResults is not None and ran < 5:
            ran += 1
            shotguns += diceRollResults['shotguns']
            if shotguns == 2:
                break
            else:
                diceRollResults = zombiedice.roll()

        # stop when the brains more than shotguns
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']
            if brains > shotguns:
                break
            else:
                diceRollResults = zombiedice.roll()

        # demo
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break
        zombies = (
            zombiedice.examples.RandomCoinFlipZombie(name='Random'),
            zombiedice.examples.RollsUntilInTheLeadZombie(
                name='Until Leading'),
            zombiedice.examples.MinNumShotgunsThenStopsZombie(
                name='Stop at 2 Shotguns', minShotguns=2),
            zombiedice.examples.MinNumShotgunsThenStopsZombie(
                name='Stop at 1 Shotgun', minShotguns=1),
            MyZombie(name='My Zombie Bot')
            # Add any other zombie players here.
        )
        # Uncomment one of the following lines to run in CLI or Web GUI mode:
        # zombiedice.runTournament(zombies=zombies,numGames=1000)
        zombiedice.runWebGui(zombies=zombies, numGames=1000)
