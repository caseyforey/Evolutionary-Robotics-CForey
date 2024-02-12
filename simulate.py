import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random as rand
# Connect to client
physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Set gravity
p.setGravity(0,0,-9.8)

# Create ground
planeId = p.loadURDF("plane.urdf")

# Create robot
robotId = p.loadURDF("body.urdf")

# Load world
p.loadSDF("world.sdf")

# Simulate the robot
pyrosim.Prepare_To_Simulate(robotId)
ITERATIONS = 1000
# Create list for back leg data
backLegSensorValues = np.zeros(ITERATIONS)
frontLegSensorValues = np.zeros(ITERATIONS)

# Array of range 0 to 1000
pi = np.pi
# Create 1000 values from -pi to pi 
vals = np.linspace(-pi,pi,ITERATIONS) 

# Back Leg 

# back leg specific vars
backLegAmplitude = pi/4
backLegFrequency = 15
backLegPhaseOffset = 0
# Sin scaled to pi/4
backLegTargetAngles = backLegAmplitude * np.sin(backLegFrequency * vals + backLegPhaseOffset)


# Front Leg

# front leg specific vars
frontLegAmplitude = pi/4
frontLegFrequency = 8
frontLegPhaseOffset = pi
# Sin scaled to pi/4
frontLegTargetAngles = frontLegAmplitude * np.sin(frontLegFrequency * vals + frontLegPhaseOffset)


# Basic Engine loop
for n in range(ITERATIONS):
    p.stepSimulation()
    backLegSensorValues[n] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[n] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # Back leg motor
    pyrosim.Set_Motor_For_Joint(

    bodyIndex = robotId,

    jointName = b"Torso_BackLeg",

    controlMode = p.POSITION_CONTROL,

    targetPosition = backLegTargetAngles[n],

    maxForce = 20)

    # Front leg motor
    pyrosim.Set_Motor_For_Joint(

    bodyIndex = robotId,

    jointName = b"Torso_FrontLeg",

    controlMode = p.POSITION_CONTROL,

    targetPosition =  frontLegTargetAngles[n],

    maxForce = 20)




    t.sleep(1/60)

np.save('data/backlegAngles',backLegTargetAngles)
np.save('data/frontlegAngles',frontLegTargetAngles)
np.save('data/backleg',backLegSensorValues)
np.save('data/frontleg',frontLegSensorValues)
p.disconnect()