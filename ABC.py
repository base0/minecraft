# https://youtu.be/Kqrc535JFik

char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

gameplay.time_set(DayTime.Day)
i = 0
last_z = player.position().get_value(Axis.Z)
def on_travelled_walk():
    global i
    global last_z
    z = player.position().get_value(Axis.Z)
    #player.say('z' + z)
    #player.say(last_z)
    if  z % 20 == 0 and z != last_z:
        blocks.print(char[i], YELLOW_CONCRETE, pos(1, 1, 20), WEST)
        last_z = z
        i += 1
        

player.on_travelled(WALK, on_travelled_walk)
