#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog
from functools import partial
#import pdftool.py

FILE_COUNT = 5
file_paths = []
ent_file_explorer = []

# window settings
window = tk.Tk()
window.title('Novlos Tool')
window.config(background = "#e6e6ff")

# File explorer
def chooseFile(i):
    filename = tk.filedialog.askopenfilename(initialdir = "~/Downloads",
                                             title = "Open Files",
                                             filetypes = (
                                             ("PDF files", "*.pdf"),
                                             ("All files", "*.*")))
    # change label to match selected file
    ent_file_explorer[i].configure(text = filename)

# create files
for i in range(FILE_COUNT):
    ent_file_explorer.append(tk.Label(window,
                                 width = 70,
                                 fg = "blue"))

    chooseFile_arg = partial(chooseFile, i)
    btn_explore = tk.Button(window,
                            text = "Select File",
                            command = chooseFile_arg)

    ent_file_explorer[i].grid(column = 0, row = i)
    btn_explore.grid(column = 1, row = i)


# wait for events
window.mainloop()
