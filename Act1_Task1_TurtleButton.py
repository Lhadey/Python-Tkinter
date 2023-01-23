import turtle

def button_action (x,y):
    print('Button was clicked!')

def create_button(x, y, width, height,color, action):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()
    turtle.color("black")
    turtle.onscreenclick(action)

create_button(-50, 0, 100, 50, "red", button_action)
turtle.mainloop()
