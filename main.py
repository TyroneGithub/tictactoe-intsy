import pygame

from helpers import check_win
from helpers import generate_possible_moves

from random_move import random_move
from minimax import gen_best_move
from level1 import level_one

from obj import Obj
from gui import GUI

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tic Tac Toe")

player, opponent = 'X', 'O'

dimension = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 128, 255)


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
                image = pygame.transform.scale(image, ((width),
                        (width)))
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
    margin = 5
    turn = True
    run = True
    area = pygame.Rect(0, 0, (margin + width) * dimension + margin, (margin + width) * dimension + margin)
    font = pygame.font.SysFont('Arial', 18)
    ai_level = None

    texts = ['Level 0: Random', 'Level 1: Hardcoded', 'Level 2: Game Tree']
    text, rect = GUI.text_list_setup(texts, font, [WHITE, WHITE, WHITE], 555, 250)
    reset, reset_rect = GUI.text_setup('Reset', font, 555, 200, WHITE)
    game_status = 'No AI Level indicated'

    while run:

        status, status_rect = GUI.text_setup(game_status, font, 515, 170, BLACK)

        for event in pygame.event.get():
            window.fill(WHITE)
            pygame.draw.rect(window, BLACK, area)
            piece = player if turn else opponent    
            
            rect[0].width = 180
            rect[0].height = 35
            rect[0].center = (515, 50)
            pygame.draw.rect(window, BLUE, rect[0])

            rect[1].width = 180
            rect[1].height = 35
            rect[1].center = (515, 90)
            pygame.draw.rect(window, BLUE, rect[1])
            
            rect[2].width = 180
            rect[2].height = 35
            rect[2].center = (515, 130)
            pygame.draw.rect(window, BLUE, rect[2])

            reset_rect.width = 180
            reset_rect.height = 35
            reset_rect.center = (515, 220)
            pygame.draw.rect(window, BLUE, reset_rect)

            GUI.render_text([reset], [reset_rect], window)
            GUI.render_text(text, rect, window)
            GUI.render_text([status], [status_rect], window)

            if ai_level is not None:
                if not check_win(grid) and generate_possible_moves(grid):
                    if not turn:
                        ai_level(grid, piece)
                        # random_move(grid, piece)
                        # levelOneMove(grid, piece)
                        # x, y = gen_best_move(grid, piece)
                        # grid[x][y].set_piece(piece)
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
                    ai_level = None
                    print(piece, 'win')

                else:
                    ai_level = None
                    print('draw')
            # else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if rect[0].collidepoint(pos):
                    ai_level = random_move
                    game_status = 'Random'

                if rect[1].collidepoint(pos):
                    ai_level = level_one
                    game_status = 'Level One'
                
                if rect[2].collidepoint(pos):
                    ai_level = gen_best_move
                    game_status = 'Minimax'

                if reset_rect.collidepoint(pos):
                    main(window, dimension)
                    return
                
            draw_grid(width, dimension, margin, grid, window, turn)

            if event.type == pygame.QUIT:
                run = False

            pygame.display.flip()

    pygame.quit()

main(window, dimension)