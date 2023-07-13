import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = dy > dx

    if slope:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    error = dx // 2  # Menggunakan pembagian bulat (integer division) di sini
    y_step = 1 if y1 < y2 else -1
    y = y1

    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if slope else (x, y)
        points.append(coord)
        error -= dy
        if error < 0:
            y += y_step
            error += dx

    return points

def onclick(event):
    global click_counter

    if click_counter == 0:
        global x1, y1
        x1 = int(event.xdata)
        y1 = int(event.ydata)
        click_counter += 1
        print("Titik mulai ditentukan di koordinat:", x1, y1)
    elif click_counter == 1:
        global x2, y2
        x2 = int(event.xdata)
        y2 = int(event.ydata)
        click_counter += 1
        print("Titik akhir ditentukan di koordinat:", x2, y2)

        # Menggunakan fungsi bresenham_line untuk membuat garis
        line_points = bresenham_line(x1, y1, x2, y2)

        # Menampilkan output setiap langkah per pixel
        for point in line_points:
            print(f"Langkah: ({point[0]}, {point[1]})")

        # Menggambar garis menggunakan matplotlib
        x_coordinates, y_coordinates = zip(*line_points)
        plt.plot(x_coordinates, y_coordinates, color='blue')
        plt.show()

# Inisialisasi program
click_counter = 0
x1, y1 = 0, 0
x2, y2 = 0, 0

# Inisialisasi figure
fig = plt.figure()
fig.canvas.mpl_connect('button_press_event', onclick)

# Menampilkan plot
plt.title("Garis menggunakan metode Bresenham")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.grid(True)
plt.show()
