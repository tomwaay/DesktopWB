import pygame
import pygame.locals
from screeninfo import get_monitors

#GET SCREEN SIZE
screenX = get_monitors()[0].width
screenY = get_monitors()[0].height

#TRY LOADING wallpaper.png FROM SOURCE (PREVIOUS DESKTOPWB SESSION)
#IF ERR, CREATE BLANK WALLPAPER AND BACKUP CURRENT WALLPAPERS


# pygame setup
pygame.init()
#update to open canvas the size of the monitor
screen = pygame.display.set_mode((screenX, screenY-50))
clock = pygame.time.Clock()
running = True

colourWHITE = pygame.Color(255,255,255)
colourBLACK = pygame.Color(0,0,0)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #DRAWING
        elif pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(screen, pygame.Color(255,255,255), pygame.mouse.get_pos(), 5)

        #CHECKING FOR KEYPRESS
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Exiting without saving")
                running = False
            #CTRL + s to save and exit
            elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                print("Exiting and saving")
                #update wallpaper
                running = False


    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("purple")

    # RENDER YOUR GAME HERE



    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

