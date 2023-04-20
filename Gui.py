import random
import time

import pygame

from Automaton import Automaton
from InputTextBox import InputTextBox

# Initialize Pygame
pygame.init()
automat = None

# Set up the display
screen_width = 700
screen_height = 700

# Set the dimensions of the matrix
matrix_width = 100
matrix_height = 100
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shachar & Liel")

# Define the font
font = pygame.font.SysFont('Arial', 16)

# Define the text boxes
p_text_box = InputTextBox("P:", pygame.Rect(10, 30, 150, 30))
l_text_box = InputTextBox("L:", pygame.Rect(200, 30, 150, 30))
pros1_text_box = InputTextBox("pros1:", pygame.Rect(10, 100, 150, 30))
pros2_text_box = InputTextBox("pros2:", pygame.Rect(200, 100, 150, 30))
pros3_text_box = InputTextBox("pros3:", pygame.Rect(10, 170, 150, 30))
pros4_text_box = InputTextBox("pros4:", pygame.Rect(200, 170, 150, 30))
endGen_text_box = InputTextBox("endGen:", pygame.Rect(10, 240, 150, 30))

# Define the submit button
submit_button = pygame.Rect(200, 240, 150, 30)
submit_text = font.render("Submit", True, (100, 50, 80))


# Define the function to be executed when the submit button is clicked
def submit_function():
    global automat
    automat = Automaton(p_text_box.input_text, l_text_box.input_text, pros1_text_box.input_text, pros2_text_box.input_text,
                    pros3_text_box.input_text, pros4_text_box.input_text, endGen_text_box.input_text)
    print(automat.p)


# Define the game loop
running = True
initial_screen = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the submit button was clicked
            if submit_button.collidepoint(event.pos):
                submit_function()
                initial_screen = False
        elif event.type == pygame.KEYDOWN:
            # Check if a key was pressed while in the input box
            if p_text_box.input_box.collidepoint(pygame.mouse.get_pos()):
                p_text_box.GetPos(event, font, screen)

            if l_text_box.input_box.collidepoint(pygame.mouse.get_pos()):
                l_text_box.GetPos(event, font, screen)

            if pros1_text_box.input_box.collidepoint(pygame.mouse.get_pos()):
                pros1_text_box.GetPos(event, font, screen)

            if pros2_text_box.input_box.collidepoint(pygame.mouse.get_pos()):
                pros2_text_box.GetPos(event, font, screen)

            if pros3_text_box.input_box.collidepoint(pygame.mouse.get_pos()):
                pros3_text_box.GetPos(event, font, screen)

            if pros4_text_box.input_box.collidepoint(pygame.mouse.get_pos()):
                pros4_text_box.GetPos(event, font, screen)

            if endGen_text_box.input_box.collidepoint(pygame.mouse.get_pos()):
                endGen_text_box.GetPos(event, font, screen)

    # Fill the background
    screen.fill((255, 255, 255))

    if initial_screen:
        # Draw the text boxes
        p_text_box.Draw(font, screen, (10, 10))
        l_text_box.Draw(font, screen, (200, 10))
        pros1_text_box.Draw(font, screen, (10, 80))
        pros2_text_box.Draw(font, screen, (200, 80))
        pros3_text_box.Draw(font, screen, (10, 150))
        pros4_text_box.Draw(font, screen, (200, 150))
        endGen_text_box.Draw(font, screen, (10, 210))

        # Draw the submit button
        pygame.draw.rect(screen, (100, 50, 80), submit_button, 2)
        screen.blit(submit_text, (submit_button.x + 5, submit_button.y + 5))

        # Update the display
        pygame.display.update()

    else:

        # Fill the background
        screen.fill((255, 255, 255))

        # Create the screen
        screen = pygame.display.set_mode((screen_width, screen_height))

        # Run the matrix loop
        while True:
            automat.matrix = [[random.random() < 0.5 for x in range(100)] for y in range(100)]

            # Draw the matrix
            cell_size = 7
            for x in range(matrix_width):
                for y in range(matrix_height):
                    rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)

                    if automat.matrix[y][x]:
                        pygame.draw.rect(screen, (255, 192, 203), rect, 0)
                    else:
                        pygame.draw.rect(screen, (255, 255, 255), rect, 0)

            # Update the display
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            time.sleep(1)
