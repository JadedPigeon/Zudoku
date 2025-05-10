from tkinter import *
from tkinter import messagebox
import board
import sys
import random

current_number = 1
action_type = 1
elapsed_time = 0
not_paused = 1
timer_after_id = None
number_counts = {i: 0 for i in range(1, 10)}
reset_board = [[0]*9 for _ in range(9)]
solved_board = [[0]*9 for _ in range(9)]
used_hint = False
current_difficulty = 0

moves_stack = []

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
        if number_buttons[current_number-1].cget("state") == "disabled":
            messagebox.showerror("Too many numbers", "You already have 9 instances of this number on the board. Please erase one before adding another.")
            return    
        button.config(text=str(current_number))
        button.config(bg="dark gray")
        move_row, move_col = button_subgrid(button)
        move_made = [move_row, move_col, str(current_number)]
        moves_stack.append(move_made)
        # Check if the board is complete, update numbers used, check for dupes
        check()
        count_numbers()
        check_dupes(button)
    elif action_type == 2:
        button.config(text="")
        button.config(bg="lightgray")  # Reset to default background color
        count_numbers()

        # The following code is commented out because it appears to be a bug
        # # Get the global row and column of the erased cell
        # global_row, global_col = button_subgrid(button)

        # # Revalidate the row
        # for col in range(9):
        #     check_dupes(cell_buttons[global_row][col])

        # # Revalidate the column
        # for row in range(9):
        #     check_dupes(cell_buttons[row][global_col])

        # # Revalidate the subgrid
        # subgrid_row_start = global_row - (global_row % 3)
        # subgrid_col_start = global_col - (global_col % 3)
        # for i in range(3):
        #     for j in range(3):
        #         check_dupes(cell_buttons[subgrid_row_start + i][subgrid_col_start + j])
        
    else:
        print("Invalid action")

def note_answer_changed(button):
    global action_type
    action_type = button.cget("value")


def new_board(difficulty, reset=False):
    global game_board
    global solved_board
    global reset_board
    global elapsed_time
    global number_counts
    global moves_stack
    global current_difficulty

    current_difficulty = difficulty
    moves_stack = []
    number_counts = {i: 0 for i in range(1, 10)}
    
    if not reset:
        game_board, solved_board = board.generate_full_board(difficulty)
        reset_board = game_board.copy()
    else:
        game_board = reset_board.copy()

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

    elapsed_time = 0
    if not_paused == 0:
        pause_play()    
    
    count_numbers()

def check():    
    for i in range(9):
        for j in range(9):
            if cell_buttons[i][j].cget("text") == "":
                return    
            
    game_board = [[0]*9 for _ in range(9)]

    for i in range(9):
        for j in range(9):
            game_board[i][j] = int(cell_buttons[i][j].cget("text"))
    if board.board_is_valid(game_board) and used_hint == False:
        messagebox.showinfo("Success", f"Congratulations! You solved the puzzle in {elapsed_time_label.config('text')[4]}!")
    elif board.board_is_valid(game_board) and used_hint == True:
        messagebox.showinfo("Success", f"Congratulations! You solved the puzzle in {elapsed_time_label.config('text')[4]}! You used a hint, so your time will not be recorded.")
    else:
        messagebox.showerror("Error", "The solution is incorrect. Please try again.")

def check_dupes(button):
    # Get the number in the button
    num = button.cget("text")
    if num == "":  # Skip empty cells
        return

    # Get the row and column of the button within its subgrid
    local_row = int(button.grid_info()["row"])
    local_col = int(button.grid_info()["column"])

    # Calculate the global row and column indices
    global_row, global_col = button_subgrid(button)

    # Check for duplicates in the same box
    for i in range(3):
        for j in range(3):
            cell_value = cell_buttons[global_row - (global_row % 3) + i][global_col - (global_col % 3) + j].cget("text")
            if (i == local_row and j == local_col) or cell_value == "":
                continue
            if cell_value == num:
                button.config(bg="red")
                return

    # Check for duplicates in the same row
    for i in range(9):
        cell_value = cell_buttons[global_row][i].cget("text")
        if i == global_col:
            continue  # Skip the current cell
        if cell_value == num:
            button.config(bg="red")
            return

    # Check for duplicates in the same column
    for i in range(9):
        cell_value = cell_buttons[i][global_col].cget("text")
        if i == global_row:
            continue  # Skip the current cell
        if cell_value == num:
            button.config(bg="red")
            return

def update_timer():
    global elapsed_time
    global timer_after_id
    elapsed_time += 1

    # Calculate minutes and seconds
    minutes = elapsed_time // 60
    seconds = elapsed_time % 60

    elapsed_time_label.config(text=f"{minutes:02}:{seconds:02}")
    timer_after_id = elapsed_time_label.after(1000, update_timer)   

    if elapsed_time > 3600:  # 1 hour
        sys.exit()

def pause_play():
    global not_paused
    global timer_after_id
    if not_paused == 0:
        not_paused = 1
        pause_button.config(text="||")
        update_timer()
    else:
        not_paused = 0
        pause_button.config(text=">")
        if timer_after_id:
            elapsed_time_label.after_cancel(timer_after_id)
            timer_after_id = None

def reset_timer():
    global elapsed_time
    global not_paused
    global timer_after_id
    elapsed_time = 0
    elapsed_time_label.config(text="00:00")
    not_paused = 1
    pause_button.config(text="||")
    if timer_after_id:
        elapsed_time_label.after_cancel(timer_after_id)
        timer_after_id = None
    update_timer()

def count_numbers():
    # Count the numbers on the board
    global number_counts
    number_counts = {i: 0 for i in range(1, 10)}
    for i in range(9):
        for j in range(9):
            if cell_buttons[i][j].cget("text") != "":
                number_counts[int(cell_buttons[i][j].cget("text"))] += 1

    for num in number_counts:
        count_labels[num].config(text=f"({number_counts[num]})")

    for num in number_counts:
        if number_counts[num] >= 9:
            number_buttons[num-1].config(state="disabled")
        else:
            number_buttons[num-1].config(state="normal")

def button_subgrid(button):
    # Get the row and column of the button within its subgrid
    local_row = int(button.grid_info()["row"])
    local_col = int(button.grid_info()["column"])

    # Identify which subgrid the button belongs to
    parent_subgrid = button.master  # The parent frame (subgrid) of the button
    for i in range(3):
        for j in range(3):
            if subframes[i][j] == parent_subgrid:
                subgrid_row = i
                subgrid_col = j
                break

    # Calculate the global row and column indices
    global_row = subgrid_row * 3 + local_row
    global_col = subgrid_col * 3 + local_col

    return global_row, global_col

def undo_move():
    if moves_stack:
        last_move = moves_stack.pop()
        row, col, _ = last_move
        cell_buttons[row][col].config(text="")
        cell_buttons[row][col].config(bg="lightgray")  # Reset to default background color
        count_numbers()

    else:
        messagebox.showinfo("Undo", "No moves to undo.")

def validate_current_board():
    count = 0
    for i in range(9):
        for j in range(9):
            cell_value = cell_buttons[i][j].cget("text")
            if cell_value != "":
                cell_value = int(cell_value)
                if cell_value != solved_board[i][j]:
                    cell_buttons[i][j].config(bg="red")
                    count += 1
    if count == 0:
        messagebox.showinfo("Validation", "The board is valid!")

def hint():
    global used_hint
    used_hint = True
    positions = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(positions)

    for row, col in positions:
        if cell_buttons[row][col].cget("text") == "":
            cell_buttons[row][col].config(text=str(solved_board[row][col]))
            cell_buttons[row][col].config(bg="lightblue")
            moves_stack.append([row, col, str(solved_board[row][col])])
            count_numbers()
            check()
            return
        
def show_solution():
    global used_hint
    used_hint = True
    for i in range(9):
        for j in range(9):
            cell_buttons[i][j].config(text=str(solved_board[i][j]))
            count_numbers()

if __name__ == "__main__":
    gui = Tk()

    gui.title("Zudoku")
    gui.geometry("1200x800")

    # Main Frame
    main_frame = Frame(gui)
    main_frame.pack()

    # # Highscores
    highscores_frame = Frame(main_frame)
    highscores_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")
    highscores_label = Label(highscores_frame, text="Highscores", font=("Arial", 12))
    highscores_label.grid(row=0, column=0, padx=5, pady=5)
    highscores_list = Listbox(highscores_frame, width=30, height=10)
    highscores_list.grid(row=1, column=0, padx=5, pady=5)
    # Add some dummy highscores
    highscores = [
        "Player1 - 00:30",
        "Player2 - 01:15",
        "Player3 - 02:45"
    ]
    for score in highscores:
        highscores_list.insert(END, score)

    

    # Create a frame for the grid
    grid_frame = Frame(main_frame, borderwidth=2, relief="solid")
    grid_frame.grid(row=0, column=1, padx=1, pady=1)

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
    button_frame.grid(row=1, column=1, padx=10, pady=1, sticky="n")

    # Create a label for the number buttons
    number_label = Label(button_frame, text="Select a number for Answer/Note modes:", font=("Arial", 10))
    number_label.grid(row=0, column=0, columnspan=9, pady=1, sticky="w")
    number_label_subtext = Label(button_frame, text="Numbers in parentheses is the count of how many are on the board", font=("Arial", 8))
    number_label_subtext.grid(row=1, column=0, columnspan=9, sticky="w")
    

    # Number Buttons
    one_button = Button(button_frame, text="1", command=lambda: number_button_clicked(1, one_button), width=2, height=2)
    one_button.grid(row=2, column=0)
    
    two_button = Button(button_frame, text="2", command=lambda: number_button_clicked(2, two_button), width=2, height=2)
    two_button.grid(row=2, column=1)

    three_button = Button(button_frame, text="3", command=lambda: number_button_clicked(3, three_button), width=2, height=2)
    three_button.grid(row=2, column=2)

    four_button = Button(button_frame, text="4", command=lambda: number_button_clicked(4, four_button), width=2, height=2)
    four_button.grid(row=2, column=3)

    five_button = Button(button_frame, text="5", command=lambda: number_button_clicked(5, five_button), width=2, height=2)
    five_button.grid(row=2, column=4)

    six_button = Button(button_frame, text="6", command=lambda: number_button_clicked(6, six_button), width=2, height=2)
    six_button.grid(row=2, column=5)

    seven_button = Button(button_frame, text="7", command=lambda: number_button_clicked(7, seven_button), width=2, height=2)
    seven_button.grid(row=2, column=6)

    eight_button = Button(button_frame, text="8", command=lambda: number_button_clicked(8, eight_button), width=2, height=2)
    eight_button.grid(row=2, column=7)

    nine_button = Button(button_frame, text="9", command=lambda: number_button_clicked(9, nine_button), width=2, height=2)
    nine_button.grid(row=2, column=8)

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

    # Create labels for the number counts
    count_labels = {}

    for i in range(1, 10):
        count_labels[i] = Label(button_frame, text=f"({number_counts[i]})", font=("Arial", 10))
        count_labels[i].grid(row=3, column=i-1, padx=5, pady=5)  
  

    # Create frame for the action buttons
    action_frame = Frame(main_frame)
    action_frame.grid(row=0, column=2, padx=20, pady=30)

    # Create a subframe for the timer
    timer_frame = Frame(action_frame)
    timer_frame.grid(row=0, column=0, padx=0, pady=0, sticky="w")

    # Timer
    timer_label = Label(timer_frame, text="Timer: ", font=("Arial", 10))
    timer_label.grid(row=0, column=0, padx=0, pady=1, sticky="w")

    elapsed_time_label = Label(timer_frame, text="", font=("Arial", 10))
    elapsed_time_label.grid(row=0, column=1, padx=5, pady=1)

    pause_button = Button(timer_frame, text="||", command=pause_play)
    pause_button.grid(row=1, column=0, padx=1, pady=5)

    reset_timer_button = Button(timer_frame, text="Reset", command=reset_timer)
    reset_timer_button.grid(row=1, column=1, padx=5, pady=10, sticky="w")


    # Action buttons
    game_options_label = Label(action_frame, text="Game Options:", font=("Arial", 10))
    game_options_label.grid(row=1, column=0, pady=5, sticky="w")

    new_game_button = Button(action_frame, text="New Game", command=lambda: new_board(difficulty_selected.get()), width=10)
    new_game_button.grid(row=2, column=0, pady=5)

    reset_board_button = Button(action_frame, text="Reset Board", command=lambda: new_board(difficulty_selected.get(), True), width=10)
    reset_board_button.grid(row=3, column=0, pady=5)

    difficulty_label = Label(action_frame, text="Difficulty:", font=("Arial", 10))
    difficulty_label.grid(row=4, column=0, pady=5, sticky="w")

    difficulty_selected = IntVar(value=0)
    easy_radio = Radiobutton(action_frame, text="Easy (default)", variable=difficulty_selected, value=0, anchor="w")
    easy_radio.grid(row=5, column=0, sticky="w")

    medium_radio = Radiobutton(action_frame, text="Medium", variable=difficulty_selected, value=1, anchor="w")
    medium_radio.grid(row=6, column=0, sticky="w")

    hard_radio = Radiobutton(action_frame, text="Hard", variable=difficulty_selected, value=2, anchor="w")
    hard_radio.grid(row=7, column=0, sticky="w")

    note_answer_label = Label(action_frame, text="Current Entry Mode:", font=("Arial", 10))
    note_answer_label.grid(row=8, column=0, pady=5, sticky="w")

    action_selected = IntVar(value=1)

    answer_radio = Radiobutton(action_frame, text="Answer", command=lambda: note_answer_changed(answer_radio), variable=action_selected, value=1, anchor="w")
    answer_radio.grid(row=9, column=0, sticky="w")

    note_radio = Radiobutton(action_frame, text="Note", command=lambda: note_answer_changed(note_radio), variable=action_selected, value=0, anchor="w", state="disabled")
    note_radio.grid(row=10, column=0, sticky="w")

    erase_radio = Radiobutton(action_frame, text="Erase", command=lambda: note_answer_changed(erase_radio), variable=action_selected, value=2, anchor="w")
    erase_radio.grid(row=11, column=0, sticky="w")

    undo_botton = Button(action_frame, text="Undo", command=undo_move, width=10)
    undo_botton.grid(row=12, column=0, pady=5, sticky="w")

    validate_button = Button(action_frame, text="Validate", command=validate_current_board, width=10)
    validate_button.grid(row=13, column=0, pady=5, sticky="w")

    hint_button = Button(action_frame, text="Hint", command=hint, width=10)
    hint_button.grid(row=14, column=0, pady=5, sticky="w")

    show_solution_button = Button(action_frame, text="Show Solution", command=show_solution, width=10)
    show_solution_button.grid(row=15, column=0, pady=5, sticky="w")
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

    update_timer()

    gui.mainloop() 

    