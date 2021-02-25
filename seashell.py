gameplay.time_set(DayTime.Day)
gameplay.set_weather(CLEAR)

player_position = player.position()
player.teleport(pos(0,0,20))

def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))
    
def on_chat():
    player.teleport(pos(0, 0, 500))
player.on_chat("t", on_chat)

N = 5

def summon():
    while True:
        loops.pause(500)
        mobs.spawn(TROPICAL_FISH, rpos(0, N, 0))
loops.run_in_background(summon)

r = 6
z = 0
for i in range(N):
    shapes.circle(GRASS, rpos(0, N-i, z), r, Axis.Y, ShapeOperation.OUTLINE)
    shapes.circle(GRASS, rpos(0, N-i-1, z), r, Axis.Y, ShapeOperation.REPLACE)
    shapes.line(AIR,rpos(-r,N-i,z+r), rpos(r,N-i,z+r))
    shapes.line(AIR,rpos(-r,N-i,z+r-1), rpos(r,N-i,z+r-1))
    shapes.circle(WATER, rpos(0, N-i, z), r-1, Axis.Y, ShapeOperation.OUTLINE)
    z += r // 2
    r = r * 3 // 2
