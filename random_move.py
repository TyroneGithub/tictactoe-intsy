import random
from datetime import datetime
def random_move(grid, piece):
    random.seed(random.randint(100,200))
    row = random.randint(0, 2)
    random.seed(random.randint(201,301))
    col = random.randint(0, 2)
    
    if grid[row][col].get_piece() is None:
        grid[row][col].set_piece(piece)
        return
    elif None not in grid:
        return
    else:
        random_move(grid, piece)
        return