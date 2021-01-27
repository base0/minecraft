for index in range(6):
    shapes.circle(GLASS,
        positions.add(player.position(), pos(0, index, 0)),
        5,
        Axis.Y,
        ShapeOperation.OUTLINE)
blocks.place(OAK_DOOR, pos(5, 0, 0))
shapes.circle(GLASS,
    positions.add(player.position(), pos(0, 5, 0)),
    5,
    Axis.Y,
    ShapeOperation.REPLACE)
for index2 in range(50):
    mobs.spawn(PARROT, player.position()) 	
