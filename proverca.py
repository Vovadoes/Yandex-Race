import pygame

x = 0
running = True
directions = {"right": False, "left": False}
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                directions['right'] = True
            elif event.key == pygame.K_LEFT:
                directions['left'] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                directions['right'] = False
            elif event.key == pygame.K_LEFT:
                directions['left'] = False
    if directions['right']:
        x += 3
    if directions['left']:
        x -= 3