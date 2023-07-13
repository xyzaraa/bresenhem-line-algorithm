import pygame
import sys
import random

# Inisialisasi Pygame
pygame.init()

# Warna
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Ukuran layar
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Membuat jendela aplikasi
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Aplikasi Seleksi Garis")

# Daftar garis
lines = []

# Menambahkan beberapa garis acak
for _ in range(10):
    start_x = random.randint(50, SCREEN_WIDTH - 50)
    start_y = random.randint(50, SCREEN_HEIGHT - 50)
    end_x = random.randint(start_x - 50, start_x + 50)
    end_y = random.randint(start_y - 50, start_y + 50)
    line = pygame.Rect(start_x, start_y, end_x - start_x, end_y - start_y)
    lines.append((line, BLACK))

# Variabel seleksi garis
selecting = False
selection_rect = pygame.Rect(0, 0, 0, 0)

# Loop utama aplikasi
while True:
    # Handle event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Tombol kiri mouse
                selecting = True
                start_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Tombol kiri mouse
                selecting = False
                end_pos = pygame.mouse.get_pos()
                selection_rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                # Ubah warna garis yang terpilih menjadi biru
                for i in range(len(lines)):
                    if lines[i][0].colliderect(selection_rect):
                        lines[i] = (lines[i][0], BLUE)
                    elif lines[i][0].clip(selection_rect) != lines[i][0]:
                        # Hanya hapus bagian yang berwarna biru
                        clipped_line = lines[i][0].clip(selection_rect)
                        if clipped_line.width > 0 and clipped_line.height > 0:
                            lines[i] = (lines[i][0], BLACK)
                            lines.append((clipped_line, BLACK))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                # Menghapus garis yang terpilih
                lines = [line for line in lines if not line[0].colliderect(selection_rect)]

    # Clear layar
    screen.fill(WHITE)

    for line, color in lines:
        pygame.draw.line(screen, color, (line.left, line.top), (line.right, line.bottom), 2)

    if selecting:
        current_pos = pygame.mouse.get_pos()
        selection_rect = pygame.Rect(start_pos, (current_pos[0] - start_pos[0], current_pos[1] - start_pos[1]))
        pygame.draw.rect(screen, RED, selection_rect, 2)

    pygame.display.flip()