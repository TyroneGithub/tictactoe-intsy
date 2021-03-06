from helpers import generate_possible_moves
from helpers import check_win
from helpers import state_check


def level_one(grid, piece, is_ai):
    possible_moves = generate_possible_moves(grid)
    moves_player, moves_ai = state_check(grid, is_ai)
    corners = [[0, 0], [0, 2], [2, 0], [2, 2]]
    rest = [[0, 1], [1, 0], [1, 2], [2, 1]]

    print(moves_player)

    # PRIORITY 1 : If agent is about to win
    if moves_ai:
        print('haha')
        row, col = moves_ai[0]
        grid[row][col].set_piece(piece)
        return

    # PRIORITY 2 : If player is about to win
    if moves_player:
        print('hehe')
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
    row, col = possible_moves[0]
    grid[row][col].set_piece(piece)