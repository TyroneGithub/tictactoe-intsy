import random
from datetime import datetime
from helpers import generate_possible_moves
from helpers import check_win
player, opponent = 'X', 'O'


def state_check(grid):
    n = 3

    winning_moves_ai = []
    winning_moves_player = []

    for row in range(n):
        for col in range(n):
            if grid[row][col].get_piece() is None:
                grid[row][col].set_piece(player)
                if check_win(grid) == 69:
                    winning_moves_player.append([row, col]) 
                grid[row][col].set_piece(None)

                grid[row][col].set_piece(opponent)
                if check_win(grid) == -69:
                    winning_moves_ai.append([row, col])
                grid[row][col].set_piece(None)

    return winning_moves_player, winning_moves_ai



def random_move(grid, piece):
    possible_moves = generate_possible_moves(grid)
    
    moved = False

    while not moved:

        random.seed(random.randint(100,200))
        row = random.randint(0, 2)
        random.seed(random.randint(201,301))
        col = random.randint(0, 2)
        move = [row, col]

        moves_player, moves_ai = state_check(grid)

        if move in possible_moves:
            # if move in moves_player:
            if moves_player:
                row, col = moves_player[0]
            
            if moves_ai:
                row, col = moves_ai[0]
            
            
            grid[row][col].set_piece(piece)
            moved = True