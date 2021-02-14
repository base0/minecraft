# https://youtu.be/e5oibdlBzOo

# set game mode to Easy
gameplay.time_set(DayTime.NIGHT)

player_position = player.position()

def rpos(x, y, z):
    global player_position
    return positions.add(player_position, pos(x, y, z))

zombie()

def zombie():
    loops.pause(1000)
    for x in range(-3, 4):
        blocks.place(AIR, rpos(x,-2,4))
        blocks.place(AIR, rpos(x,-1,4))
        blocks.place(AIR, rpos(x,-1,3))
        mobs.spawn(ZOMBIE_VILLAGER, rpos(x, -2, 4))

def earth():
    global player_position
    player_position = player.position()
    blocks.fill(GRASS, rpos(-5, 0, 8), rpos(5, 4, 8))
    zombie()

def fire():
    global player_position
    player_position = player.position()
    blocks.fill(LAVA, rpos(-5, 0, 8), rpos(5, 4, 8))
    zombie()

def h2o():
    global player_position
    player_position = player.position()
    #blocks.fill(AIR, rpos(-5, 1, 6), rpos(5, -5, 10), FillOperation.REPLACE)
    blocks.fill(WATER, rpos(-5, -1, 6), rpos(5, -3, 10), FillOperation.REPLACE)
    zombie()

player.on_chat("earth", earth)
player.on_chat("fire", fire)
player.on_chat("water", h2o)
