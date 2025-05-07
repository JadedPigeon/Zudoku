from tkinter import *
from tkinter import messagebox
import board

current_number = 1
action_type = 1

def number_button_clicked(number, button):
    global current_number
    current_number = number
    button.config(relief="sunken")
    for btn in number_buttons:
        if btn != button:
            btn.config(relief="raised")

    for i in range(9):
        for j in range(9):
            if cell_buttons[i][j].cget("text") == str(current_number):
                cell_buttons[i][j].config(bg="dark gray")
            else:
                cell_buttons[i][j].config(bg="lightgray")

def cell_button_clicked(button):
    if action_type == 0:
        print("not implemented yet")
    elif action_type == 1 and button.cget("text") == "":
        button.config(text=str(current_number))
        button.config(bg="dark gray")
        # Check for duplicates in same box, row, and column
        check_dupes(button)
        # Check if the board is complete
        check()
    elif action_type == 2:
        button.config(text="")
        button.config(bg="lightgray")
    else:
        print("Invalid action")

def note_answer_changed(button):
    global action_type
    action_type = button.cget("value")


def new_board(difficulty):
    global game_board
    game_board = board.generate_full_board(difficulty)

    for i in range(9):
        for j in range(9):
            cell_buttons[i][j].config(bg="lightgray")
            if game_board[i][j] != 0:
                cell_buttons[i][j].config(text=str(game_board[i][j]))
            else:
                cell_buttons[i][j].config(text="")
    # Keep the current number button pressed
    associated_button = number_button_map.get(current_number)
    if associated_button:
        number_button_clicked(current_number, associated_button)

def check():    
    for i in range(9):
        for j in range(9):
            if cell_buttons[i][j].cget("text") == "":
                return    
            
    game_board = [[0]*9 for _ in range(9)]

    for i in range(9):
        for j in range(9):
            game_board[i][j] = int(cell_buttons[i][j].cget("text"))
    if board.board_is_valid(game_board):
        messagebox.showinfo("Success", "Congratulations! You solved the puzzle!")
    else:
        messagebox.showerror("Error", "The solution is incorrect. Please try again.")

def check_dupes(button):
    # Checks for duplicates in the same box, row, and column
    num = button.cget("text")
    # Get the row and column of the button within its subgrid
    local_row = int(button.grid_info()["row"])
    local_col = int(button.grid_info()["column"])

    # Calculate the global row and column indices
    # Identify which subgrid the button belongs to
    parent_subgrid = button.master  # The parent frame (subgrid) of the button
    for i in range(3):
        for j in range(3):
            if subframes[i][j] == parent_subgrid:
                subgrid_row = i
                subgrid_col = j
                break

    # Calculate the global row and column indices
    global_row = subgrid_row * 3
    global_col = subgrid_col * 3

    # Check for duplicates in the same box
    for i in range(3):
        for j in range(3):
            if i == local_row and j == local_col:
                continue
            if cell_buttons[global_row + i][global_col + j].cget("text") == num:
                button.config(bg="red")
                return
            
    # Check for duplicates in the same row
    for i in range(9):
        if i == global_row:
            continue
        if cell_buttons[i][global_col].cget("text") == num:
            button.config(bg="red")
            return
    # Check for duplicates in the same column
    for i in range(9):
        if i == global_col:
            continue
        if cell_buttons[global_row][i].cget("text") == num:
            button.config(bg="red")
            return



if __name__ == "__main__":
    gui = Tk()

    gui.title("Zudoku")
    gui.geometry("1200x800")

    # Main Frame
    main_frame = Frame(gui)
    main_frame.pack()

    # Create a frame for the grid
    grid_frame = Frame(main_frame, borderwidth=2, relief="solid")
    grid_frame.grid(row=0, column=0, padx=20, pady=20)

    # Create 9 subframes for the 9 sections of the grid
    subframes = [[Frame(grid_frame, borderwidth=1, relief="solid") for _ in range(3)] for _ in range(3)]

    # Place the subframes in a 3x3 grid
    for i in range(3):
        for j in range(3):
            subframes[i][j].grid(row=i, column=j)

    # Create a 2D list to store references to the cell buttons
    cell_buttons = [[None for _ in range(9)] for _ in range(9)]

    # Create a 3x3 grid of buttons inside each subframe
    for i in range(3):
        for j in range(3):
            for x in range(3):
                for y in range(3):
                    # Calculate the global row and column indices
                    global_row = i * 3 + x
                    global_col = j * 3 + y

                    # Create the button
                    cell_button = Button(
                        subframes[i][j],
                        text="",
                        width=2,
                        height=2
                    )
                    cell_button.config(command=lambda b=cell_button: cell_button_clicked(b))
                    cell_button.grid(row=x, column=y, padx=0, pady=0)

                    # Store the button in the 2D list
                    cell_buttons[global_row][global_col] = cell_button


    # Create a frame for the buttons
    button_frame = Frame(main_frame)
    button_frame.grid(row=1, column=0, padx=20, pady=20)

    # Number Buttons
    one_button = Button(button_frame, text="1", command=lambda: number_button_clicked(1, one_button), width=2, height=2)
    one_button.grid(row=0, column=0)
    

    two_button = Button(button_frame, text="2", command=lambda: number_button_clicked(2, two_button), width=2, height=2)
    two_button.grid(row=0, column=1)

    three_button = Button(button_frame, text="3", command=lambda: number_button_clicked(3, three_button), width=2, height=2)
    three_button.grid(row=0, column=2)

    four_button = Button(button_frame, text="4", command=lambda: number_button_clicked(4, four_button), width=2, height=2)
    four_button.grid(row=0, column=3)

    five_button = Button(button_frame, text="5", command=lambda: number_button_clicked(5, five_button), width=2, height=2)
    five_button.grid(row=0, column=4)

    six_button = Button(button_frame, text="6", command=lambda: number_button_clicked(6, six_button), width=2, height=2)
    six_button.grid(row=0, column=5)

    seven_button = Button(button_frame, text="7", command=lambda: number_button_clicked(7, seven_button), width=2, height=2)
    seven_button.grid(row=0, column=6)

    eight_button = Button(button_frame, text="8", command=lambda: number_button_clicked(8, eight_button), width=2, height=2)
    eight_button.grid(row=0, column=7)

    nine_button = Button(button_frame, text="9", command=lambda: number_button_clicked(9, nine_button), width=2, height=2)
    nine_button.grid(row=0, column=8)

    number_buttons = [one_button, two_button, three_button, four_button, five_button, six_button, seven_button, eight_button, nine_button]
    
    number_button_map = {
    1: one_button,
    2: two_button,
    3: three_button,
    4: four_button,
    5: five_button,
    6: six_button,
    7: seven_button,
    8: eight_button,
    9: nine_button
}

    # Create frame for the action buttons
    action_frame = Frame(main_frame)
    action_frame.grid(row=0, column=1, padx=20, pady=20)

    # Action buttons
    new_game_button = Button(action_frame, text="New Game", command=lambda: new_board(difficulty_selected.get()), width=10)
    new_game_button.grid(row=0, column=0, pady=5)

    difficulty_label = Label(action_frame, text="Difficulty:", font=("Arial", 10))
    difficulty_label.grid(row=1, column=0, pady=5, sticky="w")

    difficulty_selected = IntVar(value=0)
    easy_radio = Radiobutton(action_frame, text="Easy (default)", variable=difficulty_selected, value=0, anchor="w")
    easy_radio.grid(row=2, column=0, sticky="w")

    medium_radio = Radiobutton(action_frame, text="Medium", variable=difficulty_selected, value=1, anchor="w")
    medium_radio.grid(row=3, column=0, sticky="w")

    hard_radio = Radiobutton(action_frame, text="Hard", variable=difficulty_selected, value=2, anchor="w")
    hard_radio.grid(row=4, column=0, sticky="w")

    note_answer_label = Label(action_frame, text="Current Entry Mode:", font=("Arial", 10))
    note_answer_label.grid(row=5, column=0, pady=5, sticky="w")

    action_selected = IntVar(value=1)
    note_radio = Radiobutton(action_frame, text="Note", command=lambda: note_answer_changed(note_radio), variable=action_selected, value=0, anchor="w")
    note_radio.grid(row=6, column=0, sticky="w")

    answer_radio = Radiobutton(action_frame, text="Answer", command=lambda: note_answer_changed(answer_radio), variable=action_selected, value=1, anchor="w")
    answer_radio.grid(row=7, column=0, sticky="w")


    erase_radio = Radiobutton(action_frame, text="Erase", command=lambda: note_answer_changed(erase_radio), variable=action_selected, value=2, anchor="w")
    erase_radio.grid(row=8, column=0, sticky="w")
    # End action buttons

    # Test board solve function
    # solved_board = [
    # [5, 3, 4, 6, 7, 8, 9, 1, 2],
    # [6, 7, 2, 1, 9, 5, 3, 4, 8],
    # [1, 9, 8, 3, 4, 2, 5, 6, 7],
    # [8, 5, 9, 7, 6, 1, 4, 2, 3],
    # [4, 2, 6, 8, 5, 3, 7, 9, 1],
    # [7, 1, 3, 9, 2, 4, 8, 5, 6],
    # [9, 6, 1, 5, 3, 7, 2, 8, 4],
    # [2, 8, 7, 4, 1, 9, 6, 3, 5],
    # [3, 4, 5, 2, 8, 6, 1, 7, 9]
    # ]

    # print(board.board_is_valid(solved_board))


    # Initialize the game board on startup
    new_board(0)
    gui.mainloop() 