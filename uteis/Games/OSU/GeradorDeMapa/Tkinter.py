import tkinter as tk
from tkinter import ttk

def main():
    # Criação da janela principal
    root = tk.Tk()
    root.title("Olá Mundo")
    root.geometry("300x150")
    
    # Estilo moderno usando ttk
    style = ttk.Style()
    style.theme_use("clam")  # Define um tema moderno
    
    # Configuração de cores para o modo escuro
    root.configure(bg="#2E2E2E")  # Fundo da janela principal
    style.configure("TLabel", background="#2E2E2E", foreground="#FFFFFF", font=("Helvetica", 16))
    style.configure("TButton", background="#444444", foreground="#FFFFFF")
    style.map("TButton", background=[("active", "#555555")])  # Cor ao passar o mouse
    
    # Label para exibir "Olá, Mundo!"
    label = ttk.Label(root, text="Olá, Mundo!")
    label.pack(pady=20)
    
    # Botão para fechar a janela
    button = ttk.Button(root, text="Fechar", command=root.destroy)
    button.pack(pady=10)
    
    # Inicia o loop da interface gráfica
    root.mainloop()

if __name__ == "__main__":
    main()
