# PyGame has to be imported before it can be used.
import pygame

# Next, it must be initialized.
pygame.init()

# Colors can be defined afterwards.
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

display_width = 800
display_height = 600
# Here we set the display size and window name.
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')

# This is the variable for exiting the game.
gameExit = False
# Other variables.
lead_x = display_width / 2
lead_y = display_height / 2
lead_x_change = 0
lead_y_change = 0
block_size = 10
FPS = 15

# Clock variable
clock = pygame.time.Clock()

# Main game loop is next.
while not gameExit:
    for event in pygame.event.get():  # Event handling loop.
        if event.type == pygame.QUIT:  # Quitting the game.
            gameExit = True
        if event.type == pygame.KEYDOWN:  # Movement
            if event.key == pygame.K_LEFT:
                lead_x_change = -block_size
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = block_size
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -block_size
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = block_size
                lead_x_change = 0
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:  # All logic points to gameExit.
            gameExit = True

    # Logic Block
    lead_x += lead_x_change
    lead_y += lead_y_change
    gameDisplay.fill(white)  # Fills the window with the color white.
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, block_size, block_size])  # Adds a black square at the specified coordinates.
    pygame.display.update()  # Tells the display to update and show our graphics.

    clock.tick(FPS)  # Framerate set to 15fps.

pygame.quit()  # Exits PyGame.
quit()  # Exits Python and closes the window.
