import pygame
from vector import Vector  

pygame.init()


screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


fish_img = pygame.image.load('fish.jpg')
fish_img = pygame.transform.scale(fish_img, (50, 50))


position = Vector(400, 300)
velocity = Vector(1, 1)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill((0, 128, 255))

    
    position += velocity

    
    screen.blit(fish_img, (position.x, position.y))

   
    pygame.display.flip()

    
    clock.tick(60)

pygame.quit()
