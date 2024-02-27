import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import world as WORLD
import constants as c
import time as t
class SIMULATION:

    def __init__(self, mode):
        # Connect to client in requested mode
        self.mode = mode
        if self.mode == 'GUI':
            self.physicsClient = p.connect(p.GUI)
        else:
            self.physicsClient = p.connect(p.DIRECT)
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.world = WORLD.WORLD()
        # Set gravity
        p.setGravity(0,0,c.GRAVITY_ACCELERATION)
        # Simulate the robot
        pyrosim.Prepare_To_Simulate(self.world.ROBOT.robotId)
        self.world.ROBOT.prepare_to_sense(pyrosim.linkNamesToIndices)
        self.world.ROBOT.prepare_to_act(pyrosim.jointNamesToIndices)        

    def run(self):
        for n in range(c.ITERATIONS):
            p.stepSimulation()
            self.world.ROBOT.sense(n)
            self.world.ROBOT.think()
            self.world.ROBOT.act()
            if self.mode == 'GUI':
                t.sleep(1/10000)
    


    def get_fitness(self):
        self.world.ROBOT.get_fitness()
    
    def __del__(self):
        p.disconnect()