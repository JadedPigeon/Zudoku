# Zudoku
An assisted Sudoku game made in Python using TKinter

# How to play
## Sudoku Rules

Sudoku is a logic-based number puzzle that is typically played on a 9x9 grid, divided into nine 3x3 subgrids (also called "regions" or "blocks"). The objective is to fill the grid with numbers from 1 to 9 according to the following rules:

1. **Unique Numbers in Rows:** Each row must contain the numbers 1 to 9, without repetition.

2. **Unique Numbers in Columns:** Each column must also contain the numbers 1 to 9, without repetition.

3. **Unique Numbers in Subgrids:** Each 3x3 subgrid must contain the numbers 1 to 9, without repetition.

4. **Given Numbers:** Some cells are pre-filled as clues. These numbers cannot be changed.

5. **One Solution:** A properly constructed Sudoku puzzle has only one possible solution.

### Tips
- Start with rows, columns, or subgrids that have the most given numbers.
- Use the process of elimination to figure out which numbers fit.
- If stuck, look for numbers that must be in a specific place within a row, column, or subgrid.

## How Zudoku assists you
1. Click a number 1 to 9 from the buttons on the bottom of the screen
2. Existing numbers on the Zudoku board will be highlighted for visibility
3. Click a cell to insert the selected number (make sure "Current Entry Mode" is set to "Answer" which is the default)
4. If the number you insert already exists in that block, row, or column, it will be highlighted red
5. When all cells have been filled the game checks if the solution is valid and informs you
6. Select a difficulty and start a new game
 

# Dev log

# Completed
1. Created the Sudoku Board
2. Created number buttons
3. Created mode and related buttons
4. Created difficulty and new game buttons
5. Implemented functionality for the above items
6. Create a valid Sudoku game and display it
7. Validate board when all cells are filled
8. Highlight currently selected number
9. Display success/failure message when all cells are filled
10. Implemented difficulty system
11. Maintain selected number after starting new board
12. Warn the user if they have a dupe in same 3x3 grid
13. Warn the user if they have a dupe in the same row or column
14. Erase resets bg color
15. Added timer with pause and reset functionality
16. Timer will reset with a new game and start again
17. Added a count for each existing number that updates when new numbers are added/erased to the board, or a new game starts
18. Fixed bug with dupe detection

# To-do
- Consider if I can even actually implement a note system
- Optional styling options ie nightmode
- Consider adding a hint button to fill a single correct cell
- Add a check button that checks all the users entries so far
- Reset button to go back to original board they started with
- Save/load
- Undo button
- Show how many numbers for each number are remaining


