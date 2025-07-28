import pygame
import ship
my_ship=ship.Ship(image=pygame.image.load(r"C:\Users\ABBY\Desktop\code\space invaders\Main Ship - Base - Full health.png"),health=100)
pygame.init()
screen=pygame.display.set_mode(size=(400,400))
#pygame.time.Clock().tick (100)
X=300
while True:
    screen.fill(color=(20,100,30))
    screen.blit(my_ship.image,(X ,200))
    pygame.display.flip()
    KEYS=pygame.key.get_pressed()
    if KEYS[pygame.K_RIGHT]:
        X=X+5
    if KEYS[pygame.K_LEFT]:
        X=X-51