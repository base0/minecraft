# https://youtu.be/N3HtUblRb5E

#agent.teleport(pos(100, 0, 0), WEST)
gameplay.time_set(DayTime.Day)
gameplay.set_weather(CLEAR)

player_position = player.position()
player.teleport(rpos(-17, 7, -22))

def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))

outline : List[Position] = []
N = 8    # N, len(outline) : 5,24  8, 40
blocks.fill(AIR, rpos(-N-1,0,-N-1), rpos(N+1,15,N+1))

shapes.circle(BLOCK_OF_QUARTZ, rpos(0, 0, 0), N, Axis.Y, ShapeOperation.HOLLOW)

# put outline positions in a list
for z in range(-N, N+1):
    for x in range(-N, N+1):
        if blocks.test_for_block(AIR, rpos(x, 0, z)) == False:
            outline.append(rpos(x, 0, z))
player.say('outline len ' + len(outline))

def distance(p1 : Position, p2 : Position):
    x1 = p1.get_value(Axis.X)
    z1 = p1.get_value(Axis.Z)
    x2 = p2.get_value(Axis.X)
    z2 = p2.get_value(Axis.Z)
    return ((x1-x2)**2+(z1-z2)**2)**0.5

# reorder the list by distance
temp : List[Position] = []
temp.append(outline[0])
outline.remove_at(0)
while len(outline) > 0:
    min_dist = 100000
    min_index = 0
    for i in range(len(outline)):
        dist = distance(temp[len(temp)-1], outline[i])
        if dist < min_dist:
            min_dist = dist
            min_index = i
    temp.append(outline[min_index])
    outline.remove_at(min_index)
outline = temp

'''
for p in outline:
    blocks.place(GOLD_BLOCK, p)
    loops.pause(500)
#player.say(outline[0].get_value(Axis.Y))
'''
# base
shapes.circle(BLOCK_OF_QUARTZ, rpos(0, 1, 0), N, Axis.Y, ShapeOperation.REPLACE)
shapes.circle(BLOCK_OF_QUARTZ, rpos(0, 0, 0), N+1, Axis.Y, ShapeOperation.REPLACE)

# gold
H = 8
shapes.sphere(GOLD_BLOCK, rpos(0, 1+H, 0), N, ShapeOperation.REPLACE)
blocks.fill(AIR, rpos(-N, 1+H, -N), rpos(N, 1+H-N+1, N))

# pillar

plan = [H, 3, 2, 1, 2, 3]
for g in range(10):
    for i in range(len(plan)):
        for y in range(plan[i]):
            blocks.place(BLOCK_OF_QUARTZ, positions.add(outline[g*6+i], pos(0, 1+H-y,0)))
