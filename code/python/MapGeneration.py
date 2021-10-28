states=[['q0',0,0]]
edges=[]
visited=[]
#CHECKING CURRENT STATE
def checkCurrentState(posX,posY):
    existing,index=checkStateExistance(posX,posY)   #checking the existance of the state
    if existing :                                   #check the existance of state
        states=states                               #getting the states
        length=len(states)-1                        #length of the states
        setEdge(states[index][0],states[length][0]) #setting the edge
        temp=states.pop(index)                      #removing the last visited state
        states.append(temp)                         #updating the last visited state
#EDGE GENERATOR
def checkEdgeExistance(state1,state2):          #CHECKS THE EXISTANCE OF EDGE
    existance=False                             #initialzing the existance
    for i in range(len(edges)):                 #loop for checking the existance
        if edges[i][0] == state1:               #checking state1 is equal to the existing state
            if edges[i][1] == state2:           #checking state2 is equal to the existing state
                existance=True                  #setting the existance to true
                break                           #breaking unwanted loop
        elif edges[i][0] == state2:             #checking state2 is equal to the existing state
            if edges[i][1] == state1:           #checking state1 is equal to the existing state
                existance=True                  #setting the existance to true
                break                           #breaking unwanted loop
    return existance                            #returning existance
def setEdge(state1,state2):                     #FROMING EDGE
    existance=checkEdgeExistance(state1,state2) #check existance existance procedure call
    if existance:                               #checking the existance
        pass                                    #the edge is already existing so doing nothing
    else:                                       #in the absence of the edge existing
        temp=[]                                 #temp for list formation
        temp.append(state2)                     #appending the state2 to temp list                  
        temp.append(state1)                     #appending the state1 to temp list  
        edges.append(temp)                      #appending the edge to the database
#STATE GENERATOR
def checkStateExistance(posX,posY):                                         #CHECKS THE EXISTANCE OF A STATE 
    existance=False                                                         #initialization the existance
    for i in range(len(states)):                                            #loop for checking the existance of the state
        if posX == states[i][1] and posY == states[i][2]:                   #checking the equality of the coordinates
            existance=True                                                  #setting the existance to true
            break                                                           #avoiding unwanted loop
    return existance,i                                                      #returning existance and index
def setState(posX,posY):                           #SETTING A NEW STATE
    existing,i=checkStateExistance(posX,posY)      #check state existance procedure call
    if existing:                                   #checking the existance of state                    
        state=0                                    #no new state
    else:                                          #new state
        temp=[]                                    #list to store the coordinates and state                           
        count=len(states)                          #length of database
        state='q'+str(count)                       #state string making 
        temp.append(state)                         #appending the state
        temp.append(posX)                          #appending x coordinate
        temp.append(posY)                          #appending x coordinate
        states.append(temp)                        #appending the new state to database
        setEdge(state,states[count-1][0])          #setting edge for new state
    return state                                   #returning the state
#GETTER METHOD
def getCurrentState(posX,posY):                                         #CHECKS THE EXISTANCE OF A STATE 
    existance=False                                                     #initialization the existance
    for i in range(len(states)):                                        #loop for checking the existance of the state
        if posX == states[i][1] and posY == states[i][2]:               #checking the equality of the coordinates
            existance=True                                              #setting the existance to true
            break                                                       #avoiding unwanted loop
    if existance:
        return states[i][0]
    else:
        return 0
#PATH FINDING
def getSubNodes(node,destinationNode):
    subNodes=[]
    for i in range(len(edges)):
        if (edges[i][1] or edges[i][0]) in visited:
            continue
        else:
            if edges[i][1] == node:
                edge=edges[i][0]
                if edge==destinationNode:
                    subNodes.append(destinationNode)
                    return subNodes,True
                else:
                    subNodes.append(edge)
            elif edges[i][0] == node:
                edge=edges[i][1]
                if edge==destinationNode:
                    subNodes.append(destinationNode)
                    return subNodes,True
                else:
                    subNodes.append(edge)
    return subNodes,False
def pathFinder(initialNode,destinationNode):
    path=[]
    for i in range(len(visited)):
        visited.pop()
    path.append([initialNode])
    i=0
    while True:
        currentNode=path[len(path)-1][0]
        if currentNode in visited:
            path[len(path)-1].remove(currentNode)
            while True:
                if len(path[len(path)-1]) == 0:
                    path.pop()
                    path[len(path)-1].pop(0)
                    continue
                else:
                    break
        else:
            subNodes,isDestination=getSubNodes(currentNode,destinationNode)
            if len(subNodes) == 0:
                break
            visited.append(currentNode)
            if isDestination:
                path.append([destinationNode])
                break
            else:
                if len(subNodes) > 1:
                    path.append(subNodes)
                else:
                    path.append(subNodes)
    return path
#RETURING PATH
def getPath(initialNode,destinationNode):
    pathNodes=pathFinder(initialNode,destinationNode)
    path=[]
    for i in range(len(pathNodes)):
        for j in range(len(states)):
            if pathNodes[i][0] == states[j][0]:
                path.append(states[j])
    return path
