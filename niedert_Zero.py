from turtle import *
canvas = Screen()
turtle = Turtle()
canvas.setup(600,400)
turtle.shape ("turtle")
turtle.color ("green")

def turn_left():
    turtle.left(90)

window.onkeypress(turn_left, "Left")
window.listen()

turtle.done ()
