import turtle
from tkinter import mainloop
def strochka():
    turtle.back(400)
    turtle.forward(800)

def strochka2():
    turtle.seth(90)
    turtle.right(45)
    turtle.back(400)
    turtle.forward(800)

def strochka3():
    turtle.seth(90)
    turtle.left(45)
    turtle.back(400)
    turtle.forward(800)

def strochka4():
    turtle.right(90)
    turtle.back(400)
    turtle.forward(800)

def hod(x, y):
    while True:

        if x == 0 and y == 0:
            if matrix[0][0] == "*":
                matrix[0][0] = sign
                break
            else:
                print("Клетка занята")
                return True
        if x == 0 and y == 1:
            if matrix[1][0] == "*":
                matrix[1][0] = sign
                break
            else:
                print("Клетка занята")
                return True
        if x == 0 and y == 2:
            if matrix[2][0] == "*":
                matrix[2][0] = sign
                break
            else:
                print("Клетка занята")
                return True
        if x == 1 and y == 0:
            if matrix[0][1] == "*":
                matrix[0][1] = sign
                break
            else:
                print("Клетка занята")
                return True
        if x == 1 and y == 1:
            if matrix[1][1] == "*":
                matrix[1][1] = sign
                break
            else:
                print("Клетка занята")
                return True
        if x == 1 and y == 2:
            if matrix[2][1] == "*":
                matrix[2][1] = sign
                break
            else:
                print("Клетка занята")
                return True
        if x == 2 and y == 0:
            if matrix[0][2] == "*":
                matrix[0][2] = sign
                break
            else:
                print("Клетка занята")
                return True
        if x == 2 and y == 1:
            if matrix[1][2] == "*":
                matrix[1][2] = sign
                break
            else:
                print("Клетка занята")
                return True
        if x == 2 and y == 2:
            if matrix[2][2] == "*":
                matrix[2][2] = sign
                break
            else:
                print("Клетка занята")
                return True

def check_victory():
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] != "*":
            strochka4()
            print(f'Победил: {matrix[i][0]}')
            return  True
        elif matrix[0][i] == matrix[1][i] == matrix[2][i] != "*":
            strochka()
            print(f'Победил: {matrix[0][i]}')
            return True
    for i in range(3):
            if matrix[0][0] == matrix[1][1] == matrix[2][2] != "*":
                strochka3()
                print(f'Победил: {matrix[1][1]}')
                return True
            elif matrix[0][2] == matrix[1][1] ==  matrix[2][0] != "*":
                strochka2()
                print(f'Победил: {matrix[0][2]}')
                return True

def nolik():
    turtle.penup()
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()
    turtle.right(90)
    turtle.back(30)
    turtle.left(90)
    turtle.pendown()

def krestik():
    turtle.seth(138.5)
    turtle.forward(30)
    turtle.back(30)
    turtle.seth(228.5)
    turtle.forward(30)
    turtle.back(30)
    turtle.setheading(318.5)
    turtle.forward(30)
    turtle.back(30)
    turtle.seth(408.5)
    turtle.forward(30)
    turtle.back(30)
    turtle.left(40)

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

def gameplay():
    for i in range(9):
        if i % 2 != 0:
            sign = "❌"
        else:
            sign = "⭕️"
        print(f"Ход за {sign}")

matrix =  (["*", "*", "*"],
          ["*", "*", "*"],
          ["*", "*", "*"])

pole()
for i in range(9):
    if check_victory():
        print("Конец игры❗️")
        break
    if i % 2 != 0:
        sign = "❌"
    else:
        sign = "⭕️"
    print(f"Ход за {sign}")
    x = int(input("Введите координату оси X: "))
    y = int(input("Введите координату оси Y: "))
    if hod(x, y):
        while True:
            x = int(input("Введите координату оси X: "))
            y = int(input("Введите координату оси Y: "))
            if hod(x, y):
                continue
            else:
                print(*matrix, sep="\n")
                if x == 0:
                    x = -100
                if x == 1:
                    x = 0
                if x == 2:
                    x = 100
                if y == 0:
                    y = 100
                if y == 1:
                    y = 0
                if y == 2:
                    y = -100
                turtle.teleport(x, y)
                if sign == "❌":
                    krestik()
                else:
                    nolik()
                break
    else:
        print(*matrix, sep="\n")
        if x == 0:
            x = -100
        if x == 1:
            x = 0
        if x == 2:
            x = 100
        if y == 0:
            y = 100
        if y == 1:
            y = 0
        if y == 2:
            y = -100
        turtle.teleport(x, y)
        if sign == "❌":
            krestik()
        else:
            nolik()

mainloop()