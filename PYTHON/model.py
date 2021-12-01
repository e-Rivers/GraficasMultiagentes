from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from agent import *
import json
from random import choice, randrange

class RandomModel(Model):
    """ 
    Creates a new model with random agents.
    Args:
        N: Number of agents in the simulation
        height, width: The size of the grid to model
    """
    def __init__(self, N, carSpan, intel):
        
        self.destCoords = []
        self.carIDs = 0
        self.carSpan = carSpan
        self.intel = intel
        dataDictionary = json.load(open("mapDictionary.txt"))

        with open('base.txt') as baseFile:
            lines = baseFile.readlines()
            self.width = len(lines[0])-1
            self.height = len(lines)

            self.grid = MultiGrid(self.width, self.height,torus = False) 
            self.schedule = RandomActivation(self)

            for r, row in enumerate(lines):
                for c, col in enumerate(row):
                    if col in ["v", "^", ">", "<", "."]:
                        agent = Road(f"r{r*self.width+c}", self, dataDictionary[col])
                        self.grid.place_agent(agent, (c, self.height - r - 1))
                    elif col in ["S", "s"]:
                        agent = Traffic_Light(f"tl{r*self.width+c}", self, False if col == "S" else True, int(dataDictionary[col]))
                        self.grid.place_agent(agent, (c, self.height - r - 1))
                    elif col == "#":
                        agent = Obstacle(f"ob{r*self.width+c}", self)
                        self.grid.place_agent(agent, (c, self.height - r - 1))
                    elif col == "D":
                        agent = Destination(f"d{r*self.width+c}", self)
                        self.grid.place_agent(agent, (c, self.height - r - 1))
                        self.destCoords.append((c, self.height - r - 1))

        self.num_agents = N
        self.running = True 

        for i in range(self.num_agents):
            carAgent = Car(f"car{self.carIDs}", self, choice(self.destCoords))
            spawnPos = (randrange(0, self.width), randrange(0, self.height))
            conType = [type(i) for i in self.grid.get_cell_list_contents([spawnPos])]
            isAtCross = True 
            while Road not in conType or Car in conType or isAtCross:
                spawnPos = (randrange(0, self.width), randrange(0, self.height))
                conType = [type(i) for i in self.grid.get_cell_list_contents([spawnPos])]
                if Road in conType:
                    isAtCross = self.grid.get_cell_list_contents([spawnPos])[0].direction == "Omni"
            self.grid.place_agent(carAgent, spawnPos)
            self.schedule.add(carAgent)
            self.carIDs += 1

    def step(self):
        self.schedule.step()
        if self.schedule.steps % 10 == 0:
            for agents, x, y in self.grid.coord_iter():
                for agent in agents:
                    if isinstance(agent, Traffic_Light):
                        agent.state = not agent.state

        if self.schedule.steps % self.carSpan == 0:
            carAgent = Car(f"car{self.carIDs}", self, choice(self.destCoords))
            self.grid.place_agent(carAgent, (0,0))
            self.schedule.add(carAgent)
            self.carIDs += 1
