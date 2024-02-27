
import pybullet as p
import time as t
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
from simulation import SIMULATION
import sys

direct_or_gui = sys.argv[1]
simulation = SIMULATION(direct_or_gui)
simulation.run()
simulation.get_fitness()
