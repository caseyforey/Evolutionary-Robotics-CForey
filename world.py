import robot as ROBOT
import pybullet as p
import pyrosim
class WORLD:
    def __init__(self):
        # Create ground
        self.planeId = p.loadURDF("plane.urdf")
        self.ROBOT = ROBOT.ROBOT()
        p.loadSDF("world.sdf")