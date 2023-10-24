import tkinter as tk
from tkinter import messagebox

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def evaluate(board):
    if is_winner(board, "X"):
        return 1
    elif is_winner(board, "O"):
        return -1
    else:
        return 0

def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, "X"):
        return 1
    if is_winner(board, "O"):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        max_eval = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_eval = -float("inf")
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                eval = minimax(board, 0, False, -float("inf"), float("inf"))
                board[i][j] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

def on_button_click(row, col):
    if board[row][col] == " ":
        board[row][col] = "O"
        buttons[row][col]["text"] = "O"
        if is_winner(board, "O"):
            messagebox.showinfo("Tic-Tac-Toe", "You win!")
            root.quit()
        elif is_draw(board):
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            root.quit()
        else:
            best_move = find_best_move(board)
            row, col = best_move
            board[row][col] = "X"
            buttons[row][col]["text"] = "X"
            if is_winner(board, "X"):
                messagebox.showinfo("Tic-Tac-Toe", "Computer wins!")
                root.quit()
            elif is_draw(board):
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                root.quit()

root = tk.Tk()
root.title("Tic-Tac-Toe")

board = [[" " for _ in range(3)] for _ in range(3)]

buttons = [[None, None, None] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", width=10, height=3, command=lambda row=i, col=j: on_button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
