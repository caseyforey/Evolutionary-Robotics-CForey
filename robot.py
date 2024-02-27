import motor as MOTOR
import sensor as SENSOR
import pybullet as p
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT:
    def __init__(self,file_id):
        # Create robot
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK(f"brain{file_id}.nndf")
        os.system(f"del brain{file_id}.nndf")


    def prepare_to_sense(self,links):
        self.sensors = {}
        for linkName in links: 
            self.sensors[linkName] = SENSOR.SENSOR(linkName)

    def sense(self, time):
        for sensor in self.sensors:
            self.sensors[sensor].get_value(time)

    def think(self):
        self.nn.Update()


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

    def get_fitness(self, id):
        xCoordinateOfLinkZero = p.getLinkState(self.robotId,0)[0][0]
        f = open(f"data/tmp{id}.txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.rename(f'data/tmp{id}.txt', f'data/fitness{id}.txt')

        exit()

