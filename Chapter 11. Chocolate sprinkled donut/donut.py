# coding: utf-8
# 도넛에 cone 초코 뿌리기

import maya.cmds as cmds
import random, math
import copy

# 거리를 계산하는 함수
def get_dis(pos1, pos2):
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

# 도넛에 Cone 코초 뿌리기
def make_choco(dis_):
    # 지난 만든 초고 거리 검사
    def check_(sel_pos):
        # 수집된 좌표 looping
        for pos_ in collect_pos:
            # 거리 검사
            if get_dis(pos_, sel_pos) < dis_:
                # 짧은 거리 True return
                return True
        # 짧은 거리 없으면, False return
        return False
    # 도넛의 모든 vtx 자표 수집
    # q(query), ws(worldSpace), t(translation)
    all_pos  = cmds.xform('pTorus1.vtx[*]', q=1, ws=1, t=1)
    # vtx (x, y, z) 로 정렬
    all_vtx = zip(all_pos[::3], all_pos[1::3], all_pos[2::3])
    # random 으로 섞기 전에 all_vtx 자료를 rand_vtx 로 복사
    rand_vtx = copy.copy(all_vtx)
    # random 으로 섞기
    random.shuffle(rand_vtx)
    # 수집할 자료 준비
    collect_pos = []
    # 섞은 자료 looping
    for sel_pos in rand_vtx:
        # 수집 자료 있으면, 거리 검사
        if collect_pos:
            # 가까운 거리 있으면 계속
            if check_(sel_pos):
                continue
        # 좌표 수집
        collect_pos.append(sel_pos)
    # 수집된 좌표 looping
    for pos_ in collect_pos:
        # 좌표에 vtx 의 normal 추출
        normal_ = cmds.polyNormalPerVertex('pTorus1.vtx[%s]' 
                                    % all_vtx.index(pos_) ,
                            query=True, xyz=True )[:3]
        # 초코 콘 만들기
        cone_ = cmds.polyCone(axis=normal_, height=1, 
                              radius=0.5)
        # 좌표로 초코콘 이동
        cmds.move(*list(pos_) + cone_[:1])
