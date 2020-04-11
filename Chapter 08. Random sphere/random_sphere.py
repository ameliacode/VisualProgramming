import maya.cmds as cmds 
import random
import math

def getDistance(pos1, pos2):
    x1,y1,z1=pos1
    x2,y2,z2=pos2
    
    distance=math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2)+math.pow(z2-z1,2))
    
    return distance
    
def makeRegDistRandSpheres(num,dist):
    
    def checkDist(new_pos):
        
        for pos in all_pos:
            
            if getDistance(new_pos,pos)<dist:
                return True
                
    all_pos=[]
    spRange=(-10,10)
    
    for count in range(num):
        
        new_pos=random.uniform(*spRange),random.uniform(*spRange),random.uniform(*spRange)
        
        if all_pos:
            
            check_count=0
            while checkDist(new_pos):
                
                new_pos=random.uniform(*spRange),random.uniform(*spRange),random.uniform(*spRange)
                check_count+=1
                
                if check_count==100:
                    return

        all_pos.append(new_pos)
        sp=cmds.sphere(radius=0.5)
        cmds.move(*list(new_pos)+sp[:1])
        
makeRegDistRandSpheres(100,1)
