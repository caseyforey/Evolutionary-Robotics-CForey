import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim
class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.ITERATIONS)

    def get_value(self,time):
        self.values[time] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def save_values(self):
        np.save(('data/' + str(self.linkName)),self.values)

    def __del__(self):
        self.save_values()