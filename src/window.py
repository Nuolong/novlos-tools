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

# action vars
action_var = tk.IntVar()

# File explorer
def chooseFile(i):
    filename = tk.filedialog.askopenfilename(initialdir = "~/Downloads",
                                             title = "Open Files",
                                             filetypes = (
                                             ("PDF files", "*.pdf"),
                                             ("All files", "*.*")))
    # change label to match selected file
    ent_file_explorer[i].configure(text = filename)


# determine action
def chooseAction():
    if action_var.get() == 0:       # encrypt
        print("0")
    elif action_var.get() == 1:     # decrypt
        print("1")
    elif action_var.get() == 2:     # merge
        print("2")
    elif action_var.get() == 3:     # split
        print("3")

# create file inputs
for i in range(FILE_COUNT):
    ent_file_explorer.append(tk.Label(window,
                                 width = 70,
                                 fg = "blue"))

    chooseFile_arg = partial(chooseFile, i)
    btn_explore = tk.Button(window,
                            text = "Select File",
                            command = chooseFile_arg)

    ent_file_explorer[i].grid(column = 0, row = i, columnspan = 4)
    btn_explore.grid(column = 4, row = i)

# create action buttons
btn_encrypt = tk.Radiobutton(window,
                             text = "Encrypt",
                             padx = 10,
                             pady = 5,
                             variable = action_var,
                             value = 0)
btn_encrypt.grid(column = 0, row = FILE_COUNT)

btn_decrypt = tk.Radiobutton(window,
                             text = "Decrypt",
                             padx = 10,
                             pady = 5,
                             variable = action_var,
                             value = 1)
btn_decrypt.grid(column = 1, row = FILE_COUNT)

btn_merge = tk.Radiobutton(window,
                             text = "Merge",
                             padx = 10,
                             pady = 5,
                             variable = action_var,
                             value = 2)
btn_merge.grid(column = 2, row = FILE_COUNT)

btn_split = tk.Radiobutton(window,
                             text = "Split",
                             padx = 10,
                             pady = 5,
                             variable = action_var,
                             value = 3)
btn_split.grid(column = 3, row = FILE_COUNT)

# execute button
btn_execute = tk.Button(window,
                        text = "Execute",
                        command = chooseAction,
                        fg = "blue",
                        bg = "#add8e6")
btn_execute.grid(column = 4, row = FILE_COUNT)

# wait for events
window.mainloop()
