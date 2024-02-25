import motor as MOTOR
import sensor as SENSOR
import pybullet as p
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    def __init__(self):
        # Create robot
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")

    def prepare_to_sense(self,links):
        self.sensors = {}
        for linkName in links: 
            self.sensors[linkName] = SENSOR.SENSOR(linkName)

    def sense(self, time):
        for sensor in self.sensors:
            self.sensors[sensor].get_value(time)
    
    # TODO: Module 7 part 18
    def think(self):
        self.nn.Update()
        self.nn.Print()


    def prepare_to_act(self,joints):
        self.motors = {}
        for jointName in joints:
            self.motors[str(jointName)[2:-1]] = MOTOR.MOTOR(jointName)

    def act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].set_value(desiredAngle,self.robotId)

