#-*- coding: utf-8 -*-

import maya.cmds as cmds
import math
from optwin import SJ_OptionsWindow 

class SJ_StairMaster(SJ_OptionsWindow):
    def __init__(self):
        SJ_OptionsWindow.__init__(self)
        self.title = 'Stair Master'
        self.actionName = 'Create and Close'

    def displayOptions(self):    
        self.xformCol = cmds.columnLayout()
        self.stepH = cmds.floatSliderGrp(
            label='Step H',field=True
        )
        self.stepD = cmds.floatSliderGrp(
            label='Step D',field=True
        )
        self.stepW = cmds.floatSliderGrp(
            label='Step W',field=True
        )
        self.noStep = cmds.intSliderGrp(
            label='No Steps',field=True
        )
        self.railH = cmds.floatSliderGrp(
            label='Rail H', field=True
        ) 
       

    def applyBtnCmd(self, *args):
        stepH = cmds.floatSliderGrp(
            self.stepH, q=True,
            value=True
        )
        stepW = cmds.floatSliderGrp(
            self.stepW, q=True,
            value=True
        )
        stepD = cmds.floatSliderGrp(
            self.stepD, q=True,
            value=True
        )
        numSteps = cmds.intSliderGrp(
            self.noStep, q=True,
            value=True
        )
        railH = cmds.floatSliderGrp(
            self.railH, q=True,
            value=True
        )
    
        totH = stepH*numSteps
        totD = stepD*numSteps
        railAngle = math.atan(totD/totH)
        rad2deg = railAngle*180/math.pi 
        railLen = math.sqrt(totH*totH+totD*totD)
        
        for i in range(0,numSteps):
            cmds.polyCube(h=stepH, w=stepW, d=stepD)
            cmds.move(0,stepH*i,stepD*i)
            
            if railH>0:
                cmds.polyCylinder(r=0.5,h=railH)
                cmds.move(stepW/2,stepH*i+0.5*railH,stepD*i)      
           
        if railH > 0:
            cmds.polyCylinder(r = 0.5,h = railLen)
            cmds.rotate(rad2deg,0,0)
            cmds.move(stepW/2,totH/2+railH-0.5*stepH,totD/2-0.5*stepD)
            
if __name__ == "__main__":
    SJ_StairMaster.showUI()
