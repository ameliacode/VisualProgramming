import maya.cmds as cmds
import random
random.seed(1234)

for i in range(500):
    x=random.uniform(0,360)
    y=random.uniform(0,360)
    z=random.uniform(0,360)
    sp=cmds.polySphere(radius=0.5)
    cmds.rotate(x,y,z,sp[0])
    cmds.move(10,0,0,sp[0],objectSpace=1)
