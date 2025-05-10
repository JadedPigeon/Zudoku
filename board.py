import random
import copy

def is_valid(board, row, col, num):
    # Cecks to make sure the number is not already in any row, column, or 3x3 grid
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row//3), 3 * (col//3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def board_is_valid(board):
    def is_valid_group(group):
        return sorted(group) == list(range(1, 10))

    for row in board:
        if not is_valid_group(row):
            return False

    for col in zip(*board):
        if not is_valid_group(col):
            return False

    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = [
                board[r][c]
                for r in range(box_row, box_row + 3)
                for c in range(box_col, box_col + 3)
            ]
            if not is_valid_group(box):
                return False

    return True

def fill_board(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                random.shuffle(numbers := list(range(1, 10)))
                for num in numbers:
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if fill_board(board):
                            return True
                        board[i][j] = 0
                return False
    return True

# Easy: 36–49 clues
# Medium: 30–35 clues
# Hard: 22–30 clues

def generate_full_board(difficulty=0):
    board = [[0]*9 for _ in range(9)]
    fill_board(board)
    solved_board = copy.deepcopy(board)

    clues = 0
    if difficulty == 0:
        clues = random.randint(36, 49) 
    elif difficulty == 1:
        clues = random.randint(30, 35)
    else:
        clues = random.randint(22, 30)
    
    remove_clues(board, clues)
    return board, solved_board

# Number of solutions - we only want one solution. We limit to 2 to speed up the process
def has_unique_solution(board, limit=2):
    def solve(board, count=[0]):
        if count[0] >= limit:
            return
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            solve(board, count)
                            board[i][j] = 0
                    return
        count[0] += 1

    count = [0]
    solve([row[:] for row in board], count)
    return count[0] == 1


def remove_clues(board, clues_to_leave):
    positions = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(positions)

    for row, col in positions:
        if sum(cell != 0 for row in board for cell in row) <= clues_to_leave:
            break

        temp = board[row][col]
        board[row][col] = 0

        if not has_unique_solution(board):
            board[row][col] = temp