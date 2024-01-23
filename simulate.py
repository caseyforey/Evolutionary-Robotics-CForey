import pybullet as p
import time as t
import pybullet_data
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
for n in range(1,1001):
    p.stepSimulation()
    t.sleep(1/60)
    print(n)


p.disconnect()
