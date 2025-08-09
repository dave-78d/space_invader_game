import pygame


class Explosion:
    def __init__(self, x, y,enemy):
        self.x = x
        self.y = y
        self.image=""
        self.image = pygame.image.load(r"C:\Users\ABBY\Desktop\code\space invaders\Foozle_2DS0013_Void_EnemyFleet_2\Nairan\Destruction\PNGs\Nairan - Frigate -  Destruction.png")
        self.width = 64
        self.height = 64
        self.allimages = []  # will hold all 14 images

        for number in range(0, 14):
            smallimage = self.image.subsurface(0 + number * 64, 0, 64, 64)
            self.allimages.append(smallimage)

        self.time = 0
        self.current_image = 0
        self.finished=False
    def show(self, screen):
        if self.current_image > 12:
            self.current_image = 0
            self.finished=True
        self.time += 0.1
        if self.time > 1:
            self.current_image = self.current_image + 1
            self.time = 0

        screen.blit(self.allimages[self.current_image], (self.x, self.y))
