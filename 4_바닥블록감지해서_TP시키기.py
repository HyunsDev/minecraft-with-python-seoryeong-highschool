from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()

ban_block = 1 # 금지할 블록 아이디 (1: 돌)
succes_block = 57 # 결승선 블록 아이디 (57: 다이아몬트 블록)

init_pos = mc.player.getTilePos() # 플레이어의 처음 위치, 금지된 블록을 밟으면 이동할 위치

while True: # 무한 반복
    now_pos = mc.player.getTilePos() # 플레이어의 현재 위치
    playerBlockType = mc.getBlock( now_pos.x, now_pos.y, now_pos.z ) # 플레이어의 현재 위치에 해당하는 블록

    if playerBlockType == ban_block: # 만약 플레이어가 금지된 블록을 밟으면
        mc.player.setTilePos(init_pos.x, init_pos.y, init_pos.z) # 플레이러를 처음 위치로 보냄
    
    elif playerBlockType == succes_block: # 만약 플레이어가 결승선 블록을 밟으면
        mc.postToChat("결승선에 도달했습니다!") # 서버에 "결승선에 도달했습니다" 매세지를 보내고
        break # 반복문을 탈출함

    else: # 금지한 블록이나 결승선 블록 모두 밟은 상태가 아니라면
        sleep(0.03) # 0.03초(약 1틱)간 대기


