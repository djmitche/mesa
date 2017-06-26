from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.option import Option

from .portrayal import portrayPDAgent
from .model import PDModel


# Make a world that is 50x50, on a 500x500 display.
canvas_element = CanvasGrid(portrayPDAgent, 50, 50, 500, 500)

model_params = {
    "height": 50,
    "width": 50,
    "schedule_type": Option("choice", "Scheduler type", value="Random",
                             choices=list(PDModel.schedule_types.keys()))
}

server = ModularServer(PDModel, [canvas_element], "Prisoner's Dilemma",
                       model_params)
