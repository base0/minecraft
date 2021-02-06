# https://youtu.be/N8FvKCuULBQ
    
gameplay.time_add(12*1000)
agent.teleport(world(1000, 0, 0), WEST)

def clear(n):
    y=4
    blocks.fill(GRASS,
        world(-n, 0, -n),
        world(n, n, n),
        FillOperation.REPLACE)
    blocks.fill(AIR,
        world(-n, y, -n),
        world(n, n, n),
        FillOperation.REPLACE)

def sphere(r):
    y = 4
    shapes.sphere(GLASS, world(0, y-1, 0), r, ShapeOperation.OUTLINE)
    blocks.fill(GRASS,
        world(-r, 0, -r),
        world(r, y - 1, r),
        FillOperation.REPLACE)


player.on_chat("s", sphere)
player.on_chat("c", clear)

