import random
from datetime import datetime


def generate_possible_moves(grid):
    
    n = 3
    possible_moves = []

    for i in range(n):
        for j in range(n):
            if grid[i][j].get_piece() is None:
                possible_moves.append([i, j])
    
    return possible_moves

def random_move(grid, piece):
    possible_moves = generate_possible_moves(grid)
    
    moved = False

    while not moved:

        random.seed(random.randint(100,200))
        row = random.randint(0, 2)
        random.seed(random.randint(201,301))
        col = random.randint(0, 2)
        move = [row, col]
        
        if move in possible_moves:
            grid[row][col].set_piece(piece)
            moved = True