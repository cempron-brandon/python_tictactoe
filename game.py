import itertools
from colorama import Fore, Style, init


def show_board(header_display, game_board):
    print(header_display)
    for count, row in enumerate(game_board):
        colored_row = ""
        for item in row:
            if item == 0:
                colored_row += "   "
            elif item == 1:
                colored_row += Fore.GREEN + " X " + Style.RESET_ALL
            elif item == 2:
                colored_row += Fore.MAGENTA + " O " + Style.RESET_ALL
        print(count, colored_row)


def make_move(game_board, player, row, col):
    replaying = False
    try:
        if game_board[row][col] == 0:
            game_board[row][col] = player
        else:
            print("Position has already been selected! Select another one.")
            replaying = True
    except IndexError:
        print("Error: Row/column is out of range!")
    except TypeError:
        print("Error: Row/column should be an integer!")
    return game_board, replaying


def check_winner(game_board):
    def match_check(items):
        if items[0] != 0 and items.count(items[0]) == len(items):
            return True
        else:
            return False

    # Tie Check
    if all(0 not in row for row in game_board):
        print(f'No winner!')
        return True

    # Horizontal
    for row in game_board:
        if match_check(row):
            print(f'Horizontal match found (-). Player {row[0]} won!')
            return True

    # Vertical
    # for col in range(len(game_board)):
    #     check = []
    #     for row in game:
    #         check.append(row[col])
    #     if match_check(check):
    #         print(f'Vertical match found (|). Player {check[0]} won!')
    #         return True
    import numpy as np
    transposed_game_board = np.array(game_board).T.tolist()
    for col in transposed_game_board:
        if match_check(col):
            print(f'Vertical match found (|). Player {col[0]} won!')
            return True

    # Diagonal
    right_diagonal = []
    for col, row in enumerate(reversed(range(len(game_board)))):
        right_diagonal.append(game[row][col])
    if match_check(list(right_diagonal)):
        print(f'Right Diagonal match found (/). Player {right_diagonal[0]} won!')
        return True

    left_diagonal = []
    for idx in range(len(game_board)):
        left_diagonal.append(game[idx][idx])
    if match_check(left_diagonal):
        print(f'Left Diagonal match found (\\). Player {left_diagonal[0]} won!')
        return True

    return False


if __name__ == "__main__":
    init()
    play = True
    players = [1, 2]
    while play:
        game_size = input("Choose a board size (default: 3): ")
        if game_size == "":
            game_size = 3
        game = [[0 for j in range(int(game_size))] for i in range(int(game_size))]
        game_end = False
        player_choice = itertools.cycle(players)

        header = "\n   " + "  ".join(str(i) for i in range(int(game_size)))
        show_board(header, game)
        replay = True
        current_player = next(player_choice)
        while not game_end:
            if not replay:
                current_player = next(player_choice)
            print(f'\nPlayer {current_player}\'s turn.')
            row_select = input("Choose row (0,1,2): ")
            col_select = input("Choose column (0,1,2): ")
            game, replay = make_move(game, player=current_player, row=int(row_select), col=int(col_select))
            show_board(header, game)
            game_end = check_winner(game)

        again = input("Play again? (y/n) ")
        if again.lower() == 'y':
            print("\nRestarting Game...")
        elif again.lower() == 'n':
            play = False
            print("OK, Thanks for playing!")
        else:
            play = False
            print("Invalid. Closing game.")
