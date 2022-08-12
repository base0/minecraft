class Ball:
    def __init__(self):
        self.x = randint(-20, 20)
        self.y = randint(  0, 20)
        self.z = randint( 30, 45)
        self.r = randint(  3,  8)

    def hit(self, other:Ball):
        dist = ((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2) ** 0.5
        return dist < (self.r + other.r)

    def build(self):
        shapes.sphere(GLASS, pos(self.x, self.y, self.z), self.r, ShapeOperation.REPLACE)

class ColorfulBall (Ball):  
    def build(self):
        g = [RED_STAINED_GLASS, ORANGE_STAINED_GLASS, YELLOW_STAINED_GLASS, GREEN_STAINED_GLASS, BLUE_STAINED_GLASS, PURPLE_STAINED_GLASS, PINK_STAINED_GLASS]
        shapes.sphere(g[randint(0,6)], pos(self.x, self.y, self.z), self.r, ShapeOperation.OUTLINE)

player.teleport(pos(200, 0, 0))
gameplay.set_weather(Weather.CLEAR)
gameplay.time_set(DayTime.DAY)
a = []
for i in range(30):
    hit = True
    while hit:
        hit = False
        b = ColorfulBall()
        for j in a:
            if b.hit(j):
                hit = True
                break
        if not hit:
            a.push(b)
            b.build()
            player.say(i)
        
