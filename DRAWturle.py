import turtle
def draw():
    window = turtle.Screen()
    window.bgcolor('red')
    brad = turtle.Turtle()
    brad.color('green')
    brad.shape('turtle')
    brad.speed(1)
    i = 1
    while i < 5:
        brad.forward(100)
        brad.right(90)
        i += 1
    Ann = turtle.Turtle()
    Ann.color('orange')
    Ann.shape('arrow')
    Ann.circle(100)
draw()