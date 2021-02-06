# https://youtu.be/BROHi5uZFq8
    
def on_on_chat(n):
    p = player.position()
    for i in range(n):
        w = n - i - 1
        from_pos = positions.add(p, pos(0 - w, i, 0 - w))
        to_pos = positions.add(p, pos(w, i, w))
        blocks.fill(GOLD_BLOCK, from_pos, to_pos, FillOperation.OUTLINE)
        
    player.teleport( positions.add(p, pos(0, n, 0)))
    p = player.position()
    
    for i in range(n*4):
        mobs.spawn(CAT, p)

player.on_chat("p", on_on_chat)
