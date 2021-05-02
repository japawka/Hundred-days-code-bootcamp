from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

angles = [0, 90, 180, 270]

screen.colormode(255)
def random_color():
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    colors = (r, g, b)
    return colors

def draw_shape(num_sides):
    for x in range(num_sides):
        tim.forward(100)
        tim.right(360 / num_sides)

for n in range(3, 11):
    tim.color(random_color())
    tim.pensize(n*2)
    draw_shape(n)

tim.clear()

# tim.speed('fastest')
# for n in range(50):
#     tim.forward(30)
#     tim.setheading(random.choice(angles))
#     tim.pencolor(random_color())
#     tim.pensize(n / 3)
#
# #
# tim.speed('fastest')
# def spirograf(n):
#
#     for _ in range(360//n):
#         tim.left(n)
#         tim.pencolor(random_color())
#         tim.circle(100)
# spirograf(5)


# import colorgram
# colors = colorgram.extract('Addictive.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     rgb_colors.append((r, g, b))

color_list = [(202, 164, 109), (153, 75, 49), (222, 201, 136), (53, 94, 124), (171, 153, 41), (136, 32, 21),
              (133, 163, 184), (197, 93, 73), (48, 123, 87), (73, 44, 36), (14, 97, 72), (145, 178, 148), (91, 73, 75),
              (233, 176, 165), (160, 143, 159), (54, 47, 50), (184, 205, 172), (35, 61, 75), (22, 85, 89),
              (146, 19, 21), (86, 146, 130), (38, 67, 91), (13, 72, 66), (106, 128, 155), (175, 99, 101),
              (176, 192, 209)]
tim.penup()
tim.hideturtle()
tim.speed('fastest')
tim.goto(-250, -250)

for n in range(10):
    for i in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.goto(-250, tim.ycor() + 50)

screen.exitonclick()
