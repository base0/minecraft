# https://youtu.be/IBacfNN0acg

gameplay.set_weather(CLEAR)

player_position = player.position()
player.teleport(offset(88, 49, -34))
#player.say(player_position.get_value(Axis.X))

def offset(x, y, z):
    return positions.add(player_position, pos(x, y, z))

def wall():
    blocks.fill(BLOCK_OF_QUARTZ, offset(0, 0, 0), offset(6, 4, 6), FillOperation.OUTLINE)
    blocks.fill(AIR, offset(1, 0, 1), offset(5, 4, 5), FillOperation.REPLACE)
    blocks.fill(PLANKS_OAK, offset(0, -1, 0), offset(6, -1, 6), FillOperation.REPLACE)

    blocks.place(OAK_DOOR, offset(3, 0, 0))

def rear_window():
    for x in [2, 3, 4]:
        for y in [1, 2]:
            blocks.place(GLASS_PANE, offset(x, y, 6))

def side_windows():
    for y in [1, 2]:
        for x in [0, 6]:
            for z in [2, 3, 4]:
                blocks.place(GLASS_PANE, offset(x, y, z))

def gable():
    x = 0
    for y in [4, 5, 6, 7, 6, 5, 4]:
        shapes.line(RED_GLAZED_TERRACOTTA, offset(x, y, 0), offset(x, y, 6))
        x += 1
def gable_end():
    for z in [0, 6]:
        for x in range(3):
            shapes.line(BLOCK_OF_QUARTZ, offset(x+1, 4+x, z), offset(6-x-1, 4+x, z))


def house():
    wall()
    rear_window()
    side_windows()
    gable()
    gable_end()
    # close the door

    if distance() < 80:
        agent.teleport(offset(3,0,-1), SOUTH)
        agent.interact(FORWARD)
    


def distance():
    p1 = offset(3,0,-1)
    p2 = player.position();
    x1 = p1.get_value(Axis.X)
    y1 = p1.get_value(Axis.Y)
    z1 = p1.get_value(Axis.Z)
    x2 = p2.get_value(Axis.X)
    y2 = p2.get_value(Axis.Y)
    z2 = p2.get_value(Axis.Z)    
    return ((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**0.5

for r in range(10):
    for c in range(10):
        old_player_position = player_position
        player_position = positions.add(player_position, pos(r*21-r, 0, c*21-c))
        blocks.fill(AIR, offset(-6,-3,-6), offset(12, 60, 12), FillOperation.REPLACE)
        blocks.fill(GRASS, offset(-6,-3,-6), offset(12, -1, 12), FillOperation.REPLACE)
        house()
        player_position = old_player_position
