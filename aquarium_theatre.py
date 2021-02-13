# https://youtu.be/VFgj0ymK7VU
# inspired by Sydney aquarium

blocks.fill(BRICKS, pos(-12, 0, 1), pos(18, 10, 20), FillOperation.OUTLINE)

blocks.fill(BRICKS,  pos(-30, 0, 20), pos(40, 20, 30), FillOperation.OUTLINE)
blocks.fill(GLASS,  pos(-12, 0, 20), pos(18, 10, 20), FillOperation.OUTLINE)

blocks.fill(AIR,  pos(-30, 20, 21), pos(40, 20, 23), FillOperation.OUTLINE)
blocks.fill(WATER,  pos(-29, 0, 21), pos(39, 19, 29), FillOperation.REPLACE)
blocks.fill(SEA_LANTERN,  pos(-29, 0, 25), pos(39, 19, 25), FillOperation.REPLACE)
blocks.fill(GLOWSTONE,  pos(-29, -1, 23), pos(39, -1, 23), FillOperation.REPLACE)
'''
for i in range(-29, 40):
    if i % 8 == 0:
        blocks.place(SOUL_SAND, pos(i, -1, 24))
'''
for i in range(40):
    mobs.spawn(SALMON, pos(0, 5, 21))
    mobs.spawn(DOLPHIN, pos(0, 5, 21))
    mobs.spawn(SEA_TURTLE, pos(0, 5, 21))
    mobs.spawn(PUFFERFISH, pos(0, 5, 21))
    mobs.spawn(TROPICAL_FISH, pos(0, 5, 21))

for i in range(12):

    mobs.spawn(VILLAGER, pos(-10 + i * 2, 2, 19))

player.teleport(pos(0, 1, 5))
