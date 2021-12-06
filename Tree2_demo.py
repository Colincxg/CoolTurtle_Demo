from turtle import *


def _init():
    bgcolor('black')
    setup(800, 800)
    pencolor('white')
    pensize(5)
    speed(0)
    up()
    goto(0, -300)
    down()
    seth(90)


_init()

"""基本形态"""


def basic_demo():
    fd(200)  # 分型最基本形态
    # 回到这条直线的起点
    up()
    bk(200)
    down()


"""画出第一阶分支"""


def branch(n):
    if n > 11:
        fd(n)  # 分型最基本形态
        rt(45)
        branch(n * 0.618)
        lt(90)
        branch(n * 0.618)
        rt(45)
        up()
        bk(n)
        down()


basic_demo()
branch(200)
mainloop()
