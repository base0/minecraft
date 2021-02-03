# https://youtu.be/-xXtd4XRypw

def building(w, material):
    y = 4
    if material == 0:
        material = GLASS
    else:
        material = SEA_LANTERN
    for i in range(y, w+y):
        blocks.fill(material, world(-w, i, -w), world(w, i, w), FillOperation.HOLLOW)
        blocks.fill(AIR, world(-w+1, i, -w+1), world(w-1, i, w-1), FillOperation.REPLACE)
    blocks.fill(material, world(-w+1, w+y, -w+1), world(w-1, w+y, w-1), FillOperation.REPLACE)

def water(w):
    y = 4
    blocks.fill(WATER, world(-w+1, w+y, -w+1), world(w-1, w+4, w-1), FillOperation.REPLACE)

def rect(t, l, r, b, y, material):
    if material == 1:
        material = SEA_LANTERN
    else:
        material = SOUL_SAND
    shapes.line(material, world(l, y, t), world(r, y, t))
    shapes.line(material, world(r, y, t), world(r, y, b))
    shapes.line(material, world(r, y, b), world(l, y, b))
    shapes.line(material, world(l, y, b), world(l, y, t))

def summon(number):
    for i in range(number):
        #mobs.spawn(SEA_TURTLE, pos(0, 9, 0))
        #mobs.spawn(SQUID, world(0, 9, 0))
        #mobs.spawn(PUFFERFISH, pos(0, 30, 0))
        mobs.spawn(TROPICAL_FISH, pos(0, 9, 0))

def rectangle(w, y, m):
    y += 4
    rect(-w, -w, w, w, y, m)
    
def clear():
    blocks.fill(AIR, world(-20, 4, -20), world(20, 20, 20), FillOperation.REPLACE)

player.on_chat("c", clear)
player.on_chat("b", building)
player.on_chat('r',  rectangle)
player.on_chat('w',  water)
player.on_chat('s', summon)

agent.teleport(pos(100, 0, 0), WEST)
