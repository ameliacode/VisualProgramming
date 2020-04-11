#-*- coding: utf-8 -*-

import maya.cmds as cmds
from optwin import SJ_OptionsWindow

class SJ_PolyOptionsWindow(SJ_OptionsWindow):
    """A class for a simple window to create polygon primitives"""
    def __init__(self):
        """Initialize base class and override data attributes"""
        SJ_OptionsWindow.__init__(self)
        # overridden from base class
        self.title = 'Polygon Creation Options'
        # overridden from base class
        self.actionName = 'Create and Close'

    def displayOptions(self):
        """Overridden from base class"""
        # primitive type selector
        self.objType = cmds.radioButtonGrp(
            label='Object Type: ',
            labelArray4=[
                'Cube',
                'Cone',
                'Cylinder',
                'Sphere'
            ],
            numberOfRadioButtons=4,
            select=1,
        )
        # a group of transform controls
        self.xformGrp = cmds.frameLayout(
            label='Transformations',
            collapsable=True,
        )
        cmds.formLayout(
            self.optionsForm, e=True,
            attachControl=(
                [self.xformGrp,'top',2,self.objType]
            ),
            attachForm=(
                [self.xformGrp,'left',0],
                [self.xformGrp,'right',0]
            )
        )
        self.xformCol = cmds.columnLayout()
        self.position = cmds.floatFieldGrp(
            label='Position: ',
            numberOfFields=3
        )
        self.rotation = cmds.floatFieldGrp(
            label='Rotation (XYZ): ',
            numberOfFields=3
        )
        self.scale = cmds.floatFieldGrp(
            label='Scale: ',
            numberOfFields=3,
            value=[1.0,1.0,1.0,1.0]
        )
        cmds.setParent('..')
        cmds.setParent('..')
        # a vertex color picker
        self.color = cmds.colorSliderGrp(
            label='Vertex Colors: '
        )
        cmds.formLayout(
            self.optionsForm, e=True,
            attachControl=(
                [self.color,'top',0,self.xformGrp]
            ),
            attachForm=(
                [self.color,'left',0],
            )
        )

    def applyBtnCmd(self, *args):
        """Overridden from base class"""
        # determine the type of object to create
        self.objIndAsCmd = {
            1:cmds.polyCube,
            2:cmds.polyCone,
            3:cmds.polyCylinder,
            4:cmds.polySphere
        }
        objIndex = cmds.radioButtonGrp(
            self.objType, q=True,
            select=True
        )
        # create the new object
        newObject = self.objIndAsCmd[objIndex]()
        # transform the new object
        pos = cmds.floatFieldGrp(
            self.position, q=True,
            value=True
        )
        rot = cmds.floatFieldGrp(
            self.rotation, q=True,
            value=True
        )
        scale = cmds.floatFieldGrp(
            self.scale, q=True,
            value=True
        )
        cmds.xform(newObject[0], t=pos, ro=rot, s=scale)
        # apply vertex colors to the new object
        col = cmds.colorSliderGrp(
            self.color, q=True,
            rgbValue=True
        )
        cmds.polyColorPerVertex(
            newObject[0],
            colorRGB=col,
            colorDisplayOption=True
        )

if __name__ == "__main__":
    SJ_PolyOptionsWindow.showUI()
