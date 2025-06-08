# import package
import turtle
from tkinter import mainloop
from turtle import Turtle

def krestik():
    turtle.seth(138.5)
    turtle.forward(10)
    turtle.back(10)
    turtle.seth(228.5)
    turtle.forward(10)
    turtle.back(10)
    turtle.setheading(318.5)
    turtle.forward(10)
    turtle.back(10)
    turtle.seth(408.5)
    turtle.forward(10)
    turtle.back(10)
    turtle.left(40)

def nolik():
    turtle.circle(10)

def pole():
    turtle.speed(20)

    turtle.penup()
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(50)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(300)
    turtle.back(200)
    turtle.right(90)
    turtle.back(100)
    turtle.forward(300)
    turtle.back(100)
    turtle.right(90)
    turtle.back(200)
    turtle.forward(300)
    turtle.back(200)
    turtle.left(90)
    turtle.back(200)
    turtle.forward(300)

    turtle.penup()
    turtle.home()
    turtle.pendown()

    turtle.penup()
    turtle.left(90)
    turtle.forward(200)
    turtle.pendown()
    turtle.write("1", font=("Arial", 20, "normal"))

    turtle.penup()
    turtle.left(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.write("0", font=("Arial", 20, "normal"))

    turtle.penup()
    turtle.back(200)
    turtle.pendown()
    turtle.write("2", font=("Arial", 20, "normal"))

    turtle.penup()
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.write("0", font=("Arial", 20, "normal"))

    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    turtle.write("1", font=("Arial", 20, "normal"))

    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    turtle.write("2", font=("Arial", 20, "normal"))


    turtle.penup()
    turtle.home()
    turtle.left(90)
    turtle.pendown()

def strochka():
    turtle.back(150)
    turtle.forward(300)

def strochka2():
    turtle.seth(90)
    turtle.right(30)
    turtle.back(150)
    turtle.forward(300)

def strochka3():
    turtle.seth(90)
    turtle.left(30)
    turtle.back(150)
    turtle.forward(300)

def strochka4():
    turtle.back(150)
    turtle.forward(300)

mainloop()
