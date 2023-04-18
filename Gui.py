import random

import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 400
screen_height = 300

# Set the dimensions of the matrix
matrix_width = 300
matrix_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Define the tab
tab = "Name"
active_tab = 0

# Define the font
font = pygame.font.SysFont(None, 24)

# Define the input box
input_box = pygame.Rect(10, 50, 200, 30)
input_text = ""

# Define the submit button
submit_button = pygame.Rect(10, 100, 100, 30)
submit_text = font.render("Submit", True, (0, 0, 0))

# Define the status message
status_text = font.render("", True, (255, 0, 0))

# Define the function to be executed when the submit button is clicked
def submit_function():
    print("The submit button was clicked! The text is:", input_text)

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
            if input_box.collidepoint(pygame.mouse.get_pos()):
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    # Fill the background
    screen.fill((255, 255, 255))

    if initial_screen:
        # Draw the tab
        tab_text = font.render(tab, True, (0, 0, 0))
        screen.blit(tab_text, (10, 10))

        # Draw the input box
        pygame.draw.rect(screen, (0, 0, 0), input_box, 2)
        input_text_surface = font.render(input_text, True, (0, 0, 0))
        screen.blit(input_text_surface, (input_box.x + 5, input_box.y + 5))

        # Draw the submit button
        pygame.draw.rect(screen, (0, 0, 0), submit_button, 2)
        screen.blit(submit_text, (submit_button.x + 5, submit_button.y + 5))

        # Draw the status message
        screen.blit(status_text, (10, 150))

        # Update the display
        pygame.display.update()

        # Get the data from the input box
        player_name = input_text

    else:
        # Fill the background
        screen.fill((255, 255, 255))

        # Create the screen
        screen = pygame.display.set_mode((screen_width, screen_height))

        # Create the matrix
        matrix = [[random.random() < 0.5 for x in range(matrix_width)] for y in range(matrix_height)]

        # Draw the matrix
        cell_size = 40
        for x in range(matrix_width):
            for y in range(matrix_height):
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

