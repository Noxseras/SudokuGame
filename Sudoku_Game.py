from termcolor import colored


class Sudoku:
    def __init__(self):
        self.board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

    # Print board and make it look better
    def display_board(self, bo):
        for i in range(len(bo)):
            if i % 3 == 0 and i != 0:
                print(" - - - - - - - - -")
            for j in range(len(bo[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                if j == 8:
                    print(bo[i][j])
                else:
                    print(str(bo[i][j]) + " ", end="")

    # Check the range of the value
    def value_range(self, l, c, v):
        l = l - 1
        c = c - 1
        if l < 0 or c < 0 or l > 8 or c > 8 or v < 1 or v > 9:
            print("Invalid option, number already exists")
            return False
        """ Check areas and sub-areas"""
        for i in range(9):
            if self.board[l][i] == v:
                print("LINE")
                return False
            if self.board[i][c] == v:
                print("COLUMN")
                return False
            if not self.subareas(l, c, v):
                return False
            else:
                self.board[l][c] = v
                return True
        return True

    # check for sub areas
    def subareas(self, l, c, v):
        ia = l // 3  # divide every number of the row with 3, if position [0, 4], its in [0, 1](min and max:[0,2]-[2,2])
        ja = c // 3
        for i in range(ia * 3, ia * 3 + 3):
            for j in range(ja * 3, ja * 3 + 3):
                if self.board[i][j] == v:
                    return False
        return True

    def completed(self):
        for r in range(0, 9):
            for c in range(0, 9):
                if self.board[r][c] == 0:
                    return False
        return True


sudoku = Sudoku()
while not sudoku.completed():
    sudoku.display_board(sudoku.board)
    x = int(input("Row: "))
    y = int(input("Col: "))
    val = int(input("Value: "))
    if not sudoku.value_range(x, y, val):
        print("Wrong position")

sudoku.display_board(sudoku.board)
print("Great job!")
exit()
