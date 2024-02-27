import numpy as np
import pyrosim.pyrosim as pyrosim
import random as rand
import os
import time
import constants as c
class SOLUTION():
    def __init__(self, id) :
        self.weights = (np.random.rand(c.NUMSENSENEURON,c.NUMMOTORNEURON) * 2) -1
        self.myID = id
    
    def start_simulation(self, mode):
        self.create_world()
        self.create_body()
        self.create_brain()
        os.system(f"start /B python3 simulate.py {mode} {self.myID}")

    def wait_for_simulation(self):
        while not os.path.exists(f"fitness{self.myID}.txt"):
            time.sleep(0.01)
        f = open(f"fitness{self.myID}.txt", "r")
        self.fitness = float(f.read())
        f.close()
        os.system(f'del fitness{self.myID}.txt')


    def mutate(self):
        row = rand.randint(0,(c.NUMSENSENEURON-1))
        col = rand.randint(0,(c.NUMMOTORNEURON-1))
        self.weights[row,col] =  (rand.random() * 2) - 1

    def set_id(self, id):
        self.myID = id



### CREATE METHODS ###
    def create_world(self):
        pyrosim.Start_SDF("world.sdf")

        length = 1
        width = 1
        height = 1
        x = -3
        y = 3
        z = 0.5

        pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

        pyrosim.End()

    def create_body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[1,1,1])

        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,1],jointAxis = "1 0 0")

        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0], size = (0.2,1,0.2))

        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")

        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0], size = (0.2,1,0.2))

        pyrosim.Send_Joint(name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0], size = (1,0.2,0.2))

        pyrosim.Send_Joint(name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0], size = (1,0.2,0.2))

        pyrosim.Send_Joint(name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")

        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-0.5], size = (0.2,0.2,1))

        pyrosim.Send_Joint(name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")

        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-0.5], size = (0.2,0.2,1))

        pyrosim.Send_Joint(name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0,0,-0.5], size = (0.2,0.2,1))

        pyrosim.Send_Joint(name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")

        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0,0,-0.5], size = (0.2,0.2,1))

        pyrosim.End()


    def create_brain(self):

        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "BackLowerLeg")

        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "FrontLowerLeg")

        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LeftLowerLeg")

        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "RightLowerLeg")

        pyrosim.Send_Motor_Neuron( name = 4 , jointName = 'Torso_BackLeg')

        pyrosim.Send_Motor_Neuron( name = 5 , jointName = 'Torso_FrontLeg')

        pyrosim.Send_Motor_Neuron( name = 6 , jointName = 'Torso_LeftLeg')

        pyrosim.Send_Motor_Neuron( name = 7 , jointName = 'Torso_RightLeg')

        pyrosim.Send_Motor_Neuron( name = 8 , jointName = 'BackLeg_BackLowerLeg')

        pyrosim.Send_Motor_Neuron( name = 9 , jointName = 'FrontLeg_FrontLowerLeg')

        pyrosim.Send_Motor_Neuron( name = 10 , jointName = 'RightLeg_RightLowerLeg')

        pyrosim.Send_Motor_Neuron( name = 11 , jointName = 'LeftLeg_LeftLowerLeg')

        
        for row in range(c.NUMSENSENEURON):
            for col in range(c.NUMMOTORNEURON):
                pyrosim.Send_Synapse( sourceNeuronName = row , targetNeuronName = col + c.NUMSENSENEURON , weight = self.weights[row][col])

        pyrosim.End()
