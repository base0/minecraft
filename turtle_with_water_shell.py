# https://youtu.be/hJLD3yX5148

gameplay.time_set(DayTime.Day)

t = [['00000','20000','22200','20000','00000'],
     ['00000','11100','11111','11100','00000',],
     ['10100','00000','00000','00000','10100'],]

player_position = player.position()

def rpos(x,y,z):
    return positions.add(player_position, world(x,y,z))

def f(b, x, y, z, dim, top, left):
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                blocks.place(b, rpos(left + x*dim+i, top - y*dim-j, z*dim+k))


def build(dim, top, left):
    
    for y in range(len(t)):
        for x in range(len(t[y])):
            for z in range(len(t[y][x])):
                if t[y][x][z] == '0':
                    b = AIR
                elif t[y][x][z] == '2':
                    b = WATER
                elif t[y][x][z] == '1':
                    b = LIME_TERRACOTTA
                f(b, x, y, z, dim, top, left)


def turtle_all_the_way(total_turtle):
    player.teleport(pos(23, 18, 18))
    width = total_turtle * len(t[0])
    for i in range(total_turtle):
        h = 0
        for j in range(i, total_turtle):
            h += (j+1)*3
        player.say(h)
        build(i+1, h-1, (width - (i+1)*len(t[0]))//2)

def bg():
    total_turtle = 3
    while True:
        loops.pause(10*1000)
        h = 0
        for j in range(total_turtle):
            h += (j+1)*3
        width = total_turtle * len(t[0])
        mobs.spawn(SEA_TURTLE, rpos(width//2, h-1, 4))


loops.run_in_background(bg)


player.on_chat("t", turtle_all_the_way)




