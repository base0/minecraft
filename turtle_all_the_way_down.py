# https://youtu.be/3AT3mS0k5iQ
ground = 3
gameplay.time_set(DayTime.Day)
#player.teleport(world(10, ground, 0))

t = [['222200','222200','222200','222200','222200'],
     ['222200','222200','222211','222200','222200'],
     ['100100','000000','000000','000000','100100'],]


def f(b, x, y, z, dim, top, left):
  for i in range(dim):
      for j in range(dim):
          for k in range(dim):
              blocks.place(b, world(left + x*dim+i, ground + top - y*dim-j, z*dim+k))


def build(dim, top, left):
    for y in range(len(t)):
        for x in range(len(t[y])):
            for z in range(len(t[y][x])):
                if t[y][x][z] == '0':
                    b = AIR
                elif t[y][x][z] == '2':
                    b = GREEN_TERRACOTTA
                elif t[y][x][z] == '1':
                    b = LIME_TERRACOTTA
                f(b, x, y, z, dim, top, left)

def turtle_all_the_way(total_turtle):
    width = total_turtle * 5
    for i in range(total_turtle):
        h = 0
        for j in range(i, total_turtle):
            h += (j+1)*3
        player.say(h)
        build(i+1, h, (width - (i+1)*5)//2)

def wall():
    for i in range(4, 6+9+12 +4 ):
        blocks.fill(GLASS, world(-6, i, -13), world(26, i, 32), FillOperation.HOLLOW)
        blocks.fill(AIR, world(-5, i, -12), world(25, i, 31), FillOperation.REPLACE)

def water():
    blocks.fill(WATER, world(-5, 30, -12), world(25, 30, 31), FillOperation.REPLACE)

def summon_turtle(number):
    for i in range(number):
        mobs.spawn(SEA_TURTLE, pos(0, 0, 0))

player.on_chat("wall", wall)
player.on_chat("water", water)
player.on_chat("t", turtle_all_the_way)
player.on_chat("s", summon_turtle)



