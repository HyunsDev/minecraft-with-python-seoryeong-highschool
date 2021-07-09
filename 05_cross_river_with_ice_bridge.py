# -*- coding: utf-8 -*-
from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()


# 플레이어의 초기 좌표 pos1에 저장
pos1 = mc.player.getTilePos()

# 얼음 블록 ID
ice = 79

while True:
    # 사용자의 현재 위치 pos2에 저장
    pos2 = mc.player.getTilePos()
    x = pos2.x
    y = pos2.y
    z = pos2.z
    # if 문 이용(pos1과 pos2가 다르면 얼음 다리 블록 놓기)
    if (pos1 != pos2):
        mc.setBlocks(x-1, y-1, z-1, x+1, y-1, z+1, ice)

    sleep(0.03)
    # pos1에 pos2 대입 
    pos1 = pos2