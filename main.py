import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkcode import CodeEditor

def open_file():
    filepath = filedialog.askopenfilename(defaultextension=".py",
                                            filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, "r") as file:
            code_editor.content = file.read()
        root.title(f"Code Editor - {filepath}")

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".py",
                                              filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, "w") as file:
            file.write(code_editor.content)
        root.title(f"Code Editor - {filepath}")

root = tk.Tk()
root.title("Code Editor")
root.option_add("*tearOff", 0)

# Menu
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar)

file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

notebook = ttk.Notebook(root)
tab_1 = ttk.Frame(notebook)
notebook.add(tab_1, text="Untitled.py")
notebook.pack(fill="both", expand=True)

code_editor = CodeEditor(
    tab_1,
    width=99,
    height=30,
    language="python",
    background="black",
    highlighter="dracula",
    font="Consolas",
    autofocus=True,
    blockcursor=True,
    insertofftime=0,
    padx=10,
    pady=10,
)

code_editor.pack(fill="both", expand=True)
code_editor.content = """print("Hello World")"""
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()
