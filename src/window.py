#!/usr/bin/env python3

# imports
import tkinter as tk
from tkinter import filedialog
from functools import partial
import pdftool as pdf

# constants
FILE_COUNT = 5
actions = ["Encrypt", "Decrypt", "Merge", "Slice"]

# widget lists
lbl_file_explorer = []
btn_actions = []

# files
file_paths = [0] * FILE_COUNT

# window settings
window = tk.Tk()
window.title('Novlos Tool')
window.config(background = "#e6e6ff")

# action variable
action_var = tk.IntVar()

# File explorer
def choose_file(i):
    filename = tk.filedialog.askopenfilename(initialdir = "~/Downloads",
                                             title = "Open Files",
                                             filetypes = (
                                             ("PDF files", "*.pdf"),
                                             ("All files", "*.*")))
    # change label to match selected file
    file_paths[i] = filename
    lbl_file_explorer[i].configure(text = filename)


# determine action - currently working on prototypes
def choose_action():
    if action_var.get() == 0:       # encrypt
        pdf.add_encryption(file_paths, lbl_file_explorer, "abc123", "test")
    elif action_var.get() == 1:     # decrypt
        pdf.rm_encryption(file_paths, lbl_file_explorer, "wrongpassword", "unlocked")
    elif action_var.get() == 2:     # merge
        print("2")
    elif action_var.get() == 3:     # split
        print("3")

# create file inputs
for i in range(FILE_COUNT):
    lbl_file_explorer.append(tk.Label(window,
                                 width = 75,
                                 fg = "blue"))

    chooseFile_arg = partial(choose_file, i)
    btn_explore = tk.Button(window,
                            text = "Select File",
                            command = chooseFile_arg)

    lbl_file_explorer[i].grid(column = 0, row = i, columnspan = 4)
    btn_explore.grid(column = 4, row = i)

# create action buttons
for i, action in enumerate(actions):
    btn_actions.append(tk.Radiobutton(window,
                                      text = action,
                                      padx = 10,
                                      pady = 5,
                                      variable = action_var,
                                      value = i))
    btn_actions[i].grid(column = i, row = FILE_COUNT)

# execute button
btn_execute = tk.Button(window,
                        text = "Execute",
                        command = choose_action,
                        fg = "blue",
                        bg = "#add8e6")
btn_execute.grid(column = 4, row = FILE_COUNT)

# wait for events
window.mainloop()
