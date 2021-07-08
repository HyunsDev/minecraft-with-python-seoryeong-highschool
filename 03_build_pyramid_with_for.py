# -*- coding: utf-8 -*-
from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()

pos = mc.player.getTilePos() # 플레어어의 좌표 가져오기

sand = 12 # 모래의 블록 ID
sandState = 0 # 모래의 상태 ID (0: 모래, 1:붉은 모래)

x = pos.x + 1 # X축으로 1칸 이동
y = pos.y 
z = pos.z

floor = int(input("원하는 피라미드의 층 수를 입력해주세요: ")) #문자열로 입력받았기 때문에 정수형으로 변경해줌
width = floor * 2 - 1 # 피라미드의 너미는 층 수의 두 배 -1

for i in range(floor): # 피라미드의 층 수만큼 반복
    mc.setBlocks(x+i, y+i, z+i, x+width-1+i, y+i, z+width-1+i, sand, sandState) #피라미드 블록 쌓기
    width = width - 2 #층수가 하나씩 올라갈 때 마다 너비 2씩 감소
    sleep(0.5) # 0.5초 대기