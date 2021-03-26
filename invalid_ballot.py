# https://www.tiktok.com/@craft_of_code/video/6943836589399346433

# spoilt, spoiled, void, null, informal, invalid or stray ballot
# breadth first search

plan=['00000000000000001','00000000000000010','00000000000000110','00000000000001100','00000000000011000','00000000000110000','00011000001110000','00111100011100000','00011110111000000','00001111110000000','00000111110000000','00000111100000000','00000011000000000','00000010000000000','00000000000000000','00000000000000000','00000000000000000',],

gameplay.set_weather(CLEAR)
player.teleport(pos(0, 0, -100))
loops.pause(1000)
a : List[List[number]] = []
b : List[number] = []
for i in range(len(plan)):
    b = []
    for j in range(len(plan[i])):
        b.append(int(plan[i][j]))
    a.append(b)

q : List[List[number]] = []
q2 : List[List[number]] = []
q.append([6,3])
a[6][3] = 0
while len(q) > 0:
    add(q[0][0]+1, q[0][1])
    add(q[0][0]-1, q[0][1])
    add(q[0][0], q[0][1]-1)
    add(q[0][0], q[0][1]+1)
    q2.append(q[0])
    q.remove_at(0)
#player.say(len(q2))

def add(r, c):
    if a[r][c] != 0:
        q.append([r, c])
        a[r][c] = 0

N = 15
sx = -16
sz = -50
sy = 33
blocks.fill(YELLOW_CONCRETE, pos(sx,sy,sz), pos(sx+N, sy-N,sz))
blocks.fill(AIR, pos(sx+2,sy-2,sz), pos(sx+N-2, sy-N+2,sz))

loops.pause(500)

for p in q2:
    #player.say(p)
    blocks.place(BLUE_CONCRETE, pos(sx+p[1], sy - p[0], sz))

loops.pause(1500)

sy = 16
blocks.fill(YELLOW_CONCRETE, pos(sx,sy,sz), pos(sx+N, sy-N,sz))
blocks.fill(AIR, pos(sx+2,sy-2,sz), pos(sx+N-2, sy-N+2,sz))

loops.pause(500)

shapes.line(BLUE_CONCRETE, pos(sx+2, sy-2, sz), pos(sx+N-2, sy-N+2, sz))
shapes.line(BLUE_CONCRETE, pos(sx+2, sy-N+2, sz), pos(sx+N-2, sy-2, sz))
