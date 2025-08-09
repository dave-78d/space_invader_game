import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
ROAD_WIDTH = 400
LANE_WIDTH = ROAD_WIDTH // 3
ROAD_LEFT = (WIDTH - ROAD_WIDTH) // 2
ROAD_RIGHT = ROAD_LEFT + ROAD_WIDTH

WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
FPS = 60

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game (No Images)")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 30)


class Car:
    def __init__(self, x, y, color):
        self.width = 50
        self.height = 100
        self.color = color
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def move(self, dx=0, dy=0):
        self.rect.move_ip(dx, dy)


class Player(Car):
    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > ROAD_LEFT:
            self.move(dx=-5)
        if keys[pygame.K_RIGHT] and self.rect.right < ROAD_RIGHT:
            self.move(dx=5)


class Enemy(Car):
    def __init__(self, lane, speed):
        x = ROAD_LEFT + LANE_WIDTH * lane + (LANE_WIDTH - 50) // 2
        y = -100
        super().__init__(x, y, RED)
        self.speed = speed

    def update(self):
        self.move(dy=self.speed)


def draw_road():
    screen.fill(GRAY)
    pygame.draw.rect(screen, (50, 50, 50), (ROAD_LEFT, 0, ROAD_WIDTH, HEIGHT))

    for i in range(0, HEIGHT, 40):
        for j in range(1, 3):
            pygame.draw.rect(
                screen,
                YELLOW,
                (
                    ROAD_LEFT + j * LANE_WIDTH - 5,
                    i,
                    10,
                    20,
                ),
            )


def game_over_screen(score):
    screen.fill(RED)
    game_over_text = font.render("GAME OVER", True, WHITE)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 40))
    screen.blit(score_text, (WIDTH // 2 - 100, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)


def main():
    player = Player(WIDTH // 2 - 25, HEIGHT - 120, BLUE)
    enemies = []
    enemy_timer = 0
    enemy_delay = 60
    score = 0
    speed_increment = 0.01
    running = True

    while running:
        clock.tick(FPS)
        keys = pygame.key.get_pressed()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(keys)

        if enemy_timer <= 0:
            lane = random.randint(0, 2)
            speed = 5 + score * speed_increment
            enemies.append(Enemy(lane, speed))
            enemy_timer = enemy_delay
        else:
            enemy_timer -= 1

        for enemy in enemies:
            enemy.update()

        enemies = [e for e in enemies if e.rect.top < HEIGHT + 100]

        # Collision detection
        for enemy in enemies:
            if player.rect.colliderect(enemy.rect):
                game_over_screen(score)
                running = False  # Don't restart the game automatically

        draw_road()
        player.draw(screen)

        for enemy in enemies:
            enemy.draw(screen)

        score += 1
        score_text = font.render(f"Score: {score}", True, GREEN)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
