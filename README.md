# SudokuSolver
A command line python program to solve sudoku puzzles.

## How to use this program
Put the python files into a directory on your machine. This includes SudokuGame.py, SudokuIO.py and SudokuSolver.py. SudokuGameTests.py is a script that does some basic testing of methods in the SudokuGame class. To run, just type `python SudokuSolver.py` at the command line to enter the program. You will be prompted for a file name. This file should be a test file with 9 lines of text, each with 9 characters, representing an unsolved sudoku puzzle. For blank cells, use 'X'.

At the prompt, enter the name of some such file. The program will then solve the puzzle, spit out the solution on the command line, and save the solution to a new file. If your puzzle file was called puzzle.txt, then the solution will be saved to puzzle.sln.txt. You can solve multiple puzzles at the REPL. There are two special inputs. 'q' will exit the program. 'TEST' will run the program for the five test files included with the problem statement.


## How this program works
The program uses backtracking to solve the puzzles. Given an unsolved sudoku puzzle, the program will make a guess to the value in the first empty square, assume that is correct, and continue to do this until there is a contradition. It will then back up and change the most recent guess. Doing this is similar to a brute force approach. A class called SudokuIO handles the reading and writing to files.

## Testing
This program has some ad-hoc type testing for some important functions in the SudokuGame class. More formal unit testing would improve the overall quality of the program. I am not familiar enough with any python unit testing frameworks to quickly make unit tests, which is why I wrote my own. Given more time on this project I would implement a unit testing library in python instead of writing tests as a script. I would also explore using a more intuition-based approach to solving a sudoku puzzle to try and improve runtime.
