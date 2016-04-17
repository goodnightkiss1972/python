import turtle

fab = turtle.Turtle()

size = 20

for j in range(5):
    for i in range(8):
        fab.forward(size*j)
        fab.right(45)

turtle.done()
