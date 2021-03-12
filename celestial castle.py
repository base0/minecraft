player_position = player.position()

gameplay.set_weather(CLEAR)
gameplay.time_set(23000) # dawn
#gameplay.time_add(7*1000)
player.teleport(pos(-24, 16, 17))


sin60 = 0.866
cos60 = 0.5
tan60 = 1.73205

sin30 = 0.5
cos30 = 0.866
tan30 = 0.57735026918962576450914878


cloud()
mobs.spawn(VILLAGER, rpos(0, 0, 0))
mobs.spawn(VILLAGER, rpos(0, 0, 0))

shapes.line(GOLD_BLOCK,rpos(0,0,7),  rpos(0,12,7) )
shapes.line(GOLD_BLOCK,rpos(0,0,3),  rpos(0,12,3) )
shapes.line(GOLD_BLOCK,rpos(0,0,-3), rpos(0,12,-3) )
shapes.line(GOLD_BLOCK,rpos(0,0,-7), rpos(0,12,-7) )

shapes.line(GOLD_BLOCK,rpos(4,0,7),  rpos(4,12,7) )
shapes.line(GOLD_BLOCK,rpos(4,0,3),  rpos(4,12,3) )
shapes.line(GOLD_BLOCK,rpos(4,0,-3), rpos(4,12,-3) )
shapes.line(GOLD_BLOCK,rpos(4,0,-7), rpos(4,12,-7) )

player_position = positions.add(player_position, pos(0,0,-5))
roof(17, 13, -1,13,0, -1)
player_position = positions.add(player_position, pos(0,0,5))
roof(22, 13, -1,13,0, -1)
player_position = positions.add(player_position, pos(0,0,5))
roof(17, 13, -1,13,0, -1)


def rpos(x, y, z):
    global player_position
    return positions.add(player_position, pos(x, y, z))

def cloud():
    shapes.circle(WOOL, rpos(0, -1, 0), 10, Axis.Y, ShapeOperation.REPLACE)
    shapes.circle(WHITE_STAINED_GLASS, rpos(0,-1,0), 10, Axis.Y, ShapeOperation.OUTLINE)
    shapes.circle(WOOL, rpos(0, -3, 0), 10, Axis.Y, ShapeOperation.REPLACE)
    shapes.circle(WHITE_STAINED_GLASS, rpos(0,-3,0), 10, Axis.Y, ShapeOperation.OUTLINE)

    shapes.circle(WOOL, rpos(0, -2, 10), 6, Axis.Y, ShapeOperation.REPLACE)
    shapes.circle(WHITE_STAINED_GLASS, rpos(0, -2, 10), 6, Axis.Y, ShapeOperation.OUTLINE)
    shapes.circle(WOOL, rpos(0, -2, -10), 6, Axis.Y, ShapeOperation.REPLACE)
    shapes.circle(WHITE_STAINED_GLASS, rpos(0, -2, -10), 6, Axis.Y, ShapeOperation.OUTLINE)

def triangle(top, bottom, base_width, x, b):
    h_base = base_width // 2
    r = h_base / sin30
    shapes.line(b, rpos(x, top, 0), rpos(x, bottom, h_base))
    shapes.line(b, rpos(x, top, 0), rpos(x, bottom, -h_base))
    shapes.line(b, rpos(x, bottom, -h_base), rpos(x, bottom, h_base))

def roof(top, bottom, x_start, length, skip_start, skip_end):
    # roof
    h_base = (top-bottom) * tan30
    base_width = h_base*2
    ceiling = bottom

    i = 0   # can remove this line if the following code has no error
    for i in range(x_start, x_start + length):
        if skip_start <= i <= skip_end:
            continue
        if i == x_start or i == x_start + length - 1:
            b = GOLD_BLOCK
        elif i == x_start+1 or i == x_start + length - 2:
            b = GREEN_WOOL
        else:
            b = GREEN_WOOL
        triangle(top, bottom, base_width, i, b)

    shapes.line(GOLD_BLOCK, rpos(0+x_start, top, 0), rpos(length-1+x_start, top, 0))
    shapes.line(GOLD_BLOCK, rpos(0+x_start, ceiling, -h_base), rpos(length-1+x_start, ceiling, -h_base))
    shapes.line(GOLD_BLOCK, rpos(0+x_start, ceiling, h_base), rpos(length-1+x_start, ceiling, h_base))

    # chor fah
    b = BIRCH_WOOD_STAIRS
    blocks.place(blocks.block_with_data(b, 4), rpos(-1+x_start,top,0))
    blocks.place(blocks.block_with_data(b, 4), rpos(-1+x_start,top+1,0))
    blocks.place(blocks.block_with_data(b, 1), rpos(0+x_start,top+1,0))
    blocks.place(blocks.block_with_data(b, 1), rpos(-1+x_start,top+2,0))
    blocks.place(blocks.block_with_data(b, 0), rpos(-1+x_start,top+3,0))

    blocks.place(blocks.block_with_data(b, 5), rpos(length+x_start,top,0))
    blocks.place(blocks.block_with_data(b, 5), rpos(length+x_start,top+1,0))
    blocks.place(blocks.block_with_data(b, 0), rpos(length-1+x_start,top+1,0))
    blocks.place(blocks.block_with_data(b, 0), rpos(length+x_start,top+2,0))
    blocks.place(blocks.block_with_data(b, 1), rpos(length+x_start,top+3,0))

    # gable
    
    for z in range(-h_base+2,h_base-1):
        y = 1
        while blocks.test_for_block(AIR, rpos(1+x_start, ceiling+y, z)):
            blocks.place(ORANGE_WOOL, rpos(1+x_start, ceiling+y, z))
            blocks.place(ORANGE_WOOL, rpos(length-2+x_start, ceiling+y, z))
            y += 1
