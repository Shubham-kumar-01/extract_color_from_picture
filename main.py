
import turtle as t
import random
t.colormode(255)
rgb_color = [(199, 251, 254), (198, 12, 32),
                        (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5),(240,230,140),(0,255,0),(100,149,237)]

tim = t.Turtle()
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
no_of_dots = 101


for dot_count in range(1,no_of_dots):
    tim.dot(20,random.choice(rgb_color))
    tim.forward(50)

    if dot_count % 10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)










screen = t.Screen()
screen.exitonclick()