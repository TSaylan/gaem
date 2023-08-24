import pygame

# display
pygame.init()
surface = pygame.display.set_mode((800, 800))
pygame.display.set_caption("")

# load
with open("save.txt", "rt") as file:
    line = file.readlines()

for i in range(len(line)):
    line[i] = line[i].strip()

x = int(line[0])
y = int(line[1])

# make player
player = pygame.Vector2(x, y)

# game loop
clock = pygame.time.Clock()
deltaTime = 0
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            
    # player movement
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player.y -= 300 * deltaTime
    if key[pygame.K_s]:
        player.y += 300 * deltaTime
    if key[pygame.K_a]:
        player.x -= 300 * deltaTime
    if key[pygame.K_d]:
        player.x += 300 * deltaTime

    # draw stuff    
    surface.fill((19, 42, 19))

    pygame.draw.circle(surface, (236, 243, 158), player, 50.0)

    # update surface
    pygame.display.flip()
    deltaTime = clock.tick(60) / 1000

# save and quit
line[0] = int(player.x)
line[1] = int(player.y)

with open("save.txt", "wt") as file:
    for i in range(len(line)):
        file.writelines(str(line[i]) + "\n")
            
pygame.quit()
