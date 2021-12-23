# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 09:58:47 2021

@author: Diva Mehta
"""
import random
import models

# Gives information on the game
def printHelp():
    print("This is a game of Rock, Paper, Scissors!\nCreated by Diva Mehta.")
    print("\nRules:")
    print("1. Choose between Rock, Paper & Scissors")
    print("2. Paper covers Rock")
    print("3. Rock breaks Scissors")
    print("4. Scissors cuts Paper")
    print("\nGame is played between a human player and the computer.")
    print("Human player needs to choose between Rock, Paper & Scissors")
    print("Computer has already made a decision which will be displayed")
    print("after counter expires. Computer will make a decision for win/loss")
    print("and display the result on the terminal.")

def getName(player):
    player.name = input("\nEnter your name: ")

def printRoPaSciChoice():
    print("Select the number corresponding to the value listed below:")
    print("1. Scissors\n2. Rock\n3. Paper")
    choice = int(input("Enter your choice: "))
    return choice

def checkWinLoss(human, computer, humanChoice, computerChoice):
    if(humanChoice == 1):
        if(computerChoice == 1):
            print("No points gained. Same Choice...")
        elif(computerChoice == 2):
            print(computer.name + " Wins...")
            computer.wins += 1
            human.losses += 1
        elif(computerChoice == 3):
            print(human.name + " Wins...")
            human.wins += 1
            computer.losses += 1
    elif(humanChoice == 2):
        if(computerChoice == 1):
            print(human.name + " Wins...")
            human.wins += 1
            computer.losses += 1
        elif(computerChoice == 2):
            print("No points gained. Same Choice...")
        elif(computerChoice == 3):
            print(computer.name + " Wins...")
            computer.wins += 1
            human.losses += 1
    elif(humanChoice == 3):
        if(computerChoice == 1):
            print(computer.name + " Wins...")
            computer.wins += 1
            human.losses += 1
        elif(computerChoice == 2):
            print(human.name + " Wins...")
            human.wins += 1
            computer.losses += 1
        elif(computerChoice == 3):
            print("No points gained. Same Choice...")
    else:
        print("Wrong choice... TRY AGAIN STUPID")

def printComputerChoice(computerChoice):
    text = "Computer selected "
    if(computerChoice == 1):
        text += "Scissors"
    elif(computerChoice == 2):
        text += "Rock"
    else:
        text += "Paper"
    print(text)

def startGameLoop(human, computer):
    continueGame = 1
    while(continueGame == 1):
        computerChoice = random.randrange(1, 3, 1)
        userChoice = printRoPaSciChoice()
        printComputerChoice(computerChoice)
        checkWinLoss(human, computer, userChoice, computerChoice)
        continueGame = int(input("\nPLAY AGAIN... Press 1... :"))
    print(human)
    print(computer)
    
def executeRoPaSci():
    printHelp()
    # Declare the 2 players
    humanPlayer = models.Player()
    computerPlayer = models.Player()
    computerPlayer.isComputer = True
    computerPlayer.name = "Rigged Computer"
    getName(humanPlayer)
    startGame = int(input("Press 5 to START GAME: "))
    if(startGame == 5):
        startGameLoop(humanPlayer, computerPlayer)
    print("\n\nThankyou for playing. Exiting GAME...")

if __name__ == "__main__":
    executeRoPaSci()

