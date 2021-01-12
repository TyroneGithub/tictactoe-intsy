from helpers import generate_possible_moves
from helpers import check_win
from helpers import state_check

player, opponent = 'X', 'O'


def level_one(grid, piece):
    possible_moves = generate_possible_moves(grid)
    moves_player, moves_ai = state_check(grid)
    corners = [[0, 0], [2, 0], [0, 2], [2, 2]]
    rest = [[0, 1], [1, 0], [1, 2], [2, 1]]

    # PRIORITY 1 : If agent is about to win
    if moves_ai:
        row, col = moves_ai[0]
        grid[row][col].set_piece(piece)
        return

    # PRIORITY 2 : If player is about to win
    if moves_player:
        row, col = moves_player[0]
        grid[row][col].set_piece(piece)
        return

    # PRIORITY 3 : If center of grid is available
    if [1, 1] in possible_moves:
        grid[1][1].set_piece(piece)
        return
    
    # PRIORITY 4 : If corners are available
    for ctr in range(4) :
        if corners[ctr] in possible_moves :
            row, col = corners[ctr]
            grid[row][col].set_piece(piece)
            return
    
    # PRIORITY 5 : Plot where available
    for ctr in range(4) :
        if corners[ctr] in possible_moves :
            row, col = corners[ctr]
            grid[row][col].set_piece(piece)
            return


    

    