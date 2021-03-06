import random
from datetime import datetime
from helpers import generate_possible_moves
from helpers import check_win
from helpers import state_check

player, opponent = 'X', 'O'

def random_move(grid, piece, is_ai):
    possible_moves = generate_possible_moves(grid)
    moved = False

    while not moved:
        random.seed(random.randint(100,200))
        row = random.randint(0, 2)

        random.seed(random.randint(201,301))
        col = random.randint(0, 2)
        
        move = [row, col]

        moves_player, moves_ai = state_check(grid, is_ai)

        if move in possible_moves:

            if moves_player:
                row, col = moves_player[0]
            
            if moves_ai:
                row, col = moves_ai[0]
            
            grid[row][col].set_piece(piece)
            moved = True