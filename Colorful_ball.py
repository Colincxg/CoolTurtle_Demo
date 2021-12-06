# 究极无敌弹球大杂烩之————重力互相反弹更多小球随机颜色大项目
# By：@爱法棍的御风少年Colin

import turtle
import time
import random

sc = turtle.Screen()
sc.setup(640, 640)
sc.bgcolor("black")
sc.tracer(0)
sc.colormode(255)

balls = []
for i in range(40):
    balls.append(turtle.Turtle())

shapes = ["circle", "triangle", "square", "turtle"]
colors = ["yellow", "red", "green", "blue", "pink"]

for ball in balls:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ball.shape(random.choice(shapes))
    ball.color(r, g, b)
    ball.up()
    x = random.randint(-300, 300)
    y = random.randint(100, 400)
    ball.goto(x, y)
    ball.vel_y = 0
    ball.vel_x = random.randint(-3, 3)
    ball.turn = random.randint(-5, 5)

gravity = 0.1
try:
    while True:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        sc.update()
        time.sleep(0.01)

        for ball in balls:
            ball.rt(ball.turn)
            ball.vel_y -= gravity
            ball.sety(ball.ycor() + ball.vel_y)
            ball.setx(ball.xcor() + ball.vel_x)

            if ball.ycor() < -320:
                ball.sety(-320)
                ball.vel_y = -ball.vel_y

            if ball.xcor() < -320 or ball.xcor() > 320:
                ball.vel_x = -ball.vel_x
                ball.turn = -ball.turn

        for m in range(len(balls)):
            for n in range(m+1, len(balls)):
                if balls[m].distance(balls[n]) < 20:
                    balls[m].color(r, g, b)
                    balls[n].color(r, g, b)

                    balls[m].vel_x, balls[n].vel_x = balls[n].vel_x, balls[m].vel_x
                    balls[m].vel_y, balls[n].vel_y = balls[n].vel_y, balls[m].vel_y
except:
    print("EXIT")
