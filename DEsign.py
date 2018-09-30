import turtle
def square(tur):
    i = 1
    while i < 5:
        tur.color('red')
        tur.forward(100)
        tur.right(90)
        tur.color('orange')
        tur.circle(5)
        i += 1
def draw():
    window = turtle.Screen()
    window.bgcolor('blue')
    brad = turtle.Turtle()
    brad.color('red')
    brad.pensize(5)
    brad.shape('turtle')
    brad.speed(0.001)
    for j in range(36):
        square(brad)
        brad.right(10)
    brad.right(90)
    brad.speed(5)
    brad.color('green')
    brad.pensize(25)
    brad.forward(1000)
draw()