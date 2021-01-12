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

    # print(winning_moves_player, winning_moves_ai)

    return winning_moves_player, winning_moves_ai

def generate_possible_moves(grid):
    n = 3
    possible_moves = []

    for i in range(n):
        for j in range(n):
            if grid[i][j].get_piece() is None:
                possible_moves.append([i, j])
    
    return possible_moves

def check_win(grid):
    n = 3
    for row in range(n):
        # if grid[row][0].get_piece() is not None or grid[row][1].get_piece() is not None or grid[row][2].get_piece() is not None: 
        if grid[row][0].get_piece() == grid[row][1].get_piece() == grid[row][2].get_piece():
            if grid[row][0].get_piece() == player:
                return 69
            elif grid[row][0].get_piece() == opponent:
                return -69
    
    for col in range(n):
        # if grid[0][col].get_piece() is not None or grid[1][col].get_piece() is not None or grid[2][col].get_piece() is not None: 
        if grid[0][col].get_piece() == grid[1][col].get_piece() == grid[2][col].get_piece():
            if grid[0][col].get_piece() == player:
                return 69
            elif grid[0][col].get_piece() == opponent:
                return -69

    if grid[1][1].get_piece() is not None:
        if grid[0][0].get_piece() == grid[1][1].get_piece() == grid[2][2].get_piece():
            if grid[0][0].get_piece() == player:
                return 69
            elif grid[0][0].get_piece() == opponent:
                return -69

        elif grid[0][2].get_piece() == grid[1][1].get_piece() == grid[2][0].get_piece():
            if grid[0][2].get_piece() == player:
                return 69
            elif grid[0][2].get_piece() == opponent:
                return -69
    
    return 0