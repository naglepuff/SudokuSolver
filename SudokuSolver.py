from SudokuGame import SudokuGame
from SudokuIO import SudokuIO

"""
Run only the test cases provided with the problem statement.
Use input "TEST" at the main prompt for this action.
"""
def run_examples():

    examples = [
        "puzzle1.txt",
        "puzzle2.txt",
        "puzzle3.txt",
        "puzzle4.txt",
        "puzzle5.txt"
    ]
    IOHandler = SudokuIO()
    for example in examples:
        try:
            game = IOHandler.read_game(example)
            game.solve()
            IOHandler.write_solution(game)
            print("Solved " + example)
        except OSError:
            print("Could not find file: " + example)
        except RuntimeError:
            print(example + " could not be parsed.")
    print("Done!")

"""
Main loop for the app. Run the python script from the command line.
Give it puzzles to solve. It will create a file with the solution as
well as print the solution in the command line.

Special inputs:
'q': quit the program
'TEST': run the example puzzles provided.
"""
def main():
    quitInput = 'q'
    prompt = "Enter a file name (" + quitInput + " to quit): "
    IOHandler = SudokuIO()
    print("Welcome to the sudoku solver!")
    fileName = input(prompt)
    if fileName == "TEST":
        run_examples()
        return

    while fileName != quitInput:
        try:
            game = IOHandler.read_game(fileName)
            game.solve()
            if game.solved:
                print("Here is the solution to " + fileName + ": ")
                print(game)
            else:
                print("No solution was found for that game.")
            IOHandler.write_solution(game)
            print("Solution written to " + fileName.split('.')[0] + ".sln.txt")
        except RuntimeError:
            print("The given file could not be parsed.")
        except OSError:
            print("No such file could be found.")
        fileName = input(prompt)

if __name__ == "__main__":
    main()