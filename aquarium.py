# https://youtu.be/CJpNyCCU464

num1 = 10
blocks.fill(GLASS,
    world(0, 0, 0),
    world(num1, num1, num1),
    FillOperation.REPLACE)
blocks.fill(AIR,
    world(1, 1, 1),
    world(num1 - 1, num1, num1 - 1),
    FillOperation.REPLACE)
blocks.fill(SOUL_SAND,
    world(1, 1, 1),
    world(num1 - 1, 1, num1 - 1),
    FillOperation.REPLACE)
blocks.fill(BLOCK_OF_QUARTZ,
    world(2, 1, 2),
    world(num1 - 2, 1, num1 - 2),
    FillOperation.REPLACE)
blocks.fill(WATER,
    world(1, 2, 1),
    world(num1 - 1, num1, num1 - 1),
    FillOperation.REPLACE)
for i in range(20):
    mobs.spawn(TROPICAL_FISH, world(3, 3, 3))
    
