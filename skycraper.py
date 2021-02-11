# https://youtu.be/5g46_MTbch4

player_position = player.position()
player.say(player_position)
player.teleport(pos(-33, 79, 9))
flr = [
    '100000000000002001',
    '100000000000020001',
    '100000000000200001',
    '111000011111111111',
]

t = []
for i in range(len(flr)):
    t.append(flr[len(flr) - i - 1])
flr = t

even_flr = []
for i in range(len(flr)):
    s = ''
    for j in range(len(flr[i])):
        tmp = flr[i]
        s += tmp[len(tmp) - 1 - j]
    even_flr.append(s)

TOTAL_FLOOR = 20
DEPTH = 5
for FL in range(TOTAL_FLOOR):
    for x in range(DEPTH):
        for y in range(len(flr)):
            for z in range(len(flr[0])):
                b = AIR
                if x == 0:
                    b = BRICKS
                elif x < 3:
                    if FL % 2 == 0:
                        if flr[y][z] != '0':
                            b = BRICKS
                    else:
                        if even_flr[y][z] != '0':
                            b = BRICKS
                else:
                    if y == 0:
                        b = BRICKS
                    else:
                        if FL % 2 == 0:
                            if flr[y][z] == '1':
                                b = BRICKS
                        else:
                            if even_flr[y][z] == '1':
                                b = BRICKS

                blocks.place(b, positions.add(player_position, world(-x, FL * len(flr) + y, z)))

