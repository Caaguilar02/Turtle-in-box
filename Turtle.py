import turtle

wn = turtle.Screen()
wn.bgcolor("white")
wn.setup(width=600, height=600)


t = turtle.Turtle()
t.shape("turtle")
t.color("black")
t.penup() 


t.speed(2)
dx = 3
dy = 2


left_border = -190
right_border = 190
top_border = 190
bottom_border = -190

border_turtle = turtle.Turtle()
border_turtle.penup()
border_turtle.goto(left_border, bottom_border)
border_turtle.pendown()
border_turtle.goto(left_border, top_border)
border_turtle.goto(right_border, top_border)
border_turtle.goto(right_border, bottom_border)
border_turtle.goto(left_border, bottom_border)
border_turtle.hideturtle()

def move_turtle():
    global dx, dy

  
    x, y = t.position()

    if x + dx > right_border or x + dx < left_border:
        dx = -dx
    if y + dy > top_border or y + dy < bottom_border:
        dy = -dy
    t.setx(x + dx)
    t.sety(y + dy)

    wn.ontimer(move_turtle, 10)


move_turtle()

wn.mainloop()
