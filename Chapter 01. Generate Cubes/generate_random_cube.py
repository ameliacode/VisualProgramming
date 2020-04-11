############################################
#예제 1 - 100개의 임의의 높이를 갖는 cube 만들기
############################################

import maya.cmds as cmds
import random
#box 100개를 생산하기

for x in range(100):
    //random.uniform(a,b): a<=n<=b의 실수값 n을 반환
    rand_height=random.uniform(0,10)
    //polyCube() 함수는 polygonal cube를 생산하는 함수
    //polyCube() 함수는 객체 이름과 node 이름으로 구성된 
    cube=cmds.polyCube(height=rand_height) 
    //cube 리스트로 저장이 된다
    //print(cube)
    //move(x,y,z,object,...) 함수는 객체를 좌표에 따라서 이동
    //cube의 높이를 반씩 이동하여 높이를 바닥에 맞춤
    cmds.move(x,rand_height/2,0,cube[0])
