# https://youtu.be/coQzNR_-R9Y
player_position = player.position()

def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))

def infinite_repeater():
    blocks.place(blocks.repeater(WEST, 4), rpos(0,0,0))
    blocks.place(REDSTONE_WIRE, rpos(1,0,0))
    blocks.place(blocks.repeater(WEST, 4), rpos(2,0,0))
    blocks.place(REDSTONE_WIRE, rpos(3,0,0))
    blocks.place(REDSTONE_WIRE, rpos(3,0,1))
    blocks.place(REDSTONE_WIRE, rpos(3,0,2))
    blocks.place(REDSTONE_WIRE, rpos(2,0,2))
    blocks.place(REDSTONE_WIRE, rpos(1,0,2))
    blocks.place(REDSTONE_WIRE, rpos(0,0,2))
    blocks.place(REDSTONE_WIRE, rpos(-1,0,2))
    blocks.place(REDSTONE_WIRE, rpos(-1,0,1))
    blocks.place(REDSTONE_WIRE, rpos(-1,0,0))
    blocks.place(REDSTONE_TORCH, rpos(-2,0,0))
    loops.pause(10)
    blocks.place(AIR, rpos(-2,0,0))
    blocks.place(PISTON, rpos(0,0,3))







while True:
    player_position = positions.add(player_position, pos(7,0,0))
    infinite_repeater()























'''
blocks.place(blocks.repeater(WEST, 4), pos(0,0,0))
blocks.place(REDSTONE_WIRE, pos(1,0,0))
blocks.place(blocks.repeater(WEST, 4), pos(2,0,0))
blocks.place(REDSTONE_WIRE, pos(3,0,0))
blocks.place(REDSTONE_WIRE, pos(3,0,1))
blocks.place(REDSTONE_WIRE, pos(3,0,2))
blocks.place(REDSTONE_WIRE, pos(2,0,2))
blocks.place(REDSTONE_WIRE, pos(1,0,2))
blocks.place(REDSTONE_WIRE, pos(0,0,2))
blocks.place(REDSTONE_WIRE, pos(-1,0,2))
blocks.place(REDSTONE_WIRE, pos(-1,0,1))
blocks.place(REDSTONE_WIRE, pos(-1,0,0))
blocks.place(REDSTONE_TORCH, pos(-2,0,0))
loops.pause(10)
blocks.place(AIR, pos(-2,0,0))
blocks.place(PISTON, pos(0,0,3))
'''
