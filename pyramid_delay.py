# https://youtu.be/jVfmjPyTnt4
    
def on_on_chat(n):
    p = player.position()
    player.teleport(positions.add(p, pos(-130, 103, 38)))   # p 100
    
    for i in range(n):
        w = n - i - 1
        from_pos = positions.add(p, pos(0 - w, i, 0 - w))
        to_pos = positions.add(p, pos(w, i, w))
        blocks.fill(GOLD_BLOCK, from_pos, to_pos, FillOperation.OUTLINE)
        loops.pause(500)
        
player.on_chat("p", on_on_chat)  
