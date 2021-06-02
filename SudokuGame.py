#
# A container for a sudoku game with properties for file name and puzzle
#
class SudokuGame:
    # construction for sudoku puzzles
    # params:
    #   fileName: the original name of the txt file containing this puzzle
    #             assume that the fileName ends with ".txt"
    #   puzzle:   a 9*9 2D array containing numbers 1-9
    def __init__(self, fileName, puzzle):
        self.file_name = fileName
        self.clues = puzzle # keep original clues intact
        self.puzzle = puzzle
        self.solved = False

    """
    Solve the puzzle represented by this object using backtracking.
    Sets the solved property for this object.
    Returns whether or not a solution was found.
    """
    def solve(self):
        wasSolved = self.__solve_inner(0, 0)
        self.solved = wasSolved
        return wasSolved

    """
    Private inner function for solve. This should always be called initially with row = col = 0
    Returns true if there is a solution, false if not.
    Side effect: completes the 2D array with the solution to the puzzle.
    Params:
      row: the row to start populating with values
      col: the column to start populating with values
    """
    def __solve_inner(self, row, col):
        
        if self.is_solved():
            return True

        nextCol = col + 1
        nextRow = row
        if nextCol == 9:
            nextCol = 0
            nextRow = row + 1

        if self.puzzle[row][col] > 0:
            return self.__solve_inner(nextRow, nextCol)

        for i in range(1, 10):
            self.puzzle[row][col] = i
            if not self.is_valid():
                continue 
            solved = self.__solve_inner(nextRow, nextCol)
            if solved:
                return True
        self.puzzle[row][col] = 0
        return False


    """
    Return true if the puzzle is in a legal state. That is, no row, column, or 3x3 subgrid
    contains more than 1 of any digit 1-9
    """
    def is_valid(self):
        
        for i in range(0, 9):
            # create a memo of valies in the ith row/col/box
            memoRow = [0] * 9
            memoCol = [0] * 9
            memoBox = [0] * 9
            for j in range(0, 9):
                # find the jth cell in the ith row/col/box
                rowCell = self.puzzle[i][j]
                colCell = self.puzzle[j][i]
                boxCell = self.puzzle[(j // 3) + 3 * (i // 3)][(j % 3) + 3 * (i % 3)]
                # check for dulplicates
                if rowCell != 0:
                    memoRow[rowCell - 1] = memoRow[rowCell - 1] + 1
                    if memoRow[rowCell - 1] > 1: 
                        return False
                if colCell != 0:
                    memoCol[colCell - 1] = memoCol[colCell - 1] + 1
                    if memoCol[colCell - 1] > 1:
                        return False
                if boxCell != 0:
                    memoBox[boxCell - 1] = memoBox[boxCell - 1] + 1
                    if memoBox[boxCell - 1] > 1:
                        return False
        return True

    """
    Returns true if there are no blank (0-value) cells in the grid
    """
    def is_complete(self):
        for row in self.puzzle:
            for num in row:
                if num == 0:
                    return False
        return True
    
    """
    Return True if the puzzle is solved. A puzzle is solved if it is valid and there are no emtpy cells.
    """
    def is_solved(self):
        return self.is_valid() and self.is_complete()


    """
    Return a string representation of the sudoku game
    """
    def __str__(self):
        border = "+---------+---------+---------+\n"
        gameString = self.file_name + '\n' + border
        
        for j in range(0, len(self.puzzle)):
            row = self.puzzle[j]
            rowString = '|'
            for i in range(0, len(row)):
                cell = str(row[i])
                if cell == '0':
                    cell = ' '
                rowString = rowString + " " + cell + " "
                if i == 2 or i == 5:
                    rowString = rowString + '|'
            rowString = rowString + '|\n'
            gameString = gameString + rowString
            if j == 2 or j == 5:
                gameString = gameString + border
        gameString = gameString + border
        return gameString