import os
from tasks.board import generate_board
from tasks.game import (
    move_tile, check_game_over, find_available_moves,
    MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT)

from tasks.visualization import format_board, format_available_moves


KEYBOARD_TO_MOVE = {
    'w': MOVE_UP,
    's': MOVE_DOWN,
    'a': MOVE_LEFT,
    'd': MOVE_RIGHT,
}


def play_gem_puzzle_game():
    print('')
    board = generate_board()
    print(format_board(board))
    print(format_available_moves(find_available_moves(board)))

    while not check_game_over(board):
        print('-' * 100)
        print('To move a tile around the unoccupied position, '
              'press one of the following keys the keyword:')

        print('W - move up, S - move down, A - move left, D - move right')
        print('Type "exit" to quit the game.')
        print('-' * 100)

        key = ''
        while key not in KEYBOARD_TO_MOVE and key.lower() != 'exit':
            key = input('Please make a move: ').lower()

        if key.lower() == 'exit':
            break

        move = KEYBOARD_TO_MOVE[key]
        move_tile(board, move)

        os.system('cls' if os.name == 'nt' else 'clear')
        print(format_board(board))
        print(format_available_moves(find_available_moves(board)))

    print('Your game is over!')


if __name__ == '__main__':
    play_gem_puzzle_game()
