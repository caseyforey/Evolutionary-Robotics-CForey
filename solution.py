import numpy as np
import pyrosim.pyrosim as pyrosim
import random as rand
import os
class SOLUTION():
    def __init__(self) :
        self.weights = (np.random.rand(3,2) * 2) -1

    def evaluate(self, mode):
        self.create_world()
        self.create_body()
        self.create_brain()
        os.system(f"python3 simulate.py {mode}")
        f = open("data/fitness.txt", "r")
        self.fitness = float(f.read())
        f.close()

    def mutate(self):
        row = rand.randint(0,2)
        col = rand.randint(0,1)
        self.weights[row,col] =  (rand.random() * 2) - 1
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

        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[1,1,1])

        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])

        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0.0,-0.5], size = (1,1,1))

        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])

        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0.0,-0.5], size = (1,1,1))

        pyrosim.End()


    def create_brain(self):

        pyrosim.Start_NeuralNetwork("brain.nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")

        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")

        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

        pyrosim.Send_Motor_Neuron( name = 3 , jointName = 'Torso_BackLeg')

        pyrosim.Send_Motor_Neuron( name = 4 , jointName = 'Torso_FrontLeg')
        
        for row in range(3):
            for col in range(2):
                pyrosim.Send_Synapse( sourceNeuronName = row , targetNeuronName = col + 3 , weight = self.weights[row][col])

        pyrosim.End()