# https://youtu.be/arzfL8sLIJI

p_position = player.position()


def rpos(x: number, y: number, z: number):
    return positions.add(p_position, pos(x, y, z))

def f(x: number, z: number):
    shapes.line(OAK_FENCE, rpos(x, 0, z), rpos(x, 0, z+10))
    shapes.line(OAK_FENCE, rpos(x+10, 0, z+10), rpos(x, 0, z+10))
    shapes.line(OAK_FENCE, rpos(x+10, 0, z+10), rpos(x+10, 0, z))
    shapes.line(OAK_FENCE, rpos(x, 0, z), rpos(x+10, 0, z))
    for i in range(10):
        mobs.spawn(SHEEP, rpos(x + 5, 0, z+5))


player.teleport(pos(29, 24, -2))
for r in range(5):
    for c in range(5):
        f(r*12, c*12)
