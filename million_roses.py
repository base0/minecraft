# https://youtu.be/XnlcA0YbVUE

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

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def total_roses():
    s = 0
    for c in count:
        s += c
    return s

def rose(left, top, index):
    global count
    left += margin
    top += margin
    for x in range(len(heart[0])):
        for z in range(len(heart)):
            if heart[z][x] == '1':
                gnd = positions.ground_position(world(x+left, 100, z+top))
                if blocks.test_for_block(GRASS, positions.add(gnd, pos(0,-1,0))):
                    blocks.place(ROSE_BUSH, gnd)
                    count[index] += 15
                    player.say(total_roses())

def go(left, top, right, bottom, index):
    for x in range(left, right, len(heart[0]) + margin*2):
        for z in range(top, bottom, len(heart) + margin*2):
            rose(x, z, index)


def on_travelled_fly():
    player.say(player.position())
    #pass
player.on_travelled(FLY, on_travelled_fly)


def on_run_in_background0():
    go(  0, 0, 15, 100000, 0)
def on_run_in_background1():
    go( 15, 0, 30, 100000, 1)
def on_run_in_background2():
    go( 30, 0, 45, 100000, 2)
def on_run_in_background3():
    go( 45, 0, 60, 100000, 3)
def on_run_in_background4():
    go( 60, 0, 75, 100000, 4)
def on_run_in_background5():
    go( 75, 0, 90, 100000, 5)
def on_run_in_background6():
    go( 90, 0,105, 100000, 6)
def on_run_in_background7():
    go(105, 0,120, 100000, 7)
def on_run_in_background8():
    go(120, 0,135, 100000, 8)
def on_run_in_background9():
    go(135, 0,150, 100000, 9)
    
loops.run_in_background(on_run_in_background0)
loops.run_in_background(on_run_in_background1)
loops.run_in_background(on_run_in_background2)
loops.run_in_background(on_run_in_background3)
loops.run_in_background(on_run_in_background4)
loops.run_in_background(on_run_in_background5)
loops.run_in_background(on_run_in_background6)
loops.run_in_background(on_run_in_background7)
loops.run_in_background(on_run_in_background8)
loops.run_in_background(on_run_in_background9)
