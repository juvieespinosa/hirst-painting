# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(201, 167, 134), (236, 243, 249), (144, 51, 99), (163, 167, 41), (238, 71, 125), (237, 83, 61), (17, 140, 64), (241, 221, 67), (225, 118, 163), (10, 142, 179), (67, 198, 219), (157, 59, 53), (23, 169, 129), (32, 187, 202), (127, 188, 163), (107, 42, 88), (248, 231, 0)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()