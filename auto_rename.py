import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import DND_FILES, TkinterDnD
import os

class FileRenamerApp(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Renamer")
        self.geometry("600x400")

        self.file_structure_label = ttk.Label(self, text="File Structure: {base_name}_{number}.{extension}")
        self.file_structure_label.pack(pady=10)

        self.base_name_label = ttk.Label(self, text="Base Name:")
        self.base_name_label.pack()
        self.base_name_entry = ttk.Entry(self)
        self.base_name_entry.insert(0, "renamed_file") # Default base name
        self.base_name_entry.pack(pady=5)

        self.drop_area = ttk.Label(self, text="Drop files here", relief="solid", borderwidth=2, padding=50)
        self.drop_area.pack(expand=True, fill="both", padx=50, pady=50)
        self.drop_area.drop_target_register(DND_FILES)
        self.drop_area.dnd_bind('<<Drop>>', self.on_drop)

    def on_drop(self, event):
        files = event.data.split()
        for file_path in files:
            self.rename_file(file_path)

    def rename_file(self, file_path):
        base_name = self.base_name_entry.get()
        file_name, file_extension = os.path.splitext(file_path)
        file_extension = file_extension.lower()
        
        dir_path = os.path.dirname(file_path)
        
        number = 1
        while True:
            new_file_name = f"{base_name}_{number}{file_extension}"
            new_file_path = os.path.join(dir_path, new_file_name)
            if not os.path.exists(new_file_path):
                break
            number += 1

        try:
            os.rename(file_path, new_file_path)
            print(f"Renamed '{file_path}' to '{new_file_path}'")
        except Exception as e:
            print(f"Error renaming '{file_path}': {e}")

if __name__ == "__main__":
    app = FileRenamerApp()
    app.mainloop()
