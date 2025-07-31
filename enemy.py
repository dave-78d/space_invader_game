import pygame
import random
class enemy:
    def __init__(self,health,x,y,):
        self.health=health
        self.x=x
        self.y=y
        self.image1=pygame.image.load(r"C:\Users\ABBY\Desktop\code\space invaders\Foozle_2DS0013_Void_EnemyFleet_2\Nairan\Designs - Base\PNGs\Nairan - Scout - Base.png")
        self.image2=pygame.image.load(r"C:\Users\ABBY\Desktop\code\space invaders\Foozle_2DS0013_Void_EnemyFleet_2\Nairan\Designs - Base\PNGs\Nairan - Frigate - Base.png")
        self.selectedimage=random.choice([self.image1,self.image2])
        self.selectedimage=pygame.transform.scale(self.selectedimage,(80,80))
        if self.selectedimage==self.image1:
            self.selectedimage=pygame.transform.scale(self.selectedimage,(150,150))
        self.rect=self.selectedimage.get_rect()