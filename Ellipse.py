import matplotlib.pyplot as plt

def draw_ellipse(a, b):
    x = 0
    y = b

    a_sqr = a * a
    b_sqr = b * b

    two_a_sqr = 2 * a_sqr
    two_b_sqr = 2 * b_sqr

    p = b_sqr - (a_sqr * b) + (0.25 * a_sqr)

    x_coords = []
    y_coords = []

    while two_b_sqr * x < two_a_sqr * y:
        x_coords.extend([x, -x, x, -x])
        y_coords.extend([y, y, -y, -y])

        if p < 0:
            x += 1
            p += two_b_sqr * x + b_sqr
        else:
            x += 1
            y -= 1
            p += two_b_sqr * x - two_a_sqr * y + b_sqr

    p = b_sqr * (x + 0.5) ** 2 + a_sqr * (y - 1) ** 2 - a_sqr * b_sqr

    for i in range(len(x_coords)):
        print(f"Pixel: ({x_coords[i]}, {y_coords[i]})")

    plt.plot(x_coords, y_coords, 'bo')
    plt.gca().set_aspect('equal', adjustable='box')

    # Tambahkan garis kotak koordinat
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.grid(True, linestyle='dashed')

    plt.show()

# Main program
if __name__ == "__main__":
    # Input jari-jari atau setengah sumbu
    r_a = int(input("Masukkan panjang sumbu x: "))
    r_b = int(input("Masukkan panjang sumbu y: "))

    # Panggil fungsi untuk menggambar elips
    draw_ellipse(r_a, r_b)
