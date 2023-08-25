import pygame

# display
pygame.init()
surface = pygame.display.set_mode((800, 800))
pygame.display.set_caption("gaem")

# load
try:
    with open("save.txt", "rt") as file:
        line = file.readlines()

except FileNotFoundError:
    with open("save.txt", "wt") as file:
        file.writelines("400\n400\n")
    with open("save.txt", "rt") as file:
        line = file.readlines()

while len(line) < 2:
    line.append("400\n")

for i in range(len(line)):
    line[i] = line[i].strip()
    if not line[i]:
        line[i] = 0

# make player
player = pygame.Vector2(int(line[0]), int(line[1]))
playerRect = pygame.Rect(0, 0, 100, 100)

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

    playerRect.center = player

    # draw stuff    
    surface.fill((30, 30, 30))

    pygame.draw.rect(surface, (255, 69, 0), playerRect)

    # update surface
    pygame.display.flip()
    deltaTime = clock.tick(90) / 1000

# save and quit
line[0] = int(player.x)
line[1] = int(player.y)

with open("save.txt", "wt") as file:
    for i in range(len(line)):
        file.writelines(str(line[i]) + "\n")
            
pygame.quit()
