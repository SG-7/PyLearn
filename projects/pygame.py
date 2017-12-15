# PyGame has to be imported before it can be used.
import pygame

# Next, it must be initialized.
pygame.init()

# Colors can be defined afterwards.
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

# Here we set the display size and window name.
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')

# This is the variable for exiting the game.
gameExit = False

# Main game loop is next.
while not gameExit:
    for event in pygame.event.get(): # Event handling for the window's exit button.
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(white) # Fills the window with the color white.
    pygame.draw.rect(gameDisplay, black, [400,300,10,10]) # Adds a black square at the specified coordinates.
    gameDisplay.fill(red, rect=[200,200,50,50]) # Adds a red square at the specified coordinates.

    pygame.display.update() # Tells the display to update and show our graphics.

pygame.quit() # Exits PyGame.
quit() # Exits Python and closes the window.
