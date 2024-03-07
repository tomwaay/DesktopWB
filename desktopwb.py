import pygame
import pygame.locals
import struct
import ctypes
from screeninfo import get_monitors
from pygame.locals import *

# pygame setup
pygame.init()

#GET SCREEN SIZE
screenX = get_monitors()[0].width
screenY = get_monitors()[0].height

#vars and depends
flags = FULLSCREEN | DOUBLEBUF
screen = pygame.display.set_mode((screenX, screenY),flags,16)
clock = pygame.time.Clock()
running = True
SPI_SETDESKWALLPAPER = 20

colourWHITE = pygame.Color(255,255,255)
colourBLACK = pygame.Color(0,0,0)

PATH = "C:\DesktopWB\dtwb_background.jpg"

def is_64bit_windows():
    """Check if 64 bit Windows OS"""
    return struct.calcsize('P') * 8 == 64

def changeBG():
    """Change background depending on bit size"""
    if is_64bit_windows():
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, PATH, 3)
    else:
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, PATH, 3)

#TODO
#BACK UP PREVIOUS WALLPAPER 
#Make drawing better & consistent movements
#add eraser
#different sizes?
#tool palette?

#Try to environment variable for easy cli launch? or create exe?

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
    
pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #DRAWING
        elif pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(screen, colourBLACK, pygame.mouse.get_pos(), 5)
            pygame.draw.circle(screen, colourBLACK, pygame.mouse.get_pos(), 5)
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
                changeBG()
                running = False


    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(600)  # limits FPS to 60
pygame.quit()

