# https://youtu.be/G-Jsk5IjE4I 

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

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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
                blocks.place(ROSE_BUSH, world(x+left, 4, z+top))
                count[index] += 15
                player.say(total_roses())

def go(left, top, right, bottom, index):
    for x in range(left, right, len(heart[0]) + margin*2):
        for z in range(top, bottom, len(heart) + margin*2):
            rose(x, z, index)

def on_run_in_background():
    global a  
    global b
    go(a, 0, b, 100000, 0)

for i in range(len(count)):    
    a = 15 * i
    b = 15 * (i+1)
    loops.run_in_background(on_run_in_background)
    loops.pause(1000)
