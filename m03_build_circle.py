# -*- coding: utf-8 -*-
import math
from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

"""

참고!!
분수는 소수로 바꿔서 입력하세요.

관련 수학 내용
수학 3단원 도형의 방정식 - 원의 방정식
"""

block = 42
block2 = 41

pos = mc.player.getTilePos()

print("원의 방정식, r²=x²+y²")
r = float(input("반지름의 길이(r)를 입력하세요: "))


mc.setBlocks(pos.x, pos.y, pos.z-round(r), pos.x, pos.y, pos.z+round(r), block2)
mc.setBlocks(pos.x-round(r), pos.y, pos.z, pos.x+round(r), pos.y, pos.z, block2)
x_min = round(r * -1)
x_max = round(r + 1) 
r_10 = r * 10

for x in range(x_min*10, x_max*10):
    try:
        y = math.sqrt((r_10**2) - (x**2))
    except Exception as e:
        print(e)
        continue

    print(f"r: {r}, x: {x}, y: {y}")

    ax = round(x/10)
    ay = round(y/10)
    mc.setBlock(pos.x+ax, pos.y, pos.z+ay, block)
    mc.setBlock(pos.x+(ax*-1), pos.y, pos.z+(ay*-1), block)



