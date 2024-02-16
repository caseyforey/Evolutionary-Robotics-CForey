import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
class MOTOR:
    def __init__(self,jointName):
        self.jointName = jointName
        self.prepare_to_act()

    def prepare_to_act(self):
        self.amplitude = c.BLA
        self.frequency = c.BLF
        self.phase_offset = c.BLP
        self.values = np.linspace(-c.pi,c.pi,c.ITERATIONS)
        if str(self.jointName)[2:-1] == 'Torso_BackLeg':
            self.amplitude = c.BLA/10
        self.motor_values = self.amplitude * np.sin(self.frequency * self.values + self.phase_offset)

    def set_value(self,time,robot_id):

        pyrosim.Set_Motor_For_Joint(

        bodyIndex = robot_id,

        jointName = self.jointName,

        controlMode = p.POSITION_CONTROL,

        targetPosition = self.motor_values[time],

        maxForce = c.BACKLEGFORCE)

    def save_values(self):
        np.save(('data/' + str(self.jointName)[2:-1]),self.values)

    def __del__(self):
        self.save_values()