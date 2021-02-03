a = [['111','001', '111', '111', '101', '111', '111', '111', '111', '111'],
     ['101','001', '001', '001', '101', '100', '100', '001', '101', '101'],
     ['101','001', '111', '111', '111', '111', '111', '001', '111', '111'],
     ['101','001', '100', '001', '001', '001', '101', '001', '101', '001'],
     ['111','001', '111', '111', '001', '111', '111', '001', '111', '111']]
     
def pos(x, y, z):
    return f'{x} {y} {z}'

def draw_d(n, x, y, z):
    for i in range(len(a)):
        for j in range(len(a[i][n])):
            b = 'air'
            if a[i][n][j] == '1':
                b = 'slime'
            world.set(pos(x+j, y-i, z), b)

def destroy(n, x, y, z):
    for i in range(len(a)):
        for j in range(len(a[i][n])):
            b = 'air'
            if a[i][n][j] == '1':
                b = 'slime'
            world.fill(pos(x+j, y-i, z), pos(x+j, y-i, z), b, 'destroy')

from datetime import datetime
import time

xs = [0, 4, 10, 14]

TOP = 10

world.set(pos(8, TOP - 1, 0), 'slime')
world.set(pos(8, TOP - 3, 0), 'slime')

now = datetime.now()
h = now.hour
m = now.minute
digits = [h//10, h%10, m//10, m%10]
for d, x in zip(digits, xs):
    draw_d(d, x, TOP, 0)
    
prev_digits = [d for d in digits]
while True:
    now = datetime.now()
    h = now.hour
    m = now.minute
    digits = [h//10, h%10, m//10, m%10]
    #say(' '.join([str(d) for d in prev_digits]))
    #say(' '.join([str(d) for d in digits]))
    for d, pd, x in zip(digits, prev_digits, xs):
        if d != pd:
            destroy(pd, x, TOP, 0)
            draw_d(d, x, TOP, 0)
    prev_digits = [d for d in digits]
    time.sleep(10)
