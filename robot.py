import motor as MOTOR
import sensor as SENSOR
import pybullet as p

class ROBOT:
    def __init__(self):
        # Create robot
        self.robotId = p.loadURDF("body.urdf")

    def prepare_to_sense(self,links):
        self.sensors = {}
        for linkName in links: 
            self.sensors[linkName] = SENSOR.SENSOR(linkName)

    def sense(self, time):
        for sensor in self.sensors:
            self.sensors[sensor].get_value(time)
    
    def prepare_to_act(self,joints):
        self.motors = {}
        for jointName in joints:
            self.motors[jointName] = MOTOR.MOTOR(jointName)
    def act(self,time):
        for motor in self.motors:
            self.motors[motor].set_value(time,self.robotId)

