
import colorgram
import turtle as t
from random import choice

rgb_color = []

colors = colorgram.extract("image.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    new_color = (r, g, b)

    rgb_color.append(new_color)

tim = t.Turtle()
t.colormode(255)
tim.speed(0)

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
# tim.pendown()
number_of_dots = 100

# tim.color(random_color)
for dot_count in range(1, number_of_dots):
    tim.dot(20, choice(rgb_color))
    tim.penup()
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        tim.penup()
