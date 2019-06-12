#!/usr/bin/env python
# Tik-Tac-Toe
r"""
I have created a Tic Tac Toe game that can be played between 2 people \n.

After each game, the scoreboard will be updated and you can either \n.
choose to play another game, or exit out when done.

Logan Riggers
"""


def print_board(game_board):
    """Create a function to make a game board."""
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            print(game_board[i][j], end="")
        print()


def make_board():
    """Create a function to make a 3x3 grid."""
    game_board = ["-"] * 3
    for i in range(3):
        game_board[i] = ["-"] * 3
    return game_board


def make_upper(sentence):
    """."""
    new_string = ""
    for i in range(len(sentence)):
        if ord(sentence[i]) >= 97 and ord(sentence[i]) <= 122:
            upper = ord(sentence[i]) - 32
            new_string += chr(upper)
        else:
            new_string += sentence[i]
    return new_string


def handle_input(user_input):
    """."""
    if len(user_input) == 1:
        count = 0
        if ord(user_input) < ord("1") or ord(user_input) > ord("3"):
            count += 1
        if count == 0:
            return True
        else:
            return False


def get_input():
    """Create a function to check for bad input."""
    while True:
        user_in_x = input("Enter which column: ")
        if handle_input(user_in_x) == False:
            print("Bad input, try again")
        else:
            break
    while True:
        user_in_y = input("Enter which row: ")
        if handle_input(user_in_y) == False:
            print("Bad input, try again")
        else:
            break
    return user_in_x, user_in_y


def refresh_board(board):
    """Refresh the board."""
    print_board(board)


def take_turn(player, board):
    """Create a function tto place tthe x's and o's."""
    if player == "1":
        mark = "O"
    else:
        mark = "X"
    print(mark + "'s turn")

    while True:
        user_in_x, user_in_y = get_input()
        check_x = int(user_in_x) - 1
        check_y = int(user_in_y) - 1

        if board[int(check_y)][int(check_x)] == "-":
            board[int(check_y)][int(check_x)] = mark
            break
        else:
            print("This position is already taken")

    refresh_board(board)
    return check_x, check_y


def check_winner(board):
    """Create a function to check for a winner."""
    for i in range(0, 3):

        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] != "-":
                return True

        elif board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] != "-":
                return True

        elif board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] != "-":
                return True

        elif board[2][0] == board[1][1] == board[0][2]:
            if board[2][0] != "-":
                return True


def change_player(player):
    """."""
    if player == "0":
        player = "1"
    else:
        player = "0"
    return player


def incriment_wins(player, xwins_, ywins_):
    """Create a function to incriment wins."""
    if player == "0":
        xwins_ += 1
    else:
        ywins_ += 1
    return xwins_, ywins_


def run_game(player):
    """Create a function to add points to the players."""
    game_board = make_board()
    print_board(game_board)
    turn = 0
    while True:
        take_turn(player, game_board)  # Player 1 = X Player 2 = O
        if check_winner(game_board) == True:
            return player, "win"

        turn += 1

        if turn == 9 and check_winner(game_board) != False:
            print("It's a draw")
            return player, "tie"

        player = change_player(player)


def congratulate(player, name1, name2):
    """Create a function to congradulate the winner."""
    if player == 0:
        print("Congratulations " + name2)
    else:
        print("Congratulations " + name1)


def main():
    """Create a main function."""
    player = "0"
    xwins_, ywins_, ties = 0, 0, 0

    player1_name = input("Enter name for player 1 (X): ")

    player2_name = input("Enter name for player 2 (O): ")

    while True:
        player, result = run_game(player)

        if result == "tie":
            ties += 1
        else:
            xwins_, ywins_ = incriment_wins(player, xwins_, ywins_)
            congratulate(player, player1_name, player2_name)

        print(
            player1_name
            + " has won "
            + str(xwins_)
            + " game[s] | "
            + player2_name
            + " has won "
            + str(ywins_)
            + " game[s] | "
            + "There has been "
            + str(ties)
            + " tie[s]."
        )

        playagain_ = input("Type Y to play again, or enter anything else to quit: ")
        if make_upper(playagain_) != "Y":
            break


main()
