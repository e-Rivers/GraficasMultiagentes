from mesa import Agent

class Car(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True, # Boolean for whether to use Moore neighborhood (including diagonals) or Von Neumann (only up/down/left/right).
            include_center=True) 
        
        # Checks which grid cells are empty
        freeSpaces = list(map(self.model.grid.is_cell_empty, possible_steps))

        next_moves = [p for p,f in zip(possible_steps, freeSpaces) if f == True]
       
        next_move = self.random.choice(next_moves)
        # Now move:
        if self.random.random() < 0.1:
            self.model.grid.move_agent(self, next_move)
            self.steps_taken+=1

        # If the cell is empty, moves the agent to that cell; otherwise, it stays at the same position
        # if freeSpaces[self.direction]:
        #     self.model.grid.move_agent(self, possible_steps[self.direction])
        #     print(f"Se mueve de {self.pos} a {possible_steps[self.direction]}; direction {self.direction}")
        # else:
        #     print(f"No se puede mover de {self.pos} en esa direccion.")

    def step(self):
        # self.direction = self.random.randint(0,8)
        # print(f"Agente: {self.unique_id} movimiento {self.direction}")
        # self.move()
        pass

class Pedestrian(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
    
    def step(self):
        pass

class StopSign(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

class Building(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

class Road(Agent):
    def __init__(self, unique_id, model, direction, isZebra):
        super().__init__(unique_id, model)
        self.direction = direction
        self.zebraCross = isZebra

class Sidewalk(Agent):
    def __init__(self, unique_id, model, orientation):
        super().__init__(unique_id, model)
        self.orientation = orientation
