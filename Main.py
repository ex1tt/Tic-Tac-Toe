#  Tic Tac Toe by ex1tt
#  https://github.com/ex1tt
#  Video that helped me build https://www.youtube.com/watch?v=pc7XhHxSgrM&ab_channel=CodingSpot

import pygame
import sys
import numpy

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLUMNS = 3
SQUARE_WIDTH = 100
SQUARE_HEIGHT = 100
BG_COLOR = (28, 170, 156)
LINE_COLOR = (20, 133, 123)
SQUARE_1_COLOR = (57, 54, 54)
SQUARE_2_COLOR = (192, 192, 192)
WINNING_LINE_WIDTH = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

board = numpy.zeros((BOARD_ROWS, BOARD_COLUMNS))


def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (20, 200), (580, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (20, 400), (580, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 20), (200, 580), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 20), (400, 580), LINE_WIDTH)


def draw_icon():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == 1:
                pygame.draw.rect(screen, SQUARE_1_COLOR,
                                 (int(col * 200 + 50, ), int(row * 200 + 50), SQUARE_WIDTH, SQUARE_HEIGHT,))

            elif board[row][col] == 2:
                pygame.draw.rect(screen, SQUARE_2_COLOR,
                                 (int(col * 200 + 50, ), int(row * 200 + 50), SQUARE_WIDTH, SQUARE_HEIGHT))


def mark_square(row, col, player):
    board[row][col] = player


def square_is_available(row, col):
    return board[row][col] == 0  # will return True or False


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == 0:
                return False
    return True


def check_win(player):
    # vertical win check
    for col in range(BOARD_COLUMNS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_line(col, player)
            return True

        # horizontal win check
        for row in range(BOARD_ROWS):
            if board[row][0] == player and board[row][1] == player and board[row][2] == player:
                draw_horizontal_line(row, player)
                return True

    # asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    # des diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_des_diagonal(player)
        return True

    return False


def draw_vertical_line(col, player):
    if player == 1:
        winning_color = SQUARE_1_COLOR
    elif player == 2:
        winning_color = SQUARE_2_COLOR

    pos_x = col * 200 + 100

    pygame.draw.line(screen, winning_color, (pos_x, 15), (pos_x, HEIGHT - 15), WINNING_LINE_WIDTH)


def draw_horizontal_line(row, player):
    if player == 1:
        winning_color = SQUARE_1_COLOR
    elif player == 2:
        winning_color = SQUARE_2_COLOR

    pos_y = row * 200 + 100

    pygame.draw.line(screen, winning_color, (15, pos_y), (WIDTH - 15, pos_y), WINNING_LINE_WIDTH)


def draw_asc_diagonal(player):
    if player == 1:
        winning_color = SQUARE_1_COLOR
    elif player == 2:
        winning_color = SQUARE_2_COLOR

    pygame.draw.line(screen, winning_color, (15, HEIGHT - 15), (WIDTH - 15, 15), WINNING_LINE_WIDTH)


def draw_des_diagonal(player):
    if player == 1:
        winning_color = SQUARE_1_COLOR
    elif player == 2:
        winning_color = SQUARE_2_COLOR

    pygame.draw.line(screen, winning_color, (15, 15), (WIDTH - 15, HEIGHT - 15), WINNING_LINE_WIDTH)


def restart_app():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            board[row][col] = 0


draw_lines()

player = 1
game_over = False

# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouse_x = event.pos[0]  # x
            mouse_y = event.pos[1]  # y

            clicked_row = int(mouse_y) // 200
            clicked_col = int(mouse_x) // 200

            if square_is_available(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2

                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1

                draw_icon()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_app()
                player = 1
                game_over = False

    pygame.display.update()
