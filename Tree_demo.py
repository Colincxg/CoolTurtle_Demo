from turtle import *

setup(600, 600)
bgcolor("wheat")
pen = Turtle()
pen.ht()

pen.up()
pen.goto(0, -150)
pen.down()
pen.setheading(90)
pen.pensize(3)
pen.pencolor("sienna")
pen.speed(0)


def branch(pen_list, branch_len):
    if branch_len > 0.011:
        new_list = []
        tracer(100)
        for pen in pen_list:
            pen.forward(branch_len)
            new_pen = pen.clone()
            pen.left(61.8)
            new_pen.right(61.8)
            new_list.append(pen)
            new_list.append(new_pen)
    branch(new_list, branch_len * 0.618)


branch([pen], 180)

done()
