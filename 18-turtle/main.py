import turtle
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('circle')
timmy_the_turtle.color('red')

# for _ in range(10):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
#
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# ns = [3, 4, 5, 6, 8]
# for n in ns:
#     timmy_the_turtle.color(random.choice(colors))
#     for i in range(n):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360//n)

# angles = [90, 180, 270, 360]
# timmy_the_turtle.width(5)
# timmy_the_turtle.pen(speed=10)
turtle.colormode(255)
timmy_the_turtle.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)
# for _ in range(100):
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.right(random.choice(angles))
#     timmy_the_turtle.forward(20)

def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        timmy_the_turtle.circle(100)
        timmy_the_turtle.color(random_color())
        current_heading = timmy_the_turtle.heading()
        timmy_the_turtle.setheading(current_heading + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()


