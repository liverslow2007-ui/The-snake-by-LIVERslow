import time
import turtle
import random

def snake():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.tracer(0)

    food = turtle.Turtle()
    food.penup()
    food.shape("square")
    food.color("red")

    head = turtle.Turtle()
    head.shape("square")
    head.color("green")
    head.penup()
    head.direction = "stop"

    clones = []

    def place():
        food.setx((random.choice(range(-39,40)) * 10))
        food.sety((random.choice(range(-29,30)) * 10))

    def clones_pos():
        for i in range(len(clones) - 1, 0, -1):
            x= clones[i-1].xcor()
            y= clones[i-1].ycor()
            clones[i].goto(x, y)

        if len(clones) > 0:
            x = head.xcor()
            y = head.ycor()
            clones[0].goto(x, y)

    def go_up():
        if head.direction != "down":
            head.direction = "up"
    def go_down():
        if head.direction !="up":
            head.direction = "down"
    def go_left():
        if head.direction != "right":
            head.direction = "left"
    def go_right():
        if head.direction != "left":
            head.direction = "right"

    screen.listen()

    screen.onkeypress(go_up, "w")
    screen.onkeypress(go_down, "s")
    screen.onkeypress(go_left, "a")
    screen.onkeypress(go_right, "d")


    def move():
        if head.direction == "up":
            head.sety(head.ycor() + 20)
        if head.direction == "down":
            head.sety(head.ycor() - 20)
        if head.direction == "left":
            head.setx(head.xcor() - 20)
        if head.direction == "right":
            head.setx(head.xcor() + 20)

    while True:

        screen.update()
        move()
        if head.distance(food) < 20:
            place()
            clone = turtle.Turtle()
            clone.shape("square")
            clone.color("green")
            clone.penup()
            clones.append(clone)
        clones_pos()
        time.sleep(0.13)

        if abs(head.xcor()) == 400 or abs(head.ycor()) == 300:
            head.teleport(0,0)
            break

    turtle.mainloop()