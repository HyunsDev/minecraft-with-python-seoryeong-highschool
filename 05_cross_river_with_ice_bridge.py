# -*- coding: utf-8 -*-
from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()


# 플레이어의 처음 위치를 first_pos에 저장
first_pos = mc.player.getTilePos()

# 얼음 블록 ID
ice = 79

while True:
    # 플레이어의 현재 위치를 last_pos에 저장
    last_pos = mc.player.getTilePos()
    x = last_pos.x
    y = last_pos.y
    z = last_pos.z
    
    # if 문 이용(first_pos과 last_pos가 다르면 얼음 다리 블록 놓기)
    if (first_pos != last_pos):
        mc.setBlocks(x-1, y-1, z-1, x+1, y-1, z+1, ice)
    first_pos = last_pos # first_pos에 last_pos 대입

    sleep(0.03)

