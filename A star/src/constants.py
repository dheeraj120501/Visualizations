from enum import Enum

WIDTH = 800

RED = (255,0,0)
GREEN = (0, 255, 0)
BLUE = (8, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class BlockState(Enum):
    DEFAULT = WHITE
    START = ORANGE
    OPEN = GREEN
    CLOSE = RED
    BARRIER = BLACK
    END = TURQUOISE
    PATH = PURPLE