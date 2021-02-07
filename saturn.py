# https://youtu.be/3NKj7qoEc1w
    
player_position = player.position()
#player_position = world(513,99, 40)

player.say(player_position)

center = positions.add(player_position, pos(0, 200 - player_position.get_value(Axis.Y ), 0))

def onRun_in_background():
    global center
    shapes.sphere(GLOWSTONE, center , 50, ShapeOperation.OUTLINE)
loops.run_in_background(onRun_in_background)

for i in range(70, 90):
    shapes.circle(BLUE_ICE, center, i, Axis.Y, ShapeOperation.OUTLINE)
        
