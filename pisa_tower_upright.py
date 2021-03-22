# https://youtu.be/8Riq1RFy9ws
R1 = 20    # R, CIRCUMFERENCE : 5,24  8,40  16,84  20,108
R2 = 16
CIRCUMFERENCE = 108   # len(outline)
H = 15
plan = [H, 3, 2, 1, 2, 3]


#agent.teleport(pos(100, 0, 0), WEST)
gameplay.time_set(8000)
gameplay.set_weather(CLEAR)

player.teleport(world(7000, 4, 0))
loops.pause(1000)
player_position = player.position()
player.teleport(rpos(37, 41, -89))

#loops.run_in_background(roof)     # problem with run roof() in background
outline1 : List[Position] = get_outline(R1)
outline2 : List[Position] = get_outline(R2)
#player.say(len(outline1))
#player.say(len(outline2))
#roof()
wall()
for i in range(20):
    mobs.spawn(VILLAGER, rpos(0, 1+2*H, 0))
    mobs.spawn(VILLAGER, rpos(0, 1+1*H, 0))
    mobs.spawn(VILLAGER, rpos(0, 1+0*H, 0))

def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))

def get_outline(R):
    #player.say(R)
    outline : List[Position] = []
    #blocks.fill(AIR, rpos(-R-1,0,-R-1), rpos(R+1,15,R+1))
    shapes.circle(STONE, rpos(0, 0, 0), R, Axis.Y, ShapeOperation.HOLLOW)

    # put outline positions in a list
    for z in range(-R, R+1):
        #player.say(z)
        for x in range(-R, R+1):
            if blocks.test_for_block(AIR, rpos(x, 0, z)) == False:
                outline.append(rpos(x, 0, z))
    
    blocks.fill(AIR, rpos(-R,0,-R), rpos(R,0,R))

    # reorder outline
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
    #player.say('end reorder')
    return temp

def distance(p1 : Position, p2 : Position):
    x1 = p1.get_value(Axis.X)
    z1 = p1.get_value(Axis.Z)
    x2 = p2.get_value(Axis.X)
    z2 = p2.get_value(Axis.Z)
    return ((x1-x2)**2+(z1-z2)**2)**0.5


# roof
def roof():
    shapes.sphere(PRISMARINE, rpos(0, 30, 0), R2, ShapeOperation.OUTLINE)
    blocks.fill(AIR, rpos(-R2, 30, -R2), rpos(R2, 30-R2, R2))


# wall
def wall():
    global outline1
    global outline2
    for i in range(6):
        shapes.circle(BLOCK_OF_QUARTZ, rpos(0, i*H, 0), R1, Axis.Y, ShapeOperation.REPLACE)
        arch_wall(outline1, plan, (i+1)*H)
    shapes.circle(BLOCK_OF_QUARTZ, rpos(0, 6*H, 0), R1, Axis.Y, ShapeOperation.REPLACE)
    arch_wall(outline2, plan, 7*H)
    shapes.circle(BLOCK_OF_QUARTZ, rpos(0, 7*H, 0), R2, Axis.Y, ShapeOperation.REPLACE)


def arch_wall(outline : List[Position], plan : List[number], top : number):
    for g in range(len(outline) // len(plan)):
        for i in range(len(plan)):
            for y in range(plan[i]):
                blocks.place(BLOCK_OF_QUARTZ, positions.add(outline[g*len(plan)+i], pos(0, top-y,0)))
