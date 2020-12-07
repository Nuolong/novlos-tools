#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog

# File explorer
def chooseFile():
    filename = tk.filedialog.askopenfilename(initialdir = "~/Downloads",
                                             title = "Open Files",
                                             filetypes = (
                                             ("PDF files", "*.pdf"),
                                             ("All files", "*.*")))
    # change label to match selected file
    lbl_file_explorer.configure(text = filename)



window = tk.Tk()
window.title('Novlos Tool')
window.config(background = "#e6e6ff")

lbl_file_explorer = tk.Label(window,
                             text = "Click 'Select File' to choose a file",
                             width = 50, height = 4,
                             fg = "blue")


btn_explore = tk.Button(window,
                        text = "Select File",
                        command = chooseFile)

lbl_file_explorer.grid(column = 1, row = 1)
btn_explore.grid(column = 1, row = 2)

# wait for events
window.mainloop()
