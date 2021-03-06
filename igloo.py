# -*- coding: utf-8 -*-
from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

global snow, air
snow = 80
air = 0

delay = 0.1

# 아래 코드는 노가다입니다. 
class Igloo(object):
    def __init__(self, x, y, z):
        self.x = x 
        self.y = y
        self.z = z

    def build(self):

        self.floor1()
        sleep(delay)
        self.floor2()
        sleep(delay)
        self.floor3()
        sleep(delay)
        self.floor4()
        sleep(delay)
        self.floor5()
        sleep(delay)
        self.door()


    def floor1(self): # 1층(y:0~2)

        mc.setBlocks(self.x)

        for i in range(5):
            mc.setBlocks(self.x-2-i, self.y, self.z+i, self.x+2+i, self.y+2, self.z+i, snow)
            mc.setBlocks(self.x-1-i, self.y, self.z+i, self.x+1+i, self.y+2, self.z+i, air)
            sleep(delay)


        mc.setBlocks(self.x-6, self.y, self.z+5, self.x+6, self.y+2, self.z+6, snow)
        mc.setBlocks(self.x-5, self.y, self.z+5, self.x+5, self.y+2, self.z+6, air)
        sleep(delay)

        for i in range(5):
            mc.setBlocks(self.x-6+i, self.y, self.z+i+7, self.x+6-i, self.y+2, self.z+7+i, snow)
            mc.setBlocks(self.x-5+i, self.y, self.z+i+7, self.x+5-i, self.y+2, self.z+7+i, air)
            sleep(delay)

        mc.setBlocks(self.x-2, self.y, self.z+11, self.x+2, self.y+2, self.z+11, snow)
        sleep(delay)
        mc.setBlocks(self.x-2, self.y+2, self.z, self.x+2, self.y+2, self.z, snow)


    def floor2(self): # 2층(y:3~4)
        for i in range(4):
            mc.setBlocks(self.x-2-i, self.y+3, self.z+1+i, self.x+2+i, self.y+4, self.z+i+1, snow)
            mc.setBlocks(self.x-1-i, self.y+3, self.z+1+i, self.x+1+i, self.y+4, self.z+i+1, air)
            sleep(delay)

        mc.setBlocks(self.x-5, self.y+3, self.z+5, self.x+5, self.y+4, self.z+6, snow)
        mc.setBlocks(self.x-4, self.y+3, self.z+5, self.x+4, self.y+4, self.z+6, air)
        sleep(delay)

        for i in range(4):
            mc.setBlocks(self.x-5+i, self.y+3, self.z+7+i, self.x+5-i, self.y+4, self.z+i+7, snow)
            mc.setBlocks(self.x-4+i, self.y+3, self.z+7+i, self.x+4-i, self.y+4, self.z+i+7, air)
            sleep(delay)

        mc.setBlocks(self.x-2, self.y+3, self.z+10, self.x+2, self.y+4, self.z+10, snow)
        mc.setBlocks(self.x-2, self.y+3, self.z+1, self.x+2, self.y+4, self.z+1, snow)
        sleep(delay)

    def floor3(self): # 3층(y:5)
        for i in range(3):
            mc.setBlocks(self.x-2-i, self.y+5, self.z+2+i, self.x+2+i, self.y+5, self.z+i+2, snow)
            mc.setBlocks(self.x-1-i, self.y+5, self.z+2+i, self.x+1+i, self.y+5, self.z+i+2, air)
            sleep(delay)


        mc.setBlocks(self.x-4, self.y+5, self.z+5, self.x+4, self.y+5, self.z+6, snow)
        mc.setBlocks(self.x-3, self.y+5, self.z+5, self.x+3, self.y+5, self.z+6, air)
        sleep(delay)

        for i in range(3):
            mc.setBlocks(self.x-4+i, self.y+5, self.z+7+i, self.x+4-i, self.y+5, self.z+i+7, snow)
            mc.setBlocks(self.x-3+i, self.y+5, self.z+7+i, self.x+3-i, self.y+5, self.z+i+7, air)
            sleep(delay)

        mc.setBlocks(self.x-2, self.y+5, self.z+9, self.x+2, self.y+5, self.z+9, snow)
        mc.setBlocks(self.x-2, self.y+5, self.z+2, self.x+2, self.y+5, self.z+2, snow)
        sleep(delay)

    def floor4(self): # 4층(y:6)
        for i in range(2):
            mc.setBlocks(self.x-2-i, self.y+6, self.z+3+i, self.x+2+i, self.y+6, self.z+3+i, snow)
            mc.setBlocks(self.x-1-i, self.y+6, self.z+3+i, self.x+1+i, self.y+6, self.z+3+i, air)
            sleep(delay)

        mc.setBlocks(self.x-3, self.y+6, self.z+5, self.x+3, self.y+6, self.z+6, snow)
        mc.setBlocks(self.x-2, self.y+6, self.z+5, self.x+2, self.y+6, self.z+6, air)
        sleep(delay)

        for i in range(2):
            mc.setBlocks(self.x-3+i, self.y+6, self.z+7+i, self.x+3-i, self.y+6, self.z+7+i, snow)
            mc.setBlocks(self.x-2+i, self.y+6, self.z+7+i, self.x+2-i, self.y+6, self.z+7+i, air)
            sleep(delay)

        mc.setBlocks(self.x-2, self.y+6, self.z+8, self.x+2, self.y+6, self.z+8, snow)
        mc.setBlocks(self.x-2, self.y+6, self.z+3, self.x+2, self.y+6, self.z+3, snow)
        sleep(delay)

    def floor5(self): # 5층(y:7)
        mc.setBlocks(self.x-2, self.y+7, self.z+4, self.x+2, self.y+7, self.z+7, snow)
        sleep(delay)

    def door(self): # 문 만들기
        mc.setBlocks(self.x-1, self.y, self.z-1, self.x+1, self.y+2, self.z-1, snow)
        mc.setBlocks(self.x, self.y, self.z-1, self.x, self.y+1, self.z-1, air)
        sleep(delay)