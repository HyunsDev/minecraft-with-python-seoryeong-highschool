#마인크래프트와 연결
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# 플레이어의 초기 좌표 pos1에 저장
pos1 = mc.player.getTilePos()

# 얼음 블록 ID
ice = 79

# for 문을 이용하여 0.1초 마다 100번 반복하는 반복문을 만들기
import time # time 모듈 추가
# for 문

for i in range(100):
    # 사용자의 현재 위치 pos2에 저장
    pos2 = mc.player.getTilePos()
    x = pos2.x
    y = pos2.y
    z = pos2.z
    # if 문 이용(pos1과 pos2가 다르면 얼음 다리 블록 놓기)
    if (pos1 != pos2):
        mc.setBlocks(x-2, y-1, z, x+2, y-1, z, ice)
        mc.setBlock(x-2, y, z, ice)
        mc.setBlock(x+2, y, z, ice)

    time.sleep(0.1)
    # pos1에 pos2 대입 
    pos1 = pos2