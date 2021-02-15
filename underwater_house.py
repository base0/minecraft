# https://youtu.be/BYXTgNNIjBw
def on_item_interacted():
    z = 10
    x = 4
    blocks.fill(AIR, pos(0, 0, 0), pos(0, 1, z))
    blocks.place(OAK_DOOR, pos(0,0,1))
    agent.teleport(pos(0, 0, 0), SOUTH)
    agent.interact(FORWARD)
    agent.teleport(pos(0, 0, -100), SOUTH)
    blocks.fill(AIR, pos(-x, 0, z), pos(x, 3, z+x*2))
    for i in [-x, x]:
        for j in [z, z+x*2]:
            blocks.place(TORCH, pos(i,1,j))
    #glass room
    blocks.fill(AIR,   pos(-3,  0, 1), pos(-5, 2, 4))
    blocks.fill(GLASS, pos(-3,  0, 1), pos(-6, 2, 1))
    blocks.place(GLOWSTONE, pos(-4,3,3))
    # tunnel
    blocks.fill(AIR, pos(-x+1, 0, z), pos(-x+1, 1, 3))

    for k in range(50):
        mobs.spawn(TROPICAL_FISH, pos(-5, 0, -2))

player.on_item_interacted(DIAMOND_HOE, on_item_interacted)

def on_chat():
    blocks.fill(AIR, pos(-6,0,0), pos(1, 3, 7))
player.on_chat("c", on_chat)
