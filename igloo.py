
player_position = player.position()

plan = ['010',
 '101',
 '101']

t = []
for i in range(len(plan)):
    t.append(plan[len(plan) - i - 1])
plan = t


def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))

def igloo():
    blocks.fill(SNOW, rpos(5, -1, -5), rpos(15, -5, 5))
    blocks.fill(AIR, rpos(5, 0, -5), rpos(15, 5, 5))
    shapes.sphere(ICE, rpos(10, 0, 0), 5, ShapeOperation.OUTLINE)
    blocks.place(AIR, rpos(10, 5, 0))
    blocks.place(GLOWSTONE, rpos(10, -1, 0))
    blocks.fill(ICE, rpos(9, 0, -5), rpos(10, 1, 5))
    blocks.fill(AIR, rpos(9, 0, -4), rpos(10, 1, 4))
    for x in [6,5]:
        for y in range(len(plan)):
            for z in range(len(plan[0])):
                b = AIR
                if plan[y][z] == '1':
                    b = ICE
                blocks.place(b, rpos(x, y, z-len(plan[0])//2))

player.teleport(pos(-6, 22, 15))
ref_pos = player_position
for c in range(3):
    gameplay.set_weather(CLEAR)
    gameplay.time_set(DayTime.Night)
    for r in range(3):
        player_position = positions.add(ref_pos, pos(c * 15, 0, r * 15))
        igloo()

loops.pause(15)
gameplay.set_weather(RAIN)
