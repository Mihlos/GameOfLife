import pygame
import numpy as np
import time

from config import sizeConfig, colorConfig

# Initialize PyGame
pygame.init()

# Set size of screen
screen = pygame.display.set_mode([sizeConfig.width, sizeConfig.height])


# Alive = 1; Dead = 0
# Intialize status of cells
status = np.zeros((sizeConfig.nX, sizeConfig.nY))

pauseRun = False
running = True

while running:

    newStatus = np.copy(status)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            pauseRun = not pauseRun

        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            x, y = int(np.floor(posX / sizeConfig.xSize)), int(
                np.floor(posY / sizeConfig.ySize)
            )
            newStatus[x, y] = not mouseClick[2]

    # Clen screen
    screen.fill(colorConfig.bg)

    for x in range(0, sizeConfig.nX):
        for y in range(0, sizeConfig.nY):

            if not pauseRun:

                # Number of neightbours
                # % to toroidal behavour
                nNeigh = (
                    status[(x - 1) % sizeConfig.nX, (y - 1) % sizeConfig.nY]
                    + status[(x) % sizeConfig.nX, (y - 1) % sizeConfig.nY]
                    + status[(x + 1) % sizeConfig.nX, (y - 1) % sizeConfig.nY]
                    + status[(x - 1) % sizeConfig.nX, (y) % sizeConfig.nY]
                    + status[(x + 1) % sizeConfig.nX, (y) % sizeConfig.nY]
                    + status[(x - 1) % sizeConfig.nX, (y + 1) % sizeConfig.nY]
                    + status[(x) % sizeConfig.nX, (y + 1) % sizeConfig.nY]
                    + status[(x + 1) % sizeConfig.nX, (y + 1) % sizeConfig.nY]
                )

                # Rule 1: Dead cell with 3 neighbours comes alive
                if status[x, y] == 0 and nNeigh == 3:
                    newStatus[x, y] = 1

                # Rule 2: Alive cell with more than 3 neigh. or less than 2 -> x_x
                elif status[x, y] == 1 and (nNeigh < 2 or nNeigh > 3):
                    newStatus[x, y] = 0

            poly = [
                (x * sizeConfig.xSize, y * sizeConfig.ySize),
                ((x + 1) * sizeConfig.xSize, y * sizeConfig.ySize),
                ((x + 1) * sizeConfig.xSize, (y + 1) * sizeConfig.ySize),
                (x * sizeConfig.xSize, (y + 1) * sizeConfig.ySize),
            ]

            if newStatus[x, y] == 1:
                pygame.draw.polygon(screen, colorConfig.live, poly, 0)
            else:
                pygame.draw.polygon(screen, colorConfig.dead, poly, 1)

    status = np.copy(newStatus)
    time.sleep(0.1)
    pygame.display.flip()


pygame.quit()
