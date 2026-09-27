class Balloon:
    def __init__(self, x, y, d, c, speed):
        self.x = x
        self.y = y
        self.d = d
        self.c = c
        self.speed = speed

    def show(self):
        noFill()
        stroke(90)
        strokeWeight(1.5)
        bezier(self.x, self.y + self.d * 0.68,
               self.x - 10, self.y + self.d * 1.1,
               self.x + 10, self.y + self.d * 1.5,
               self.x, self.y + self.d * 1.9)

        noStroke()
        fill(self.c[0], self.c[1], self.c[2])
        ellipse(self.x, self.y, self.d, self.d * 1.2)
        triangle(self.x, self.y + self.d * 0.56,
                 self.x - self.d * 0.09, self.y + self.d * 0.68,
                 self.x + self.d * 0.09, self.y + self.d * 0.68)

        fill(255, 255, 255, 110)
        ellipse(self.x - self.d * 0.2, self.y - self.d * 0.22,
                self.d * 0.18, self.d * 0.3)

    def move(self):
        self.y = self.y - self.speed
        if self.y < -self.d * 2:
            self.y = height + self.d


balloons = [
    Balloon(80, 300, 60, (231, 76, 60), 1.0),
    Balloon(190, 420, 70, (243, 156, 18), 1.6),
    Balloon(300, 250, 55, (46, 204, 113), 1.2),
    Balloon(410, 480, 80, (52, 152, 219), 2.0),
    Balloon(520, 360, 65, (155, 89, 182), 1.4),
]


def setup():
    size(600, 400)


def draw():
    background(200, 230, 255)
    for b in balloons:
        b.show()
        b.move()