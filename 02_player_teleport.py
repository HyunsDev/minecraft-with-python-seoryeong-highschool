# -*- coding: utf-8 -*-
from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()

pos = mc.player.getTilePos() # 플레이어의 좌표 가져오기
pos.x = pos.x - 5 # x축으로 -5칸한 좌표
pos.y = pos.y + 3 # y축으로 +3칸한 좌표
pos.z = pos.z - 5 # z축으로 -5칸한 좌표

mc.player.setTilePos(pos.x, pos.y, pos.z) # 플레이어의 좌표를 위에서 구한 좌표로 설정(tp)