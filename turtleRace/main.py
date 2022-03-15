from turtle import Turtle, Screen
import random as r

violet = Turtle()
indigo = Turtle()
blue = Turtle()
green = Turtle()
yellow = Turtle()
orange = Turtle()
red = Turtle()

violet.name = 'violet'
indigo.name = 'indigo'
blue.name = 'blue'
green.name = 'green'
yellow.name = 'yellow'
orange.name = 'orange'
red.name = 'red'

screen = Screen()
screen.setworldcoordinates(-100, -100, 100, 100)
screen.bgcolor('grey')

violet.color('violet')
indigo.color('indigo')
blue.color('blue')
green.color('green')
yellow.color('yellow')
orange.color('orange')
red.color('red')

turtles = [violet, indigo, blue, green, yellow, orange, red]
for turtle in turtles:
    turtle.shape('turtle')
    turtle.shapesize(2, 2, 1)


def start_line():
    x = -100
    y = 70
    for char in turtles:
        char.penup()
        char.setpos(x, y)
        y -= 20


bet = screen.textinput('Turtle Race', 'Bet on a turtle to win <participants are colors of VIBGYOR> :')
start_line()


def race():
    for i in range(len(turtles)):
        speed = r.randint(1, 6)
        turtles[i].forward(speed)


def is_race_over(t=None):
    if t is None:
        t = [Turtle()]
    for char in t:
        if int(char.xcor()) >= 100:
            if char.name == bet.lower():
                char.write(f'your turtle {char.name} Won', align='center')
            else:
                char.write(f'your turtle {bet} lost, {char.name} won', align='center')
            return True
    return False


race_over = False

while not race_over:
    race_over = is_race_over(turtles)
    race()

screen.exitonclick()
