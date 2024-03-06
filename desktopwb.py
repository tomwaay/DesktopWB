import pygame
import pygame.locals
from screeninfo import get_monitors

# pygame setup
pygame.init()

#GET SCREEN SIZE
screenX = get_monitors()[0].width
screenY = get_monitors()[0].height

#vars and depends
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
running = True

colourWHITE = pygame.Color(255,255,255)
colourBLACK = pygame.Color(0,0,0)

#TODO
#BACK UP PREVIOUS WALLPAPER 
#SET DESKTOP BACKGROUND ON CTRL+S ACTION
try:
    bg = pygame.image.load('dtwb_background.jpg').convert()
    screen.blit(bg, (0,0))
    print("background found.")
except:
    print("No background. Creating one.")
    screen.fill(colourWHITE)
    pygame.image.save(screen, 'dtwb_background.jpg')
else:
    pygame.image.save(screen, 'dtwb_background.jpg')
    

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #DRAWING
        elif pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(screen, colourBLACK, pygame.mouse.get_pos(), 5)

        #CHECKING FOR KEYPRESS
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Exiting without saving")
                running = False
            #CTRL + s to save and exit
            elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                print("Exiting and saving")
                pygame.image.save(screen, 'dtwb_background.jpg')
                #update wallpaper
                running = False


    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
pygame.quit()

