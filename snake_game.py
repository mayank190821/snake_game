import random
import time
import turtle

delay = 0.1
score = 0
hscore = 0
sc = turtle.Screen()
sc.title("Snake Game")
sc.bgcolor("black")
sc.setup(width=600, height=600)
sc.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("orange")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("blue")
food.penup()
food.goto(0, 100)
food.direction = "stop"

parts = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("courier", 24, "normal"))


# function

def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)

    if head.direction == "down":
        head.sety(head.ycor() - 20)

    if head.direction == "left":
        head.setx(head.xcor() - 20)

    if head.direction == "right":
        head.setx(head.xcor() + 20)

    # keyboard binding


sc.listen()
sc.onkeypress(go_up, "w")
sc.onkeypress(go_down, "s")
sc.onkeypress(go_left, "a")
sc.onkeypress(go_right, "d")
# loop
while True:
    sc.update()
    # check for collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        # hide the parts
        for part in parts:
            part.goto(1000, 1000)
        parts.clear()
        delay = 0.1
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, hscore), align="center", font=("courier", 24, "normal"))
        # check collision with food
    if head.distance(food) < 20:
        # move the food randomly
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        # add parts
        new_parts = turtle.Turtle()
        new_parts.speed(0)
        new_parts.shape("circle")
        new_parts.color("red")
        new_parts.penup()
        parts.append(new_parts)
        delay -= 0.001
        # increase score
        score += 10
        if score > hscore:
            hscore = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, hscore), align="center", font=("courier", 24, "normal"))
    # the end pats first i revers
    for i in range(len(parts) - 1, 0, -1):
        x = parts[i - 1].xcor()
        y = parts[i - 1].ycor()
        parts[i].goto(x, y)
    # MOve segments 0 to where the head is
    if len(parts) > 0:
        x = head.xcor()
        y = head.ycor()
        parts[0].goto(x, y)
    move()

    # check the collision with the body
    for part in parts:
        if part.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            # hide the parts
            for part in parts:
                part.goto(1000, 1000)
            parts.clear()
            delay = 0.1
            score = 0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, hscore), align="center", font=("courier", 24, "normal"))
    time.sleep(delay)
sc.mainloop()
