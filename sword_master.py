# https://youtu.be/S70g5bEo4dE

gameplay.time_set(DayTime.Night)
gameplay.set_weather(CLEAR)
agent.teleport(pos(100, 0, 0), WEST)

def on_item_interacted():
    blocks.clone(world(140, 64, 48), world(140, 70, 71), pos(-2, 0, 3), CloneMask.REPLACE, CloneMode.NORMAL)
player.on_item_interacted(IRON_SWORD, on_item_interacted)

for i in range(100):
    mobs.spawn(ZOMBIE, pos(randint(-30, 30), 0, randint(-30, 30)))
