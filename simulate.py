import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
# Connect to client
physicsClient = p.connect(p.GUI)
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

# Create list for back leg data
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

# Basic Engine loop
for n in range(1000):
    p.stepSimulation()
    backLegSensorValues[n] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[n] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    
    # Back leg motor
    pyrosim.Set_Motor_For_Joint(

    bodyIndex = robotId,

    jointName = b"Torso_BackLeg",

    controlMode = p.POSITION_CONTROL,

    targetPosition = -np.pi/4,

    maxForce = 500)


    # Front leg motor
    pyrosim.Set_Motor_For_Joint(

    bodyIndex = robotId,

    jointName = b"Torso_FrontLeg",

    controlMode = p.POSITION_CONTROL,

    targetPosition = np.pi/4,

    maxForce = 500)




    t.sleep(1/60)

np.save('data/backleg',backLegSensorValues)
np.save('data/frontleg',frontLegSensorValues)
p.disconnect()