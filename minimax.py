from helpers import check_win
from helpers import generate_possible_moves
player, opponent = 'X', 'O'

def minimax(grid, depth, is_max):
    score = check_win(grid)
    n = 3
    if score == 10:
        return score
    
    if score == -10:
        return score

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


def gen_best_move(grid, piece):
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
    row, col = best_move
    grid[row][col].set_piece(piece)


# def gen_best_move(grid, piece):
#     best_score = -1000
#     best_move = None

#     for move in generate_possible_moves(grid):
#         row, col = move
#         grid[row][col].set_piece(piece)
#         score = minimax(grid, False)
#         grid[row][col].set_piece(None)

#         if score > best_score:
#             best_score = score
#             best_move = move

#     grid[row][col].set_piece(piece)

# def minimax(grid, is_max):
#     score = check_win(grid)
#     piece = player if is_max else opponent
#     if score == 10:
#         return score

#     if score == -10:
#         return score

#     if score == 0:
#         return score

    
#     scores = []

#     for move in generate_possible_moves(grid):
#         row, col = move

#         grid[row][col].set_piece(piece)
#         scores.append(minimax(grid, not is_max))
#         grid[row][col].set_piece(None)

#     return max(scores) if is_max else min(scores)
