import turtle
import math


def draw(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

def transform(p, t):
    c = [[0 for _ in range(len(p[0]))] for _ in range(len(p))]

    for i in range(len(p)):
        for j in range(len(p[0])):
            sum = 0
            for k in range(len(t)):
                sum += t[i][k] * p[k][j]
            c[i][j] = sum

    for i in range(len(p)):
        for j in range(len(p[0])):
            p[i][j] = c[i][j]

def myCleardevice():
    turtle.clear()

# Konversi sudut dalam derajat ke radian
def d2r(degrees):
    return math.radians(degrees)

# Inisialisasi turtle
turtle.setup(width=800, height=600)
screen = turtle.Screen()
screen.title("2D Transformation")

# Gambar sumbu x dan y
draw(-400, 0, 400, 0)
draw(0, -300, 0, 300)

# Input nilai
p = [[50, 50, 50, 60, 60, 60, 60, 50, 60, 200, 200, 200, 200, 60, 60, 120, 120, 60],
     [50, 200, 200, 200, 200, 50, 50, 50, 200, 200, 200, 120, 120, 120, 120, 160, 160, 200],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

for i in range(0, len(p[0]), 2):
    draw(p[0][i], p[1][i], p[0][i+1], p[1][i+1])

while True:
    print("*** MENU ***")
    print("1. Translate")
    print("2. Scale")
    print("3. Rotation")
    print("4. Reflection")
    print("5. Exit")
    print("Pilih transformasi yang ingin Anda lakukan: ")
    choice = int(input())

    if choice == 1:
        t = [[1, 0, 100],
             [0, 1, 100],
             [0, 0, 1]]

        transform(p, t)

    elif choice == 2:
        t = [[-2, 0, 0],
             [0, 2, 0],
             [0, 0, 1]]

        transform(p, t)

    elif choice == 3:
        t = [[math.cos(d2r(30)), -math.sin(d2r(30)), 0],
             [math.sin(d2r(30)), math.cos(d2r(30)), 0],
             [0, 0, 1]]


        transform(p, t)

    elif choice == 4:
        t = [[1, 0, 0],
             [0, -1, 0],
             [0, 0, 1]]

        transform(p, t)

    elif choice == 5:
        break

    myCleardevice()
    draw(-400, 0, 400, 0)
    draw(0, -300, 0, 300)

    for i in range(0, len(p[0]), 2):
        draw(p[0][i], p[1][i], p[0][i+1], p[1][i+1])

turtle.done()