import random
winOrLose = False
pWin = "You Win"
pLose = "You Lose"
firstRoll = True
while winOrLose == False:
    hitReturn = input("Hit Enter to Roll the dice")
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    aRoll = die1 + die2
    print (f"You rolled a: {aRoll}")
    if (firstRoll and (aRoll == 7 or aRoll == 11)):
        print(pWin)
        winOrLose = True
    if (firstRoll and (aRoll == 2 or aRoll == 3 or aRoll == 12)):
        print(pLose)
        winOrLose = True
    if (winOrLose == False):
        if firstRoll:
            point = aRoll
        else:
            if (aRoll == point):
                print(pWin)
                winOrLose = True
            if (aRoll == 7):
                print(pLose)
                winOrLose = True

    firstRoll = False
