# https://www.tiktok.com/@craft_of_code/video/6930909315943468290
gameplay.set_weather(CLEAR)

player_position = player.position()
#player.teleport(offset(88, 49, -34))

def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))

DEPTH = 10
blocks.fill(BLOCK_OF_QUARTZ, rpos(0,0,-1), rpos(6,5,-DEPTH * 10), FillOperation.OUTLINE)

for i in range(DEPTH):
    blocks.place(REDSTONE_LAMP, rpos(3, 5, -i*10))
    blocks.place(LEVER, rpos(2, 4, -i*10))
    agent.teleport(rpos(2, 4, 1+i*-10), NORTH)
    agent.interact(FORWARD)

player.teleport(rpos(1, 1, -3))
loops.pause(10000)
for i in range(DEPTH):
    #loops.pause(1)
    agent.teleport(rpos(2, 4, 1+(DEPTH-1-i)*-10), NORTH)
    agent.interact(FORWARD)

loops.pause(500)
mobs.spawn(ZOMBIE, pos(0, 0, -2))
#blocks.place(SEA_LANTERN, pos(0,1,1))

