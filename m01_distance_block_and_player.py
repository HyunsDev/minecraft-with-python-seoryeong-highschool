# -*- coding: utf-8 -*-
from mcpi.minecraft import Minecraft
import math

mc = Minecraft.create()

"""
참고!!
이 프로그램은 y축은 무시하고, x축과 z축으로 된 2차원 상에서의 거리를 구합니다! 즉 높이가 반영되지 않습니다!
3차원 상에서 두 물체의 거리를 구하는 것은 아직 나간 부분이 아니라 생략합니다.

관련 수학 내용
수학 3단원 도형의 방정식 - 평면좌표
"""

# 위치 가져오기
input("첫 번째 위치로 이동한 뒤 Enter를 누르세요")
pos1 = mc.player.getTilePos()
mc.postToChat(f"first pos ({pos1.x},{pos1.z})")

input("두 번째 위치로 이동한 뒤 Enter를 누르세요")
pos2 = mc.player.getTilePos()
mc.postToChat(f"twice pos ({pos2.x},{pos2.z})")

# 계산하기
"""
두 점 사이의 거리의 공식
거리 = √{(x₂-x₁)² + (y₂-y₁)²}
"""

pos1_x = int(pos1.x) # 첫 번째 위치의 x좌표
pos1_y = int(pos1.z) # 첫 번째 위치의 y좌표 (실제 마인크래프트에서는 z축이지만, 편의를 위해 y를 사용합니다.)
pos2_x = int(pos2.x) # 두 번째 위치의 x좌표
pos2_y = int(pos2.z) # 두 번째 위치의 y좌표

distance = math.sqrt((pos2_x - pos1_x)**2 + (pos2_y - pos1_y)**2) # 두 점 사이의 거리 공식을 이용하여 거리를 계산.

mc.postToChat(f"distance: {distance}") # 마인크래프에 메세지 보내기

