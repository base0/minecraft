sin60 = 0.866
cos60 = 0.5
tan60 = 1.73205

sin30 = 0.5
cos30 = 0.866
tan30 = 0.57735026918962576450914878

gameplay.time_set(DayTime.Day)
player_position = player.position()
player.teleport(pos(41, 19, -39))

def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))

def triangle(top, base_width, x, b):
    h_base = base_width // 2
    r = h_base / sin30
    shapes.line(b, rpos(x, top, 0), rpos(x, top-r*sin60, h_base))
    shapes.line(b, rpos(x, top, 0), rpos(x, top-r*sin60, -h_base))
    shapes.line(b, rpos(x, top-r*sin60, -h_base), rpos(x, top-r*sin60, h_base))

top = 28
length = 22
bottom = 8
ceiling = bottom
roof(top, bottom, 0, length, 0, -1) # 0 -1 means no skip
roof(top-3, bottom, -4, length + 8, 1, length-2)

#roof(top, bottom, 0, 6, 0, -1) # 0 -1 means no skip
#roof(top-3, bottom, -4, 6 + 8, 1, 5-1)

#base_width = 20
#h_base = base_width // 2
#r = h_base / sin30
#ceiling = top-r*sin60

def roof(top, bottom, x_start, length, skip_start, skip_end):
    # roof
    h_base = (top-bottom) * tan30
    base_width = h_base*2
    ceiling = bottom +1

    for i in range(x_start, x_start+length):
        if skip_start <= i <= skip_end:
            continue
        if i == x_start or i == x_start+length - 1:
            b = BLOCK_OF_QUARTZ
        elif i == x_start+1 or i == x_start+length - 2:
            b = GREEN_WOOL
        else:
            b = ORANGE_WOOL
        triangle(top, base_width, i, b)

    shapes.line(BLOCK_OF_QUARTZ, rpos(0+x_start, top, 0), rpos(length-1+x_start, top, 0))
    shapes.line(BLOCK_OF_QUARTZ, rpos(0+x_start, ceiling, -h_base), rpos(length-1+x_start, ceiling, -h_base))
    shapes.line(BLOCK_OF_QUARTZ, rpos(0+x_start, ceiling, h_base), rpos(length-1+x_start, ceiling, h_base))

    # chor fah
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 4), rpos(-1+x_start,top,0))
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 4), rpos(-1+x_start,top+1,0))
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 1), rpos(0+x_start,top+1,0))
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 1), rpos(-1+x_start,top+2,0))
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 0), rpos(-1+x_start,top+3,0))

    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 5), rpos(length+x_start,top,0))
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 5), rpos(length+x_start,top+1,0))
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 0), rpos(length-1+x_start,top+1,0))
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 0), rpos(length+x_start,top+2,0))
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 1), rpos(length+x_start,top+3,0))

    # gable
    for z in range(-h_base+2,h_base-1):
        y = 1
        while blocks.test_for_block(AIR, rpos(1+x_start, ceiling+y, z)):
            blocks.place(ORANGE_WOOL, rpos(1+x_start, ceiling+y, z))
            blocks.place(ORANGE_WOOL, rpos(length-2+x_start, ceiling+y, z))
            y += 1
'''
h_base = (top-3-bottom) * tan30
box(h_base, -4, length+4)

def box(h_base, x_start, length):
    # wall
    x_end = length - x_start
    blocks.fill(BLOCK_OF_QUARTZ, rpos(1+x_start, 0, -h_base+1), rpos(x_end-2, ceiling, h_base-1), FillOperation.HOLLOW)
    blocks.fill(BLOCK_OF_QUARTZ, rpos(0+x_start, 0, -h_base), rpos(x_end-1, 1, h_base), FillOperation.HOLLOW)


# window
x = 4+x_start
while x < length -2-x_start:
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 2), rpos(x, 3, -h_base+1))
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 2), rpos(x+1, 3, -h_base+1))
    blocks.place(AIR, rpos(x, 4, -h_base+1))
    blocks.place(AIR, rpos(x+1, 4, -h_base+1))
    blocks.place(AIR, rpos(x, 5, -h_base+1))
    blocks.place(AIR, rpos(x+1, 5, -h_base+1))
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 6), rpos(x, 6, -h_base+1))
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 6), rpos(x+1, 6, -h_base+1))

    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 3), rpos(x, 3, h_base-1))
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 3), rpos(x+1, 3, h_base-1))
    blocks.place(AIR, rpos(x, 4, h_base-1))
    blocks.place(AIR, rpos(x+1, 4, h_base-1))
    blocks.place(AIR, rpos(x, 5, h_base-1))
    blocks.place(AIR, rpos(x+1, 5, h_base-1))
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 7), rpos(x, 6, h_base-1))
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 7), rpos(x+1, 6, h_base-1))

    x += 4

# door
x = length-2-x_start
blocks.fill(AIR, rpos(x,2,-2), rpos(x, 5, 2))
blocks.place(AIR, rpos(x, 6,-1))
blocks.place(AIR, rpos(x, 6,0))
blocks.place(AIR, rpos(x, 6,1))
blocks.place(AIR, rpos(x, 7,0))

# QUARTZ_STAIRS
for z in range(-2,3):
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 1), rpos(length-1-x_start, 1, z))
    #blocks.place(BLOCK_OF_QUARTZ, rpos(0, 1, z))
    blocks.place(blocks.block_with_data(QUARTZ_STAIRS, 1), rpos(length-x_start, 0, z))

# ceiling
gameplay.time_set(DayTime.Night)
x = 4+x_start
while x < length -2-x_start:
    blocks.place(GLOWSTONE, rpos(x, ceiling, -h_base+3))
    blocks.place(GLOWSTONE, rpos(x+1, ceiling, -h_base+3))
    blocks.place(GLOWSTONE, rpos(x, ceiling, h_base-3))
    blocks.place(GLOWSTONE, rpos(x+1, ceiling, h_base-3))
    x += 4

zz = -h_base + 4
while zz < h_base - 4:
    blocks.place(GLOWSTONE, rpos(length - 4-x_start, ceiling, zz))
    blocks.place(GLOWSTONE, rpos(length - 4-x_start, ceiling, zz+1))
    zz += 4

'''
