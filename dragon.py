xs = [1.0,
 0.7071067811865476,
 6.123233995736766e-17,
 -0.7071067811865475,
 -1.0,
 -0.7071067811865477,
 -1.8369701987210297e-16,
 0.7071067811865474,
 1.0]
zs = [0.0,
 0.7071067811865475,
 1.0,
 0.7071067811865476,
 1.2246467991473532e-16,
 -0.7071067811865475,
 -1.0,
 -0.7071067811865477,
 -2.4492935982947064e-16]

    
spiral_radius = 6
radius = 3
dy = radius

player_position = player.position()
player.say(player_position)

def offset(x, y, z):
  return positions.add(player_position, pos(x, y, z))

shapes.line(RED_CONCRETE, offset(0, 0, 0), offset(0, 100, 0))

y = radius / 2
for i in range(len(xs)):
    b = GRASS if i < 8 else GOLD_BLOCK
    x = spiral_radius * xs[i]
    z = spiral_radius * zs[i]
    player.say(x+' ' + y + ' '  + z)
    shapes.sphere(b, offset(x, y, z), radius, ShapeOperation.OUTLINE)
    y += dy

# head
radius -= 1
y -= dy
d = radius + 2
blocks.fill(GRASS, offset(x - radius, y - d, z), offset(x + radius, y + d, z + radius * 2))


# mouth
blocks.fill(GRASS, offset(x - radius, y - d, z + radius * 2), offset(x + radius, y, z + radius * 5))

# eye
blocks.fill(GLASS, offset(x + radius - 1, y + d - 2, z + radius * 2 - 1),
                   offset(x + radius,     y + d - 1, z + radius * 2))

blocks.fill(GLASS, offset(x - radius + 1, y + d - 2, z + radius * 2 - 1),
                   offset(x - radius,     y + d - 1, z + radius * 2))

