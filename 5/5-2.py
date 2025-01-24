# Tic-Tac-Toe Game in Python

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Function to check if there is a winner
def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # Horizontal
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), # Vertical
                      (0, 4, 8), (2, 4, 6)]            # Diagonal
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full (tie)
def is_board_full(board):
    return ' ' not in board

# Function to get the player's move
def get_move(board):
    while True:
        try:
            # Prompt the player for a move in the 1-3 grid format
            move = input("Enter your move (row, col) as 'row,col' (e.g., 1,1): ")
            row, col = map(int, move.split(','))
            
            # Validate the row and column numbers
            if row < 1 or row > 3 or col < 1 or col > 3:
                print("Invalid move. Row and column should be between 1 and 3. Try again.")
                continue
            
            # Calculate the index based on row and column
            index = (row - 1) * 3 + (col - 1)
            
            if board[index] == ' ':
                return index
            else:
                print("That spot is already taken, try again.")
        except (ValueError, IndexError):
            print("Invalid move. Please enter the row and column as 'row,col' between 1 and 3.")

# Main function to play the game
def play_game():
    board = [' '] * 9
    current_player = 'X'
    
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        print(f"Player {current_player}'s turn:")
        move = get_move(board)
        board[move] = current_player
        print_board(board)
        
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
if __name__ == "__main__":
    play_game()
