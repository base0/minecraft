# https://youtu.be/SNcw9wZYEqc

heart = [
    '00110001100',
    '01111011110',
    '11111111111',
    '11111111111',
    '01111111110',
    '00111111100',
    '00011111000',
    '00001110000',
    '00000100000'
        ]

margin = 2

def rose(left, top):
    left += margin
    top += margin
    for x in range(len(heart[0])):
        for z in range(len(heart)):
            if heart[z][x] == '1':
                gnd = positions.ground_position(world(x+left, 100, z+top))
                if blocks.test_for_block(GRASS, positions.add(gnd, pos(0,-1,0))):
                    blocks.place(ROSE_BUSH, gnd)

def go(left, top, right, bottom):
    for x in range(left, right, len(heart[0]) + margin*2):
        for z in range(top, bottom, len(heart) + margin*2):
            player.say(x + ' ' + z)
            rose(x, z)

def on_travelled_fly():
    player.say(player.position())
player.on_travelled(FLY, on_travelled_fly)



