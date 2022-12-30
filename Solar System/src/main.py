import pygame
import math
import constants as C

canvas = pygame.display.set_mode((C.WIDTH, C.HEIGHT))
pygame.display.set_caption("Solar System Simulation")

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


    pygame.quit()

main()
