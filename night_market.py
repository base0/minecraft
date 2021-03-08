# https://youtu.be/4Xv1EvZBLRE

sin60 = 0.866
cos60 = 0.5
tan60 = 1.73205

sin30 = 0.5
cos30 = 0.866
tan30 = 0.57735026918962576450914878

gameplay.time_set(DayTime.Night)
player_position = player.position()

player.teleport(pos(-14, 32, 1))
# people
for r in range(10):
    for c in range(10):
        x_start = 15+r*10
        z_start = 15+c*10
        mobs.spawn(VILLAGER, spos(0, 0, 0))
# pause
#loops.pause(10*1000)

def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))

x_start = 0
z_start = 0
def spos(x, y, z):
    return positions.add(player_position, pos(x+x_start, y, z+z_start))

# road
for i in range(-2, 12):
    zz = 10*i
    blocks.fill(STONE_BRICKS, rpos(-6,-1,zz), rpos(6,-1,9+zz))
    shapes.line(BLOCK_OF_QUARTZ, rpos(0,-1,0+zz), rpos(0,-1,1+zz))
    shapes.line(BLOCK_OF_QUARTZ, rpos(0,-1,5+zz), rpos(0,-1,6+zz))

    blocks.fill(STONE_BRICKS, rpos(zz,-1,-6), rpos(9+zz,-1,6))
    shapes.line(BLOCK_OF_QUARTZ, rpos(0+zz,-1,0), rpos(1+zz,-1,0))
    shapes.line(BLOCK_OF_QUARTZ, rpos(5+zz,-1,0), rpos(6+zz,-1,0))

blocks.fill(STONE_BRICKS, rpos(-6,-1,-6), rpos(6,-1,6))

# zebra lane
for i in range(5):
    if i % 2 == 0:
        b = BLOCK_OF_QUARTZ
    else:
        b = STONE_BRICKS
    blocks.fill(b, rpos(1-6+(i*2),-1,-7), rpos(1-6+(i*2)+1,-1,-11))
    blocks.fill(b, rpos(1-6+(i*2),-1,7), rpos(1-6+(i*2)+1,-1,11))
    blocks.fill(b, rpos(7,-1,1-6+(i*2)), rpos(11,-1,1-6+(i*2)+1))
    blocks.fill(b, rpos(-7,-1,1-6+(i*2)), rpos(-11,-1,1-6+(i*2)+1))

# footpath
for i in range(60):
    blocks.fill(STONE_BRICKS, rpos(8,0,7+(i*2)), rpos(10,0,7+(i*2)+1))
    blocks.fill(STONE_BRICKS, rpos(7+(i*2),0,8), rpos(7+(i*2)+1,0,10))

for i in range(60):
    if i % 2 == 0:
        b = RED_WOOL
    else:
        b = BLOCK_OF_QUARTZ    
    blocks.fill(b, rpos(7,0,7+(i*2)), rpos(7,0,7+(i*2)+1))
    blocks.fill(b, rpos(7+(i*2),0,7), rpos(7+(i*2)+1,0,7))

# tents
for r in range(20):
    for c in range(10):
        x_start = 15+r*12
        z_start = 15+c*12
        tent()
def tent():
    p_y = 3
    HEIGHT = 3
    a = [RED_WOOL, GREEN_WOOL, YELLOW_WOOL, PINK_WOOL, CYAN_WOOL, MAGENTA_WOOL, LIME_WOOL, LIGHT_BLUE_WOOL, PURPLE_WOOL]
    r = randint(0,len(a)-1)
    for i in range(HEIGHT+1):
        blocks.fill(a[r], spos(-(HEIGHT-i), p_y+i, -(HEIGHT-i)), spos(HEIGHT-i, p_y+i, HEIGHT-i))
    for i in range(1,HEIGHT+1):
        blocks.fill(GLOWSTONE, spos(-(HEIGHT-i), p_y+i-1, -(HEIGHT-i)), spos(HEIGHT-i, p_y+i-1, HEIGHT-i))
    
    shapes.line(BLOCK_OF_QUARTZ, spos(-HEIGHT, 0, -HEIGHT),spos(-HEIGHT, HEIGHT, -HEIGHT))
    shapes.line(BLOCK_OF_QUARTZ, spos(-HEIGHT, 0, HEIGHT),spos(-HEIGHT, HEIGHT, HEIGHT))
    shapes.line(BLOCK_OF_QUARTZ, spos(HEIGHT, 0, HEIGHT),spos(HEIGHT, HEIGHT, HEIGHT))
    shapes.line(BLOCK_OF_QUARTZ, spos(HEIGHT, 0, -HEIGHT),spos(HEIGHT, HEIGHT, -HEIGHT))



'''
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

'''
