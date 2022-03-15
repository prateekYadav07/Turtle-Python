import random as r
from turtle import Turtle, Screen

screen = Screen()
# screen.addshape('turtle.gif')
screen.colormode(255)
screen.screensize(400, 400)
screen.bgcolor('light cyan')

jimmy = Turtle()
timmy = Turtle()

jimmy.shape('turtle')
timmy.shape('turtle')

timmy.color('red', 'dark olive green')
jimmy.color('medium aquamarine', 'dark green')

jimmy.shapesize(2, 2, 3)
timmy.shapesize(2, 2, 3)

jimmy.speed(0)
timmy.speed(2)

jimmy.pensize(2)
timmy.pensize(5)

jimmy.hideturtle()
timmy.hideturtle()


def spirograph(turtle = Turtle()):
    colors = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
    jimmy.pencolor(colors)
    turtle.circle(100)
    turtle.left(5)


for i in range(200):
    spirograph(jimmy)


def random_walk(turtle=Turtle()):
    way = r.choice([0, 1,2])
    if way == 0:
        turtle.left(90)
    elif way == 1:
        turtle.right(90)
    else:
        turtle.back(30)

    turtle.forward(30)


# color_palette = ['blue', 'deep sky blue', 'dark green', 'steel blue', 'dark goldenrod', 'AliceBlue']

for i in range(1000):
    colors = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
    jimmy.pencolor(colors)

    random_walk(jimmy)


# def motion():
#     jimmy.forward(10)
#     jimmy.penup()
#     jimmy.forward(10)
#     jimmy.pendown()


# angle = 0
# for i in range(3,11):
#     angle = 360/i
#
#     colors = (r.randint(0, 256), r.randint(0, 256), r.randint(0, 256))
#     jimmy.pencolor(colors)
#
#     colors = (r.randint(0, 256), r.randint(0, 256), r.randint(0, 256))
#     timmy.pencolor(colors)
#     for j in range(i):
#         jimmy.forward(100)
#         timmy.forward(100)
#
#         jimmy.left(angle)
#         timmy.right(angle)


screen.exitonclick()
