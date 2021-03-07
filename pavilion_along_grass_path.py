# https://youtu.be/AoYZbwQdwMg

sin60 = 0.866
cos60 = 0.5
tan60 = 1.73205

sin30 = 0.5
cos30 = 0.866
tan30 = 0.57735026918962576450914878

gameplay.time_set(DayTime.Night)
player_position = player.position()

player.teleport(pos(10, 17, -7))
for i in range(3):
    mobs.spawn(VILLAGER,rpos(randint(-10,10),0,randint(10,50)))
    mobs.spawn(HORSE,rpos(randint(-10,10),0,randint(10,50)))
    mobs.spawn(COW,rpos(randint(-10,10),0,randint(10,50)))
loops.pause(10*1000)

def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))

x_start = 0
z_start = 0
def spos(x, y, z):
    return positions.add(player_position, pos(x+x_start, y, z+z_start))

for i in range(10):
    zz = 10*i
    blocks.fill(GRASS_PATH, rpos(-5,-1,zz), rpos(2,-1,9+zz))
for i in range(6):
    x_start = -7
    z_start = 15*i
    pavilion()

def pavilion():
    global z_start
    size = 13
    blocks.fill(GRASS_PATH, spos(0, -1, 0), spos(-size+1, -1, size-1))
    # pillar
    p_y = 6
    shapes.line(BROWN_WOOL, spos(-2,0,2), spos(-2,p_y,2))
    shapes.line(BROWN_WOOL, spos(-2,0,size-3), spos(-2,p_y,size-3))
    shapes.line(BROWN_WOOL, spos(-size+3,0,2), spos(-size+3,p_y,2))
    shapes.line(BROWN_WOOL, spos(-size+3,0,size-3), spos(-size+3,p_y,size-3))
    #shapes.line(BROWN_WOOL, spos(2,0,-size+2), spos(2,p_y,-size+2))
    # pyramid
    p_height = 3
    p_y += 1
    for i in range(p_height):
        blocks.fill(BROWN_WOOL, spos(0-i,p_y+i,0+i), spos(-size+1+i,p_y+i,size-1-i), FillOperation.OUTLINE)
    # light
    blocks.place(GLOWSTONE, spos((-size+1)//2, p_y, (size-1)//2))
    blocks.place(GLOWSTONE, spos((-size+1)//2, p_y, 1+(size-1)//2))
    blocks.place(GLOWSTONE, spos((-size+1)//2, p_y, -1+(size-1)//2))
    top = 15
    length = 7
    bottom = 9
    ceiling = bottom 
    z_start += 6
    roof(top, bottom, -2-length, length, 0, -1) # 0 -1 means no skip


def triangle(top, base_width, x, b):
    h_base = base_width // 2
    r = h_base / sin30
    shapes.line(b, spos(x, top, 0), spos(x, top-r*sin60, h_base))
    shapes.line(b, spos(x, top, 0), spos(x, top-r*sin60, -h_base))
    shapes.line(b, spos(x, top-r*sin60, -h_base), spos(x, top-r*sin60, h_base))




def roof(top, bottom, start, length, skip_start, skip_end):
    # roof
    h_base = (top-bottom) * tan30
    base_width = h_base*2
    ceiling = bottom +1

    for i in range(start, start+length):
        if skip_start <= i <= skip_end:
            continue
        if i == start or i == start+length-1:
            b = BLOCK_OF_QUARTZ
        else:
            b = BROWN_WOOL
        triangle(top, base_width, i, b)

    # gable
    '''
    for z in range(-h_base+2,h_base-1):
        y = 1
        while blocks.test_for_block(AIR, spos(1+x_start, ceiling+y, z)):
            blocks.place(BLOCK_OF_QUARTZ, spos(1+x_start, ceiling+y, z))
            blocks.place(BLOCK_OF_QUARTZ, spos(length-2+x_start, ceiling+y, z))
            y += 1
    '''
