player_position = player.position()
#player.teleport(rpos(-26, 116, 44))

def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))


RADIUS = 5
MAX = 3

x = 0
z = 0
for i in range(MAX):
    if i > MAX // 2 - 1:
        for j in range(i+1):
            for y in range(2):
                shapes.circle(GRASS, rpos(x, y, z - RADIUS * 2 * j), RADIUS, Axis.Y, ShapeOperation.HOLLOW)
            blocks.fill(AIR, rpos(x + 1, 0, z - RADIUS * 2 * j + RADIUS), rpos(x + RADIUS, 1, z - RADIUS * 2 * j - RADIUS), FillOperation.REPLACE)
    x += 0.87*RADIUS*2
    z += 0.5*RADIUS*2

x = 0.87 * RADIUS * 2 * (MAX-1)
z = 0
for y in range(2):
    shapes.circle(GRASS, rpos(x, y, z), RADIUS * (MAX+1), Axis.Y, ShapeOperation.OUTLINE)

blocks.place(WATER, rpos(x, 0, z))
mobs.spawn(TROPICAL_FISH, rpos(x, 0, z))

def onRun_in_background():
    global x
    global z
    d = RADIUS * (MAX+1)-1
    for i in range(1000000):
        rx = randint(-d, d)
        rz = randint(-d, d)
        if ((rx)**2+(rz)**2)**0.5 <  d:
            if blocks.test_for_block(GRASS, rpos(x + rx, 1, z + rz)) == False:
                blocks.place(WATER, rpos(x + rx, 1, z + rz))
loops.run_in_background(onRun_in_background)

for i in range(50):
   mobs.spawn(TROPICAL_FISH, rpos(x, 0, z))

#
'''
# not working because water flow
fill(x, z)

def fill(sx, sz):
    queue = []
    queue.append((sx,sz))
    while len(queue) != 0:
        x, z = queue.pop()
        if blocks.test_for_block(AIR, rpos(x, 0, z)):
            blocks.place(WATER, rpos(x, 0, z))
            queue.append((x, z-1))
            queue.append((x, z+1))
            queue.append((x-1, z))
            queue.append((x+1, z))
    player.say('end')
'''
