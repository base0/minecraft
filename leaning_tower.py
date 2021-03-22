# https://youtu.be/ooJgOOKco1M

#blocks.fill(AIR, pos(-30,-1,-30), pos(30,3,30))
#blocks.fill(GRASS, pos(-30,-1,-30), pos(30,-1,30))
'''
sin5 = 0.08715574274765817355806427083747
cos5 = 0.99619469809174553229501040247389

player.teleport(world(7099, 50, 103))
ox = 7000
nx = 7100
for y in range(4,110): #4, 110)
    for x in range(-20,21):
        for z in range(-20, 21):
            if blocks.test_for_block(AIR, world(ox+x, y, z)) == False:
                blocks.place(BLOCK_OF_QUARTZ, world(nx+(x*cos5-y*sin5),0+x*sin5+y*cos5,z))
'''
for i in range(6):
    #for j in range(10):
        mobs.spawn(VILLAGER, world(7100, i*15+2, 0))
