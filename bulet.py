import pygame
class Bullet:
    def __init__(self,x,y):
       self.image=pygame.image.load(r"C:\Users\ABBY\Desktop\code\space invaders\Laser Sprites\17.png")
       self.image=pygame.transform.scale(self.image,(25,40),)
       self.x=x
       self.y=y 
       self.rect=self.image.get_rect()
