import pygame
from random_move import random_move

from obj import Obj
pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tic Tac Toe")

dimension = 3


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def get_clicked_pos(pos, width, margin):
  row = pos[1] // (width + margin)
  col= pos[0] // (width+margin)

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


def check_row(grid):
    n = 3
    for row in range(n):
        if grid[row][0].get_piece() is not None or grid[row][1].get_piece() is not None or grid[row][2].get_piece() is not None: 
            if grid[row][0].get_piece() == grid[row][1].get_piece() == grid[row][2].get_piece():
                return True
    return False


def check_col(grid):
    n = 3
    for col in range(n):
        if grid[0][col].get_piece() is not None or grid[1][col].get_piece() is not None or grid[2][col].get_piece() is not None: 
            if grid[0][col].get_piece() == grid[1][col].get_piece() == grid[2][col].get_piece():
                return True
    return False

def check_diagonal(grid):
    n = 3

    if grid[1][1].get_piece() is not None:
        if grid[0][0].get_piece() == grid[1][1].get_piece() == grid[2][2].get_piece():
            return True
        elif grid[0][2].get_piece() == grid[1][1].get_piece() == grid[0][2].get_piece():
            return True
    return False

def check_win(grid):
    # print(check_col(grid) or check_row(grid) or check_diagonal(grid))
    print('row', check_row(grid))
    print('col', check_col(grid))
    print('diagonal', check_diagonal(grid))
    return check_col(grid) or check_row(grid) or check_diagonal(grid)


def get_clicked_pos(pos, width, margin):
  row = pos[1] // (width + margin)
  col= pos[0] // (width+margin)

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
            piece = 'X' if turn else 'O'    
            window.fill(WHITE)
            pygame.draw.rect(window, BLACK, area)

            # if check_win(grid):
            #     print('win')
            # else:
            #     random_move(grid, piece)
            #     turn = not turn

            if not check_win(grid):

                if not turn:
                    random_move(grid, piece)
                    turn = not turn

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    if event.button == 1:
                        if area.collidepoint(event.pos):
                            row, col = get_clicked_pos(pos, width, margin)
                            # print(row, col)
                            clicked(grid, row, col, piece)
                            turn = not turn
            else:
                print('win')

            

            # pygame.time.delay(200)

            draw_grid(width, dimension, margin, grid, window, turn)
            if event.type == pygame.QUIT:
                run = False
            pygame.display.flip()

    pygame.quit()
main(window, dimension)