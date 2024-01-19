import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5
# TODO finish step 33 from many links
i = -1
j = -1
for i in range(5):
    for j in range(5):
        k = 0
        length = 1
        width = 1
        height = 1
        for k in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x+i,y+j,z+k] , size=[length,width,height])
            length = length * 0.9
            width = height * 0.9
            height = height * 0.9

pyrosim.End()