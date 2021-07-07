from mcpi.minecraft import Minecraft # 마인크래프트에 연결
mc = Minecraft.create()

string = "Hello" # string이라는 변수에 Hello라는 값 지정
mc.postToChat(string) # string에 담긴 값을 마인크래프트 채팅창에 출력