import random

play = True
class Slot:
    # the class Slot has as attributes the symbols, and winnings per symbol
    # Constructor
    def __init__(self):
        self.symbols = ["", "@", "€", "£", "%", "&", "*"]
        self.symbolWin = [5, 10, 20, 70, 200, 1000, 100000]

    # gets the index that is supposed to come out
    def getIndex(self, num):
        if (0 < num <= 50): return 0
        if (50 < num <= 90): return 1
        if (90 < num <= 120): return 2
        if (120 < num <= 140): return 3
        if (140 < num <= 150): return 4
        if (150 < num <= 155): return 5
        if (num == 156): return 6
    
    def roll(self, bet, availCredits):
        symbols = []
        for i in range(3):
            num = (random.randint(1, 156))
            ind = self.getIndex(num)
            symbols += self.symbols[ind]
                
        print("------------------\n|"+symbols[0]+"\t"+symbols[1]+"\t"+symbols[2]+"|\n------------------")
        
        if (symbols[0] == symbols[1] == symbols[2]):
            wins = self.symbolWin[ind]
            totalWins = bet*wins
            print("Congratulations! You won " + str(totalWins) + " credits\n")  
        else: print("Better luck next time")
        
        print("TOTAL CREDITS:" + str(availCredits) + "\n")
        if (availCredits == 0): 
            endGame()
            return 0

def startGame():
    while play == True:
        answer = str(input("Welcome! Would you like to play? YES/NO\n"))
        answer = answer.lower()
        if (answer == "yes" or answer == "y"):
            checkCredsInput()
            break
        elif (answer == "no" or answer == "n"):
            print("Hope to see you soon!\n")
            break
        else:
            print("Invalid answer\n")

def checkCredsInput():
    while play == True:
        initCreds = input("How many credits would you like to deposit?\n")
        if(initCreds.isnumeric()):
            initCreds = int(initCreds)
            if (initCreds > 0):
                startRound(initCreds)
                break
        else:
            print("Please incert a valid amount.\n")

def startRound(availCredits):
    slot = Slot()
    while (availCredits > 0):
        bet = input("How many credits would you like to bet?\n")
        if(bet.isnumeric()):
            bet = int(bet)
            if (bet > availCredits): 
                print("You don't have enough credits. Please incert a valid amount.\n")
            if (bet <= 0): 
                print("Please incert a valid amount of credits.\n")

            elif(bet <= availCredits):
                availCredits -= bet
                slot.roll(bet, availCredits)
        else: print("\nPlease incert a valid amount of credits.\n")

def endGame():
    print("You are out of credits. Game Over!")
    play = False
    return 0

startGame()