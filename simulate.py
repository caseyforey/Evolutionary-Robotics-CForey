import pybullet as p
import time as t
physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
for n in range(1,1001):
    p.stepSimulation()
    print(n)
    t.sleep(1/60)


p.disconnect()
