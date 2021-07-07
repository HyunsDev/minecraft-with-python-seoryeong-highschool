from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()


# checkBlock 함수
"""  뒤에서 설명 """
def checkBlock(x, y, z, lastx, lastz):
    blockType = 66 # 레일 블록 id 66
    
    if (blockType == mc.getBlock(x+1,y,z)) and (lastx != x+1): # x축으로 +1칸이 레일인지 확인 + 이전 블록이 아닌지 확인
        pos = [x+1,y,z]
        return pos

    elif (blockType == mc.getBlock(x,y,z+1)) and (lastz != z+1): #z축으로 +1칸이 레일인지 확인
        pos = [x,y,z+1]
        return pos

    elif (blockType == mc.getBlock(x-1,y,z)) and (lastx != x-1): #x축으로 -1칸이 레일인지 확인
        pos = [x-1,y,z]
        return pos

    elif (blockType == mc.getBlock(x,y,z-1)) and (lastz != z-1): #z축으로 +1칸이 레일인지 확인
        pos = [x,y,z-1]
        return pos

    else: # 만약 이동할 레일이 없다면
        mc.postToChat("레일이 끝났습니다!") # "레일이 끝났습니다" 출력

cake = 92 # 케이크 블록 id 

ans = input("철도의 시작 지점으로 이동하고, Enter키를 누르세요")
pos = mc.player.getTilePos() # 플레이어의 위치를 처음 케이크의 위치로 설정 

# 철도의 시작 좌표
x = pos.x
y = pos.y - 2
z = pos.z

lastX = pos.x # lastX 변수 초기화

while(True):
    pos2 = checkBlock(x, y, z, lastX) # 케이크가 이동할 위치 가져오기

    # 케이크 블록 옮기기
    mc.setBlock(pos2[0], pos2[1]+1, pos2[2], cake) # 이동할 위치에 케이크 생성하기
    mc.setBlock(x, y+1, z, 0) # 이전 위치의 케이크 제거하기
    
    time.sleep(0.1) # 0.1초 기다리기
    lastX = x # x 다음 레일 좌표로 변경 하기 전에 lastX에 저장

    # 현재 레일의 좌표를 케이크가 옮겨진 레일의 좌표로 변경
    x = pos2[0]
    y = pos2[1]
    z = pos2[2]