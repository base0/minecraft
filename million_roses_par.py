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

a = [world(0,0,0)]
a.pop()

def scan(left, top, right, bottom):
    a.append(world(0,0,0))
    a.pop()
    for t in range(top, bottom, len(heart) + margin*2):
        for l in range(left, right, len(heart[0]) + margin*2):
            #player.say(l + ' ' + t)
            l += margin
            t += margin
            for x in range(len(heart[0])):
                for z in range(len(heart)):
                    if heart[z][x] == '1':
                        gnd = positions.ground_position(world(x+l, 150, z+t))
                        if blocks.test_for_block(GRASS, positions.add(gnd, pos(0,-1,0))):
                           a.append(gnd)
                           if len(a) % 1000 == 0:
                               player.say(len(a))
                           if len(a) > 1000000 / 15 :
                               return

def place(index):
    player.teleport(a[0])
    for i in range(index, len(a), 10):
        blocks.place(ROSE_BUSH, a[i])



def onRun_in_background0():
    place(0)

def onRun_in_background1():
    place(1)

def onRun_in_background2():
    place(2)

def onRun_in_background3():
    place(3)

def onRun_in_background4():
    place(4)

def onRun_in_background5():
    place(5)

def onRun_in_background6():
    place(6)

def onRun_in_background7():
    place(7)

def onRun_in_background8():
    place(8)

def onRun_in_background9():
    place(9)

def gggg():
    x = -270
    z = -60
    scan(x, z, x + 13*10, 1000000)
    loops.run_in_background(onRun_in_background0)
    loops.run_in_background(onRun_in_background1)
    loops.run_in_background(onRun_in_background2)
    loops.run_in_background(onRun_in_background3)
    loops.run_in_background(onRun_in_background4)
    loops.run_in_background(onRun_in_background5)
    loops.run_in_background(onRun_in_background6)
    loops.run_in_background(onRun_in_background7)
    loops.run_in_background(onRun_in_background8)
    loops.run_in_background(onRun_in_background9)

def on_travelled_fly():
    player.say(player.position())
    #pass
player.on_travelled(FLY, on_travelled_fly)

#gggg()
