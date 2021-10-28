#PRE BUILD LIBRARIES
import turtle               #importing turtle
#USER BUILD LIBRARIES
import MapGeneration        #importing MapGeneration
import Localization         #importing Localization
import HardwareInterface
#INITIALIZATION OF TURTLE
screen=turtle.Screen()      #initializing turtle screen
screen.screensize(800,500)  #setting screen width and height
leftWall=turtle.Turtle()    #initializing left wall
leftWall.left(90)           #rotating left pen to point upward
leftWall.penup()
path=turtle.Turtle()        #initialing path pen
path.left(90)               #rotating path pen to point upward
path.write('q0')            #marking initial state
rightWall=turtle.Turtle()   #initializing right wall
rightWall.left(90)          #rotating right pen to point upward
rightWall.penup()
#LIMIT VARIABLES
wallLimit=140               #setting the wall limit to be drawn based on sensor data
forwardLimit=20             #forward limit to move
rotationLimit=30            #rotationLimit
#ROOM BLUE PRINT DRAWER
def drawWall(instruction,movement):
    head=path.heading()                                          #getting the head of the path
    x=path.xcor()                                                #getting the x coordinate of path
    y=path.ycor()                                                #getting the y coordinate of path
    sensorDataLeft=instruction[0]                                #getting left sensor data
    sensorDataRight=instruction[2]                               #getting right sensor data                 
    if movement == 'L' or movement == 'R':                       #SETTING NO DRAWING FOR ROTATION
        leftWall.penup()                                         #left pen up
        rightWall.penup()                                        #right pen up                                                                        
    if head == 0:                                                #HEADING EAST
        leftWall.setposition(x-forwardLimit,y+sensorDataLeft)    #adjusting left wall based on sensor value    
        rightWall.setposition(x-forwardLimit,y-sensorDataRight)  #adjusting right wall based on sensor value
        leftWall.setheading(head)                                #setting heading angle of left wall based on path pen
        rightWall.setheading(head)                               #setting heading angle of right wall based on path pen
    if head == 90:                                               #HEADING NORTH
        leftWall.setposition(x-sensorDataLeft,y-forwardLimit)    #adjusting left wall based on sensor value
        rightWall.setposition(x+sensorDataRight,y-forwardLimit)  #adjusting right wall based on sensor value
        leftWall.setheading(head)                                #setting heading angle of left wall based on path pen
        rightWall.setheading(head)                               #setting heading angle of right wall based on path pen
    if head ==180:                                               #HEADING WEST
        leftWall.setposition(x+forwardLimit,y-sensorDataLeft)    #adjusting left wall based on sensor value
        rightWall.setposition(x+forwardLimit,y+sensorDataRight)  #adjusting right wall based on sensor value
        leftWall.setheading(head)                                #setting heading angle of left wall based on path pen
        rightWall.setheading(head)                               #setting heading angle of right wall based on path pen
    if head == 270:                                              #HEADING SOUTH
        leftWall.setposition(x+sensorDataLeft,y+forwardLimit)    #adjusting left wall based on sensor value
        rightWall.setposition(x-sensorDataRight,y+forwardLimit)  #adjusting right wall based on sensor value
        leftWall.setheading(head)                                #setting heading angle of left wall based on path pen
        rightWall.setheading(head)                               #setting heading angle of right wall based on path pen
    checkLimit(instruction)                                      #checkLimit procedure call
def checkLimit(instruction):
    if instruction[0] < wallLimit and instruction[2] < wallLimit:   #draw both side
        leftWall.pendown()                                          #left pen down
        rightWall.pendown()                                         #right pen down
    elif instruction[0] > wallLimit and instruction[2] < wallLimit: #draw right side
        leftWall.penup()                                            #left pen up
        rightWall.pendown()                                         #right pen down
    elif instruction[0] < wallLimit and instruction[2] > wallLimit: #draw left side
        leftWall.pendown()                                          #left pen down
        rightWall.penup()                                           #right pen up
    else:                                                           #draw No side
        leftWall.penup()                                            #left pen up
        rightWall.penup()                                           #right pen up
#MOVEMENT CONTROL FUNCTIONS
##MOVEMENT WITH GETTING SENOSOR DATA
def rotateLeft():                         #ROTATION LEFT
    x,y=Localization.getCoordinates()     #getting current coordinates
    state=MapGeneration.setState(x,y)     #updating states for intersection
    data=HardwareInterface.rotateLeftP()
    if state !=0 :                        #checking the existance of state
        path.write(state)                 #marking the state in map
    if data[2]<rotationLimit:
        pass
    else:
        path.left(90)                     #pen rotation left
        drawWall(data,'L')                #draw module call 
def moveForward():                                   #MOVE FORWARD
    Localization.setCoordinates(int(path.heading())) #setting the coordinates after the movement
    x,y=Localization.getCoordinates()                #getting the current coordinates
    globalState=MapGeneration.checkCurrentState(x,y) #cheking the current position is a state
    data=HardwareInterface.moveForwardP()
    if data[1]<forwardLimit:                         #checking whether the vehicle moved or not
        pass                                         #vehicle not moved
    else:                                            #vehicle moved
        path.forward(20)                             #pen move forward
        drawWall(data,'F')                           #draw module call
def rotateRight():                        #ROTATION RIGHT
    x,y=Localization.getCoordinates()     #getting current coordinates
    state=MapGeneration.setState(x,y)     #updating states for intersection
    data=HardwareInterface.rotateRightP()
    if state !=0 :                        #checking the existance of state
        path.write(state)                 #marking the state in map
    if data[0]<rotationLimit:             #checking rotation occurance
        pass
    else:
        path.right(90)                    #pen rotation right
        drawWall(data,'R')                #draw module call
#MAP INTERFACE
def mapRotateLeft():                           #ROTATION LEFT
    HardwareInterface.rotateLeft()
    path.left(90)                              #moving path left
def mapMoveForward():                          #MOVMENT FORWARD
    HardwareInterface.moveForward()
    Localization.setCoordinates(path.heading())#setting the coordinates
    path.forward(20)                           #moving path forward              
def mapRotateRight():                          #ROTATION RIGHT
    HardwareInterface.rotateRight()
    path.right(90)                             #moving path right
def getToHead(head,node1,node2):          #GETTING HEADING POSITION
    if node1[1] == node2[1]:              #same axis check
        if node1[2]>node2[2]:             #node position check
            toHead=270                    #setting to head                 
            sameAxis='x'                  #setting same axis
        else:
            toHead=90                     #setting to head
            sameAxis='x'                  #setting same axis
    else:
        if node1[1]>node2[1]:             #node position check
            toHead=180                    #setting to head
            sameAxis='y'                  #setting same axis
        else:
            toHead=0                      #setting to head
            sameAxis='y'                  #setting same axis
    return toHead,sameAxis
def setHead(head,toHead):                  #SETTING THE HEAD POSITION
    if toHead == 0:                        #toHead check 0
        if head == 0:                      #heading check 0
            pass
        if head == 90:                     #heading check 90                
            mapRotateRight()               #rotate right call
        if head == 180:                    #heading check 180
            mapRotateRight()               #rotate right call
            mapRotateRight()               #rotate right call
        if head == 270:                    #heading check 270
            mapRotateLeft()                #rotate left call
    elif toHead == 90:                     #toHead check 90
        if head == 0:                      #heading check 0
            mapRotateLeft()                #rotate left call
        if head == 90:                     #heading check 90 
            pass
        if head == 180:                    #heading check 180
            mapRotateRight()               #rotate right call
        if head == 270:                    #heading check 270
            mapRotateLeft()                #rotate left call
            mapRotateLeft()                #rotate left call
    elif toHead == 180:                    #toHead check 180
        if head == 0:                      #heading check 0
            mapRotateRight()               #rotate right call
            mapRotateRight()               #rotate right call
        if head == 90:                     #heading check 90 
            mapRotateLeft()                #rotate left call
        if head == 180:                    #heading check 180
            pass
        if head == 270:                    #heading check 270
            mapRotateRight()               #rotate right call
    elif toHead == 270:                    #toHead check 270
        if head == 0:                      #heading check 0
            mapRotateRight()               #rotate right call
        if head == 90:                     #heading check 90 
            mapRotateLeft()                #rotate left call
            mapRotateLeft()                #rotate left call
        if head == 180:                    #heading check 180
            mapRotateLeft()                #rotate left call
        if head == 270:                    #heading check 270
            pass
def getSign(value):  #SIGN DETECTION
    if value >= 0:   #checking whether the number is positive
        sign='p'     #positive
    else:
        sign='n'     #negative
    return sign      
def setForward(node1,node2,sameAxis):                                                       #FORWARD MOVEMENT GENERATION    
    if sameAxis == 'x':
        node1Sign=getSign(node1[2])                                                         #getting sign of x in node 1
        node2Sign=getSign(node2[2])                                                         #getting sign of x in node 2
        if node1Sign == 'n' and node2Sign == 'n':                                           #negative negative check
            num1=max(node1[2],node2[2])                                                     #to move y
            num2=min(node1[2],node2[2])                                                     #from move y
            result=(-num1)+num2                                                             #calculatng number of forward
            for i in range(result):
                mapMoveForward()                                                            #move forward call
        elif node1Sign == 'n' and node2Sign == 'p' or node1Sign == 'p' and node2Sign == 'n':#negative poitive check
            num1=max(node1[2],node2[2])                                                     #to move y
            num2=min(node1[2],node2[2])                                                     #from move y
            result=num1+(-num2)                                                             #calculatng number of forward
            for i in range(result):
                mapMoveForward()                                                            #move forward call
        elif node1Sign =='p' and node2Sign == 'p':                                          #positive positive check
            num1=max(node1[2],node2[2])                                                     #to move y
            num2=min(node1[2],node2[2])                                                     #from move y
            result=num1-num2                                                                #calculatng number of forward
            for i in range(result):
                mapMoveForward()                                                            #move forward call
    else:
        node1Sign=getSign(node1[1])                                                         #getting sign of y in node 1
        node2Sign=getSign(node2[1])                                                         #getting sign of y in node 2
        if node1Sign == 'n' and node2Sign == 'n':                                           #negative negative check
            num1=max(node1[1],node2[1])                                                     #to move x
            num2=min(node1[1],node2[1])                                                     #from move x
            result=(-num1)+num2                                                             #calculatng number of forward
            for i in range(result):
                mapMoveForward()                                                            #move forward call
        elif node1Sign == 'n' and node2Sign == 'p' or node1Sign == 'p' and node2Sign == 'n':#negative poitive check
            num1=max(node1[1],node2[1])                                                     #to move x
            num2=min(node1[1],node2[1])                                                     #from move x
            result=num1+(-num2)                                                             #calculatng number of forward
            for i in range(result):
                mapMoveForward()                                                            #move forward call
        elif node1Sign =='p' and node2Sign == 'p':                                          #positive positive check
            num1=max(node1[1],node2[1])                                                     #to move x
            num2=min(node1[1],node2[1])                                                     #from move x
            result=num1-num2                                                                #calculatng number of forward
            for i in range(result):
                mapMoveForward()                                                            #move forward call
def mapMoveOnPath(pathNodes):                                  #AUTONOMOUS DRIVING COMMANDS
    for i in range(len(pathNodes)-1):                          
        head=path.heading()                                    #getting the path heading
        toHead,axis=getToHead(head,pathNodes[i],pathNodes[i+1])#getting to head and 
        setHead(head,toHead)                                   #seting the head
        setForward(pathNodes[i],pathNodes[i+1],axis)           #move forward call
def pathGenerator():                                #MAP INTERFACE
    destination=input('enter where u want to go\n') #getting the destination
    x,y=Localization.getCoordinates()               #getting the coordinates
    position=MapGeneration.getCurrentState(x,y)     #state finding call
    path=MapGeneration.getPath(position,destination)#path finding call
    mapMoveOnPath(path)                             #autonomous driving call
#EVENT LISTNER MODULES
turtle.listen()                       #initilization of the listner
turtle.onkey(rotateLeft,"Left")       #module call for left key press
turtle.onkey(moveForward,"Up")        #module call for up key press
turtle.onkey(rotateRight,"Right")     #module call for right key press
turtle.onkey(pathGenerator,"Tab")     #convertion to map mode
turtle.mainloop()                     #event listner loop


