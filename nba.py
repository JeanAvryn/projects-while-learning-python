#NBA 2K Python Edition
import random

def nbapython_greet(username):
    print(f"Welcome to NBA 2K Python Edition, {username}!")
    
def invalidity():
    print("Invalid keywords. Please input a valid keyword.")
    
def cut():
    print("----------------------------------------------")
    
def playerGreet():
    print(f"Welcome to the NBA, {playerName} in the position of {selectPos}!")
    
def draftpick():
    print("You will now enter the 2024 Draft Pick!")
    
def finalMessage():
    print(f"Thank you for playing a sneak peek of NBA 2K Python Edition, {username}! We hope you had fun playing your player named {playerName} as a {selectPos}! See you around next time!")

cut()

username = input("Enter your username: ")

while username  == "":
    invalidity()
    username = input("Enter your name: ")
    

else:
    nbapython_greet(username)
    
cut()

playerName = input("Write a name for your NBA player: ")

while playerName == "":
    invalidity()
    playerName = input("Write a name for your NBA player: ")

playerPos = ["Shooting Guard", "Point Guard", "Small Forward", "Power Forward", "Center"]

selectPos = input("Select a position for your player: ")

while selectPos not in playerPos:
    invalidity()
    selectPos = input("Select a position for your player: ")
    
else:
    cut()
    playerGreet()
    
cut()

draftpick()

nbaTeams = ["Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets", "Chicago Bulls",
    "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets", "Detroit Pistons",
    "Golden State Warriors", "Houston Rockets", "Indiana Pacers", "Los Angeles Clippers",
    "Los Angeles Lakers", "Memphis Grizzlies", "Miami Heat", "Milwaukee Bucks",
    "Minnesota Timberwolves", "New Orleans Pelicans", "New York Knicks", "Oklahoma City Thunder",
    "Orlando Magic", "Philadelphia 76ers", "Phoenix Suns", "Portland Trail Blazers",
    "Sacramento Kings", "San Antonio Spurs", "Toronto Raptors", "Utah Jazz", "Washington Wizards"]

drafted_team = random.choice(nbaTeams)

draftNumber = random.randint(1, 60)

print("Which team would you go?\n..............")

print(f"Congratulations, {playerName}! You have been drafted #{draftNumber} overall by the {drafted_team}! Congratulations and good luck on your NBA career!")

cut()

firstOPP = random.choice(nbaTeams)

print(f"For your first official NBA game, you will face off the {firstOPP}!")

cut()

result = ["120-116", "100-99", "87-103", "99-104", "95-94", "93-86", "76-90", "92-90", "85-86", "104-102", "106-118", "68-87", "103-101", "134-120", "99-96", "96-99"]

start = input("Do you want to start the game? (yes/no): ")

firstgame = random.choice(result)

if start == "yes":
    print(f"The result of your first game is {firstgame}!")
    
elif start == "no":
    print(f"Your teammates played a game with the result of {firstgame}!")

else:
    while not start in ["yes", "no"]:
     invalidity()
     start = input("Do you want to start the game? (yes/no): ")
     
cut()

if selectPos == "Point Guard":
    points = random.randint(5, 15)
    assists = random.randint(13, 17)
    rebounds = random.randint(7, 10)
    steals = random.randint(2, 5)
    blocks = random.randint(0, 2)
    
elif selectPos == "Shooting Guard":
    points = random.randint(13, 25)
    assists = random.randint(10, 15)
    rebounds = random.randint(3, 7)
    steals = random.randint(3, 5)
    blocks = random.randint(0, 2)
    
elif selectPos == "Small Forward":
    points = random.randint(11, 22)
    assists = random.randint(14, 15)
    rebounds = random.randint(8, 10)
    steals = random.randint(4, 10)
    blocks = random.randint(0, 7)
    
elif selectPos == "Power Forward":
    points = random.randint(10, 14)
    assists = random.randint(10, 15)
    rebounds = random.randint(5, 15)
    steals = random.randint(6, 14)
    blocks = random.randint(3, 5)

elif selectPos == "Center":
    points = random.randint(3, 12)
    assists = random.randint(9, 15)
    rebounds = random.randint(12, 18)
    steals = random.randint(6, 14)
    blocks = random.randint(3, 10)

if start == "yes":
    print(f"Here are your stats:\nPoints: {points}\nAssists: {assists}\nRebounds: {rebounds}\nSteals: {steals}\nBlocks: {blocks}")
    
cut()

secondOPP = random.choice(nbaTeams)

print(f"For your second official game, you will face off the {secondOPP}! ")

cut()

start = input("Do you want to start the game? (yes/no): ")

firstgame = random.choice(result)

if start == "yes":
    print(f"The result of your first game is {firstgame}!")
    
elif start == "no":
    print(f"Your teammates played a game with the result of {firstgame}!")

else:
    while not start in ["yes", "no"]:
     invalidity()
     start = input("Do you want to start the game? (yes/no): ")

cut()

if selectPos == "Point Guard":
    points = random.randint(5, 15)
    assists = random.randint(13, 17)
    rebounds = random.randint(7, 10)
    steals = random.randint(2, 5)
    blocks = random.randint(0, 2)
    
elif selectPos == "Shooting Guard":
    points = random.randint(13, 25)
    assists = random.randint(10, 15)
    rebounds = random.randint(3, 7)
    steals = random.randint(3, 5)
    blocks = random.randint(0, 2)
    
elif selectPos == "Small Forward":
    points = random.randint(11, 22)
    assists = random.randint(14, 15)
    rebounds = random.randint(8, 10)
    steals = random.randint(4, 10)
    blocks = random.randint(0, 7)
    
elif selectPos == "Power Forward":
    points = random.randint(10, 14)
    assists = random.randint(10, 15)
    rebounds = random.randint(5, 15)
    steals = random.randint(6, 14)
    blocks = random.randint(3, 5)

elif selectPos == "Center":
    points = random.randint(3, 12)
    assists = random.randint(9, 15)
    rebounds = random.randint(12, 18)
    steals = random.randint(6, 14)
    blocks = random.randint(3, 10)

if start == "yes":
    print(f"Here are your stats:\nPoints: {points}\nAssists: {assists}\nRebounds: {rebounds}\nSteals: {steals}\nBlocks: {blocks}")
    
cut()

thirdOPP = random.choice(nbaTeams)

print(f"For your third official game, you will face off the {thirdOPP}!")

cut()

start = input("Do you want to start the game? (yes/no): ")

firstgame = random.choice(result)

if start == "yes":
    print(f"The result of your first game is {firstgame}!")
    
elif start == "no":
    print(f"Your teammates played a game with the result of {firstgame}!")

else:
    while not start in ["yes", "no"]:
     invalidity()
     start = input("Do you want to start the game? (yes/no): ")

cut()

if selectPos == "Point Guard":
    points = random.randint(5, 15)
    assists = random.randint(13, 17)
    rebounds = random.randint(7, 10)
    steals = random.randint(2, 5)
    blocks = random.randint(0, 2)
    
elif selectPos == "Shooting Guard":
    points = random.randint(13, 25)
    assists = random.randint(10, 15)
    rebounds = random.randint(3, 7)
    steals = random.randint(3, 5)
    blocks = random.randint(0, 2)
    
elif selectPos == "Small Forward":
    points = random.randint(11, 22)
    assists = random.randint(14, 15)
    rebounds = random.randint(8, 10)
    steals = random.randint(4, 10)
    blocks = random.randint(0, 7)
    
elif selectPos == "Power Forward":
    points = random.randint(10, 14)
    assists = random.randint(10, 15)
    rebounds = random.randint(5, 15)
    steals = random.randint(6, 14)
    blocks = random.randint(3, 5)

elif selectPos == "Center":
    points = random.randint(3, 12)
    assists = random.randint(9, 15)
    rebounds = random.randint(12, 18)
    steals = random.randint(6, 14)
    blocks = random.randint(3, 10)

if start == "yes":
    print(f"Here are your stats:\nPoints: {points}\nAssists: {assists}\nRebounds: {rebounds}\nSteals: {steals}\nBlocks: {blocks}")

cut()

salary = random.randint(35000, 195000)

print(f"For the past official three games you earned a salary of ${salary}!")

cut()
finalMessage()
