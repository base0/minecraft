sin60 = 0.866
cos60 = 0.5
tan60 = 1.73205

sin30 = 0.5
cos30 = 0.866
tan30 = 0.57735026918962576450914878

gameplay.time_set(DayTime.Day)
player_position = player.position()
#player.teleport(pos(-20, 8, 20))

def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))

def triangle(top, base_width, x, b):
    h_base = base_width // 2
    r = h_base / sin30
    shapes.line(b, rpos(x, top, 0), rpos(x, top-r*sin60, h_base))
    shapes.line(b, rpos(x, top, 0), rpos(x, top-r*sin60, -h_base))
    shapes.line(b, rpos(x, top-r*sin60, -h_base), rpos(x, top-r*sin60, h_base))

top = 13
length = 7
bottom = 7
ceiling = bottom
roof(top, bottom, 0, length, 0, -1) # 0 -1 means no skip

lower_roof = 3
for i in range(lower_roof):
    blocks.fill(YELLOW_WOOL, rpos(-1-i,bottom-i,-4-i), rpos(-1+8+i,bottom-i,4+i), FillOperation.OUTLINE)

min_x = -1-lower_roof-1
max_x = -1+8-lower_roof-1+4
min_z = -4-lower_roof-1
max_z = 4+lower_roof-1
for i in range(5):
    #blocks.fill(BROWN_WOOL, rpos(min_x+2,+bottom-i-lower_roof,min_z+2), rpos(min_x+3,bottom-i-lower_roof,min_z+3), FillOperation.OUTLINE)
    #blocks.fill(BROWN_WOOL, rpos(min_x+2,+bottom-i-lower_roof,max_z-3), rpos(min_x+3,bottom-i-lower_roof,max_z-2), FillOperation.OUTLINE)
    #blocks.fill(BROWN_WOOL, rpos(max_x-2,+bottom-i-lower_roof,min_z+2), rpos(max_x-3,bottom-i-lower_roof,min_z+3), FillOperation.OUTLINE)
    #blocks.fill(BROWN_WOOL, rpos(max_x-2,+bottom-i-lower_roof,max_z-3), rpos(max_x-3,bottom-i-lower_roof,max_z-2), FillOperation.OUTLINE)
    blocks.fill(BROWN_WOOL, rpos(min_x+4,+bottom-i-lower_roof,min_z+4), rpos(min_x+4,bottom-i-lower_roof,min_z+4), FillOperation.OUTLINE)
    blocks.fill(BROWN_WOOL, rpos(min_x+4,+bottom-i-lower_roof,max_z-2), rpos(min_x+4,bottom-i-lower_roof,max_z-2), FillOperation.OUTLINE)
    blocks.fill(BROWN_WOOL, rpos(max_x,+bottom-i-lower_roof,min_z+4), rpos(max_x,bottom-i-lower_roof,min_z+4), FillOperation.OUTLINE)
    blocks.fill(BROWN_WOOL, rpos(max_x,+bottom-i-lower_roof,max_z-2), rpos(max_x,bottom-i-lower_roof,max_z-2), FillOperation.OUTLINE)

blocks.fill(STONE_BRICKS, rpos(min_x+2, -1, min_z), rpos(max_x+2, -1, max_z))


def roof(top, bottom, x_start, length, skip_start, skip_end):
    # roof
    h_base = (top-bottom) * tan30
    base_width = h_base*2
    ceiling = bottom +1

    for i in range(x_start, x_start+length):
        if skip_start <= i <= skip_end:
            continue
        if i == x_start or i == x_start+length-1:
            b = BLOCK_OF_QUARTZ
        else:
            b = YELLOW_WOOL
        triangle(top, base_width, i, b)

    #shapes.line(BLOCK_OF_QUARTZ, rpos(0+x_start, top, 0), rpos(length-1+x_start, top, 0))
    #shapes.line(BLOCK_OF_QUARTZ, rpos(0+x_start, ceiling, -h_base), rpos(length-1+x_start, ceiling, -h_base))
    #shapes.line(BLOCK_OF_QUARTZ, rpos(0+x_start, ceiling, h_base), rpos(length-1+x_start, ceiling, h_base))

    # gable
    for z in range(-h_base+2,h_base-1):
        y = 1
        while blocks.test_for_block(AIR, rpos(1+x_start, ceiling+y, z)):
            blocks.place(BLOCK_OF_QUARTZ, rpos(1+x_start, ceiling+y, z))
            blocks.place(BLOCK_OF_QUARTZ, rpos(length-2+x_start, ceiling+y, z))
            y += 1
