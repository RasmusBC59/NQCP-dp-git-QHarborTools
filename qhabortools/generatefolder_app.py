import tkinter as tk
from qhabortools.generatefolder import FolderGeneratorApp


def run():
    root = tk.Tk()

    FolderGeneratorApp(root)

    root.mainloop()
