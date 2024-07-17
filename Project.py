import random
import time

easy_boards = [
    [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ],
    [
        [9, 0, 2, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 7, 0, 0, 4, 0, 9],
        [0, 7, 0, 9, 0, 0, 0, 6, 1],
        [4, 0, 6, 0, 5, 0, 8, 3, 2],
        [2, 1, 8, 0, 0, 0, 0, 4, 5],
        [7, 0, 3, 0, 8, 4, 0, 9, 0],
        [5, 3, 0, 6, 0, 0, 9, 0, 4],
        [6, 0, 9, 0, 0, 1, 0, 5, 0],
        [0, 0, 0, 5, 4, 0, 0, 1, 0],
    ],
    [
        [0, 7, 2, 0, 0, 4, 0, 5, 3],
        [0, 4, 9, 0, 1, 0, 0, 8, 2],
        [8, 0, 0, 2, 5, 7, 9, 6, 0],
        [0, 0, 0, 7, 4, 0, 0, 0, 0],
        [0, 0, 7, 8, 0, 0, 6, 4, 9],
        [0, 8, 4, 0, 9, 0, 0, 0, 5],
        [9, 2, 0, 0, 6, 1, 0, 3, 0],
        [0, 0, 0, 4, 0, 0, 0, 1, 0],
        [0, 0, 0, 3, 7, 8, 0, 9, 0],
    ],
    [
        [9, 8, 4, 0, 3, 1, 0, 7, 2],
        [6, 1, 0, 0, 0, 7, 0, 0, 0],
        [2, 5, 7, 0, 0, 9, 8, 0, 0],
        [3, 0, 0, 0, 6, 0, 0, 1, 0],
        [0, 0, 0, 3, 7, 0, 9, 2, 0],
        [0, 0, 9, 0, 0, 5, 0, 0, 0],
        [0, 3, 0, 0, 0, 6, 0, 0, 0],
        [0, 4, 5, 0, 1, 8, 0, 9, 6],
        [1, 9, 6, 7, 0, 0, 2, 8, 0],
    ],
]
# We have some medium boards that will displayed randomly
medium_boards = [
    [
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 8, 0, 0, 0, 7, 0, 9, 0],
        [6, 0, 2, 0, 0, 0, 5, 0, 0],
        [0, 7, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 4, 0],
        [0, 0, 5, 0, 0, 0, 6, 0, 3],
        [0, 9, 0, 4, 0, 0, 0, 7, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
    ],
    [
        [5, 0, 0, 0, 1, 6, 2, 0, 0],
        [0, 0, 0, 9, 8, 0, 5, 0, 4],
        [0, 3, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 6, 0, 0, 1, 0, 0],
        [9, 0, 6, 0, 0, 0, 0, 0, 2],
        [0, 2, 3, 0, 4, 9, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 8, 1],
        [3, 1, 5, 2, 9, 0, 0, 6, 7],
        [8, 0, 9, 4, 7, 1, 0, 2, 5],
    ],
    [
        [2, 0, 4, 0, 6, 5, 3, 1, 7],
        [5, 0, 1, 3, 4, 9, 0, 6, 8],
        [8, 0, 3, 0, 0, 0, 9, 0, 0],
        [0, 3, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 6, 9, 0, 5, 7, 0],
        [0, 1, 9, 0, 8, 6, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 7, 0, 0],
        [0, 5, 0, 2, 3, 0, 0, 0, 1],
    ],
    [
        [0, 0, 5, 0, 7, 6, 4, 3, 0],
        [0, 0, 7, 1, 3, 0, 0, 0, 8],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [1, 3, 0, 0, 0, 4, 0, 6, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 2, 9],
        [0, 0, 1, 0, 0, 0, 0, 0, 6],
        [0, 0, 9, 2, 6, 7, 5, 0, 0],
        [0, 5, 0, 0, 9, 1, 0, 4, 3],
    ],
]
# We have some hard boards that will displayed randomly
hard_boards = [
    [
        [0, 0, 0, 0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 3, 5, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 4, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 2, 0, 6, 0, 0, 0, 0, 0],
    ],
    [
        [9, 0, 0, 3, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 2, 0, 7, 0, 0],
        [0, 0, 7, 5, 0, 0, 0, 0, 8],
        [0, 6, 0, 0, 0, 2, 1, 0, 7],
        [2, 8, 0, 7, 4, 0, 0, 9, 0],
        [0, 0, 5, 0, 0, 6, 0, 0, 0],
        [0, 1, 0, 9, 8, 4, 6, 0, 2],
        [6, 0, 4, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 4, 0],
    ],
    [
        [0, 1, 0, 0, 0, 0, 0, 0, 5],
        [2, 6, 0, 4, 3, 7, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 5, 0, 7, 0, 9],
        [0, 0, 0, 7, 4, 3, 0, 0, 2],
        [0, 4, 0, 0, 0, 1, 0, 5, 0],
        [0, 0, 0, 0, 0, 6, 0, 9, 3],
        [9, 0, 0, 9, 0, 0, 8, 0, 7],
        [6, 3, 0, 1, 7, 9, 0, 0, 0],
    ],
    [
        [8, 3, 0, 0, 0, 0, 4, 0, 6],
        [0, 4, 0, 3, 9, 0, 0, 0, 0],
        [0, 0, 6, 2, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 1, 0, 4, 9],
        [0, 0, 0, 6, 7, 2, 5, 0, 0],
        [0, 1, 0, 0, 0, 9, 8, 0, 7],
        [0, 7, 0, 0, 1, 5, 0, 0, 0],
        [0, 0, 9, 0, 6, 0, 1, 0, 5],
        [0, 0, 0, 9, 0, 0, 3, 0, 0],
    ],
]


def display_menu():
    print(
        "Welcome to the game, I hope you enjoy playing this game."
        " In this game you should fill the squares in a way that there"
        " is no repeated number in each square, in each line and in each column."
    )
    print("Select Sudoku Difficulty Level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4: Exit")
    choice = input("Enter your choice (1/2/3/4): ")
    return choice


def get_random_board(level):
    if level == "1":
        return random.choice(easy_boards)
    elif level == "2":
        return random.choice(medium_boards)
    elif level == "3":
        return random.choice(hard_boards)
    elif level == "4":
        print("See you soon!")
        exit()
    else:
        print("Invalid choice! Please choose a valid difficulty level.")
        return None


def print_board(
    board, highlight_positions=None, invalid_positions=None, success_positions=None
):
    print("    " + "   ".join(str(i + 1) for i in range(9)))
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("    " + "-" * 29)
        print(f"{i + 1}| ", end=" ")
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end="  ")
            if success_positions and (i, j) in success_positions:
                print(f"\033[92m{num if num != 0 else '.'}\033[0m ", end=" ")
            elif highlight_positions and (i, j) in highlight_positions:
                print(f"\033[93m{num if num != 0 else '.'}\033[0m ", end=" ")
            elif invalid_positions and (i, j) in invalid_positions:
                print(f"\033[91m{num}\033[0m ", end=" ")
            else:
                print(f"{num if num != 0 else '.'} ", end=" ")
        print()


def is_valid_move(board, row, col, num):
    conflict_positions = []
    for i in range(9):
        if board[row][i] == num:
            conflict_positions.append((row, i))
        if board[i][col] == num:
            conflict_positions.append((i, col))
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                conflict_positions.append((i, j))
    if conflict_positions:
        return False, conflict_positions
    return True, []


def get_user_input(board, valid_moves):
    try:
        row = int(input("Enter row (1-9): ")) - 1
        col = int(input("Enter column (1-9): ")) - 1
        num = int(input("Enter number (1-9): "))

        if not (0 <= row < 9) or not (0 <= col < 9) or not (1 <= num <= 9):
            raise ValueError

        if board[row][col] == 0:
            valid, conflict_positions = is_valid_move(board, row, col, num)
            board[row][col] = num  # Temporarily place the number for display purposes
            if valid:
                valid_moves.append((row, col))
                print("\033[92mMove accepted\033[0m")
            else:
                print_board(
                    board,
                    highlight_positions=valid_moves,
                    invalid_positions=[(row, col)] + conflict_positions,
                )
                print("\033[91mInvalid move, please try again.\033[0m")
                board[row][col] = 0  # Reset the number since it was invalid
        else:
            print(
                "\033[91m"
                + f"Cell already filled at column {col + 1} and row {row + 1} with number {(board[row][col])}"
                + "\033[0m"
            )

    except ValueError:
        print(
            "Invalid input, please enter numbers within the range 1-9 for row and column, and 1-9 for number"
        )
    except IndexError:
        print(
            "Invalid input, please enter numbers within the range 1-9 for row and column, and 1-9 for number"
        )


def is_board_complete(board):
    for row in board:
        if 0 in row:
            return False
    return True


def main():
    choice = display_menu()
    board = get_random_board(choice)
    valid_moves = []
    if board:
        time1 = time.time()
        while not is_board_complete(board):
            print_board(board, highlight_positions=valid_moves)
            get_user_input(board, valid_moves)
        print_board(board, success_positions=valid_moves)
        print("Well Done with your choices!")
        time2 = time.time()
        totaltime = time2 - time1
        minut = totaltime // 60
        sec = totaltime
        print("You did it in ", minut, "minutes and", sec, "second")


if __name__ == "__main__":
    main()
