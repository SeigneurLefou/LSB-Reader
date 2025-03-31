import tkinter as tk
from tkinter import filedialog

def select_file():
    # Ouvrir la boîte de dialogue pour sélectionner un fichier
    file_path = filedialog.askopenfilename()
    if file_path:
        print(f"Fichier sélectionné : {file_path}")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Sélectionner un fichier")

# Créer un bouton pour ouvrir la boîte de dialogue de sélection de fichier
select_button = tk.Button(root, text="Sélectionner un fichier", command=select_file)
select_button.pack(pady=20)

# Lancer la boucle principale de l'application
root.mainloop()