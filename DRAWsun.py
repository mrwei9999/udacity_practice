import turtle
def square(tur):
    i = 1
    while i < 5:
        tur.forward(100)
        tur.right(90)
        i += 1
def draw():
    window = turtle.Screen()
    window.bgcolor('red')
    brad = turtle.Turtle()
    brad.color('green')
    brad.shape('turtle')
    brad.speed(0.001)
    for j in range(36):
        square(brad)
        brad.right(10)
    #Ann = turtle.Turtle()
    #Ann.color('orange')
    #Ann.shape('arrow')
    #Ann.circle(100)
draw()
