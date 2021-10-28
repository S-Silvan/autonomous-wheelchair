import turtle
def moveForward():
    print("up")
def moveForwardRelease():
    print("up release")
turtle.listen()                       #initilization of the listner
turtle.onkey(moveForward,"Up")
turtle.onkeyrelease(moveForwardRelease,"Up")   #module call for up key press
turtle.mainloop() 
