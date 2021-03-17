# https://youtu.be/oQ2tejU_D14

gameplay.time_set(DayTime.Night)
gameplay.set_weather(RAIN)
agent.teleport(pos(100, 0, 0), WEST)

N = 10
# room
b = YELLOW_CONCRETE # BLOCK_OF_QUARTZ
blocks.fill(b, world(0,3,-2), world(N*2,8,3), FillOperation.HOLLOW)
# roof
blocks.fill(GLOWSTONE, world(0,8,-2), world(N*2,8,3))
# cage
blocks.fill(b, world(0, 4, 3), world(N*2, 7, 5))
#for i in range(1, N):
#    blocks.place(TORCH, world(i*2, 5, 2))
for i in range(N):
    blocks.place(AIR, world(i*2+1, 6, 4))
def free():
    for i in range(N):
        blocks.place(AIR,world(i*2+1, 6, 5))

def glass():
    for i in range(N):
        blocks.place(GLASS,world(i*2+1, 6, 3))

def cat():
    for i in range(N):
        blocks.place(b,world(i*2+1, 6, 5))
        mobs.spawn(CAT, world(i*2+1, 6, 4))

'''
def onRun_in_background():
    loops.pause(10*1000)
    while True:
        prev_i = 1
        for i in range(2, 18):
            blocks.place(AIR, world(prev_i, 4, 0))
            blocks.place(ARMOR_STAND, world(i, 4, 0))
            prev_i = i
            loops.pause(500)
            
loops.run_in_background(onRun_in_background)
'''
player.on_chat("f", free)
player.on_chat("c", cat)
player.on_chat("g", glass)

