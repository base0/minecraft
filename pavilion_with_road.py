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
    mobs.spawn(VILLAGER,rpos(randint(-10,10),0,randint(10,30)))
    mobs.spawn(HORSE,rpos(randint(-10,10),0,randint(10,30)))
    mobs.spawn(COW,rpos(randint(-10,10),0,randint(10,30)))
loops.pause(10*1000)

x_start = 0
z_start = 0
def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))

def spos(x, y, z):
    return positions.add(player_position, pos(x+x_start, y, z+z_start))

for i in range(40):
    zz = 10*i
    blocks.fill(STONE_BRICKS, rpos(-6,-1,zz), rpos(6,-1,9+zz))
    shapes.line(BLOCK_OF_QUARTZ, rpos(0,-1,0+zz), rpos(0,-1,1+zz))
    shapes.line(BLOCK_OF_QUARTZ, rpos(0,-1,5+zz), rpos(0,-1,6+zz))

#for i in range(5):
x_start = -7
z_start = 20  #+30*i
pavilion()

def pavilion():
    global z_start
    size = 13
    blocks.fill(STONE_BRICKS, spos(0, -1, 0), spos(-size+1, -1, size-1))
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
        blocks.fill(YELLOW_WOOL, spos(0-i,p_y+i,0+i), spos(-size+1+i,p_y+i,size-1-i), FillOperation.OUTLINE)
    blocks.place(GLOWSTONE, spos((-size+1)//2, p_y, (size-1)//2))
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

'''
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
'''



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
            b = YELLOW_WOOL
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
