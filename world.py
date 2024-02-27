import robot as ROBOT
import pybullet as p
import pyrosim
class WORLD:
    def __init__(self,brain_id):
        # Create ground
        self.planeId = p.loadURDF("plane.urdf")
        self.ROBOT = ROBOT.ROBOT(brain_id)
        p.loadSDF("world.sdf")