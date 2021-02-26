gameplay.time_set(DayTime.Day)
gameplay.set_weather(CLEAR)

player_position = player.position()
#player.teleport(offset(88, 49, -34))

def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))

plan = [
    '010',
    '101',
    '101'
    ]

t = []
for i in range(len(plan)):
    t.append(plan[len(plan) - i - 1])
plan = t


def rect(b, x1, z1, x2, z2, y):
    blocks.fill(b, rpos(x1,y,z1), rpos(x2,y,z2))
    blocks.fill(AIR, rpos(x1+1,y,z1+1), rpos(x2-1,y,z2-1))

def octagon_outline(b, x1, z1, x2, z2, y, c):
    a = [rpos(x1+c,y,z1), rpos(x2-c,y,z1), rpos(x2,y,z1+c), rpos(x2,y,z2-c), rpos(x2-c,y,z2),rpos(x1+c,y,z2),rpos(x1,y,z2-c),rpos(x1,y,z1+c)]
    a.append(a[0])
    for i in range(len(a)-1):
        shapes.line(b, a[i], a[i+1])
        
def octagon_fill(b, x1, z1, x2, z2, y, c):
    blocks.fill(b, pos(x1, y, z1), pos(x2,y,z2))
    for i in range(c):
        shapes.line(AIR, rpos(x1, y, z1+i), rpos(x1+i, y, z1))
        shapes.line(AIR, rpos(x2, y, z1+i), rpos(x2-i, y, z1))
        shapes.line(AIR, rpos(x2, y, z2-i), rpos(x2-i, y, z2))
        shapes.line(AIR, rpos(x1, y, z2-i), rpos(x1+i, y, z2))
