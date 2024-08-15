
import turtle as t
import random

screen = t.Screen()

screen.setup(500, 500)

color = ["violet", "red", "blue", "orange", "green", "yellow", "teal"]
y_cor = [120, 80, 40, 0, -40, -80, -120]
all_turtles = []
y = 120
for c in color:
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.setpos(-230, y)
    new_turtle.color(c)
    y -= 40
    all_turtles.append(new_turtle)


#for tur in all_turtles:

