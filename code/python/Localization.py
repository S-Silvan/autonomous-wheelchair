coordinates=[0,0]                               #initizing coordinates to 0,0
#SETTING CURRENT COORDINATES 
def setCoordinates(head): 
    if head == 90 :                             #checking the heading is north 
        coordinates.append(coordinates[1]+1)    #adding to the coordinate of y
        coordinates.pop(1)                      #pop extra coordinate
    elif head == 270 :                          #checking the heading is south
        coordinates.append(coordinates[1]-1)    #subracting to the coordinate of y
        coordinates.pop(1)                      #pop extra coordinate
    elif head == 0 :                            #checking the heading is east
        coordinates.insert(0,coordinates[0]+1)  #adding to the coordinate of x
        coordinates.pop(1)                      #pop extra coordinate
    elif head == 180 :                          #checking the heading is west
        coordinates.insert(0,coordinates[0]-1)  #subracting to the coordinate of x
        coordinates.pop(1)                      #pop extra coordinate
#RETURNING CURRENT COORDINATES
def getCoordinates():
    return coordinates[0],coordinates[1]        #retruning both the coordinates
    
