# https://youtu.be/mrV1t41pMoU

player_position = player.position()


cx = 0
cy = 5
cz = 14
radius = 6


def on_item_interacted_diamond_hoe():
    blocks.replace(AIR, DIAMOND_BLOCK, pos(cx-radius, cy-radius, cz-radius), pos(cx+radius, cy+radius, cz+radius))
    
player.on_item_interacted(DIAMOND_HOE, on_item_interacted_diamond_hoe)

def on_item_interacted_golden_hoe():
    blocks.replace(AIR, GOLD_BLOCK, pos(cx-radius, cy-radius, cz-radius), pos(cx+radius, cy+radius, cz+radius))
    
player.on_item_interacted(GOLDEN_HOE, on_item_interacted_golden_hoe)

def random_item():
    r = randint(0, 2)
    if r == 0:
        return CAKE
    elif r == 1:
        return CARROT
    return BUCKET

def random_mobs():
    r = randint(0, 2)
    if r == 0:
        return HORSE
    elif r == 1:
        return CHICKEN
    return BEE

def loot():
    shapes.sphere(DIAMOND_BLOCK, pos(cx, cy, cz), radius, ShapeOperation.OUTLINE)
    shapes.sphere(GOLD_BLOCK, pos(cx, cy, cz), radius - 2, ShapeOperation.OUTLINE)
    agent.teleport(pos(cx, cy+1, cz-radius+1), WEST)
    agent.set_item(random_item(), 1, 1)
    agent.set_slot(1)
    agent.drop_all(FORWARD)
    agent.teleport(pos(0, 0, -100), WEST)
    mobs.spawn(random_mobs(), pos(cx, cy, cz))
    player.say('use Diamon Hoe then Gold Hoe to open')

player.on_chat("loot", loot)
