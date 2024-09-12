from model_1 import Persuasion_Model
from mesa.visualization.modules import CanvasGrid
from mesa.experimental import JupyterViz

def agent_portrayal(agent):
  size = 60
  color = "tab:grey"
  if agent.love_hsma == True:
    color = "tab:red"
  return {"size":size, "color":color}