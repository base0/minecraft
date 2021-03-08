N = 10
blocks.fill(STONE, pos(0, 0, 0+3), pos(N*2, 2, 2+3))
for i in range(N):
    blocks.place(AIR,pos(i*2+1, 1, 1+3))
    blocks.place(GLASS,pos(i*2+1, 1, 0+3))
    mobs.spawn(CAT, pos(i*2+1, 1, 1+3))
