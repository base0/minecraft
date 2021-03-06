# https://youtu.be/7DONth96xmI

xs = [1.0,
    0.7071067811865476,
    6.123233995736766e-17,
    -0.7071067811865475,
    -1.0,
    -0.7071067811865477,
    -1.8369701987210297e-16,
    0.7071067811865474,
    ]

zs = [0.0,
    0.7071067811865475,
    1.0,
    0.7071067811865476,
    1.2246467991473532e-16,
    -0.7071067811865475,
    -1.0,
    -0.7071067811865477,
    ]

    
spiral_radius = 6
radius = 3
dy = radius

player_position = player.position()
player.teleport(offset(-26, 116, 44))

def offset(x, y, z):
    return positions.add(player_position, pos(x, y, z))

ROUND = 4
shapes.line(RED_CONCRETE, offset(0, 0, 0), offset(0, ROUND * 9 * radius, 0))

y = radius / 2
for i in range(ROUND*len(xs)):
    b = LIME_GLAZED_TERRACOTTA #GRASS if i < 8 else GOLD_BLOCK
    x = spiral_radius * xs[i%len(xs)]
    z = spiral_radius * zs[i%len(zs)]
    #player.say(x+' ' + y + ' '  + z)
    shapes.sphere(b, offset(x, y, z), radius, ShapeOperation.OUTLINE)
    y += dy

# head
radius -= 1
y -= dy
d = radius + 2
blocks.fill(LIME_GLAZED_TERRACOTTA, offset(x - radius, y - d, z), offset(x + radius, y + d-1, z + radius * 2 + 2))

# mouth
blocks.fill(YELLOW_GLAZED_TERRACOTTA, offset(x - radius, y - d, z + radius * 2 - 2), offset(x + radius, y, z + radius * 5))

blocks.fill(AIR, offset(x - radius, y - d + 1, z + radius * 2 + 2), offset(x + radius, y - d +1, z + radius * 5))

# eye
blocks.fill(GLASS, offset(x + radius - 1, y + d - 3, z + radius * 2 - 1),
                   offset(x + radius,     y + d - 2, z + radius * 2))

blocks.fill(GLASS, offset(x - radius + 1, y + d - 3, z + radius * 2 - 1),
                   offset(x - radius,     y + d - 2, z + radius * 2))

# horn
blocks.fill(RED_GLAZED_TERRACOTTA, offset(x - radius, y + d - 2, z - 5), offset(x - radius, y + d, z + 1))               
blocks.fill(RED_GLAZED_TERRACOTTA, offset(x + radius, y + d - 2, z - 5), offset(x + radius, y + d, z + 1))               
