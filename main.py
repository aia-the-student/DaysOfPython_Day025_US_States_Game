import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

state_pointer = turtle.Turtle()
state_pointer.penup()
state_pointer.hideturtle()

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_ds = pd.read_csv('50_states.csv')
states_ds['checked'] = 0


def find_the_state(answer):
    answer_in_ds = states_ds.loc[(states_ds['state'] == answer) & \
                                 (states_ds['checked'] == 0)]
    is_correct = 0
    if answer_in_ds.shape[0] > 0:
        is_correct = 1
        states_ds.loc[states_ds['state'] == answer, 'checked'] = 1
        state_pointer.goto(answer_in_ds.x.item(), answer_in_ds.y.item())
        state_pointer.write(answer_in_ds.state.item(), align='center')
    return is_correct


n_answers = 0
while n_answers < states_ds.shape[0]:
    answer_state = screen.textinput(title=str(n_answers) + '/50 States Correct',
                                    prompt='What is another state name?').title()
    if answer_state == 'Exit':
        break
    is_state_found = find_the_state(answer_state)
    n_answers += is_state_found

states_ds[states_ds['checked'] == 0]['state'].to_csv('States_to_learn.csv')
