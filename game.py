
import pygame
import ship
import bulet
import enemy
import explosion
my_ship=ship.Ship(image=pygame.image.load(r"C:\Users\ABBY\Desktop\code\space invaders\Main Ship - Base - Full health.png"),health=100)
bg=pygame.image.load(r"C:\Users\ABBY\Desktop\code\space invaders\Space Background (1).png")
pygame.init()
screen=pygame.display.set_mode(size=(400,400))
pygame.time.Clock().tick (120)
X=300
all_bullets=[]
all_enemies=[]
all_explosions=[]
for number in range(1,6):
    alien_enemy=enemy.enemy(health=10,x=0+number*50,y=10)
    all_enemies .append(alien_enemy)
while True:
    screen.fill(color=(20,100,30))
    screen.blit(bg,(0,0))
    screen.blit(my_ship.image,(X ,350))
    pygame.display.set_caption("SPACE INVADER")
    for click in pygame.event.get():
        if click.type==pygame.QUIT:
            exit()
        elif click.type==pygame.KEYDOWN:
            if click.key==pygame.K_SPACE:
                newbulett=bulet.Bullet(x=X+10,y=350)
                all_bullets.append(newbulett)
    KEYS=pygame.key.get_pressed()
    if KEYS[pygame.K_RIGHT]:
        X=X+0.5
    if KEYS[pygame.K_LEFT]:
        X=X-0.5
    for b in all_bullets:
        screen.blit(b.image,(b.x,b.y))
        b.y=b.y-5
        b.rect.centerx=b.x
        b.rect.centery=b.y
        if b.y < 0 :
            all_bullets.remove(b) 
    if X < 0:
        X=400
    elif X > 400:
        X=0
    for e in all_enemies:
        screen.blit(e.selectedimage,(e.x,e.y))
        e.y=e.y+0.05 
        e.rect.centery=e.y
        e.rect.centerx=e.x
    for b in all_bullets:
        for e in all_enemies:
            if b.rect.colliderect(e.rect):
                print("hit ditected")
                newexplosion=explosion.Explosion(x=e.x,y=e.y,enemy=e)
                all_explosions.append (newexplosion)
                all_enemies.remove(e)
                all_bullets.remove(b)
    for ex in all_explosions:
       ex.show(screen)
       if ex.finished==True:
           all_explosions.remove(ex) 
    if len(all_enemies)==0:
        for number in range(1,6):
            alien_enemy=enemy.enemy(health=10,x=0+number*50,y=10)
            all_enemies .append(alien_enemy  )
    pygame.display.flip()