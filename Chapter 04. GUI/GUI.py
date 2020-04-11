import maya.cmds as cmds
#윈도우 창 생성

#1.cmds.deleteUI(win,window=True)
#먼저 하는 이유?: 이 전에 동일한 이름이 있는 윈도우를 삭제한다. 이름이 같은 윈도우는 실행되지 않으므로
if cmds.window(win,exists=True): #존재하지 않으면 위와 충돌을 하기 때문에 없을 상황에만 창을 삭제해야 한다!
    cmds.deleteUI(win,window=True)

win=cmds.window("optionWindow", title="First Window",widthHeight=(540,350))
#widthHeight 각 각 픽셀 값
#이름이 같은 윈도우는 동시에 실행되지 않는다.

cmds.showWindow(win)
