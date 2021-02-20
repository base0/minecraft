
# https://youtu.be/VXjNlY2ULGg

gameplay.set_weather(CLEAR)

player_position = player.position()
#player.teleport(offset(88, 49, -34))

def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))

cx = 0
cy = 0
cz = 11
radius = 5

plan = [
    '00000000000003',
    '00000000000003',
    '00000000000003',
    '00000000000003',
    '00000000000003',
    '00000000000003',
    '00000000000001',
    '00000000000001',
    '00000000000001',
    '00000000000001',
    '00000000000010',
    '00000000000010',
    '00000000000010',
    '00000000000010',
    '00000000000100',
    '00000000000100',
    '00000000000100',
    '00000000000100',
    '00000000001000',
    '00000000001000',
    '00000000001000',
    '00000000001000',
    '00000000010000',
    '00000000010000',
    '00000000010000',
    '00000000020000',
    '00000000020000',
    '00000001000000',
    '00000010000000',
    '00000010000000',
    '00000100000000',
    '00001000000000',
    '00001000000000',
    '00001000000000',
    '00010000000000',
    '00100000000000',
    '00100000000000',
    '00100000000000',
    '02000000000000',
    '20000000000000',
    '20000000000000',
    ]

t = []
for i in range(len(plan)):
    t.append(plan[len(plan) - i - 1])
plan = t

cx = len(plan[0])
cz = cx + 20
for y in range(len(plan)):
    if y == 1:
        loops.pause(20000)
    i = 0
    while plan[y][i] == '0':
        i+=1
    if plan[y][i] == '2':
        blocks.fill(GOLD_BLOCK, 
                    rpos(cx-(len(plan[0])-i), y, cz-(len(plan[0])-i)), 
                    rpos(cx+(len(plan[0])-i), y, cz+(len(plan[0])-i)))
    elif plan[y][i] == '1':
        shapes.circle(GOLD_BLOCK, rpos(cx, y, cz), len(plan[0])-i, Axis.Y, ShapeOperation.REPLACE)
    else:
        blocks.place(GOLD_BLOCK, rpos(cx, y, cz))
