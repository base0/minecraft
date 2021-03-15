# https://youtu.be/U7fIiiiBHoo

gameplay.time_set(DayTime.Day)
gameplay.set_weather(CLEAR)

player_position = player.position()
#player.teleport(offset(88, 49, -34))

def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))


plan=['0000011111100000','0001100000111000','0010000000011100','0100000110001110','0100000110001111','1000000000011111','1000000000011111','1000000000111111','1000001111111111','1000011111111111','1000011111111111','0100111001111110','0100111001111110','0010011111111100','0001111111111000','0000011111100000',],
t = []
for i in range(len(plan)):
    t.append(plan[len(plan) - i - 1])
plan = t

DISTANCE = 30

def tile():
    cz = len(plan[0]) // 2
    for y in range(len(plan)):
        for z in range(len(plan[0])):
            if plan[y][z] == '1':
                blocks.place(GLOWSTONE, rpos(DISTANCE,y+2, z-cz))

def level_mountain():
    for i in range(2,DISTANCE):
        blocks.fill(AIR, rpos(i, 0, -20), rpos(i,40, 20))
    for i in range(20):
        mobs.spawn(VILLAGER,rpos(DISTANCE-randint(1,20), 0, randint(-10,10)))

gameplay.time_set(DayTime.Day)
player.teleport(pos(0, 0, 18))
loops.pause(1000)
level_mountain()
loops.pause(1000)
gameplay.time_set(DayTime.Night)
tile()

#player.on_chat("l", level_mountain)
#player.on_chat("t", tile)

