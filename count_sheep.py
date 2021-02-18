# https://youtu.be/6mZUbJA_zCA

char = ['1', '2', '3', '4','5','6','7','8','9','10']
gameplay.time_set(DayTime.Day)
gameplay.set_weather(CLEAR)
i = 0
last_z = player.position().get_value(Axis.Z)
def on_travelled_walk():
    global i
    global last_z
    z = player.position().get_value(Axis.Z)
    #player.say('z' + z)
    if  z % 30 == 0 and z != last_z:
        blocks.print(char[i], YELLOW_CONCRETE, pos(-1, 1, -20), EAST)
        for j in range(i+1):
            mobs.spawn(SHEEP, pos(-5+j,1,-14))
        last_z = z
        i += 1

        

player.on_travelled(WALK, on_travelled_walk)
