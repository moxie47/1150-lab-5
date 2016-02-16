"""
Tryggve Rogness  ITEC1150
This is Hangman in python, gee I hope this works.
I imported turtle up here, hoping it would speed things up.
"""
#It seemed to work better getting the turtle graphics rolling early
import turtle
wn = turtle.Screen()
Link = turtle.Turtle()
Link.speed(0)
Link.hideturtle()
Link.backward(100)
Link.forward(50)
Link.left(90)
Link.forward(200)
Link.right(90)
Link.forward(40)
Link.right(90)
Link.forward(10)
Link.left(90)
print("Gallows pole is almost ready in the graphics window.")
#Welcoming the player with a text graphic
print("Welcome to:")
print("H   H    A    N   N   GGG   M     M    A    N   N")
print("H   H   A A   NN  N  G      MM   MM   A A   NN  N")
print("HHHHH  A   A  N N N  G  GG  M M M M  A   A  N N N")
print("H   H AAAAAAA N  NN  G   G  M  M  M AAAAAAA N  NN")
print("H   H A     A N   N   GGG   M     M A     A N   N")
print("A Rogness Abomination")

#Here are blank starting variables that are built up, in-game
Wrongs=0
alphaWrongs=""
blanks=""
letterlist=[]

#Pulled some of the start up out and tried to recurse on bad input
from randoWord import getInTheGame
gameType=getInTheGame()
if gameType=="1":
        Word=str(input("Player 1 please enter the word you would like your \
opponent to guess: "))
elif gameType=="2":
    from randoWord import gitWord
    Word=gitWord()
else:
    print("Invlaid input, please restart")
    quit()

#Establishing values unavailable before Word was chosen

for letter in range(len(Word)):
    blanks=str((blanks)+("_ "))  #essential for progress on correct guesses
    letterlist=letterlist+[Word[letter]]   #a list comprised of letters in Word
    #letterlist orients the letters for the blanks and allows for easy indexing
iterNums=(len(Word)+6)


#Printing the play surface and opening Turtle graphics window
print("Thank you and good luck.")
print(" ")
print(" ")
print(" ")
print(blanks)



#Letting the game know the maximum play duration
while iterNums>=1:
    if blanks.count("_")==0:
        print("Congratulations!  You have successfully guessed enough \
correct letters to save the condemned!")  #the win notifier
        iterNums=0  #stop the game from reporting the previous statement a lot more
    elif Wrongs<6:
        iterNums=(iterNums-1)
        JustGuessedLet=str(input("Guess a letter: ")) #wrongs were a lot easier to
        if letterlist.count(JustGuessedLet)==0:     #handle, just check to see if
            print(blanks)                           #it's there, no, add to list
            Wrongs=Wrongs+1       #track wrongs to check against losing capacity (6)                              
            alphaWrongs=alphaWrongs+str(JustGuessedLet+" ")
            if Wrongs==1:
                for paces in range(270):
                    Link.forward(.7)
                    Link.right(2)
            elif Wrongs==2:
                Link.right(-90)
                Link.forward(80)
                Link.forward(-70)
                Link.right(30)
            elif Wrongs==3:
                Link.forward(50)
                Link.forward(-50)
                Link.right(-60)
            elif Wrongs==4:
                Link.forward(50)
                Link.forward(-50)
                Link.right(30)
                Link.forward(70)
                Link.right(-30)
            elif Wrongs==5:
                Link.forward(60)
                Link.forward(-60)
                Link.right(60)
            elif Wrongs==6:
                Link.forward(60)
                
                
            print(alphaWrongs)        #print list as well as updated game display
                       
#lost faith in here a few times, I kept getting the spacing wrong
#kept forgetting about the spacing in "blanks" thus the "2*/"-ing
        else:
            while letterlist.count(JustGuessedLet)>0:
                aplace=0
                aplace=2*(letterlist.index(JustGuessedLet))  
                ltraplace=int(aplace/2)
                blanks=(blanks[0:aplace]+str(JustGuessedLet)\
                        +blanks[(aplace+1):(2*len(Word))])
                letterlist.remove(JustGuessedLet)            
                letterlist.insert((ltraplace),"1")           
            print(blanks)
            print(alphaWrongs)
    elif Wrongs==6:
        print("The word you were looking for was ", Word)
        print("You have failed to save the condemned and the gallows pole\
 claims another.  Better luck next time.") #losing statement
        iterNums=0 #stop the game from reporting the previous statement a lot more
