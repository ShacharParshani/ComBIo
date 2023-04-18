import pygame
import random

# Set the dimensions of the screen
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Set the dimensions of the matrix
MATRIX_WIDTH = 10
MATRIX_HEIGHT = 10

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create the matrix
matrix = [[random.random() < 0.5 for x in range(MATRIX_WIDTH)] for y in range(MATRIX_HEIGHT)]

# Draw the matrix
cell_size = 40
for x in range(MATRIX_WIDTH):
    for y in range(MATRIX_HEIGHT):
        rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
        if matrix[y][x]:
            pygame.draw.rect(screen, (255, 192, 203), rect, 0)
        else:
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)

# Update the display
pygame.display.flip()

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
