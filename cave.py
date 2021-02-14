

def on_item_interacted():
    z = 10
    x = 3
    blocks.fill(AIR, pos(0, 0, 0), pos(0, 1, z))
    blocks.place(OAK_DOOR, pos(0,0,1))
    agent.teleport(pos(0, 0, 0), SOUTH)
    agent.interact(FORWARD)
    agent.teleport(pos(0, 0, -100), SOUTH)
    blocks.fill(AIR, pos(-x, 0, z), pos(x, 3, z+x*2))
    for i in [-x, x]:
        for j in [z, z+x*2]:
            blocks.place(TORCH, pos(i,1,j))
player.on_item_interacted(DIAMOND_HOE, on_item_interacted)
