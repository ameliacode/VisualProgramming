import maya.cmds as cmds
import math
import random

def getDistance(pos1, pos2):
    x1,y1,z1=pos1
    x2,y2,z2=pos2
    
    distance=math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2)+math.pow(z2-z1,2))
    
    return distance

for x in range(20):
    for z in range(20):
        box=cmds.polyCube(height=1,width=1,depth=1)
        cmds.move((x-9)*1.2,0,(z-9)*1.2,box[0])
        
def ripple(time_):
    for obj in cmds.ls('pCube*',type='transform'):
        #cube 위치값 뽑기
        pos=cmds.xform(obj,query=1,worldSpace=1,translation=1)
        pos[1]=0 #all y axis = 0
        #원점에서 box까지의 거리 값 추출
        sin_source=getDistance([0,0,0],pos)
        # input y axis value into sin distance
        moveY=math.sin(sin_source*0.5+time_)*2
        cmds.move(moveY,obj,moveY=1)
        
