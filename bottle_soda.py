# https://youtu.be/IGgET81vDP4
player_position = player.position()

gameplay.set_weather(CLEAR)
gameplay.time_set(23000) # dawn
#gameplay.time_add(7*1000)
player.teleport(pos(-54, 47, 40))

loops.pause(1000)

plan=['0000000000002222222','0000000000021000011','0000000000020000011','0000000000020000011','0000000000002000011','0000000000002000011','0000000000001000011','0000000000020000011','0000000000020000011','0000000000002000011','0000000000002000011','0000000000002000011','0000000000020000011','0000000000020000011','0000000000210000011','0000000002100000011','0000000021000000011','0000000210000000011','0000002100000000011','0000021000000000011','0000210000000000011','0000200000000000011','0002000000000000011','0020000000000000011','0020000000000000011','0200000000000000011','0200000000000000011','2100000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2000000000000000011','2100000000000000011','2100000000000000011','0200000000000000011','0200000000000000011','0200000000000000011','0200000000000000011','0210000000000000011','0020000000000000011','0020000000000000011','0021000000000000011','0002000000000000011','0002000000000000011','0000200000000000011','0000022221122222221',],



def rpos(x, y, z):
    global player_position
    return positions.add(player_position, pos(x, y, z))

t = []
for i in range(len(plan)):
    t.append(plan[len(plan) - i - 1])
plan = t

#cx = 0len(plan[0])
#cz = cx + 20
for y in range(len(plan)):
    #if y == 1:
        #    loops.pause(20*1000)
    i = 0
    while plan[y][i] == '0':
        i+=1

    radius = len(plan[0])-i
    loops.run_in_background(onRun_in_background)
    loops.pause(10)

def onRun_in_background():
    shapes.circle(GLASS, rpos(0, y, 0), radius, Axis.Y, ShapeOperation.OUTLINE)

# water
for y in range(51, 62):
    water(y)

# ice
for i in range(20):
    blocks.place(BLUE_ICE, rpos(randint(-5, 5),61, randint(-5, 5)))

# soda bubble
i = 0
while plan[len(plan)-2][i] == '0':
    i+=1
radius = len(plan[0])-i-1
shapes.circle(SOUL_SAND, rpos(0, 1, 0), radius, Axis.Y, ShapeOperation.REPLACE)

def water(y):

    i = 0
    while plan[y][i] == '0':
        i+=1
    radius = len(plan[0])-i-1
    shapes.circle(WATER, rpos(0, y, 0), radius, Axis.Y, ShapeOperation.REPLACE)


