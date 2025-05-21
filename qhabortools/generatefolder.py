import pandas as pd
import pathlib
from qdrive.dataset import generate_dataset_info
import tkinter as tk
from tkinter import filedialog, messagebox

def folderfromxl(rootfolder, infofile):
    folderinfo = pd.read_excel(infofile)
    for row in folderinfo.iterrows():
        info_dict = row[1].to_dict()
        folder = info_dict.pop("Folder")
        # TODO tjekk schema 
        subjectID = info_dict["SubjectID"]
        folder_path = rootfolder / subjectID / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        generate_dataset_info(folder_path, attributes=info_dict)
        

class FolderGeneratorApp:
    def __init__(self, root):        
        self.root = root
        self.root.title("Generate Folders")
        self.root.geometry("300x200")
        self.rootfolder = None
        self.infofile = None
        #text_var = tk.StringVar()
        #text_var.set("Hello, World!")
        tk.Button(root, text="Select Root Folder", command=self.select_folder).pack(expand=True, pady=10)
        self.folder_label = tk.Label(root, text="No folder selected", anchor="w")
        self.folder_label.pack(fill="x", padx=10, pady=5)
        tk.Button(root, text="Select Info File", command=self.select_file).pack(expand=True, pady=10)
        self.infofile_label = tk.Label(root, text="No Info File selected", anchor="w")
        self.infofile_label.pack(fill="x", padx=10, pady=5)
        tk.Button(root, text="Generate Folder", command=self.generate_file).pack(expand=True, pady=10)
    
    def folderfromxlapp(self):
        folderfromxl(self.rootfolder, self.infofile)
    


    
    def select_folder(self):
        path = filedialog.askdirectory()
        if path:
            self.rootfolder = pathlib.Path(path)
            self.folder_label.config(text=f"Selected folder: {path}")
            messagebox.showinfo("Folder Selected", f"Selected folder:\n{path}")


    def select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.infofile = pathlib.Path(file_path)
            self.infofile_label.config(text=f"Selected file: {file_path}")
            messagebox.showinfo("File Selected", f"Selected file:\n{file_path}")
            
    def generate_file(self):
        if self.rootfolder is None or self.infofile is None:
            messagebox.showerror("Error", "Please select both a root folder and an info file.")
            return
        self.folderfromxlapp()
        messagebox.showinfo("Success", "Folders generated successfully.")


root = tk.Tk()

app = FolderGeneratorApp(root)

root.mainloop()