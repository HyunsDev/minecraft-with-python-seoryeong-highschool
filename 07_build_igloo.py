from mcpi.minecraft import Minecraft
from time import sleep
from igloo import Igloo

mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

newIgloo1 = Igloo(x, y, z)
newIgloo1.build()
sleep(0.5)

newIgloo2 = Igloo(x+15, y, z)
newIgloo2.build()
sleep(0.5)

newIgloo3 = Igloo(x, y, z+15)
newIgloo3.build()
sleep(0.5)

newIgloo4 = Igloo(x+15, y, z+15)
newIgloo4.build()
sleep(0.5)