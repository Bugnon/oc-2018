import turtle

a = turtle.Turtle()
a.speed(0)
for i in range(200):
    a.circle(0+4*i)
    a.penup()
    a.rt(90)
    a.fd(4)
    a.lt(90)
    a.pendown()