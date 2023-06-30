import turtle
import pandas
# Nastavenie obrazovky
screen = turtle.Screen()
screen.title("USA GAME")

# pridanie obrazka na screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# nastavenie korytnacku, ktora bude sluzit na vypis mien statov pre konkretnu poziciu
tim = turtle.Turtle()
tim.hideturtle()
tim.penup()

# subor so statmi a ich suradnice
states = pandas.read_csv("50_states.csv")

# Potrebne atributy pre hru
correct_answers = []
score = 0
game_is_on = True
must_lear_state_list = []


# funkcia sluzi na vypi nazvu statu na mapu
def write_text_on_map(tim, state, correct_answers,name):
    x = state.x.iloc[0]
    y = state.y.iloc[0]
    position = (x, y)
    tim.goto(position)
    tim.write(f"{name}", False, align="center", font=('Arial', 10, 'normal'))
    correct_answers.append(name)


# pre opakovanie hry alebo jej ukoncenie
def new_game():
    answer = screen.textinput(title="The end of game", prompt="You win!.Do you wanna play again? Yes or No?").lower()
    if answer == "yes":
        return True
    else:
        return False


# vypise csv subor so statmi, ktore sa treba sa doucit
def must_to_learn():
    list_states = states["state"].tolist()
    for state in list_states:
        if state not in correct_answers:
            must_lear_state_list.append(state)

    data = pandas.DataFrame(must_lear_state_list)
    data.to_csv("must_learn.txt")


# hlavny cyklus
while game_is_on:
    answer = screen.textinput(title="Guess the state", prompt="Whats is another name of state?").title()
    if answer == "Exit":
        must_to_learn()
        break
    state = states[states.state == answer]
    print(state)
    if state.empty == False:
        name = state.state.iloc[0]
        if name not in correct_answers:
            write_text_on_map(tim, state,correct_answers,name)
            score += 1
    screen.title(f"USA GAME {score}/50")
    screen.update()
    if score >= 50:
        if new_game():
            correct_answers = []
            score = 0
            game_is_on = True
            screen.clear()
            screen.addshape(image)
            turtle.shape(image)
        else:
            game_is_on = False
            must_to_learn()







