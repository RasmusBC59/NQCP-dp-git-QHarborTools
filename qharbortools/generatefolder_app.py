import tkinter as tk

from qharbortools.generatefolder import FolderGeneratorApp


def run() -> None:
    root = tk.Tk()

    FolderGeneratorApp(root)

    root.mainloop()
