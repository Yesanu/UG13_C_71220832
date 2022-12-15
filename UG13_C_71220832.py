import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
s.bgcolor('blue')

# No 8 diatas tengah
t.pensize(10)
t.penup()
t.goto(0,100)
t.pendown()
t.circle(30,360)
t.penup()
t.goto(0,160)
t.pendown()
t.circle(30,360)

# huruf S di kanan
t.pensize(10)
t.penup()
t.goto(120,-50)
t.pendown()
t.circle(30,180)
t.circle(-30,180)

# No 3 di tengah
t.pensize(10)
t.penup()
t.goto(0,-50)
t.pendown()
t.circle(30,180)
t.right(180)
t.circle(30,180)

# No 2 di bawah
t.penup()
t.goto(0,-80)
t.pendown()
t.circle(30,90)
t.left(180)
t.circle(-30,180)
t.right(30)
t.forward(100)
t.left(120)
t.forward(80)

# hururf Y disbeelah kiri
t.penup()
t.goto(-100,10)
t.pendown()
t.right(90)
t.forward(60)
t.right(180)
t.forward(60)
t.left(45)
t.forward(60)
t.left(180)
t.forward(60)
t.left(90)
t.forward(60)



s.exitonclick()
