import turtle as t
t.speed(0)
t.left(35)
t.bgcolor("black")
for i in range(22):
    for colours in ("red","magenta","blue","indigo","green"):
        t.color(colours)
        t.pensize(2)
        t.forward(200)
        t.left(144)
        t.forward(201)
        t.left(145)
