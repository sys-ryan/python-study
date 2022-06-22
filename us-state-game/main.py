import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
total = len(data)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = turtle.textinput(title=f"{len(guessed_states)}/{total} States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()
    answer = data[data.state == answer_state]
    # print(answer.x, answer.y)
    # print(answer_state.title())
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer.empty:
        continue
    else:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(answer.x), int(answer.y))
        t.write(answer.state.item())



turtle.mainloop()


# screen.exitonclick()

