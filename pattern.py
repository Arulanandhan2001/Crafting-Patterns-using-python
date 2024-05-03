import turtle

def BangelFlower():
    
    turtle.bgcolor("black")

    turtle.pensize(5) #you can give any thickness to pensize

    turtle.speed(0) #you can give speed to draw

    for i in range(12):

        for colors in ["orange", "white", "yellow green"]: #you can give as many colors as you want
    
            turtle.color(colors)

            turtle.circle (100) # how many circles you want to draw

            turtle.left(10) #it will start from left
        
            turtle.hideturtle()

# star
import random

def draw (n, x, angle):

        for i in range(n):

            turtle.colormode(255)

            a = random.randint(0, 255)

            b = random.randint(0, 255)

            c = random.randint(0, 255)

            turtle.pencolor(a, b, c)

            turtle.fillcolor(a, b, c)

            turtle.begin_fill()

            for j in range(5):

                turtle.forward(5* n-5* i)

                turtle.right(x)
            
                turtle.forward(5* n-5* i)

                turtle.right(72-x)

        turtle.end_fill()

        turtle.rt(angle)

def star():
    
    turtle.bgcolor("black")

    turtle.speed(0)     

    n = 50

    x = 144

    angle = 18

    draw(n, x, angle)

# chakra

from turtle import *

import colorsys

speed(0)

bgcolor("black")

h = 0.1

pensize(4)

def chakra():

    def fun():

        global h

        for i in range(4):

            c=colorsys.hsv_to_rgb(h,1,1)

            fillcolor(c)

            h+=0.004

            begin_fill()

            fd(50)

            rt(20)

            fd(40)

            rt(9)

            end_fill()

    for j in range(300):

        fun()

        goto(0,0)

        rt(10)

    Done()

from turtle import *

def rasingan():
    
    speed(0.3)

    color('cyan')

    bgcolor('black')

    b = 200

    while b> 0:

        left(b)

        forward(b*3)

        b = b-1

# Flower lite

import turtle as tur

import colorsys as cs

def flower_lite():

    tur.setup(800,800)

    tur.speed(0)

    tur.tracer(10)

    tur.width(2)

    tur.bgcolor("black")

    for j in range(25):

        for i in range(15):
    
            tur.color(cs.hsv_to_rgb(i/15,j/25,1))

            tur.right(90)

            tur.circle(200-j*4,90)

            tur.left(90)

            tur.circle(200-j*4,90)

            tur.right(180)

            tur.circle(50,24)

    tur.hideturtle()

    tur.done()

# star flower

from turtle import *

import random

def flower_star():

    bgcolor("black")

    speed(0)

    def draw (n, x, angle):

        for i in range(n):

            colormode(255)

            a = random.randint(0, 255)

            b = random.randint(0, 255)

            c = random.randint(0, 255)

            pencolor(a, b, c)

            fillcolor(a, b, c)

            begin_fill()

            for j in range(5):

                forward(5* n-5* i)
        
                right(x)
            
                forward(5* n-5* i)

                right(72-x)

            end_fill()
    
            rt(angle)
        
    n = 50

    x = 144

    angle = 18

    draw(n, x, angle)

    done()


# flower

from turtle import *

import colorsys

def flower():
    
    speed (0)

    bgcolor("black")
    
    h = 0

    for i in range(16):

        for j in range(18):

            c = colorsys.hsv_to_rgb(h, 1, 1)

            color(c)

            h = 0.005

            rt (90)

            circle (150 - j * 6, 90)

            lt(90)

            circle (150 - j * 6, 90)

            rt(180)

            circle (40, 24)

    done()

# circus

from turtle import *

import colorsys

def circus():

    tracer (500)

    def draw():

        h = 0

        for i in range(100):

            c = colorsys.hsv_to_rgb(h,1,1)

            h += 0.5

            up()

            goto (0,0)

            down()

            color('black')

            fillcolor (c)

            begin_fill()

            rt (98)

            circle(i, 12)

            fd (290)

            fd(i)

            lt (29)

            fd(i)

            for j in range(129):

                fd(i)
                
                circle(j, 299, steps=2)

            end_fill()

    draw()

    done()