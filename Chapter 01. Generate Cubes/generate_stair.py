import maya.cmds as cmds
import random

for i in range(5):
    cube=cmds.polyCube(height=2,width=3,depth=4) #polyCube 생성
    cmds.move(2*i,2*i,0,cube[0]) #cube이동 
