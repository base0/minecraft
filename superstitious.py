# https://youtu.be/UXX34K07SFY

gameplay.time_set(DayTime.Night)
gameplay.set_weather(RAIN)

N = 10
# room
b = YELLOW_CONCRETE # BLOCK_OF_QUARTZ
blocks.fill(b, world(0,3,-2), world(N*2,7,3), FillOperation.HOLLOW)
# roof
blocks.fill(GLASS, world(0,7,-2), world(N*2,7,3))
# cage
blocks.fill(b, world(0, 4, 3), world(N*2, 6, 5))
for i in range(1, N):
    blocks.place(TORCH, world(i*2, 5, 2))
for i in range(N):
    blocks.place(AIR, world(i*2+1, 5, 4))
def free():
    for i in range(N):
        blocks.place(AIR,world(i*2+1, 5, 5))

def glass():
    for i in range(N):
        blocks.place(GLASS,world(i*2+1, 5, 3))

def cat():
    for i in range(N):
        blocks.place(b,world(i*2+1, 5, 5))
        mobs.spawn(CAT, world(i*2+1, 5, 4))

player.on_chat("free", free)
player.on_chat("cat", cat)
player.on_chat("glass", glass)

