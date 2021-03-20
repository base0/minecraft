#agent.teleport(pos(100, 0, 0), WEST)

outline : List[Position] = []
N = 5
blocks.fill(AIR, pos(-N-1,0,-N-1), pos(N+1,15,N+1))

shapes.circle(GRASS, pos(0, 0, 0), N, Axis.Y, ShapeOperation.HOLLOW)

# put outline positions in a list
for z in range(-N, N+1):
    for x in range(-N, N+1):
        if blocks.test_for_block(AIR, pos(x, 0, z)) == False:
            outline.append(pos(x, 0, z))
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
    player.say(len(temp)+' '+min_dist)
    temp.append(outline[min_index])
    outline.remove_at(min_index)
outline = temp

for p in outline:
    blocks.place(GOLD_BLOCK, p)
    loops.pause(500)

player.say(outline[0].get_value(Axis.Y))
    
