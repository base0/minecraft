def on_item_interacted():
    global center2, p1, p2, x1, x2, z1, z2, radius, cx, cz
    center2 = player.position()
    player.teleport(world(-304, 97, 223))
    loops.pause(5*1000)
    #player.say(center2)
    #player.say(perim)
    p1 = center2
    p2 = perim
    x1 = p1.get_value(Axis.X)
    x2 = p2.get_value(Axis.X)
    z1 = p1.get_value(Axis.Z)
    z2 = p2.get_value(Axis.Z)
    radius = ((x1 - x2) ** 2 + (z1 - z2) ** 2) ** 0.5
    player.say(radius)
    cx = x1
    cz = z1
    y = center2.get_value(Axis.Y)
    for j in [0, 2]:
        i = 0
        while i <= len(sins) - 1 - 1:
            x1 = coss[i] * (radius - j)
            z1 = sins[i] * (radius - j)
            x2 = coss[i + 1] * (radius - j)
            z2 = sins[i + 1] * (radius - j)
            shapes.line(OAK_WOOD_SLAB,
                world(cx + x1, y, cz + z1),
                world(cx + x2, y, cz + z2))
            i += 1
    
    i = 2
    while i < len(sins):
        x1 = coss[i] * (radius + 5)
        z1 = sins[i] * (radius +5)
        for k in range(10):
            blocks.clone(world(-344, 62+k, 136), world(-350, 62+k, 129), world(cx+x1, y+k, cz+z1), CloneMask.REPLACE, CloneMode.NORMAL)
        i += 2

def on_item_interacted2():
    global perim
    perim = player.position()
    #player.say(perim)
cz = 0
cx = 0
radius = 0
z2 = 0
z1 = 0
x2 = 0
x1 = 0
p2: Position = None
p1: Position = None
center2: Position = None
perim: Position = None
sins: List[number] = []
coss: List[number] = []
coss = [6.123233995736766e-17,
 -0.1950903220161282,
 -0.3826834323650897,
 -0.555570233019602,
 -0.7071067811865475,
 -0.8314696123025453,
 -0.9238795325112868,
 -0.9807852804032305,
 -1.0,
 -0.9807852804032302,
 -0.9238795325112863,
 -0.8314696123025445,
 -0.7071067811865464,
 -0.5555702330196007,
 -0.3826834323650879,
 -0.19509032201612606]
sins = [1.0,
 0.9807852804032304,
 0.9238795325112867,
 0.8314696123025455,
 0.7071067811865476,
 0.5555702330196022,
 0.38268343236508945,
 0.19509032201612772,
 -7.657137397853899e-16,
 -0.19509032201612922,
 -0.3826834323650909,
 -0.5555702330196034,
 -0.7071067811865487,
 -0.8314696123025462,
 -0.9238795325112875,
 -0.9807852804032309]
center = player.position()
perim = player.position()
player.on_item_interacted(GOLDEN_HOE, on_item_interacted)
player.on_item_interacted(IRON_HOE, on_item_interacted2)
