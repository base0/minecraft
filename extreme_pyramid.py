def on_on_chat(n):
    p = player.position()
    for i in range(n):
        w = n - i - 1
        shapes.line(GOLD_BLOCK, positions.add(p, pos(-w, i, -w)), positions.add(p, pos(-w, i, w)))
        shapes.line(GOLD_BLOCK, positions.add(p, pos(-w, i, w)), positions.add(p, pos(w, i, w)))
        shapes.line(GOLD_BLOCK, positions.add(p, pos(w, i, w)), positions.add(p, pos(w, i, -w)))
        shapes.line(GOLD_BLOCK, positions.add(p, pos(w, i, -w)), positions.add(p, pos(-w, i, -w)))

    player.teleport( positions.add(p, pos(0, n, 0)))
    p = player.position()
    for i in range(n * 4):
        mobs.spawn(CAT, p)

player.on_chat("p", on_on_chat)

def tel_y():
    p = player.position()
    player.say(p.get_value(Axis.Y))

player.on_chat("y", tel_y)

