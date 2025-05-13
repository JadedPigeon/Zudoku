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
7. Zudoku offers tools to validate your current game, save your game, provide a hint revealing a random cell, or showing the board's solution
 
# How to run the game
## Linux/MacOS (Reccomended for styling purposes):
```
python3 -m zudoku
```

## Windows
```
python zudoku.py
```

# Dev log
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
19. Alert user if they try to enter a number they already have 9 of on the board
20. Added completion time to congratulations pop up
21. Reformatted the timer section to be a subframe of actions instead of it's own separate frame
22. Added a Reset button to go back to original board they started with
23. Refactor code to use a helper function to determine a cell button's position in the grid
24. Refactor dupe code to simplify it and make it more consistent
25. Implemented undo button to undo last move - works for full history of current game
26. Implemented validate button that validates all moves so far
27. Implemented hint button
28. Implemented a show solution button and updated the validation of a solved board to check if a hint, or show solution, was used
29. Implemented a highscore system that persists locally. Shows top 10 in fastest time
30. Highscores can now be filtered by difficulty and load preselected to the "Easy" filter. Highscores are also updated when a new game begins and will filter to the difficulty of the new game
31. Implemented a save system which retains the current board, time elapsed, undo list, the original board to reset to, the solution board
32. Fixed Bug: If a dupe is marked red and you change the selected number it changes back to light gray
33. Erase shows a warning popup if you try to use it on an already empty cell
34. Highscores and difficulty radio button are updated to the current difficulty of a loaded save game when game starts
35. Fixed Bug: Can continue playing the game if paused - should resume timer if cell is clicked
36. Added an About button for context and instructions

# Future Considerations
- Consider if I can even actually implement a note system
- Optional styling options ie nightmode and make the game look better on windows

# Bugs
- Bug: Click valid cell, click another cell in the same box that would be valid if the first click wasn't made. Erase first click. Second click still shows red (Ignoring this defect for now because it's not a common workflow and the work around is to simply erase the number and enter it again)




