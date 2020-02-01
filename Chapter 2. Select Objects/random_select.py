import maya.cmds as cmds
import random

for x in range(5):
	for z in range(5):
		cube = cmds.polyCube(h=1, w=1, d=1)
		cmds.move(x*1.5, 0.5, z*1.5, cube)


#cmds.ls(selection=True)   //위 아래 서로 같은 의미이다. True = 1, 이 때 리스트 마지막 객체가  select
#cmds.ls(sl=1)

#cmds.select(all=True)      //위 아래 서로 같은 의미이다. (아래만)이 때 모두 선택할 때 동등한 입장에서 선택이 된다.
#cmds.select('*')          //좀 더 쉼게 말하면 폴리곤 다수 선택시 가장 마지막에 선택했다고 표시되는 녹색 부분이 없다.

#cmds.select(u'pCube5')    //여기서 u는 unicode를 의미한다.
#cmds.select(u'pCube4', u'pCube5')    //select는 여러 폴리곤을 선택할 수 있다.

#cmds.select(all=True)                //모든 폴리곤 선택      
#mysel = cmds.ls(selection=True)      //선택된 폴리곤 리스트에 저장
mysel = cmds.ls(u'pCube*')            #//pCube와 관련된 폴리곤 리스트에 저장

#cmds.select(mysel[0])                //리스트 첫 폴리곤 선택
#cmds.select(mysel[0:10])             //리스트 첫 번째 폴리곤부터 11번째 폴리곤까지 선택

#mysel.index('pCube4')                 //반환값은 정수형이며 3이다
#cmds.select(mysel[3])
#mysel[3]
#mysel.remove('pCube25')               //mysel리스트에서 pCube25제거 

#setA = set(cmds.ls(sl=1))
#setB = set(cmds.ls(sl=1))

#cmds.select(list(setA))
#cmds.select(list(setB))

#cmds.select(list(setA | setB)) # | -> Or
#cmds.select(list(setA & setB)) # & -> And
#cmds.select(list(setA - setB))
#cmds.select(list(setA ^ setB))

random.shuffle(mysel)                            #//무작위로 객체 shuffle
#cmds.select(mysel[:5])
#cmds.select(mysel[:random.randint(5,15)])        //randint(최소,최대) 범위
cmds.select(mysel[:random.randint(5,16)])
