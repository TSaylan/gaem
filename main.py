import pygame

# display
pygame.init()
surface = pygame.display.set_mode((800, 800))
pygame.display.set_caption("")

# load
with open("save", "rt") as file:
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
    surface.fill((80, 80, 80))

    pygame.draw.circle(surface, (160, 160, 160), player, 50.0)

    # update surface
    pygame.display.flip()
    deltaTime = clock.tick(60) / 1000

# save and quit
line[0] = player.x
line[1] = player.y

with open("save", "wt") as file:
    file.write('\n'.join(line))
            
pygame.quit()
