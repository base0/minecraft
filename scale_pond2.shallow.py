gameplay.set_weather(CLEAR)
player_position = player.position()
#player.teleport(rpos(17, 32, -1))  # 3
#player.teleport(rpos(35, 46, -3))  # 5
player.teleport(rpos(91, 90, 78))  # 11

def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))

RADIUS = 5
MAX = 11

x = 0.87 * RADIUS * 2 * (MAX-1)
z = 0
for y in range(1):
    shapes.circle(STONE_BRICKS, rpos(x, y, z), RADIUS * (MAX+1), Axis.Y, ShapeOperation.OUTLINE)

x = 0
z = 0
for i in range(MAX):
    if i > MAX // 2 - 1:
        for j in range(i+1):
            for y in range(1):
                shapes.circle(STONE_BRICKS, rpos(x, y, z - RADIUS * 2 * j), RADIUS, Axis.Y, ShapeOperation.HOLLOW)
            blocks.fill(AIR, rpos(x + 1, 0, z - RADIUS * 2 * j + RADIUS), rpos(x + RADIUS, 1, z - RADIUS * 2 * j - RADIUS), FillOperation.REPLACE)
    x += 0.87*RADIUS*2
    z += 0.5*RADIUS*2

x = 0.87 * RADIUS * 2 * (MAX-1)
z = 0
for y in range(1):
    shapes.circle(STONE_BRICKS, rpos(x, y, z), RADIUS * (MAX+1), Axis.Y, ShapeOperation.OUTLINE)

d = RADIUS * (MAX+1)-1
for rx in range(-d, d):
    for rz in range(-d, d):
        if ((rx)**2+(rz)**2)**0.5 <  d:
            if blocks.test_for_block(STONE_BRICKS, rpos(x + rx, 0, z + rz)) == False:
                blocks.place(WATER, rpos(x + rx, 0, z + rz))
                if randint(0, 3) == 0:
                    mobs.spawn(TROPICAL_FISH, rpos(x + rx, 0, z + rz))
