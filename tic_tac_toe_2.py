import math

# Define a simple Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':  # Max
        return 1
    elif winner == 'O':  # Min
        return -1
    elif is_full(board):
        return 0  # Tie

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'  # Max's move
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '  # Undo the move
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'  # Min's move
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '  # Undo the move
                    best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'  # Max's move
                score = minimax(board, 0, False)
                board[i][j] = ' '  # Undo the move
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Example usage
if __name__ == "__main__":
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)
    
    while True:
        # Max's turn (AI)
        i, j = best_move(board)
        board[i][j] = 'X'
        print("AI (X) makes a move:")
        print_board(board)
        
        if check_winner(board) or is_full(board):
            break
        
        # Min's turn (Player)
        i, j = map(int, input("Enter your move (row and column): ").split())
        if board[i][j] == ' ':
            board[i][j] = 'O'
            print_board(board)
        else:
            print("Invalid move! Try again.")

        if check_winner(board) or is_full(board):
            break

    winner = check_winner(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a tie!")
