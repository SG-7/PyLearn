# PyGame has to be imported before it can be used.
import pygame

# Next, it must be initialized.
pygame.init()

# Colors can be defined afterwards.
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Here we set the display size and window name.
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Slither')

# This is the variable for exiting the game.
gameExit = False
# Other variables.
lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0

# Clock variable
clock = pygame.time.Clock()

# Main game loop is next.
while not gameExit:
    for event in pygame.event.get():  # Event handling loop.
        if event.type == pygame.QUIT:  # Quitting the game.
            gameExit = True
        if event.type == pygame.KEYDOWN:  # Movement
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10
            if event.key == pygame.K_UP:
                lead_y_change = -10
            if event.key == pygame.K_DOWN:
                lead_y_change = 10

    # Logic Block
    lead_x += lead_x_change
    lead_y += lead_y_change

    gameDisplay.fill(white)  # Fills the window with the color white.
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10])  # Adds a black square at the specified coordinates.
    pygame.display.update()  # Tells the display to update and show our graphics.

    clock.tick(15)  # Framerate set to 15fps.

pygame.quit()  # Exits PyGame.
quit()  # Exits Python and closes the window.
