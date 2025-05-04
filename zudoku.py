from tkinter import *

current_number = 1

# note = 0 # answer = 1
action_type = 1

def number_button_clicked(number, button):
    global current_number
    current_number = number
    button.config(relief="sunken")
    for btn in number_buttons:
        if btn != button:
            btn.config(relief="raised")

def cell_button_clicked(button):
    global current_number
    if action_type == 1:
        button.config(text=str(current_number))
    elif action_type == 2:
        button.config(text="")
    else:
        print("not implemented yet")

def note_answer_changed(btn):
    global action_type
    action_type = btn.cget("value")
    print("Action type changed to:", action_type)

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

    # Create a 3x3 grid of buttons inside each subframe
    for i in range(3):
        for j in range(3):
            for x in range(3):
                for y in range(3):
                    cell_button = Button(
                        subframes[i][j],
                        text="",
                        width=2,
                        height=2
                    )
                    cell_button.config(command=lambda b=cell_button: cell_button_clicked(b))
                    cell_button.grid(row=x, column=y, padx=0, pady=0)


    # Create a frame for the buttons
    button_frame = Frame(main_frame)
    button_frame.grid(row=1, column=0, padx=20, pady=20)

    # Number Buttons
    one_button = Button(button_frame, text="1", command=lambda: number_button_clicked(1, one_button), width=2, height=2, relief="sunken")
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

    # Create frame for the action buttons
    action_frame = Frame(main_frame)
    action_frame.grid(row=0, column=1, padx=20, pady=20)

    # Action buttons
    note_answer_label = Label(action_frame, text="Mode:", font=("Arial", 10))
    note_answer_label.grid(row=0, column=0)

    selected = StringVar()
    note_radio = Radiobutton(action_frame, text="Note", command=lambda: note_answer_changed(note_radio), variable=selected, value=0, anchor="w")
    note_radio.grid(row=1, column=0, sticky="w")
    
    answer_radio = Radiobutton(action_frame, text="Answer", command=lambda: note_answer_changed(answer_radio), variable=selected, value=1, anchor="w")
    answer_radio.grid(row=2, column=0, sticky="w")
    answer_radio.select()

    erase_radio = Radiobutton(action_frame, text="Erase", command=lambda: note_answer_changed(erase_radio), variable=selected, value=2, anchor="w")
    erase_radio.grid(row=3, column=0, sticky="w")

    gui.mainloop() 