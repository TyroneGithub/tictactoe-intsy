# player, opponent = 'X', 'O'

def state_check(grid, is_ai):
    n = 3
    player = 'X' if not is_ai else 'O'
    opponent = 'O' if not is_ai else 'X'
    winning_moves_ai = []
    winning_moves_player = []

    for row in range(n):
        for col in range(n):
            if grid[row][col].get_piece() is None:
                grid[row][col].set_piece(player)

                if check_win(grid, is_ai) == 10:
                    winning_moves_player.append([row, col])

                grid[row][col].set_piece(None)
                grid[row][col].set_piece(opponent)

                if check_win(grid, is_ai) == -10:
                    winning_moves_ai.append([row, col])

                grid[row][col].set_piece(None)

    return winning_moves_player, winning_moves_ai

def generate_possible_moves(grid):
    n = 3
    possible_moves = []

    for i in range(n):
        for j in range(n):
            if grid[i][j].get_piece() is None:
                possible_moves.append([i, j])
    
    return possible_moves

def check_win(grid, is_ai):
    player = 'X' if not is_ai else 'O'
    opponent = 'O' if not is_ai else 'X'
    for row in range(3):
        if grid[row][0].get_piece() == grid[row][1].get_piece() and grid[row][1].get_piece() == grid[row][2].get_piece():
            if grid[row][0].get_piece() == player:
                return 10
            elif grid[row][0].get_piece() == opponent:
                return -10
    
    for col in range(3):
        if grid[0][col].get_piece() == grid[1][col].get_piece() and grid[1][col].get_piece() == grid[2][col].get_piece():
            if grid[0][col].get_piece() == player:
                return 10
            elif grid[0][col].get_piece() == opponent:
                return -10
    

    if grid[0][0].get_piece() == grid[1][1].get_piece() and grid[1][1].get_piece() == grid[2][2].get_piece():
        if grid[0][0].get_piece() == player:
            return 10
        elif grid[0][0].get_piece() == opponent:
            return -10
    
    if grid[0][2].get_piece() == grid[1][1].get_piece() and grid[1][1].get_piece() == grid[2][0].get_piece():
        if grid[0][2].get_piece() == player:
            return 10
        elif grid[0][2].get_piece() == opponent:
            return -10
    
    return 0