# https://youtu.be/5HwyshXx2tk
player_pos = player.position()

def offset(x, y, z):
    global player_pos
    return positions.add(player_pos, world(x, y, z))

y = 0
def on_travelled_walk():
    global y
    for i in range(3):
        blocks.place(GLASS, offset(1+y, y, -1))
        blocks.place(GLASS, offset(1+y, y, 0))
        blocks.place(GLASS, offset(1+y, y, 1))
        y += 1

player.on_travelled(WALK, on_travelled_walk)

