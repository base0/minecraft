# https://www.tiktok.com/@craft_of_code/video/6930861464022420738

gameplay.set_weather(CLEAR)

player_position = player.position()
#player.teleport(offset(88, 49, -34))

def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))

cx = 0
cy = 0
cz = 11
radius = 5
dr = 3
N = 5
shapes.circle(WATER, rpos(cx,cy+1,cz), radius + (N-1)*dr, Axis.Y, ShapeOperation.REPLACE)
for i in range(N):
    if i == 1:
        for j in range(50):
            mobs.spawn(TROPICAL_FISH, rpos(cx, cy, cz))
    shapes.circle(STONE_BRICKS, rpos(cx,cy,cz), radius, Axis.Y, ShapeOperation.OUTLINE)
    if i == 0:
        loops.pause(20000)
    shapes.circle(STONE_BRICKS, rpos(cx,cy+1,cz), radius, Axis.Y, ShapeOperation.OUTLINE)

    if i % 4 == 0:
        dx = (radius-dr)
        dz = 0
    elif i % 4 == 1:
        dx = 0
        dz = (radius-dr)
    elif i % 4 == 2:
        dx = -(radius-dr)
        dz = 0
    else:
        dx = 0
        dz = -(radius-dr)
        
    blocks.place(WATER, rpos(cx+dx, cy+1, cz+dz))            
    blocks.place(WATER, rpos(cx+dx, cy, cz+dz))            
    radius += dr
        
