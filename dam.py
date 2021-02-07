# https://youtu.be/1h6hwFdI57M

player_position = player.position()
#player_position = world(513,99, 40)

player.say(player_position)

index = 0
def onRun_in_background():
    global index
    global player_position
    i = index
    y = -5
    shapes.circle(GOLD_BLOCK, positions.add(player_position, pos(0, y - i, 0)), 300, Axis.Y, ShapeOperation.OUTLINE)
    player.say(i)

for i in range(80):
    index = i
    loops.run_in_background(onRun_in_background)
    loops.pause(1000)

#shapes.circle(WATER, positions.add(player_position, pos(0, -5, 0)), 299, Axis.Y, ShapeOperation.REPLACE)
