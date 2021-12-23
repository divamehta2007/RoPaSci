# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 09:58:13 2021

@author: Diva Mehta
"""

class Player:
    # Constructor always called when the class is created
    def __init__(self):
        self.name = ""
        self.wins = 0
        self.losses = 0
        # -1 = no chocie, 1 = scissors, 2 = rock, 3 = paper
        self.hand = -1
    
    # Used to print the Player object
    def __str__(self):
        print("Name: " + self.name)
        print("Wins: " + str(self.wins))
        print("Losses: " + str(self.losses))
        #print("Selected Hand: " + str(self.hand))
        return ""

    def __repr__(self):
        print("Name: " + self.name)
        print("Wins: " + str(self.wins))
        print("Losses: " + str(self.losses))
        #print("Selected Hand: " + str(self.hand))
        return ""
