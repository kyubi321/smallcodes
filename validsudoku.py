
def valid_sudoku(board):
    seen = set()
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                # Check row
                if f"row {i} {board[i][j]}" in seen:
                    return False
                seen.add(f"row {i} {board[i][j]}")

                # Check column
                if f"column {j} {board[i][j]}" in seen:
                    return False
                seen.add(f"column {j} {board[i][j]}")

                # Check box
                box = f"box {i // 3} {j // 3} {board[i][j]}"
                if box in seen:
                    return False
                seen.add(box)
    return True


board = [["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
print(valid_sudoku(board))
