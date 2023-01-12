from re import fullmatch

PLAYER_O = "O"
PLAYER_X = "X"
REGEX_PATTERN = "[0-9][ ][0-9]"
INITIAL_ARRAY = " " * 9


def print_array(array):
    print(f"""---------
| {array[0][0]} {array[0][1]} {array[0][2]} |
| {array[1][0]} {array[1][1]} {array[1][2]} |
| {array[2][0]} {array[2][1]} {array[2][2]} |
---------""")


def row_win(player, array):
    array_to_calc = ["".join(i) for i in array]
    winning_com = sum([1 if row == player * 3 else 0 for row in array_to_calc])
    return winning_com


def col_win(player, array):
    array_to_calc = ["".join([array[0][i], array[1][i], array[2][i]]) for i in range(3)]
    winning_com = sum([1 if row == player * 3 else 0 for row in array_to_calc])
    return winning_com


def diag_down_win(player, array):
    array_to_calc = "".join([array[0][0], array[1][1], array[2][2]])
    winning_com = 1 if array_to_calc == player * 3 else 0
    return winning_com


def diag_up_win(player, array):
    array_to_calc = "".join([array[0][2], array[1][1], array[2][0]])
    winning_com = 1 if array_to_calc == player * 3 else 0
    return winning_com


def check_wins(player, array):
    """ If the passed string is correct there are four types of winning patterns:
        - row win
        - column win
        - diagonal downward
        - diagonal upward

        More than one row or column winning combination is forbidden.

        For every type of winning pattern a separate array must be created."""

    winning_chart = [row_win(player, array),
                     col_win(player, array),
                     diag_up_win(player, array),
                     diag_down_win(player, array)]

    if any(winning_chart):
        return sum(winning_chart)
    else:
        return False


def game(player_X, player_O, array):

    player_to_play = player_X
    player_to_wait = player_O

    print_array(array)

    print("Type in coordinates: ('q' - exits the game)")

    while True:
        player_input = input()
        if player_input == "q":
            break

        # we could change a bit REGEX_PATTERN to enclose the next condition
        # but we have to print "Coordinates should be from 1 to 3!" ;)
        if not fullmatch(REGEX_PATTERN, player_input):
            print("You should enter numbers!")
            continue

        player_input = [int(x) for x in player_input.split()]

        if any(x for x in player_input if x not in range(1, 4)):
            print("Coordinates should be from 1 to 3!")
            continue

        row, col = player_input[0] - 1, player_input[1] - 1

        if array[row][col] == " ":
            array[row][col] = player_to_play

            print_array(array)

            if check_wins(player_to_play, array):
                print(f"{player_to_play} wins")
                break
            elif "".join([array[i][j] for i in range(3) for j in range(3)]).count(" ") == 0:
                print("Draw")
                break
            else:
                player_to_play, player_to_wait = player_to_wait, player_to_play
        else:
            print("This cell is occupied! Choose another one!")
            continue


if __name__ == "__main__":

    array = [[x for x in INITIAL_ARRAY[i:i + 3]] for i in range(0, 7, 3)]

    game(PLAYER_X, PLAYER_O, array)
