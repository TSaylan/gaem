import game
import fileStuff

# display
game.pygame.init()
surface = game.pygame.display.set_mode(size=(800, 800))
game.pygame.display.set_caption(title="gaem")

# load
line = fileStuff.load(file="save.txt")

# game loop
clock = game.pygame.time.Clock()
deltaTime = 0
RUNNING = True
while RUNNING:
    for event in game.pygame.event.get():
        if event.type == game.pygame.QUIT:
            RUNNING = False     

    # draw stuff    
    surface.fill(color=(30, 30, 30))

    # update surface
    game.pygame.display.flip()
    deltaTime = clock.tick(framerate=90) / 1000

# save and quit
fileStuff.save(file="save.txt", line=line)
game.pygame.quit()
