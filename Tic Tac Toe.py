import math

# Initialize board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------")
    print("\n")

# Check for winner
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check if board is full
def is_full():
    return " " not in board

# Minimax algorithm
def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    elif check_winner("X"):
        return -1
    elif is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# Find best move for AI
def best_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X'. AI is 'O'.")
    print_board()

    while True:
        # Human move
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if move >= 0 and move < 9 and board[move] == " ":
                    board[move] = "X"
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a valid number between 1 and 9.")

        print_board()

        if check_winner("X"):
            print("🎉 You win!")
            break
        elif is_full():
            print("It's a draw!")
            break

        # AI move
        print("AI is thinking...")
        ai_move = best_move()
        board[ai_move] = "O"
        print_board()

        if check_winner("O"):
            print("🤖 AI wins! Better luck next time.")
            break
        elif is_full():
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
