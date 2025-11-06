import tkinter as tk
from tkinter import filedialog

def escolher_pdf():
    path = filedialog.askopenfilename(
        title="Escolha um arquivo PDF",
        filetypes=[("Arquivos PDF", "*.pdf"), ("Todos os arquivos", "*.*")]
    )
    if path:
        lbl_arquivo.config(text=path)

def criar_interface():
    root = tk.Tk()
    root.title("Selecionar PDF")
    root.geometry("600x120")
    root.resizable(False, False)

    btn = tk.Button(root, text="Escolher arquivo PDF", command=escolher_pdf)
    btn.pack(pady=12)

    global lbl_arquivo
    lbl_arquivo = tk.Label(root, text="Nenhum arquivo selecionado", anchor="w")
    lbl_arquivo.pack(fill="x", padx=12)

    root.mainloop()

if __name__ == "__main__":
    criar_interface()