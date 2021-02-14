gameplay.time_set(DayTime.NIGHT)

agent.teleport(pos(100, 0, 100), WEST)
player_position = player.position()

def rpos(x, y, z):
    global player_position
    return positions.add(player_position, pos(x, y, z))

zombie(20)

def zombie(n):
    n = n // 2
    loops.pause(1000)
    for x in range(-n, n + 1):
        blocks.place(AIR, rpos(x,-2,2))
        blocks.place(AIR, rpos(x,-1,2))
        blocks.place(AIR, rpos(x,-1,1))
        mobs.spawn(ZOMBIE_VILLAGER, rpos(x, -2, 2))

def earth():
    global player_position
    player_position = player.position()
    blocks.fill(GRASS, rpos(-5, 0, 8), rpos(5, 4, 8))
    zombie(20)

def fire():
    global player_position
    player_position = player.position()
    blocks.fill(LAVA, rpos(-5, 0, 8), rpos(5, 4, 8))
    zombie(20)

def h2o():
    global player_position
    player_position = player.position()
    #blocks.fill(AIR, rpos(-5, 1, 6), rpos(5, -5, 10), FillOperation.REPLACE)
    blocks.fill(WATER, rpos(-5, -1, 6), rpos(5, -3, 10), FillOperation.REPLACE)
    zombie(20)

player.on_chat("earth", earth)
player.on_chat("fire", fire)
player.on_chat("water", h2o)
