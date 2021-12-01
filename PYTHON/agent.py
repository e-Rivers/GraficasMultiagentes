from mesa import Agent
from random import randint

class Car(Agent):
    def __init__(self, unique_id, model, destPos):
        super().__init__(unique_id, model)
        # Value used to make the car "disappear"
        self.y = 1
        # Attributes to make the agent know where to go 
        self.destination = destPos
        self.tmpDir = ""
        # Attributes used to avoid cycles
        self.takenRoute = [[],[]]

    def step(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True, # Boolean for whether to use Moore neighborhood (diagonals) or Von Neumann (up/down/left/right).
            include_center=True) 
        
        getConOfCell = lambda x: self.model.grid.get_cell_list_contents([x])
        getConTypeOfCell = lambda x: [type(i) for i in getConOfCell(x)]
        posStepsCont = [getConOfCell(i) for i in possible_steps]
        posStepsType = [[type(j) for j in i] for i in posStepsCont]
        currPos = possible_steps.index(self.pos)
        motion = self.getMotion(possible_steps)
        
        # ################ FIRST FILTER 
        # If it's already in a Destination, then quits
        if Destination in getConOfCell(self.pos):
            self.y = -1000000
            return

        # ################ SECOND FILTER
        # Scans to find if there's a destination around
        for neighbor in possible_steps:
            # If it finds a destination point, it moves there
            if self.destination == neighbor:
                self.model.grid.move_agent(self, neighbor)
                return
    
        # ################ THIRD FILTER
        # Checks if is on the road (which it is, but to differentiate from the Traffic Light cell)
        if Road == posStepsType[currPos][0]: 

            # Checks if the car is on a "decision section"
            if posStepsCont[currPos][0].direction == "Omni":
                futurePos = possible_steps[motion[self.tmpDir]]
                #"""
                if self.tmpDir == "Left" or self.tmpDir == "Right":
                    posDirs = [(futurePos[0], futurePos[1]+1), futurePos, (futurePos[0], futurePos[1]-1), (self.pos[0], self.pos[1]+1), (self.pos[0], self.pos[1]-1)]
                    dirIndex = self.getBestMove(posDirs, getConTypeOfCell, 1)
                    self.takenRoute[0].append(self.pos)
                    self.takenRoute[1].append(posDirs[dirIndex])
                    self.model.grid.move_agent(self, posDirs[dirIndex])
                elif self.tmpDir == "Up" or self.tmpDir == "Down":
                    posDirs = [(futurePos[0]+1, futurePos[1]), futurePos, (futurePos[0]-1, futurePos[1]), (self.pos[0]+1, self.pos[1]), (self.pos[0]-1, self.pos[1])]
                    dirIndex = self.getBestMove(posDirs, getConTypeOfCell, 0)
                    self.takenRoute[0].append(self.pos)
                    self.takenRoute[1].append(posDirs[dirIndex])
                    self.model.grid.move_agent(self, posDirs[dirIndex])
            else:
                futurePos = motion[posStepsCont[currPos][0].direction]
                # If there's a traffic light in front
                if Traffic_Light == posStepsType[futurePos][0]:
                    if posStepsCont[futurePos][0].state:
                        self.model.grid.move_agent(self, possible_steps[futurePos]) 
                        self.tmpDir = posStepsCont[currPos][0].direction
                # If there's another car in front
                elif Car not in posStepsType[futurePos]:
                    self.model.grid.move_agent(self, possible_steps[futurePos]) 
                    self.tmpDir = posStepsCont[currPos][0].direction
                    
        # If the car is in the cell where the traffic light is
        else:
            self.model.grid.move_agent(self, possible_steps[motion[self.tmpDir]]) 

    def getMotion(self, posSteps):
        motion = {}
        for c in range(len(posSteps)):
            if posSteps[c][0] == self.pos[0]+1 and posSteps[c][1] == self.pos[1]:
                motion["Right"] = c
            elif posSteps[c][0] == self.pos[0]-1 and posSteps[c][1] == self.pos[1]:
                motion["Left"] = c
            elif posSteps[c][0] == self.pos[0] and posSteps[c][1] == self.pos[1]+1:
                motion["Up"] = c
            elif posSteps[c][0] == self.pos[0] and posSteps[c][1] == self.pos[1]-1:
                motion["Down"] = c
        return motion

    def getBestMove(self, posDirs, getConTypeOfCell, axis):
        minDistSigma = self.model.width*2 + self.model.height*2
        bestFuture = None
        #if self.pos in self.takenRoute[0]:

        for p in range(len(posDirs)):
            #print(self.pos)
            #print(self.takenRoute)
            #if self.pos not in self.takenRoute[0]:
            if (self.model.width-1 >= posDirs[p][0] >= 0) and (self.model.height-1 >= posDirs[p][1] >= 0):
                if Road in getConTypeOfCell(posDirs[p]) or (Traffic_Light in getConTypeOfCell(posDirs[p]) and self.pos[axis] == posDirs[p][axis]):
                    if abs(1+self.destination[0]-posDirs[p][0])+abs(1+self.destination[1]-posDirs[p][1]) < minDistSigma:
                        minDistSigma = abs(1+self.destination[0]-posDirs[p][0])+abs(1+self.destination[1]-posDirs[p][1])
                        bestFuture = p
        return bestFuture


class Traffic_Light(Agent):
    def __init__(self, unique_id, model, state = False, timeToChange = 10):
        super().__init__(unique_id, model)
        self.state = state
        self.timeToChange = timeToChange

class Destination(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

class Obstacle(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

class Road(Agent):
    def __init__(self, unique_id, model, direction= "Left"):
        super().__init__(unique_id, model)
        self.direction = direction
