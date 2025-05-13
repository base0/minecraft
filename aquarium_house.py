def on_on_chat():
    pass
player.on_chat("run", on_on_chat)

def rect(b, x1, z1, x2, z2, y):
    shapes.line(b, pos(x1, y, z1), pos(x1, y, z2))
    shapes.line(b, pos(x1, y, z1), pos(x2, y, z1))
    shapes.line(b, pos(x2, y, z2), pos(x1, y, z2))
    shapes.line(b, pos(x2, y, z2), pos(x2, y, z1))

def rect2(b, x, z, y):
    rect(b, -x, -z, x, z, y)

gameplay.time_set(gameplay.time(DAY))

#rect2(SOUL_SAND, 6, 6, -1)
for i in range(5):
    rect2(GLASS, 5, 5, i)
    rect2(GLASS, 8, 8, i)
    rect2(WATER, 6, 6, i)
    rect2(WATER, 7, 7, i)
rect2(GLASS, 5, 5, 5)
rect2(GLASS, 8, 8, 5)
#rect2(MAGMA_BLOCK, 6, 6, 4)
#blocks.place(SOUL_SAND, pos(-6, -1, -6))
blocks.place(SOUL_SAND, pos(-6, -1,  6))
for index in range(30):
    mobs.spawn(TROPICAL_FISH, pos(6, 1, 6))
    #mobs.spawn(PUFFERFISH, pos(0, 0, 0))

        #mobs.spawn(PUFFERFISH, pos(0, 0, 0))
# blocks.fill(GLASS, pos(7, -1, 7), pos(-7, 5, -7), FillOperation.OUTLINE)
# blocks.fill(GLASS, pos(9, -1, 9), pos(-9, 7, -9), FillOperation.OUTLINE)
# blocks.fill(WATER, pos(8, 6, 8), pos(-8, 6, -8), FillOperation.REPLACE)
# blocks.fill(WATER, pos(8, 5, 8), pos(-8, 5, -8), FillOperation.OUTLINE)
# blocks.fill(GLASS, pos(7, 1, 7), pos(-7, 1, -7), FillOperation)
# blocks.fill(WATER, pos(8, 1, 8), pos(-8, 1, -8), FillOperation.OUTLINE)
#blocks.fill(GLASS, pos(9, 1, 9), pos(-9, 1, -9), FillOperation.HOLLOW)
# blocks.fill(WATER, pos(8, 1, 9), pos(-8, 1, -8), FillOperation.HOLLOW)
# blocks.fill(GLASS, pos(7, 1, 7), pos(-7, 1, -7), FillOperation.HOLLOW)
