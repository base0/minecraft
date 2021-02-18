# https://youtu.be/Zu7EaYRFkK0

ref  = 24000
player.teleport(world(756, 75, ref+171))
tpos = player.position()
player_position = tpos


def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))

def star():
    blocks.fill(BLACK_CONCRETE, rpos(-2,-1,0), rpos(1,-1,2))
    blocks.place(blocks.repeater(WEST, 4), rpos(0,0,0))
    blocks.place(blocks.repeater(EAST, 4), rpos(0,0,2))
    blocks.place(blocks.repeater(NORTH, 4), rpos(1,0,1))
    blocks.place(blocks.repeater(SOUTH, 4), rpos(-1,0,1))
    blocks.place(REDSTONE_WIRE, rpos(-1,0,2))
    blocks.place(REDSTONE_WIRE, rpos(1,0,2))
    blocks.place(REDSTONE_WIRE, rpos(-1,0,0))
    blocks.place(REDSTONE_WIRE, rpos(1,0,0))
    blocks.place(REDSTONE_TORCH, rpos(-2,0,0))
    loops.pause(1)
    blocks.place(AIR, rpos(-2,0,0))
    blocks.place(REDSTONE_LAMP, rpos(0,-1,0))

#player.teleport(world(835, 75, ref+143))
gameplay.set_weather(CLEAR)
#gameplay.time_set(DayTime.Day)
gameplay.time_set(DayTime.Night)
for r in range(20):
    for c in range(10):
    
        player_position = positions.add(tpos, pos(r*20+randint(0,8), 40+randint(0,5), c*20+randint(0,8)))
        
        star()
























