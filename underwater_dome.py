# https://youtu.be/e4Lkrw7t_e8
    
def sphere(r):
    y = 4
    shapes.sphere(GLASS, world(0, y-1, 0), r, ShapeOperation.OUTLINE)
    blocks.fill(GRASS,
        world(-r, 0, -r),
        world(r, y - 1, r),
        FillOperation.REPLACE)

def wall(w):
    for i in range(4, w*2):
        blocks.fill(GLASS, world(-w, i, -w), world(w, i, w), FillOperation.HOLLOW)
        blocks.fill(AIR, world(-w+1, i, -w+1), world(w-1, i, w-1), FillOperation.REPLACE)

def water(w):
    blocks.fill(WATER, world(-w+1, w*2, -w+1), world(w-1, w*2, w-1), FillOperation.REPLACE)

def summon(number):
    for i in range(number):
        #mobs.spawn(SEA_TURTLE, pos(0, 30, 0))
        mobs.spawn(TROPICAL_FISH, pos(0, 30, 0))
        #mobs.spawn(PUFFERFISH, pos(0, 30, 0))

player.on_chat("wall", wall)
player.on_chat("water", water)
player.on_chat("summon", summon)
player.on_chat("sphere", sphere)
agent.teleport(pos(100, 0, 0), WEST)
