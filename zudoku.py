from tkinter import *
from board import *

if __name__ == "__main__":
    gui = Tk()
    app = Board(gui)
    #Start the GUI event loop 
    gui.mainloop() 