'''
1150 - 2014, David Kesler Final Project "Attack Turtles" 

import modules, setup screen
'''

import turtle
import time
from random import randint

wn = turtle.Screen()

wn.screensize(20,20)

'''
initialize variables
'''

playerScore = 0
playerHealth = 5
interceptPosX = 0
interceptPosY = -150
attackPos1X = 0
attackPos1Y = 0
attackPos2X = 0
attackPos2Y = 0
attackPos3X = 0
attackPos3Y = 0
stampPosX = 0
stampPosY = 0

'''
define turtle objects
'''
    
AttackTurtle1 = turtle.Turtle()
AttackTurtle1.ht()
AttackTurtle1.shape('turtle')
AttackTurtle1.color('Red')
AttackTurtle1.penup()
AttackTurtle1.turtlesize(2)
AttackTurtle1.speed(0)

AttackTurtle2 = turtle.Turtle()
AttackTurtle2.ht()
AttackTurtle2.shape('turtle')
AttackTurtle2.color('Red')
AttackTurtle2.penup()
AttackTurtle2.turtlesize(2)
AttackTurtle2.speed(0)

AttackTurtle3 = turtle.Turtle()
AttackTurtle3.ht()
AttackTurtle3.shape('turtle')
AttackTurtle3.color('Red')
AttackTurtle3.penup()
AttackTurtle3.turtlesize(2)
AttackTurtle3.speed(0)

InterceptTurtle = turtle.Turtle()
InterceptTurtle.ht()
InterceptTurtle.shape('turtle')
InterceptTurtle.penup()
InterceptTurtle.turtlesize(2)
InterceptTurtle.sety(-150)
InterceptTurtle.speed(0)

ScreenTurtle = turtle.Turtle()
ScreenTurtle.ht()
ScreenTurtle.shape('classic')
ScreenTurtle.width(138)
ScreenTurtle.pencolor('Blue')
ScreenTurtle.penup()
ScreenTurtle.setpos(-300, 200)

StampTurtle = turtle.Turtle()
StampTurtle.ht()
StampTurtle.shape('circle')
StampTurtle.turtlesize(3)
StampTurtle.color('Yellow')
StampTurtle.penup()
StampTurtle.speed(0)

'''
define functions

first function draws screen
'''

def drawScreen():

    ScreenTurtle.st()
    ScreenTurtle.pendown()
    ScreenTurtle.forward(600)
    ScreenTurtle.penup()
    ScreenTurtle.ht()
    ScreenTurtle.setpos(-300, -280)
    ScreenTurtle.width(10)
    ScreenTurtle.pendown()
    ScreenTurtle.st()
    ScreenTurtle.forward(600)
    ScreenTurtle.ht()
    
'''
opening 'graphics'
'''

def screenColor():

    wn = turtle.Screen()   
    for i in range (10):
        wn.bgcolor("orange")
        time.sleep(.04)
        wn.bgcolor("yellow")
        time.sleep(.04)
    wn.bgcolor("white")

    
'''
defines stamp when turtle is intercepted
'''

def turtleStamp(stampPosX, stampPosY):

    StampTurtle.setpos(stampPosX, stampPosY)
    StampTurtle.st()
    StampTurtle.stamp()
    StampTurtle.ht()

    
'''
defines InterceptTurtle key movement
'''
    
def go_up():

    global interceptPosX
    global interceptPosY    
    InterceptTurtle.setheading(90)
    listTurtle = InterceptTurtle.position()
    if (listTurtle[1]) >= 100:
        turtle.forward(0)
        interceptPosX = InterceptTurtle.xcor()
        interceptPosY = InterceptTurtle.ycor()
    else:
        InterceptTurtle.forward(10)
        interceptPosX = InterceptTurtle.xcor()
        interceptPosY = InterceptTurtle.ycor()

def go_right():

    global interceptPosX
    global interceptPosY    
    InterceptTurtle.setheading(0)
    InterceptTurtle.forward(10)
    interceptPosX = InterceptTurtle.xcor()
    interceptPosY = InterceptTurtle.ycor()
    
def go_left():

    global interceptPosX
    global interceptPosY        
    InterceptTurtle.setheading(180)
    InterceptTurtle.forward(10)
    interceptPosX = InterceptTurtle.xcor()
    interceptPosY = InterceptTurtle.ycor()


def go_down():

    global interceptPosX
    global interceptPosY        
    InterceptTurtle.setheading(270)
    InterceptTurtle.forward(10)
    interceptPosX = InterceptTurtle.xcor()
    interceptPosY = InterceptTurtle.ycor()

turtle.onkey(go_up, "Up")
turtle.onkey(go_down, "Down")
turtle.onkey(go_left, "Left")
turtle.onkey(go_right, "Right")

turtle.listen()

'''
defines main behavior of game
'''

def runAttack():


    global playerScore
    global playerHealth
    
    global interceptPosX
    global interceptPosY

    global attackPos1X
    global attackPos1Y

    global attackPos2X
    global attackPos2Y

    global attackPos3X
    global attackPos3Y



#first turtle start point and trajectory defined 

    def runAttack1():
        AttackTurtle1.ht ()    
        AttackTurtle1.setpos (220, 240)
        randomAngle1 = randint (230, 280)
        AttackTurtle1.setheading (randomAngle1)
        AttackTurtle1.st () 


#econd turtle start point and trajectory defined 


    def runAttack2():
        AttackTurtle2.ht ()    
        AttackTurtle2.setpos (-220, 240)
        randomAngle2 = randint (280, 315)
        AttackTurtle2.setheading (randomAngle2)
        AttackTurtle2.st ()
        

#third turtle start point and trajectory defined 


    def runAttack3():
        AttackTurtle3.ht ()
        AttackTurtle3.setpos (0, 240)
        randomAngle3 = randint (250, 290)
        AttackTurtle3.setheading (randomAngle3)
        AttackTurtle3.st ()


#first AttackTurtle speed and speed in relation to score defined.


    def speedAttack1():
        global attackPos1X
        global attackPos1Y
        global playerScore
        AttackTurtle1.st ()
        AttackTurtle1.forward(10)
        if playerScore <5:
            time.sleep(.06)
        elif playerScore <10:
            time.sleep(.03)
        elif playerScore <15:
            time.sleep(.015)
        else:
            time.sleep(0)
        attackPos1X = AttackTurtle1.xcor()
        attackPos1Y = AttackTurtle1.ycor()

#second AttackTurtle speed and speed in relation to score defined. 

    def speedAttack2():
        global attackPos2X
        global attackPos2Y
        global playerScore
        AttackTurtle2.st()
        AttackTurtle2.forward(10)
        if playerScore <5:
            time.sleep(.06)
        elif playerScore <10:
            time.sleep(.03)
        elif playerScore <15:
            time.sleep(.015)
        else:
            time.sleep(0)
        attackPos1X = AttackTurtle1.xcor()
        attackPos1Y = AttackTurtle1.ycor()
        attackPos2X = AttackTurtle2.xcor()
        attackPos2Y = AttackTurtle2.ycor()


#third AttackTurtle speed and speed in relation to score defined 


    def speedAttack3():
        global attackPos3X
        global attackPos3Y
        global playerScore
        AttackTurtle3.st()
        AttackTurtle3.forward(10)
        if playerScore <5:
            time.sleep(.06)
        elif playerScore <10:
            time.sleep(.03)
        elif playerScore <15:
            time.sleep(.015)
        else:
            time.sleep(0)
        attackPos1X = AttackTurtle1.xcor()
        attackPos1Y = AttackTurtle1.ycor()
        attackPos2X = AttackTurtle2.xcor()
        attackPos2Y = AttackTurtle2.ycor()        
        attackPos3X = AttackTurtle3.xcor()
        attackPos3Y = AttackTurtle3.ycor()


#AttackTurtle1 and InterceptTurtle relationship defined.



    def checkIntercept1():
        global playerScore
        global interceptPosX
        global interceptPosY
        global attackPos1X
        global attackPos1Y
        if (abs(attackPos1X - interceptPosX) <= 20) and (abs(attackPos1Y - interceptPosY) <= 20):
            playerScore += 1
            turtleStamp(attackPos1X, attackPos1Y)
            runAttack1()


#AttackTurtle2 and InterceptTurtle relationship defined.
           

    def checkIntercept2():
        global playerScore
        global interceptPosX
        global interceptPosY
        global attackPos2X
        global attackPos2Y
        if (abs(attackPos2X - interceptPosX) <= 20) and (abs(attackPos2Y - interceptPosY) <= 20):
            playerScore += 1
            turtleStamp(attackPos2X, attackPos2Y)
            runAttack2()

#AttackTurtle3 and InterceptTurtle relationship defined.


    def checkIntercept3():
        global playerScore
        global interceptPosX
        global interceptPosY
        global attackPos3X
        global attackPos3Y
        if (abs(attackPos3X - interceptPosX) <= 20) and (abs(attackPos3Y - interceptPosY) <= 20):
            playerScore += 1
            turtleStamp(attackPos3X, attackPos3Y)
            runAttack3()

#Run sequence initiated.


    runAttack1()
                
    for i in range(18):
        
        speedAttack1()
        time.sleep(.03)
        checkIntercept1()

        if attackPos1Y <= -250:
            playerHealth -= 1
            if playerHealth > 0:
                runAttack1()
            else:
                break

    runAttack2()

    for i in range(18):

        speedAttack1()
        time.sleep(.01)
        speedAttack2()
        checkIntercept1()
        checkIntercept2()

        if attackPos1Y <= -250:
            playerHealth -= 1
            if playerHealth > 0:
                runAttack1()
            else:
                break
 
        if attackPos2Y <= -250:
            playerHealth -= 1
            if playerHealth > 0:
                runAttack2()            
            else:
                break

    runAttack3()

    while playerHealth > 0:

        speedAttack1()     
        speedAttack2()    
        speedAttack3()

        checkIntercept1()
        checkIntercept2()
        checkIntercept3()

        if attackPos1Y <= -250:
            playerHealth -= 1
            if playerHealth > 0:
                runAttack1()
            else:
                break
           
        if attackPos2Y <= -250:
            playerHealth -= 1
            if playerHealth > 0:
                runAttack2()
            else:
                break

        if attackPos3Y <= -250:
            playerHealth -= 1
            if playerHealth > 0:
                runAttack3()
            else:
                break


#End of game behavior.

    wn.bye()
    print ("Your score was: " + str(playerScore))
    raise SystemExit

'''
Main defined.
'''


def main():

    time.sleep(1)
    
    drawScreen()

    InterceptTurtle.st()

    time.sleep(.5)
    
    screenColor()
    
    runAttack()

'''
Main initiated.
'''

main()
