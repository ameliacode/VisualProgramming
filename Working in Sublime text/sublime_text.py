#-*-coding:utf-8 -*- #:다른 언어를 표현하고자 할 때 utf를 사용한다.
#remote.py로 저장

import maya.cmds as cmds

try:
	cmds.commandPort(name=":7001",close=True)

#7001을 닫아라

except:
	cmds.warning('not opened yet...')

try:
	cmds.commandPort(name=":7002",close=True)

except:
	cmds.warning('not opened yet...')
	
cmds.commandPort(name=":7001",sourceType="mel")
cmds.commandPort(name=":7002",sourceType="python")
