#!/usr/bin/env python3

# imports
import tkinter as tk
from tkinter import filedialog
from functools import partial
import pdftool as pdf

# constants
FILE_COUNT = 5
actions = ["Encrypt", "Decrypt", "Merge", "Slice"]
background_clr = "#e6e6ff"

# widget lists
lbl_file_explorer = []
btn_actions = []
ent_file_names = []

# files
file_paths = [0] * FILE_COUNT

# window settings
window = tk.Tk()
window.title('Novlos Tool')
window.config(background = background_clr)

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
        pdf.add_encryption(file_paths, lbl_file_explorer, "abc123", ent_file_names)
    elif action_var.get() == 1:     # decrypt
        pdf.rm_encryption(file_paths, lbl_file_explorer, "wrongpassword", "unlocked")
    elif action_var.get() == 2:     # merge
        print("2")
    elif action_var.get() == 3:     # split
        print("3")

# create file inputs
for i in range(FILE_COUNT):
    # file names
    lbl_file_explorer.append(tk.Label(window,
                                 width = 75,
                                 fg = "blue"))

    # choose file button
    chooseFile_arg = partial(choose_file, i)
    btn_explore = tk.Button(window,
                            text = "Select File",
                            command = chooseFile_arg)

    # arrow appearance
    lbl_arrow = tk.Label(window,
                         text = " --> ",
                         bg = background_clr)

    # new filename entries
    ent_file_names.append(tk.Entry(window,
                                   justify = "center"))

    lbl_file_explorer[i].grid(column = 0, row = i, columnspan = 4, padx = (5,0))
    btn_explore.grid(column = 4, row = i)
    lbl_arrow.grid(column = 5, row = i)
    ent_file_names[i].grid(column = 6, row = i, padx = (0,5))

# create action buttons
for i, action in enumerate(actions):
    btn_actions.append(tk.Radiobutton(window,
                                      text = action,
                                      padx = 10,
                                      pady = 5,
                                      variable = action_var,
                                      value = i))
    btn_actions[i].grid(column = i, row = FILE_COUNT, pady = (5, 5))

# execute button
btn_execute = tk.Button(window,
                        text = "Execute",
                        command = choose_action,
                        fg = "blue",
                        bg = "#add8e6",
                        width = 25)
btn_execute.grid(column = 4, row = FILE_COUNT, columnspan = 3)



# wait for events
window.mainloop()
