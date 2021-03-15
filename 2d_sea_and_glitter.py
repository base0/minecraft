# https://youtu.be/AWhLA7M3WkI
gameplay.time_set(DayTime.Night)

player_position = player.position()
agent.teleport_to_player()
#loops.pause(5*1000)
player.teleport(pos(18, 20, -34))

def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))

def glitter():
    while True:
        agent.teleport(rpos(randint(0,40), 60, 4), WEST)
        agent.set_item(GLOWSTONE, 1, 1)
        agent.drop_all(FORWARD)


#blocks.fill(SOUL_SAND, rpos(0, 0, 0), rpos(4*5*2,0,3*3))
loops.run_in_background(glitter)

loops.pause(10*1000)
for i in range(12):
    for j in range(6):
        radius = 5
        ss = 0
        ss = radius if i % 2 == 0 else 0
        shapes.circle(WATER, rpos(j*radius*2+ss, i*radius, i*3), radius, Axis.Z, ShapeOperation.REPLACE)




