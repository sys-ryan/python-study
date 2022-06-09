from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()


is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet.", prompt="Which turtle will win the race? Enter the color: ")


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

def init_turtle_position(t, x, y):
    t.penup()
    t.goto(x=x, y=y)
    t.pendown()
    turtles.append(t)

for i in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    init_turtle_position(t, -230, (-175 + 50*(i+1)))
    # t.goto(x=-230, y=(-175 + 50 * (i+1)))
    # turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:

    for t in turtles:
        if t.xcor() > 230:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        t.forward(random.randint(0, 10))


# screen.listen()
# # screen.onkey(key="space", fun=move_forward)
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="d", fun=move_right)
# screen.onkey(key="c", fun=clear)
screen.exitonclick()