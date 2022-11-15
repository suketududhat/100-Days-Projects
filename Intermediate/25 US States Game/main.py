import turtle
import pandas as pd

df = pd.read_csv(
    "C:/Users/suk2d/pyproj/Udemy/100-Days-Projects/Intermediate/25 US States Game/50_states.csv"
)

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "100-Days-Projects/Intermediate/25 US States Game/blank_states_img.gif"
screen.bgpic(image)

score = 0
answered_states = []
while score < 50:
    answer_state = screen.textinput(
        title=f"{score}/50 States Correct", prompt="What's another state's name?"
    )
    answer_state = answer_state.title()
    if answer_state in df["state"].values and answer_state not in answered_states:
        x_pos = df.loc[df["state"] == answer_state, "x"]
        y_pos = df.loc[df["state"] == answer_state, "y"]
        score += 1
        answered_states.append(answer_state)

turtle.mainloop()
# screen.exitonclick()
