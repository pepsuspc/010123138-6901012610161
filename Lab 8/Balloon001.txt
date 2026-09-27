xs = [80, 190, 300, 410, 520]
ys = [300, 420, 250, 480, 360]
sizes = [60, 70, 55, 80, 65]
speeds = [1.0, 1.6, 1.2, 2.0, 1.4]
colors = [(231, 76, 60), (243, 156, 18), (46, 204, 113),
          (52, 152, 219), (155, 89, 182)]


def setup():
    size(600, 400)


def draw():
    background(200, 230, 255)
    for i in range(len(xs)):
        draw_balloon(xs[i], ys[i], sizes[i], colors[i])
        ys[i] = ys[i] - speeds[i]
        if ys[i] < -sizes[i] * 2:
            ys[i] = height + sizes[i]


def draw_balloon(x, y, d, c):
    noFill()
    stroke(90)
    strokeWeight(1.5)
    bezier(x, y + d * 0.68,
           x - 10, y + d * 1.1,
           x + 10, y + d * 1.5,
           x, y + d * 1.9)

    noStroke()
    fill(c[0], c[1], c[2])
    ellipse(x, y, d, d * 1.2)
    triangle(x, y + d * 0.56,
             x - d * 0.09, y + d * 0.68,
             x + d * 0.09, y + d * 0.68)

    fill(255, 255, 255, 110)
    ellipse(x - d * 0.2, y - d * 0.22, d * 0.18, d * 0.3)