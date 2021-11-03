import sys
import RPi.GPIO as GPIO
sys.path.insert(0, './raspirobotboard3/python')
import time
from rrb3 import *
import pygame

from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
#initialize rrb3
#RRB3(battery voltage, motor output voltage)
rr = RRB3(6, 6)
rr.set_led1(1)

#Initialize pygame
pygame.init()

def turn_left():
    rr.set_motors(1, 0, 0, 0)
def turn_right():
    rr.set_motors(1, 1, 0, 0)
def forward():
    rr.set_motors(0, 0, 1, 0)
def backward():
    rr.set_motors(0, 0, 1, 1)
def stop():
    rr.set_motors(0, 0, 0, 0)
    time.sleep(.2)

# Define a player object by extending pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            print("key up pressed")
            forward()
        elif pressed_keys[K_DOWN]:
            print("key down pressed")
            backward()
        elif pressed_keys[K_LEFT]:
            print("key left pressed")
            turn_left()
        elif pressed_keys[K_RIGHT]:
            print("key right pressed")
            turn_right()
        else:
            print("no keys pressed")
            stop()



#Drawing window
SCREEN_WIDTH = 250
SCREEN_HEIGHT = 250
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Instantiate player. Right now, this is just a rectangle.
player = Player()

#Game clock
clock = pygame.time.Clock()

#Run until quit
running = True
while running:

    #Check for event
    for event in pygame.event.get():
        if event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                print("Esc pressed, closing game")
                running = False

        elif event.type == QUIT:
            print("Quit pressed, closing game")
            running = False

    #Check for pressed keys
    pressed_keys = pygame.key.get_pressed()

    #Update sprite based on keypress
    player.update(pressed_keys)
    
    #Game background color
    screen.fill((0, 0, 0))

    #Updates screen
    pygame.display.flip()

    #Game ticks per second
    clock.tick(30)

pygame.quit()

