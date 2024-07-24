import random
import time

# We have some easy boards that will displayed randomly
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
    """
    Displays the main menu for the game and returns the user's choice.
    Returns:
        str: The user's menu choice.
    """
    print(
        "Welcome to the game, I hope you enjoy playing this game."
        " In this game you should fill the squares in a way that there"
        " is no repeated number in each square, in each line and in each column."
    )
    print("Select Sudoku Difficulty Level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Solve a New Board")
    print("5. Exit")
    choice = input("Enter your choice (1/2/3/4/5): ")
    return choice


def get_random_board(level):
    """
    Retrieves a Sudoku board based on the chosen difficulty level or generates a new board for solving.
    Args:
        level (str): The chosen difficulty level or '4' for a new board.
    Returns:
        list: The selected Sudoku board.
    """
    if level == "1":
        return random.choice(easy_boards)
    elif level == "2":
        return random.choice(medium_boards)
    elif level == "3":
        return random.choice(hard_boards)
    elif level == "4":
        return generate_valid_sudoku()  # Generate a new board for solving
    elif level == "5":
        print("See you soon!")
        exit()
    else:
        print("Invalid choice! Please choose a valid difficulty level.")
        return None


def print_board(
    board,
    highlight_positions=None,
    invalid_positions=None,
    success_positions=None,
    new_positions=None,
):
    """
    Prints the Sudoku board with options to highlight positions, indicate invalid entries, and show success.
    Args:
        board (list): The Sudoku board.
        highlight_positions (list): List of positions to highlight.
        invalid_positions (list): List of positions with invalid entries.
        success_positions (list): List of positions with successful entries.
        new_positions (list): List of positions with new entries.
    """
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
                print(f"\033[91m{num if num != 0 else '.'}\033[0m ", end=" ")
            elif new_positions and (i, j) in new_positions:
                print(f"\033[96m{num if num != 0 else '.'}\033[0m ", end=" ")
            else:
                print(f"{num if num != 0 else '.'} ", end=" ")
        print()


def is_valid_move(board, row, col, num):
    """
    Checks if placing a number in a specific cell is valid according to Sudoku rules.
    Args:
        board (list): The Sudoku board.
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        num (int): The number to place.
    Returns:
        tuple: A boolean indicating validity and a list of conflicting positions.
    """
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
    """
    Prompts the user for input and updates the board with the user's move.
    Args:
        board (list): The Sudoku board.
        valid_moves (list): List of valid moves to highlight.
    """
    try:
        row = int(input("Enter row (1-9): ")) - 1
        col = int(input("Enter column (1-9): ")) - 1
        num = int(input("Enter number (1-9): "))

        if not (0 <= row < 9) or not (0 <= col < 9) or not (1 <= num <= 9):
            raise ValueError

        if board[row][col] == 0:
            valid, conflict_positions = is_valid_move(board, row, col, num)
            board[row][col] = num
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
                board[row][col] = 0
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
    """
    Checks if the Sudoku board is completely filled.
    Args:
        board (list): The Sudoku board.
    Returns:
        bool: True if the board is complete, False otherwise.
    """
    for row in board:
        if 0 in row:
            return False
    return True


def generate_valid_sudoku():
    """
    Generates a valid Sudoku board with some cells blanked out.
    Returns:
        list: The generated Sudoku board with some cells filled.
    """
    board = [[0] * 9 for _ in range(9)]

    def is_valid(board, row, col, num):
        """
        Checks if placing a number in a specific cell is valid.
        Args:
            board (list): The Sudoku board.
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            num (int): The number to place.
        Returns:
            bool: True if valid, False otherwise.
        """
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def solve(board):
        """
        Solves the Sudoku board using a simple backtracking algorithm.
        Args:
            board (list): The Sudoku board.
        Returns:
            bool: True if solved, False otherwise.
        """
        empty = find_empty_location(board)
        if not empty:
            return True
        row, col = empty
        nums = list(range(1, 10))
        random.shuffle(nums)
        for num in nums:
            if is_valid(board, row, col, num):
                board[row][col] = num
                if solve(board):
                    return True
                board[row][col] = 0  # Backtrack
        return False

    solve(board)

    # Add some blanks to make the board partially solved
    num_blanks = 60  # Number of blanks
    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)
    for i, j in cells[:num_blanks]:
        board[i][j] = 0  # Set some cells to blank

    return board

def most_constrained_variable(board):
    """
    Selects the cell with the fewest possible values (most constrained).
    Args:
        board (list): The Sudoku board.
    Returns:
        tuple: The (row, col) of the most constrained cell.
    """
    min_options = float("inf")
    best_cell = None
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                num_options = sum(
                    1 for num in range(1, 10) if is_valid_move(board, row, col, num)[0]
                )
                if num_options < min_options:
                    min_options = num_options
                    best_cell = (row, col)
    return best_cell