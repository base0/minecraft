player_position = player.position()
gameplay.time_set(DayTime.Night)

plan = ['010',
 '101',
 '101']

t = []
for i in range(len(plan)):
    t.append(plan[len(plan) - i - 1])
plan = t

coss = [0.9238795325112867,
    0.38268343236508984,
    -0.3826834323650897,
    -0.9238795325112867,
    -0.9238795325112868,
    -0.38268343236509034,
    0.38268343236508917,
    0.9238795325112865]

sins = [0.3826834323650898,
    0.9238795325112867,
    0.9238795325112867,
    0.3826834323650899,
    -0.38268343236508967,
    -0.9238795325112865,
    -0.923879532511287,
    -0.3826834323650904]

def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))

def web():
    for radius in [5, 9, 13, 17]:
        Radius = radius / sins[0]
        for i in range(len(coss)):
            cx = coss[i] * Radius
            cz = sins[i] * Radius
            cy = 0
            shapes.circle(WHITE_CONCRETE, rpos(cx, cy, cz), radius, Axis.Y, ShapeOperation.OUTLINE)
            cx = coss[i] * (Radius+2)
            cz = sins[i] * (Radius+2)
            shapes.circle(AIR, rpos(cx, cy, cz), radius, Axis.Y, ShapeOperation.REPLACE)


    Radius = 17 / sins[0]
    shapes.line(WHITE_CONCRETE, rpos(-Radius, 0, 0), rpos(Radius,0,0))
    shapes.line(WHITE_CONCRETE, rpos(0,0,-Radius), rpos(0,0,Radius))
    c = 0.7071067811865476
    shapes.line(WHITE_CONCRETE, rpos(-Radius*c,0,-Radius*c), rpos(Radius*c,0,Radius*c))
    shapes.line(WHITE_CONCRETE, rpos(Radius*c,0,-Radius*c), rpos(-Radius*c,0,Radius*c))


def spider(n):
    for i in range(n):
        mobs.spawn(SPIDER, rpos(0,1,0))

def teleport():
    player.teleport(pos(500, 0, 0))

player.on_chat("w", web)
player.on_chat("s", spider)
player.on_chat("t", teleport)
