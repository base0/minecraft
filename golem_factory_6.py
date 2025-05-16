gameplay.time_set(DayTime.MIDDAY)
gameplay.set_weather(RAIN)

N = 15
for i in range(N):
    p = pos(-1, 0, -N).to_world()
    p = p.add(pos(0,0,i))
    for index in range(3):
        blocks.place(IRON_BLOCK, p)
        p = p.add(pos(0, 1, 0))
        blocks.place(IRON_BLOCK, p)
        p = p.add(pos(0, 0, -1))
        blocks.place(IRON_BLOCK, p)
        p = p.add(pos(0, 0, 2))
        blocks.place(IRON_BLOCK, p)
        p = p.add(pos(0, 1, -1))
        blocks.place(JACK_O_LANTERN, p)
        p = p.add(pos(1, -2, 0))
    
