from tkinter import *

class Cell:
    def __init__(self, bed_frame, IsHint=False):
        # A cell is a 3x3 grid where each cell is a number from 1 to 9 or a number occupys the whole grid

        self.IsHint = IsHint
        self.bed_frame = bed_frame
        # A cell exists in a bed_frame and not it's own frame
        if self.IsHint:
            print("Creating a hint cell")
            self.entries = [[None for _ in range(3)] for _ in range(3)]
            for i in range(9):
                for j in range(9):
                    # I need to adjust the size of the entries later
                    entry = Entry(self.bed_frame, width=2, font=("Arial", 24), justify="center")
                    entry.grid(row=i, column=j, padx=1, pady=1)
                    self.entries[i][j] = entry

        else:
            self.entry = Entry(self.bed_frame, width=2, font=("Arial", 24), justify="center")
            
class Bed:
    def __init__(self, sudoku_frame):
        self.bed_frame = Frame(sudoku_frame, bg="black", bd=5, relief="solid")
        self.cell_grid = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                # Pass the row and column to the Cell
                self.cell_grid[i][j] = Cell(self.bed_frame, IsHint=False)
                # Place the Cell's Entry widget in the correct position
                self.cell_grid[i][j].entry.grid(row=i, column=j, padx=1, pady=1)



class Board:
    def __init__(self, app_gui):
        # A board is a 3x3 grid of beds
        # Each bed is a 3x3 grid of cells
        # Each cell is a number from 1 to 9 or a number occupies the whole grid
        # Internally I'll refer to each bed by it's cardinal position with bed 5 being the center
        # IE bed 1 is NW, bed 2 is N, bed 3 is NE, bed 4 is W, bed 5 is C, bed 6 is E, bed 7 is SW, bed 8 is S, bed 9 is SE
        
        # Create a frame for the Sudoku grid
        self.sudoku_frame = Frame(app_gui, bg="black", bd=5, relief="solid")
        self.sudoku_frame.pack(pady=50)


        # Create a 3x3 grid of Bed widgets
        self.beds = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                # Create a Bed and pass the sudoku_frame to it
                self.beds[i][j] = Bed(self.sudoku_frame)
                # Place the Bed's frame in the correct position
                self.beds[i][j].bed_frame.grid(row=i, column=j, padx=5, pady=5)


        

if __name__ == "__main__":
    # Testing
    gui = Tk()
    gui.configure(background="#D3D3D3")
    gui.title("Zudoku test")
    gui.geometry("1200x1200")
    gui.resizable(True, True)
    app = Board(gui)
    # Start the GUI event loop
    gui.mainloop()