from helpers import check_win
from helpers import generate_possible_moves
player, opponent = 'X', 'O'


def minimax(grid, depth, is_max):
    score = check_win(grid)
    n = 3
    if score == 69:
        return score
    
    if score == -69:
        return score

    if not generate_possible_moves(grid):
        print('no moves', depth)
        return 0

    if is_max:
        best = -1000

        for row in range(n):
            for col in range(n):
                if grid[row][col].get_piece() is None:
                    grid[row][col].set_piece(player)
                    score = minimax(grid, depth + 1, False)
                    best = max(best, score)
                    grid[row][col].set_piece(None)

        return best

    else:
        best = 1000 
        for row in range(n):
            for col in range(n):
                if grid[row][col].get_piece() is None:
                    grid[row][col].set_piece(opponent)
                    score = minimax(grid, depth + 1, True)
                    best = min(best, score)
                    grid[row][col].set_piece(None)

        return best


def gen_best_move(grid):
    best = -1000
    best_move = [-100, -100]
    n = 3
    for row in range(n):
        for col in range(n):

            if grid[row][col].get_piece() is None:
                
                grid[row][col].set_piece(player)
                move = minimax(grid, 0, False)
                grid[row][col].set_piece(None)

                if move > best:
                    best_move = [row, col]
                    best = move
    
    return best_move


