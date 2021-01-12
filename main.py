import pygame

from helpers import check_win
from helpers import generate_possible_moves

from random_move import random_move
from minimax import gen_best_move
from level1 import levelOneMove

from obj import Obj

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tic Tac Toe")

player, opponent = 'X', 'O'

dimension = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def get_clicked_pos(pos, width, margin):
  row = pos[1] // (width + margin)
  col = pos[0] // (width + margin)

  return row, col

def init_grid(dimension):
    grid = []

    for row in range(dimension):
        grid.append([])

        for col in range(dimension):
            piece = Obj(row, col)
            grid[row].append(piece)

    return grid

def draw_grid(width, dim, margin, grid, win, turn):
    for row in range(dim):
        for col in range(dim):
            # color = grid[row][col].get_color()
            image = None
            rect = pygame.draw.rect(win, WHITE, [(margin + width) * col + margin,
                    (margin + width) * row + margin,width,width])

            if grid[row][col].get_piece() is not None:
                if grid[row][col].get_piece() == 'X':
                    image = pygame.image.load('images/x.png').convert()
                elif grid[row][col].get_piece() == 'O':
                    image = pygame.image.load('images/O.png').convert()

            if image is not None:
                image = pygame.transform.scale(image, ((margin*2 + width),
                        (margin*2 + width)))
                win.blit(image, rect)

def get_clicked_pos(pos, width, margin):
    row = pos[1] // (width + margin)
    col = pos[0] // (width + margin)

    return row, col

def clicked(grid, row, col, piece):
    if grid[row][col].get_piece() is None:
        grid[row][col].set_piece(piece)

def main(window, dimension):
    grid = init_grid(dimension)
    area_w = 800
    width = area_w // (dimension * 2)
    margin = 2
    turn = True
    run = True
    area = pygame.Rect(0, 0, (margin + width) * dimension + margin, (margin + width) * dimension + margin)
    # grid[0][0].set_piece('X')
    # grid[0][1].set_piece('X')
    # grid[0][2].set_piece('X')
    while run:
        for event in pygame.event.get():
            piece = player if turn else opponent    
            window.fill(WHITE)
            pygame.draw.rect(window, BLACK, area)
            
            if not check_win(grid) and generate_possible_moves(grid):
                if not turn:
                    # random_move(grid, piece)
                    # levelOneMove(grid, piece)
                    x, y = gen_best_move(grid)
                    grid[x][y].set_piece(piece)
                    turn = not turn

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    if event.button == 1:
                        if area.collidepoint(event.pos):
                            row, col = get_clicked_pos(pos, width, margin)
                            # print(row, col)
                            clicked(grid, row, col, piece)
                            turn = not turn

            elif check_win(grid):
                piece = 'X' if not turn else 'O'
                # print(piece, 'win')

            else:
                pass
                # print('draw')
                
            draw_grid(width, dimension, margin, grid, window, turn)

            if event.type == pygame.QUIT:
                run = False

            pygame.display.flip()

    pygame.quit()

main(window, dimension)