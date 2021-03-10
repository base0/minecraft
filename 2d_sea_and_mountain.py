# https://youtu.be/anz3mgNw8VA
gameplay.time_set(DayTime.Day)

player_position = player.position()
player.teleport(pos(18, 20, -34))

def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))

for i in range(4):
    for j in range(5):
        radius = 5
        ss = 0
        ss = radius if i % 2 == 0 else 0
        shapes.circle(WATER, rpos(j*radius*2+ss, i*radius, i*3), radius, Axis.Z, ShapeOperation.REPLACE)

xs = [16,0,15,-5]
ws = [15,20,25,30]
ys = [23,25, 35, 40]
for i in range(3):
    z = 4*3+i
    shapes.circle(GRASS_PATH, rpos(xs[i]+ws[i]//2, ys[i], z), ws[i]//2, Axis.Z, ShapeOperation.REPLACE)
    shapes.circle(STONE, rpos(xs[i]+ws[i]//2, ys[i], z), ws[i]//2, Axis.Z, ShapeOperation.OUTLINE)
    blocks.fill(GRASS_PATH, rpos(xs[i], 0, z), rpos(xs[i]+ws[i], ys[i], z))
