gameplay.time_set(DayTime.Night)


loops.pause(5*1000)
for z in range(-5, 5):
    for x in range(10):
        loops.pause(100)
        #blocks.clone(world(-2, 4, -2), world(2, 8, 2), pos(0, 0, 10), CloneMask.REPLACE, CloneMode.NORMAL)
        blocks.clone(world(-2, 4, -2), world(2, 8, 2), pos(x*7+10, 0, z*7), CloneMask.REPLACE, CloneMode.NORMAL)
def teleport():
    player.teleport(pos(1000, 0, 0))

#player.on_chat("l", lantern)
player.on_chat("t", teleport)
