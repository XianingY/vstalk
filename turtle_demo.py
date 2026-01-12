import turtle

pen = turtle.Turtle()
pen.hideturtle()  # Hide the turtle cursor
pen.color("black","red")
pen.begin_fill()

# draw a star
for _ in range(5):
    pen.forward(100)
    pen.right(144)
    pen.forward(100)
    pen.right(36)
pen.end_fill()
turtle.done()