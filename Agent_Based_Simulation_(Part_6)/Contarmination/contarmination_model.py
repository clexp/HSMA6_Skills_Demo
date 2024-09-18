import mesa

from mesa import Agent, Model
from mesa.time import RandomActivation # random order of agent actions
from mesa.space import MultiGrid # multiple agents per cell
from mesa.datacollection import DataCollector

import random
import numpy

# class representing individuals
class HSMA_Agent(Agent):
    # Constructor
    def __init__(self, unique_id, model, initial_infection_prob, move_probability,
                immunised_percentage, infection_days, stay_at_home):
        # Call the constructor from the parent Agent class, which will do all
        # the hard work of defining what an agent is - we just give it an ID
        # and a model that it will live in
        super().__init__(unique_id, model)

        # Determine if the agent should begin by being infected 
        if random.uniform(0, 1) < initial_infection_prob:
            self.infected = True
        else:
            self.infected = False

        if self.infected == True:
            self.infected_hours = infection_days * 24
        else:
            self.infected_hours = 0

        if (random.uniform(0, 1) < immunised_percentage) and (self.infected == False):
            self.immunity_status = True
        else:
            self.immunity_status = False

        self.move_probability = move_probability
        self.infection_days = infection_days
        self.stay_at_home = stay_at_home
        
    # Agent movement method - this is called if it is determined the agent
    # is going to move on this time step
    def move(self):
        # Get a list of possible neighbouring cells to which to move
        # We use the get_neighborhood function, giving it the agent's current
        # position on the grid, stating we want a Moore neighbourhood (which
        # includes diagonals), and that we don't want to include the centre
        # (where the agent is currently) in the returned neighbourhood list
        possible_steps = self.model.grid.get_neighborhood(
                self.pos, moore=True, include_center=False)
            
        # Select new position at random
        new_position = random.choice(possible_steps)
          
        # Move the agent to the randomly selected new position
        # Only move based on probability
        if random.uniform(0, 1) < self.move_probability:
            self.model.grid.move_agent(self, new_position)


    # Method to talk to other HSMAs (if there are any around) and potentially 
    # influence the opinion of other agents if there are other agents in the 
    # same cell
    def talk(self):
        # Get list of agents in this cell.  We use the get_cell_list_contents
        # function of the grid object and pass it our current position
        cellmates = self.model.grid.get_cell_list_contents([self.pos])

        # Check if there are other agents here - if the list of cellmates is
        # greater than 1 then there must be more here than this agent
        if len(cellmates) > 1:
            # for each agent in the cell
            for inhabitant in cellmates:
                # check if the agent has a different opinion to our agent
                # note - one of the inhabitants will be THIS agent, but that's
                # ok, because they will obviously have the same opinion as
                # themselves, and so the rest of the code won't action
                # if feeling is not also neg/pos
                if inhabitant.infected == False and self.infected == True:
                    # Randomly determine whether this agent will influence the
                    # other agent's opinion, and change it to match theirs,
                    # based on this agent's persuasiveness
                    if inhabitant.immunity_status == False:
                        # Change the other agent's opinion to match this agent's
                        # inhabitant.love_hsma = self.love_hsma
                        inhabitant.infected = True
                        inhabitant.infected_hours = self.infection_days * 24


    # Step method - this defines which of the agent's actions will be taken
    # on a time step, and in which order
    def step(self):

        #stay at home if infected?!
        if self.infected == False:
            self.move()
        elif self.infected == True and self.stay_at_home == 0:
            self.move()

        # Regardless of whether or not the agent moved, it should begin its
        # talking behaviour for this time step
        self.talk()

        if self.infected == True:
            self.infected_hours -= 1

        if self.infected_hours == 0 and self.infected == True:
            self.infected = False
            self.immunity_status = True


# Class representing our ABS model
class Persuasion_Model(Model):
    # 2D Model initialisation constructor - initialise with N agents, and 
    # specified width and height.  Also pass in the things we need to pass
    # to our agents when instantiating them.
    def __init__(self, N, width, height, initial_infection_prob, move_probability,
                immunised_percentage, infection_days, stay_at_home):
        self.running = True # this code is required for BatchRunner
        self.num_agents = N

        # Set up a Toroidal multi-grid (Toroidal = if the agent is in a cell
        # on the border of the grid, and moves towards the border, they'll
        # come out the other side.  Think PacMan :) The True Boolean passed in
        # switches that on.  Multi-Grid just means we can have more than one 
        # agent per cell)
        self.grid = MultiGrid(width, height, True)

        # Set up a scheduler with random order of agents being activated 
        # each turn.  A random activation is probably the best in most cases,
        # unless you have information that certain agents will act before
        # certain other agents
        self.schedule = RandomActivation(self)

        # Create HSMA agents up to the number specified
        for i in range(self.num_agents):
            # Create agent with ID taken from for loop - we pass in the i
            # value as the unique_id, self (the model here) as the model, and 
            # then the various parameter values we specified
            a = HSMA_Agent(i, self, initial_infection_prob, move_probability,
                immunised_percentage, infection_days, stay_at_home)
            
            # Add the agent to the scheduler
            self.schedule.add(a)

            # Try adding the agent to a random empty cell
            try:
                start_cell = self.grid.find_empty()
                self.grid.place_agent(a, start_cell)
            # If you can't find an empty cell, just pick any cell at random
            except:
                x = random.randrange(self.grid.width)
                y = random.randrange(self.grid.height)
                self.grid.place_agent(a, (x,y))

        # We set up a DataCollector that can collect agent-specific and
        # model-wide data.  Here, we tell it to collect data on the total number
        # of agents loving and hating HSMA, which it calculates by calling the
        # functions we name here (we write them further down).
        # We don't use any agent reporters here, but we could if we wanted to
        # track an attribute of agents over time
        self.datacollector = DataCollector(
            model_reporters={"Total Infected":calculate_infected,
                             "Total Healthy":calculate_healthy},
            agent_reporters={}
        )

    # Function to advance the model by one step (we just tell the scheduler to
    # step forward one time step)
    def step(self):
        # Tell the data collector to collect the data for this time step
        self.datacollector.collect(self)
        
        # Ask scheduler to step forward one time step
        self.schedule.step()

# Function used by the data collector to calculate the total number of agents
# who love HSMA.  This will run at each time step.
def calculate_infected(model):
    total_infected = 0

    for agent in model.schedule.agents:
        if agent.infected == True:
            total_infected += 1

    return total_infected

# Function used by the data collector to calculate the total number of agents
# who hate HSMA.  This will run at each time step.
def calculate_healthy(model):
    total_healthy = 0

    for agent in model.schedule.agents:
        if agent.infected == False:
            total_healthy += 1

    return total_healthy

