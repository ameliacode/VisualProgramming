# coding: utf-8

import maya.cmds as cmds
import random
import math

# 거리를 계산하는 함수
def getDistance(pos1, pos2):
    '''
    pos1 = (x1, y1, z1)
    pos2 = (x2, y2, z2)
    '''
    # pos 을 x, y, z 형식으로 분해
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    # 거리 공식을 적용해서 거리 값을 계산
    distance = math.sqrt(math.pow(x2-x1, 2)
                         + math.pow(y2-y1, 2)
                         + math.pow(z2-z1, 2))
    # 거리 값을 return
    return distance

# GUI 만들기 function
def sp_com():
    # 전역 변수 지정
    global sp, sel, rad, selVtx
    
    # 기본값 설정
    sp = None
    sel = None
    rad = 1
    selVtx = None
    
    # 영역 Sphere controller 만들기
    def makeSphere(evt):
        # 전역 변수 sp 설정
        global sp
        # sphere 만들기
        
        sp = cmds.sphere(ax=[0, 1, 0], radius=rad)
        # sphere 컨트롤 slider 전부 활성화
        cmds.floatSliderGrp('my_radius', e=1, en=True )
        cmds.intSliderGrp('my_count', e=1, en=True )
        cmds.button('my_select', e=1, en=True )
            
    # sphere 의 radius 조정
    def selVtx(evt):
        global rad
        # slider 에서 radius 값 호출
        rad = cmds.floatSliderGrp('my_radius',
                                  q=1, v=1)
        # radius 값 지정
        cmds.setAttr('%s.radius' % sp[1], rad)
        # vertex 선택하기
        selList = []
        global allVtxList
        
        # 선택된 mesh 의 모든 vertex 좌표 추출
        all_vtx = cmds.xform('%s.vtx[*]' % sel[0],
                             q=1, t=1, ws=1)
        # 모든 vtx 정보 (x, y, z) 형식으로 제정렬
        allVtxList = zip(*[all_vtx[x::3]
                           for x in range(3)])
        # sphere 의 위치를 추출
        sp_pos = cmds.xform(sp[0], q=1, t=1, ws=1)
        # select 된 mesh 의 vtx 의 자표 거리안에 있는지
        for c, pos in enumerate(allVtxList):
            # 거리를 검사
            if rad > getDistance(sp_pos, pos):
                # rdius 안에 있으면 수집
                selList.append(c)
        # 수집된 좌표가 있는지 검사
        if selList:
            # random 하게 섞음
            random.shuffle(selList)
            # 선택할 vtx 의 갯수의 값을 추출
            count = cmds.intSliderGrp('my_count',
                                      q=1, v=1)
            # 원하는 갯수와 선택된 갯수 비교
            if len(selList) < count:
                # 적으면, 선택 갯수로 지정
                count = len(selList)
            # 전역 변수 지정
            global selVtx
            # 선택된 vtx 자표 목록
            selVtx = selList[:count]
            # 선택된 vtx 목록 select 해서 보여주기
            cmds.select(['%s.vtx[%s]' % (sel[0], x)
                         for x in selVtx])
        # bouble 버튼 활성화 하기
        cmds.button('my_bouble', e=1, en=True)


    # random vtx 선택하기 function
    def make_bouble_vtx(evt):
        # select 한 vertex 목록 looping
        for vn in selVtx:
            # 좌표 추출
            pos = allVtxList[vn]
            # radius random 지정 하기
            radius = random.uniform(0.2, 1)
            # # 버블 만들기 function
            blo = cmds.sphere(radius=radius)
            # 지정된 위치로 이동
            cmds.move(*list(pos)+blo[:1])
        # bouble 만들고 contrl sphere 지우기
        cmds.delete(sp[0])
    # select 된 object 학인하기 function
    def new_sel(evt):
        global sel
        sel = cmds.ls(sl=1)
        # 선택한 obj 가 mesh 인지 검사
        if sel and cmds.nodeType(cmds.listRelatives( sel[0], shapes=1)[0]) == 'mesh':
            # sphere 만들기 활성화
            cmds.button('make_sp', e=1, en=True)
            # select 된 obj 이름 표시
            cmds.text('sel_obj', e=1, label='Selected : %s' % sel[0])
        else:
            # sphere 만들기 비 활성화
            cmds.button('make_sp', e=1, en=False)
            # obj 지정 안됨 표시
            cmds.text('sel_obj', e=1, label='Undefind')
            # sphere 의 radius slider 비 활성화
            cmds.floatSliderGrp('my_radius', e=1, en=False)
            # select vtx 갯수 slider 비 활성화
            cmds.intSliderGrp('my_count', e=1, en=False)
            
    # 같은 이름의 window 있는지 검사
    if cmds.window('mywin', exists=1):
        # 같은 window 지우기
        cmds.deleteUI('mywin')
    # window 만들기
    window = cmds.window('mywin', title='Bouble Maker')
    # window 의 layout 지정
    cmds.columnLayout( adjustableColumn=True )
    # select obj 이름 표시
    cmds.text('sel_obj', label='Undefind' )
    # select update button
    cmds.button('update_butt', label='Select Update', c=new_sel)
    # control 영역 sphere 만들기 button
    cmds.button('make_sp', label='Make Sphere', c=makeSphere, en=False)
    # sphere 의 radius 를 조절하는 slider
    cmds.floatSliderGrp('my_radius', label='Radius',
                        field=True, minValue=0.01,
                        maxValue=10.0,
                        fieldMinValue=0.01,
                        fieldMaxValue=100.0,
                        value=1, cc=selVtx, en=False)
    # 선택할 vtx 갯수를 지정할 slider
    cmds.intSliderGrp('my_count', label='Count',
                      field=True, minValue=1, maxValue=300,
                      fieldMinValue=1, fieldMaxValue=300,
                      value=10, cc=selVtx, en=False)
    # 새로 선택할 vtx button
    cmds.button('my_select', label='Select Vertex', c=selVtx, en=False)
    # bouble 만들기 button
    cmds.button('my_bouble', label='Make Bouble', c=make_bouble_vtx, en=False )
    # 화면 닫기
    cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )
    # select 학인 function 호출
    new_sel(None)
    # window 사이즈 지정
    cmds.window('mywin', e=1,  widthHeight=(450, 180))
    # 윈도우 보기
    cmds.showWindow( window )

sp_com()
