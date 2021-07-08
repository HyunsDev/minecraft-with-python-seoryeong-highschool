# -*- coding: utf-8 -*-
from mcpi.minecraft import Minecraft # 마인크래프트 모듈 불러오기
mc = Minecraft.create() # 마인크래프트 서버에 연결하기

string = input("서버에 전송할 메세지를 입력하세요: ") # 서버에 전송할 메세지 입력하여 string 변수에 담기
mc.postToChat(string) # string에 담긴 값을 마인크래프트 채팅창에 출력