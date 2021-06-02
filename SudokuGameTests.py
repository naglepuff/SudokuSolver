"""
This is a script to test some of the methods in the SudokuGame class.
Important things to test are is_valid and is_complete.
"""

from SudokuGame import SudokuGame

"""
Helper function to make test cases easy to construct.
"""
def make_grid(val = 0):
    return [[val] * 9] * 9

"""
Test the is_valid function of the Sudoku game class.
"""
def test_is_valid(messages):
    # case 1: test two values in same row
    testGrid = make_grid()
    testGrid[0][0] = 5
    testGrid[0][5] = 5
    game = SudokuGame("", testGrid)
    if game.is_valid():
        messages = messages + [["is_valid: two equal values in the same row should be invalid."]]

    # case 2: test two values in same column
    testGrid = make_grid()
    testGrid[0][0] = 5
    testGrid[5][0] = 5
    game = SudokuGame("", testGrid)
    if game.is_valid():
        messages = messages + [["is_valid: two equal values in the same row should be invalid."]]

    # case 3: two values in same subgrid
    # here we test multiple subgrids to make sure our index calculations are correct
    testGrid = make_grid()
    testGrid[3][3] = 5
    testGrid[4][4] = 5
    game1 = SudokuGame("", testGrid)
    game1Valid = game1.is_valid()
    testGrid[3][3] = 0
    testGrid[4][4] = 0
    testGrid[7][7] = 5
    testGrid[8][8] = 5
    game2 = SudokuGame("", testGrid)
    game2Valid = game2.is_valid()
    if game1Valid or game2Valid:
        messages = messages + ["is_valid: two equal values in the same subgrid should be invalid."]


"""
Test the is_complete function of the Sudoku game class.
"""
def test_is_complete(messages):
    # case 1: empty grid
    testGrid = make_grid()
    game = SudokuGame("", testGrid)
    if game.is_complete():
        messages = messages + ["is_complete: an empty sudoku grid is not complete"]
    
    # case 2: full grid
    testGrid = make_grid(5)
    game = SudokuGame("", testGrid)
    if not game.is_complete():
        messages = messages + ["is_complete: an complete sudoku grid is not incomplete"]

    # case 3: single empty square
    testGrid = make_grid(5)
    testGrid[8][8] = 0
    game = SudokuGame("", testGrid)
    if game.is_complete():
        messages = messages + ["is_complete: a sudoku grid with an empty cell is not complete"]

"""
Run the tests, keep track of error messages in a list.
"""
def main():
    errors = []
    test_is_valid(errors)
    test_is_complete(errors)
    if len(errors) == 0:
        print("All tests passed.")
    else:
        for error in errors:
            print(error)

if __name__ == "__main__":
    main()