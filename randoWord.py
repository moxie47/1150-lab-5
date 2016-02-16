def gitWord():
    from random import randint
    dictionary=["ant", "apple", "banana", "cat", "dog", "elf", "frog", "golf", "eulogy", "freezer", "grease", "hydraulic", "indigo"]
    dictEvener=(len(dictionary)-1)
    luckyNum=randint(0,dictEvener)
    return dictionary[luckyNum]

def getInTheGame():
    gameNum=input("What type of game would you like to play(1 for PvP, 2 for PvC)?")
    if gameNum is 1 or 2:
        return gameNum
    else:
        randoWord.getInTheGame()
