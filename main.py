import pygame
import fileStuff

# display
pygame.init()
surface = pygame.display.set_mode(size=(800, 800))
pygame.display.set_caption(title="gaem")

# load
line = fileStuff.load(file="save.txt")

# game loop
clock = pygame.time.Clock()
deltaTime = 0
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False     

    # draw stuff    
    surface.fill(color=(30, 30, 30))

    # update surface
    pygame.display.flip()
    deltaTime = clock.tick(framerate=90) / 1000

# save and quit
fileStuff.save(file="save.txt", line=line)
pygame.quit()
