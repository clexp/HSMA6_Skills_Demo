import mesa

from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

import random

class HSMA_Agent(Agent):
  def __init__(self, unique_id, model, initial_love_prob, persuasiveness_max):
    super().__init__(unique_id, model)
    if random.uniform(0,1) < initial_love_prob:
      self.love_hsma = True
    else: 
      self.love_hsma = False
    self.persuasiveness = random.uniform(0.0, persuasiveness_max)

  def move(self):
    possible_steps = self.model.grid.get_neighborhood(
      self.pos, moore = True, include_center = False
    )
    new_position = random.choice(possible_steps)
    self.model.grid.move_agent(self, new_position)
  
  def talk(self):
    cellmates = self.model.grid.get_cell_list_contents([self.pos])
    if len(cellmates) >1:
      for inhabitant in cellmates:
        if inhabitant.love_hsma != self.love_hsma:
          if random.uniform(0,1) < self.persuasiveness:
            inhabitant.love_hsma = self.love_hsma
  
  def step(self):
    if random.choice([True, False]) == True:
      self.move()
    self.talk()

class Persuasion_Model():
  def __init__(self, N, width, height, initial_love_prob, persuasiveness_max,
                 move_probability):
    self.running = True
    self.num_agents = N
    self.grind = MultiGrid(width,height, True)
    self.schedule = RandomActivation(self)
    for i in range(self.num_agents):
      a = HSMA_Agent(i, self, initial_love_prob, persuasiveness_max, move_probability)
      self.schedule.add(a)
      try:
        start_cell = self.grid.find_empty()
        self.grid.place_agent(a, start_cell)
      except:
        x = random.randrange(self.grid.width)
        y = random.randrange(self.grid.height)
        self.grid.place_agent(a, (x, y))
    self.datacollector = DataCollector(model_reporters={"Total Loving HSMA":calculate_number_loving_hsma, "Total Hating HSMA":calculate_number_hating_hsma}, agent_reporters={})

  def step(self):
    self.datatcollector.collect(self)
    self.schedule.step()

def calculate_number_loving_hsma(model):
  total_loving_hsma = 0
  for agent in model.schedule.agents:
    if agent.love_hsma == True:
      total_loving_hsma += 1
  return total_loving_hsma

def calculate_number_hating_hsma(model):
  total_hating_hsma = 0
  for agent in model.schedule.agents:
    if agent.love_hsma == False:
      total_hating_hsma +=1
  return total_hating_hsma