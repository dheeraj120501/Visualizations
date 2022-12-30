import pygame
import math
from queue import PriorityQueue
import constants as C
from constants import BlockState

canvas = pygame.display.set_mode((C.WIDTH, C.WIDTH))
pygame.display.set_caption("A* Path Finding Visualization")

class Block:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.x = row*width
        self.y = col*width
        self.state = BlockState.DEFAULT
        self.neighbors = []

    def get_pos(self):
        return self.row, self.col

    def get_state(self):
        return self.state

    def update_state(self, state):
        self.state = state

    def is_state(self, state):
        return self.state == state

    def get_color(self):
        return self.state.value

    def draw(self, canvas):
        pygame.draw.rect(canvas, self.state.value, (self.x, self.y, self.width, self.width))

    def update_neighbour(self, grid):
        self.neighbors = []

        if(self.row + 1 < self.total_rows and not grid[self.row + 1][self.col].is_state(BlockState.BARRIER)):
            self.neighbors.append(grid[self.row + 1][self.col])

        if(self.row - 1 > -1 and not grid[self.row - 1][self.col].is_state(BlockState.BARRIER)):
            self.neighbors.append(grid[self.row - 1][self.col])

        if(self.col + 1 < self.total_rows and not grid[self.row][self.col + 1].is_state(BlockState.BARRIER)):
            self.neighbors.append(grid[self.row][self.col + 1])

        if(self.col - 1 < -1 and not grid[self.row][self.col - 1].is_state(BlockState.BARRIER)):
            self.neighbors.append(grid[self.row][self.col - 1])
        

    def __lt__(self, other):
        pass

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return abs(x1-x2) + abs(y1-y2)

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            block = Block(i, j, gap, rows)
            grid[i].append(block)
    
    return grid

def draw_grid(canvas, rows, width):
    gap = width // rows

    for i in range(rows):
        pygame.draw.line(canvas, C.GREY, (0, i*gap), (width, i*gap))
        pygame.draw.line(canvas, C.GREY, (i*gap, 0), (i*gap, width))

def draw(canvas, grid, rows, width):
    canvas.fill(C.WHITE)

    for row in grid:
        for block in row:
            block.draw(canvas)

    draw_grid(canvas, rows, width)
    pygame.display.update()

def get_click_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap
    
    return row, col

def main(canvas, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    run = True
    find = False

    start = None
    end = None

    while run:
        draw(canvas, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if find:
                continue
            
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_click_pos(pos, ROWS, width)
                block: Block = grid[row][col]

                if block.is_state(BlockState.DEFAULT):
                    if not start:
                        block.update_state(BlockState.START)
                        start = block
                    elif not end:
                        block.update_state(BlockState.END)
                        end = block
                    else:
                        block.update_state(BlockState.BARRIER)

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_click_pos(pos, ROWS, width)
                block = grid[row][col]
                if(block.is_state(BlockState.START)):
                    start = None
                elif(block.is_state(BlockState.END)):
                    end = None
                block.update_state(BlockState.DEFAULT)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not find:
                    for row in grid:
                        for block in row:
                            block.update_neighbour(grid)



    pygame.quit()

main(canvas, C.WIDTH)

