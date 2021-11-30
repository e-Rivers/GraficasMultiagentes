from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from agent import *
import json

class RandomModel(Model):
    def __init__(self, N, size=1):

        lines = []
        cityMap = []
        with open("base.txt") as baseFile:
            lines = baseFile.readlines()

        # Multiplies the map times the value of size
        for line in lines:
            cityMap.append([item for i in range(size) for item in line.replace("\n","")])
        cityMapCopy = cityMap.copy()
        for i in range(size-1):
            cityMap.extend(cityMapCopy)


        self.width = len(cityMap[0])
        self.height = len(cityMap)

        self.grid = MultiGrid(self.width, self.height,torus = False) 
        self.schedule = RandomActivation(self)

        for r, row in enumerate(lines):
            for c, col in enumerate(row):
                if col in ["v", "^", ">", "<"]:
                    agent = Road(f"r{r*self.width+c}", self, dataDictionary[col])
                    self.grid.place_agent(agent, (c, self.height - r - 1))
                elif col in ["S", "s"]:
                    agent = Traffic_Light(f"tl{r*self.width+c}", self, False if col == "S" else True, int(dataDictionary[col]))
                    self.grid.place_agent(agent, (c, self.height - r - 1))
                    self.schedule.add(agent)
                elif col == "#":
                    agent = Obstacle(f"ob{r*self.width+c}", self)
                    self.grid.place_agent(agent, (c, self.height - r - 1))
                elif col == "D":
                    agent = Destination(f"d{r*self.width+c}", self)
                    self.grid.place_agent(agent, (c, self.height - r - 1))

        self.num_agents = N
        self.running = True 

    def step(self):
        pass
        """
        self.schedule.step()
        if self.schedule.steps % 10 == 0:
            for agents, x, y in self.grid.coord_iter():
                for agent in agents:
                    if isinstance(agent, Traffic_Light):
                        agent.state = not agent.state
        """
