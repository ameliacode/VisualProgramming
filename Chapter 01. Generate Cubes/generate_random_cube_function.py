import maya.cmds as cmds
import random

def generate_box(box_num, height_val =10):
    for x in range(100):
        rand_height=random.uniform(0,10)//uniform은 범위
        cube=cmds.polyCube(height=rand_height) 
        cmds.move(x,rand_height/2,0,cube[0])

//generate_box 함수 생성하고 custom shelf에 저장+script저장 
//이 때 저장할 때 example01로 저장한다.
//파일 내 스크립트를 확인할 수 있다.

import example01 as ex01
reload(ex01) #수정된 코드 업데이트 
ex01.generate_box(10,10)
