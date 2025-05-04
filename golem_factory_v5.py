ROW = 20
COL = 4
'''
# 1. run this part first
for i in range(ROW):
    for j in range(COL):
        x = j * 4 + 1
        z = i * 2 + 1
        blocks.place(IRON_BLOCK, pos(x, 0, z))
        blocks.place(IRON_BLOCK, pos(x, 1, z))
        blocks.place(IRON_BLOCK, pos(x-1, 1, z))
        blocks.place(IRON_BLOCK, pos(x+1, 1, z))
'''
# 2. then run this 
# agent must be at the leftmost golem of the front row
agent.turn(LEFT_TURN)
agent.turn(LEFT_TURN)
agent.move(UP, 2)
agent.set_item(JACK_O_LANTERN, 64, 1)
for i in range(ROW):
    for j in range(COL):
        agent.place(FORWARD)
        if i % 2 == 0:
            agent.move(RIGHT, 4)
        else:
            agent.move(LEFT, 4)
    agent.move(FORWARD, 2)
    if i % 2 == 0:
        agent.move(LEFT, 4)
    else:
        agent.move(RIGHT, 4)
