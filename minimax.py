from helpers import check_win
from helpers import generate_possible_moves


def minimax(grid, depth, is_max, player, opponent, is_ai):
    score = check_win(grid, is_ai)
    n = 3
    if score == 10:
        return score - depth
    
    if score == -10:
        return score + depth

    if score == 0:
        return score

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


def gen_best_move(grid, piece, is_ai):
    best = -1000
    best_move = [-100, -100]
    n = 3
    player = 'X' if not is_ai else 'O'
    opponent = 'O' if not is_ai else 'X'
    # p = player if not is_ai else opponent

    #

    for row in range(n):
        for col in range(n):

            if grid[row][col].get_piece() is None:
                
                grid[row][col].set_piece(player)
                move = minimax(grid, 0, False, player, opponent, is_ai)
                grid[row][col].set_piece(None)

                if move > best:
                    best_move = [row, col]
                    best = move
    row, col = best_move
    grid[row][col].set_piece(piece)

