# https://youtu.be/hI911-kK4a4

gameplay.set_weather(CLEAR)

player_position = player.position()
#player.teleport(offset(-26, 116, 44))

def offset(x, y, z):
    return positions.add(player_position, pos(x, y, z))

def wall():
    blocks.fill(BLOCK_OF_QUARTZ, offset(0, 0, 0), offset(6, 4, 6), FillOperation.OUTLINE)

    blocks.fill(AIR, offset(1, 0, 1), offset(5, 4, 5), FillOperation.OUTLINE)

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
    agent.teleport(offset(3,0,-1), SOUTH)
    agent.interact(FORWARD)

for r in range(10):
    for c in range(10):
        old_player_position = player_position
        player_position = positions.add(player_position, pos(r*20, 0, c*20))
        blocks.fill(AIR, offset(-5,-3,-5), offset(11, 5, 11), FillOperation.REPLACE)
        blocks.fill(GRASS, offset(-5,-3,-5), offset(11, -1, 11), FillOperation.REPLACE)
        house()
        player_position = old_player_position
