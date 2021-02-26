gameplay.set_weather(CLEAR)
gameplay.time_set(DayTime.Day)

def on_chat():
    player.teleport(pos(0, 0, 500))
player.on_chat("t", on_chat)
# https://youtu.be/VXjNlY2ULGg

gameplay.set_weather(CLEAR)
gameplay.time_set(DayTime.Night)
player_position = player.position()
#player.teleport(offset(88, 49, -34))

def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))

cx = 0
cy = 0
cz = 11
radius = 5

plan = [
    '000000000000000000000000003',
    '000000000000000000000000003',
    '000000000000000000000000003',
    '000000000000000000000000003',
    '000000000000000000000000001',
    '000000000000000000000000001',
    '000000000000000000000000001',
    '000000000000000000000000001',
    '000000000000000000000000010',
    '000000000000000000000000010',
    '000000000000000000000000010',
    '000000000000000000000000010',
    '000000000000000000000000100',
    '000000000000000000000000100',
    '000000000000000000000000100',
    '000000000000000000000000100',
    '000000000000000000000001000',
    '000000000000000000000001000',
    '000000000000000000000001000',
    '000000000000000000000001000',
    '000000000000000000000010000',
    '000000000000000000000010000',
    '000000000000000000000010000',
    '000000000000000000000010000',
    '000000000000000000000200000',
    '000000000000000000000020000',
    '000000000000000000000200000',
    '000000000000000000000010000',
    '000000000000000000000100000',
    '000000000000000000010000000',
    '000000000000000001000000000',
    '000000000000000010000000000',
    '000000000000000100000000000',
    '000000000000001000000000000',
    '000000000000001000000000000',
    '000000000000010000000000000',
    '000000000000010000000000000',
    '000000000000100000000000000',
    '000000000000100000000000000',
    '000000000001000000000000000',
    '000000000001000000000000000',
    '000000000010000000000000000',
    '000000000010000000000000000',
    '000000000100000000000000000',
    '000000001000000000000000000',
    '000000100000000000000000000',
    '000001000000000000000000000',
    '000010000000000000000000000',
    '002000000000000000000000000',
    '020000000000000000000000000',
    '200000000000000000000000000',
    ]

t = []
for i in range(len(plan)):
    t.append(plan[len(plan) - i - 1])
plan = t

for i in range(100):
    mobs.spawn(VILLAGER, rpos(-20,0,-20))

cx = len(plan[0])
cz = cx + 20
for y in range(len(plan)):
    if y == 1:
        loops.pause(20*1000)

    i = 0
    while plan[y][i] == '0':
        i+=1

    radius = len(plan[0])-i
    if plan[y][i] == '2':
        octagon(GOLD_BLOCK,cx-radius, cz-radius,
                           cx+radius, cz+radius, y, radius*2*3//10)
    elif plan[y][i] == '1':
        shapes.circle(GOLD_BLOCK, rpos(cx, y, cz), radius, Axis.Y, ShapeOperation.REPLACE)
        blocks.place(GLOWSTONE, rpos(cx-radius, y, cz))
        blocks.place(GLOWSTONE, rpos(cx+radius, y, cz))
        blocks.place(GLOWSTONE, rpos(cx, y, cz-radius))
        blocks.place(GLOWSTONE, rpos(cx, y, cz+radius))
    else:
        blocks.place(GOLD_BLOCK, rpos(cx, y, cz))

def octagon(b, x1, z1, x2, z2, y, c):
    blocks.fill(b, rpos(x1, y, z1), rpos(x2,y,z2))
    for i in range(c):
        shapes.line(AIR, rpos(x1, y, z1+i), rpos(x1+i, y, z1))
        shapes.line(AIR, rpos(x2, y, z1+i), rpos(x2-i, y, z1))
        shapes.line(AIR, rpos(x2, y, z2-i), rpos(x2-i, y, z2))
        shapes.line(AIR, rpos(x1, y, z2-i), rpos(x1+i, y, z2))

octagon(GOLD_BLOCK, 0,0,6,6,10,2)
