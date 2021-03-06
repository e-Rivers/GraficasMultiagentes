# -*- coding: utf-8 -*-
"""
model.py

Definition of the model that will regulate the general behaviour of the
environment of a city traffic simulation

Authors: Melissa Garduño Ruiz (A01748945), Omar Rodrigo Sorchini Puente (A01749389), Emilio Rios Ochoa (A01378965)
Date: December 4th, 2021
"""

from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from agent import *
import json
from random import choice, randrange

# The class of the model that will be used
class TrafficModel(Model):
    def __init__(self, N, carSpan, lightSpan):
        """
        Class initializer (constructor) to create a new Robot agent
        ● Parameters: 
            N: Number of initial cars randomly distributes
            carSpan: Number of steps a new car has to wait to appear
            lightSpan: Number of steps the traffic light will remain on each color
        ● Return: None
        """
        self.destCoords = []
        self.carIDs = 0
        self.carSpan = carSpan
        self.lightSpan = lightSpan
        dataDictionary = json.load(open("mapDictionary.txt"))

        with open('base.txt') as baseFile:
            lines = baseFile.readlines()
            self.width = len(lines[0])-1
            self.height = len(lines)

            self.grid = MultiGrid(self.width, self.height,torus = False) 
            self.schedule = RandomActivation(self)

            # Iterates through rows and cols to build the board of the simulation
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

        # Creates N new cars
        for i in range(self.num_agents):
            # Assings a random destination so the car movement won't be random
            carAgent = Car(self.carIDs, self, choice(self.destCoords))
            spawnPos = (randrange(0, self.width), randrange(0, self.height))
            conType = [type(i) for i in self.grid.get_cell_list_contents([spawnPos])]
            isAtCross = True
            # Verifies if the car was placed where another car is or in the middle of an intersection, if so, tries again
            while Road not in conType or Car in conType or isAtCross:
                spawnPos = (randrange(0, self.width), randrange(0, self.height))
                conType = [type(i) for i in self.grid.get_cell_list_contents([spawnPos])]
                if Road in conType:
                    isAtCross = self.grid.get_cell_list_contents([spawnPos])[0].direction == "Omni"
            self.grid.place_agent(carAgent, spawnPos)
            self.schedule.add(carAgent)
            self.carIDs += 1

    def step(self):
        """
        Method that gets executed to update the environement and allow agents to move
        ● Parameters: 
            self: Reference to class' instance
        ● Return: None 
        """
        self.schedule.step()
        # Every lightSpan steps changes the state of the traffic light
        if self.schedule.steps % self.lightSpan == 0:
            for agents, x, y in self.grid.coord_iter():
                for agent in agents:
                    if isinstance(agent, Traffic_Light):
                        agent.state = not agent.state

        # Every carSpan steps, creates a new car, assigns it a destination and places it in 
        # any of the corners of the board
        if self.schedule.steps % self.carSpan == 0:
            carAgent = Car(self.carIDs, self, choice(self.destCoords))
            self.grid.place_agent(carAgent, (choice([0, self.width-1]), choice([0, self.height-1])))
            self.schedule.add(carAgent)
            self.carIDs += 1
