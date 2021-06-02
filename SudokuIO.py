
from SudokuGame import SudokuGame
import io

class SudokuIO:

    # used for reading files into SudokuGame objects
    translation_table = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'X': 0,
        'x': 0
    }

    """
    Splits 1 line of input text into a list of numbers.
    Expects the input text to contain only characters 1-9 and 'X', throws an exception if unable to parse.
    Returns: a list of numbers, 0-9 representing a row of a sudoku board. (0 is an empty cell).
    """
    def process_line(self, line):
        charList = list(line)
        for i in range(0, len(charList)):
            key = charList[i]
            if key in self.translation_table.keys():
                charList[i] = self.translation_table[key]
            else:
                raise RuntimeError("File can not be parsed as a sudoku puzzle")
        return charList

    """
    Constructs a SudokuIO object
    """
    def __init__(self):
        pass

    """
    Reads a file containing a sudoku game
    Throws an exception if unable to parse file into a sudoku game.
    params: 
      fileName: string representing the name of the file to read
    returns:
      a new sudoku game object with the puzzle and file name properties set.
    """
    def read_game(self, fileName):
        file = open(fileName, 'r')
        sudokuBoard = []
        with file:
            sudokuBoard = file.read().splitlines()
            if(len(sudokuBoard) != 9):
                raise RuntimeError("File can not be parsed as a sudoku puzzle")
            sudokuBoard = [self.process_line(line) for line in sudokuBoard]
        sudokuGame = SudokuGame(fileName, sudokuBoard)
        file.close()
        return sudokuGame
    

    """ 
    Writes a solved sudoku game to a new file
    Side affects: solves the puzzle if it isn't already solved
    params:
       sudokuGame: a SudokuGame object with a solved puzzle
    """
    def write_solution(self, sudokuGame):
        fileName = sudokuGame.file_name[:len(sudokuGame.file_name) - 4] + ".sln.txt"
        solutionFile = open(fileName, 'w')
        with solutionFile:
            if not sudokuGame.solved:
                sudokuGame.solve()
                if not sudokuGame.solved:
                    solutionFile.write("This puzzle cannot be solved!")
                    return
            for row in sudokuGame.puzzle:
                stringRow = [str(num) for num in row]
                solutionFile.write(''.join(stringRow))
                solutionFile.write('\n')
        solutionFile.close()
