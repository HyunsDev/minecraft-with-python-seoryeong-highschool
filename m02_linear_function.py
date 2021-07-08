# -*- coding: utf-8 -*-
from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

"""
참고!!
분수는 소수로 바꿔서 입력하세요.

관련 수학 내용
수학 3단원 도형의 방정식 - 직선의 방정식1
"""

block = 42
block2 = 41

pos = mc.player.getTilePos()

print("직선의 방정식, y=ax+b")
a = float(input("a를 입력하세요: "))
b = float(input("b를 입력하세요: "))

pos.x += 3

mc.setBlocks(pos.x, pos.y-20, pos.z, pos.x, pos.y + 20, pos.z, block2)
mc.setBlocks(pos.x-20, pos.y, pos.z, pos.x+20, pos.y, pos.z, block2)
for x in range(-100, 101):
    y = a*x + b
    ax = round(x/10)
    ay = round(y/10)
    mc.setBlock(pos.x+ax, pos.y+ay, pos.z, block)
    sleep(0.05)
