gameplay.time_set(DayTime.MIDDAY)
gameplay.set_weather(RAIN)

N = 10
for i in range(N):
    p = pos(-2, 0, -N).to_world()
    p = p.add(pos(0,0,i))
    for index in range(5):
        blocks.place(SNOW, p)
        p = p.add(pos(0, 1, 0))
        blocks.place(SNOW, p)
        p = p.add(pos(0, 1, 0))
        blocks.place(JACK_O_LANTERN, p)
        p = p.add(pos(1, -2, 0))
    
