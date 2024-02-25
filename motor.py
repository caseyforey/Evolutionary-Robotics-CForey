import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
class MOTOR:
    def __init__(self,jointName):
        self.jointName = jointName

    def set_value(self,desiredAngle,robot_id):

        pyrosim.Set_Motor_For_Joint(

        bodyIndex = robot_id,

        jointName = self.jointName,

        controlMode = p.POSITION_CONTROL,

        targetPosition = desiredAngle,

        maxForce = c.BACKLEGFORCE)