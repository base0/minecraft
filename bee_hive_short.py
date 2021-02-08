# https://youtu.be/P4xN5A2i5rY

hive = [
    '0002000',
    '1120211',
    '1200021',
    '2000002',
    '2000002',
    '2000002',
    '0211120',
    '0021200',
    '0002000',
    '0002000',
    '0002000',
        ]

t = []
for i in range(len(hive)):
    t.append(hive[len(hive) - i-1])
hive = t


#gameplay.time_set(10*1000)

ROW = 8
COL = 12    # COL = 1.5 * ROW

DEPTH = 4

p = player.position()
for top in range(ROW):
    for left in range(COL):
        for x in range(DEPTH):
            for y in range(len(hive)):
                for z in range(len(hive[0])):
                    b = BROWN_WOOL
                    if x != 0:
                        if hive[y][z] == '1':
                            b = BROWN_WOOL
                        elif hive[y][z] == '2':
                            b = GLOWSTONE
                        else:
                            b = AIR
                    blocks.place(b, positions.add(p, world(-x, top * len(hive)  - top + y, left * len(hive[0]) - left + z)))

for top in range(ROW):
    for left in range(COL):
        y = 0
        z = 0
        mobs.spawn(BEE, positions.add(p, world(1, top * len(hive) - top + y, left * len(hive[0]) - left + z)))
        y = 6
        z = 0
        mobs.spawn(BEE, positions.add(p, world(1, top * len(hive) - top + y, left * len(hive[0]) - left + z)))
        y = 4
        z = 6
        mobs.spawn(BEE, positions.add(p, world(1, top * len(hive) - top + y, left * len(hive[0]) - left + z)))


