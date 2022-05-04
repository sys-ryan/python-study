import colorgram
import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)

rgb_colors = []
colors = colorgram.extract('image.jpeg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    rgb_colors.append((r, g, b))

tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)

for i in range(10):
    for j in range(10):
        tim.dot(10, random.choice(rgb_colors))

        tim.penup()
        tim.forward(20)
        tim.pendown()
    tim.penup()
    tim.backward(200)
    tim.left(90)
    tim.forward(20)
    tim.right(90)
    tim.pendown()


screen = turtle.Screen()
screen.exitonclick()