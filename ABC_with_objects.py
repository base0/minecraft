# https://youtu.be/Rc29AuuVBKo

char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mob = [ None, BEE, CAT, DONKEY,None, FOX,      None,HORSE,    None,          None,None,None,        None,         None,OCELOT, PIG,          None,RABBIT,SHEEP,SEA_TURTLE,None,VILLAGER, None,SKELETON,           None,ZOMBIE]
con = [ None,None,None,   None,None,None,      None, None,BLUE_ICE,JACK_O_LANTERN,None,LAVA,        None, NETHER_BRICK,  None,None,BLOCK_OF_QUARTZ,  None, None,      None,None,    None,WATER,    None,           None,  None]
itm = [APPLE,None,None,   None, EGG,None,GOLD_INGOT, None,    None,          None,KELP,None,RED_MUSHROOM,         None,  None,None,           None,  None, None,      None,None,    None, None,    None,YELLOW_CONCRETE,  None]
msg = ['Apple','Bee','Cat','Donkey','Egg','Fox','Gold','Horse','Ice','Jack O Lantern','Kelp','Lava','Mushroom','Nether Brick','Ocelot','Pig','Quartz','Rabbit','Sheep','Turtle','','Villager','Water','X-Ray','Yellow','Zombie']
gameplay.time_set(DayTime.Day)
gameplay.set_weather(CLEAR)
i = 0
last_z = player.position().get_value(Axis.Z)
def on_travelled_walk():
    global i
    global last_z
    z = player.position().get_value(Axis.Z)
    #player.say('z' + z)
    if  z % 30 == 0 and z != last_z:
        blocks.print(char[i], YELLOW_CONCRETE, pos(-1, 1, -20), EAST)
        if char[i] == 'R':
            gameplay.set_weather(RAIN)
        if mob[i] != None:
            mobs.spawn(mob[i], pos(0,1,-14))
        elif con[i] != None:
            blocks.place(con[i], pos(-2,0,-14))
        elif itm[i] != None:
            agent.teleport(pos(-2, 0, -14), EAST)
            agent.set_item(itm[i], 1, 1)
            agent.drop(FORWARD, 1, 1)
        if char[i] == 'W':
            loops.pause(1000)
            gameplay.time_set(DayTime.Night)
        player.say(msg[i])
        last_z = z
        i += 1

        

player.on_travelled(WALK, on_travelled_walk)
