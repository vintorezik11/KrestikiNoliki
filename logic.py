
def check_victory():
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] != "*":
            print(f'Победил: {matrix[i][0]}')
            return  True
        elif matrix[0][i] == matrix[1][i] == matrix[2][i] != "*":
            print(f'Победил: {matrix[0][i]}')
            return True
    for i in range(3):
            if matrix[0][0] == matrix[1][1] == matrix[2][2] != "*":
                print(f'Победил: {matrix[1][1]}')
                return True
            elif matrix[0][2] == matrix[1][1] ==  matrix[2][0] != "*":
                print(f'Победил: {matrix[0][2]}')
                return True

def gameplay():
    for i in range(9):
        if i % 2 != 0:
            sign = "❌"
        else:
            sign = "⭕️"
        print(f"Ход за {sign}")

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

matrix =  (["*", "*", "*"],
          ["*", "*", "*"],
          ["*", "*", "*"])

