import pygame
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
                if not turn:
                    image = pygame.image.load('images/x.png').convert()
                else:
                    image = pygame.image.load('images/O.png').convert()

            if image is not None:
                image = pygame.transform.scale(image, ((margin*2 + width),
                        (margin*2 + width)))
                win.blit(image, rect)



def main(window, dimension):
    grid = init_grid(dimension)
    area_w = 800
    width = area_w // (dimension * 2)
    margin = 2
    turn = None
    run = True
    area = pygame.Rect(0, 0, (margin + width) * dimension + margin, (margin + width) * dimension + margin)

    while run:
        for event in pygame.event.get():
            window.fill(WHITE)
            pygame.draw.rect(window, BLACK, area)

            draw_grid(width, dimension, margin, grid, window, turn)
            if event.type == pygame.QUIT:
                run = False
            pygame.display.flip()

    pygame.quit()
main(window, dimension)