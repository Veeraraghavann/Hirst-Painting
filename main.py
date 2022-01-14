import turtle
from turtle import Turtle, Screen
import random

# import colorgram
#
# colors = colorgram.extract('image2.jpg', 30)
# colour_list = []
# for i in range(30):
#     first_color = colors[i]
#     #print(first_color)
#     rgb = first_color.rgb # e.g. (255, 151, 210)
#     #print(rgb)
#     hsl = first_color.hsl # e.g. (230, 255, 203)
#     proportion  = first_color.proportion # e.g. 0.34
#     red = rgb[0]
#     green = rgb[1]
#     blue = rgb[2]
#     colour = (red, green, blue)
#     colour_list.append(colour)
# print(colour_list)

def random_colour():
 colour_list = [(1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39),
                (215, 87, 63), (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57),
                (95, 6, 20), (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85),
                (145, 227, 217), (122, 193, 147), (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178)]
 color = random.choice(colour_list)
 r = color[0]
 g = color[1]
 b = color[2]
 return r,g,b


colour_list = [(1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20), (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217), (122, 193, 147), (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178)]
tom = Turtle()
tom.shape("arrow")
turtle.colormode(255)
tom.penup()
tom.hideturtle()
tom.setposition(-300, -300)
x_cordinate = tom.xcor()
for i in range(10):
    tom.speed("fast")
    y_cordinate = tom.ycor()
    tom.setx(x_cordinate)
    for i in range(10):
        tom.dot(20, random_colour())
        tom.forward(10)
        tom.forward(50)
    tom.sety(y_cordinate + 50)




screen = Screen()
screen.exitonclick()