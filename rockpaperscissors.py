##rock-paper-scissors
import random

playerPts = 0
compPts = 0

while True:
    items = ["rock", "paper", "scissors"]

    compChoice = random.choice(items).lower()
    playerChoice = input("Select a choice (rock/paper/scissors:  (Type done if you want to exit the system.) ").lower()
    
    if compChoice == playerChoice:
        print(f"The computer chose {compChoice}. Draw!")
    elif compChoice == items[0] and playerChoice == items[1]:
        print(f"The computer chose {compChoice}. Player wins!")
        playerPts += 1
    elif compChoice == items[1] and playerChoice == items[0]:
        print(f"The computer chose {compChoice}. Computer wins!")
        compPts +=1
    elif compChoice == items[0] and playerChoice == items[2]:
        print(f"The computer chose {compChoice}. Computer wins!")
        compPts += 1
    elif compChoice == items[2] and playerChoice == items[0]:
        print(f"The computer chose {compChoice}. Computer wins!")
        playerPts +=1
    elif compChoice == items[1] and playerChoice == items[2]:
        print(f"The computer chose {compChoice}. Player wins!")
        playerPts += 1
    elif compChoice == items[2] and playerChoice == items[1]:
        print(f"The computer chose {compChoice}. Computer wins!")
        compPts += 1
    elif playerChoice == "done":
        if playerPts == compPts:
            print(f"DRAW! You and computer had {playerPts} points!")
            break
        elif playerPts > compPts:
            print(f"You win! You had a total of {playerPts} points. Congratulations!")
            break
        elif playerPts < compPts:
            print(f"Nice try! You had a total of {playerPts} points. Better luck next time!")
            break
    else:
        break
