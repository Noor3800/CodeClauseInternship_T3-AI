import random

# Display the board
def print_board(board):
    print()
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

# Check for a winner
def check_winner(board, symbol):
    for row in board:
        if all(s == symbol for s in row):
            return True
    for col in range(3):
        if all(row[col] == symbol for row in board):
            return True
    if all(board[i][i] == symbol for i in range(3)):
        return True
    if all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

# Check for draw
def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Convert 1–9 input to board index
def position_to_index(position):
    position -= 1
    return position // 3, position % 3

# Get all available moves
def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

# AI move logic
def ai_move(board, ai_symbol, player_symbol):
    # Try to win
    for i, j in get_available_moves(board):
        board[i][j] = ai_symbol
        if check_winner(board, ai_symbol):
            return
        board[i][j] = " "

    # Try to block player win
    for i, j in get_available_moves(board):
        board[i][j] = player_symbol
        if check_winner(board, player_symbol):
            board[i][j] = ai_symbol
            return
        board[i][j] = " "

    # Take center if available
    if board[1][1] == " ":
        board[1][1] = ai_symbol
        return

    # Else, pick random spot
    i, j = random.choice(get_available_moves(board))
    board[i][j] = ai_symbol

# Game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("🎮 Welcome to Tic-Tac-Toe!")
    print("Choose your move by entering a number (1–9):")
    print("""
     1 | 2 | 3
    -----------
     4 | 5 | 6
    -----------
     7 | 8 | 9
    """)

    # Ask player to choose X or O
    while True:
        player_symbol = input("Do you want to be X or O? ").upper()
        if player_symbol in ["X", "O"]:
            break
        else:
            print("❗ Please choose either X or O.")

    ai_symbol = "O" if player_symbol == "X" else "X"
    print(f"You are '{player_symbol}' and AI is '{ai_symbol}'. Let's play!")

    current_turn = "Player" if player_symbol == "X" else "AI"

    while True:
        print_board(board)

        if current_turn == "Player":
            try:
                move = int(input("Your move (1–9): "))
                if move < 1 or move > 9:
                    print("⚠️ Invalid input. Choose between 1 and 9.")
                    continue
            except ValueError:
                print("⚠️ Please enter a number.")
                continue

            row, col = position_to_index(move)
            if board[row][col] != " ":
                print("⚠️ That spot is already taken!")
                continue

            board[row][col] = player_symbol

            if check_winner(board, player_symbol):
                print_board(board)
                print("🎉 You win!")
                break
            current_turn = "AI"

        else:
            print("AI is making a move...")
            ai_move(board, ai_symbol, player_symbol)

            if check_winner(board, ai_symbol):
                print_board(board)
                print("AI wins! Better luck next time.")
                break
            current_turn = "Player"

        if is_draw(board):
            print_board(board)
            print("😐 It's a draw!")
            break

    print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    play_game()
