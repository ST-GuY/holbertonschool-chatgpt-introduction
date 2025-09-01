#!/usr/bin/env python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 5)

def check_winner(board):
    # Lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_move(player):
    while True:
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Row and column must be 0, 1, or 2.")
                continue
            return row, col
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        row, col = get_move(player)

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Changement de joueur
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
