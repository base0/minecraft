gameplay.set_weather(CLEAR)

player_position = player.position()
#player.teleport(offset(88, 49, -34))

def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))
