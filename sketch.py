import turtle as t

screen=t.Screen()


tim= t.Turtle()

def move_forward():
    tim.forward(50)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def move_back():
    tim.backward(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_back,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear_screen,"c")



screen.exitonclick()