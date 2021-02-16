gameplay.set_weather(CLEAR)

player_position = player.position()
#player.teleport(offset(88, 49, -34))

def rpos(x, y, z):
    return positions.add(player_position, pos(x, y, z))

plan = [
    '010',
    '101',
    '101'
    ]

t = []
for i in range(len(plan)):
    t.append(plan[len(plan) - i - 1])
plan = t
