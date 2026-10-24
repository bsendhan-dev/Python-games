import random
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
stars = [[random.randint(0, 600), random.randint(0, 600), random.randint(1, 3)] for _ in range(50)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for star in stars:
        star[1] += star[2]
        if star[1] > 600:
            star[1] = 0
            star[0] = random.randint(0, 600)
        pygame.draw.circle(screen, (255, 255, 255), (star[0], star[1]), 2)

    pygame.draw.rect(screen, (0, 255, 0), (250, 300, 100, 100), 3)
    pygame.draw.line(screen, (0, 0, 255), (300, 220), (250, 300), 3)
    pygame.draw.line(screen, (0, 0, 255), (300, 220), (350, 300), 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
