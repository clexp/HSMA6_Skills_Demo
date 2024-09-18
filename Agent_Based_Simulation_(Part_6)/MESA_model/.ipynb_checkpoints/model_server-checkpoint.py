from model_1 import Persuasion_Model
from mesa.visualization.modules import CanvasGrid
from mesa.experimental import JupyterViz

def agent_portrayal(agent):
  size = agent.persuasivenes * 100
  alpha = abs(agent.love_score)
  color = "tab:grey"
  if agent.love_score > 0:
    color = "tab:pink"
  return {"size":size, "color":color}

grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)

model_params = {
  "N":{
    "type":"SliderInt",
    "value":20,
    "label":"Number of HSMAs",
    "min":2,
    "max":100,
    "step": 1
  },
  "initial_love_prob":{
    "type":"SliderFloat",
    "value":0.5,
    "label":"Probability low HSMA at start",
    "min":0.0,
    "max":1.0,
    "step":0.01
  },
  "Persuasiveness_max":{
    "type":"SliderFloat",
    "value":0.5,
    "label":"Maximum persuasiveness",
    "min":0.0,
    "max":1.0,
    "step":0.01
  },
  "Move Probability":{
    "type":"SliderFloat",
    "value":0.5,
    "label":"Probability of Movement",
    "min":0.0,
    "max":1.0,
    "step":0.01
  },
  "width":10,
  "height":10
}

page = JupyterViz(
  Persuasion_Model,
  model_params,
  measures=["Total Loving HSMA", "Total Hating HSMA"],
  agent_portrayal=agent_portrayal
)

page
