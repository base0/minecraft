class Ball:
    def __init__(self):
        self.x = randint(-20, 20)
        self.y = randint(  0, 20)
        self.z = randint( 15, 30)
        self.r = randint(  3,  8)

    def hit(self, other:Ball):
        dist = ((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2) ** 0.5
        return dist < (self.r + other.r)

    def build(self):
        shapes.sphere(GLASS, pos(self.x, self.y, self.z), self.r, ShapeOperation.REPLACE)

player.teleport(pos(200, 0, 0))
gameplay.set_weather(Weather.CLEAR)
gameplay.time_set(DayTime.DAY)
a = []
i = 0
while i != 20:
    b = Ball()
    hit = False
    for j in a:
        if b.hit(j):
            hit = True
            break
    if not hit:
        a.push(b)
        b.build()
        i += 1

