# Tic-Tac-Toe AI using Minimax Algorithm
# Human = "X", AI = "O"

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]


def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif not empty_cells(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for r, c in empty_cells(board):
            board[r][c] = "O"
            score = minimax(board, False)
            board[r][c] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for r, c in empty_cells(board):
            board[r][c] = "X"
            score = minimax(board, True)
            board[r][c] = " "
            best_score = min(score, best_score)
        return best_score


def best_move(board):
    best_score = -float("inf")
    move = None
    for r, c in empty_cells(board):
        board[r][c] = "O"
        score = minimax(board, False)
        board[r][c] = " "
        if score > best_score:
            best_score = score
            move = (r, c)
    return move


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are X | AI is O")
    print_board(board)

    while True:
        # Human move
        while True:
            try:
                row, col = map(int, input("Enter your move (row and column 0-2): ").split())
                if board[row][col] != " ":
                    print("Cell is taken! Try again.")
                else:
                    break
            except (ValueError, IndexError):
                print("Invalid input! Enter two numbers between 0 and 2 separated by space.")

        board[row][col] = "X"
        print("\nYour move:")
        print_board(board)

        if check_winner(board):
            print("You win!")
            break
        if not empty_cells(board):
            print("It's a draw!")
            break

        # AI move
        r, c = best_move(board)
        board[r][c] = "O"
        print("\nAI's move:")
        print_board(board)

        if check_winner(board):
            print("AI wins! Better luck next time.")
            break
        if not empty_cells(board):
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()
