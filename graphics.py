import tkinter as tk

# Root of the app
root = tk.Tk()

root.title('LSB Reader')
root.geometry('360x480')
root.minsize(360,480)
root.maxsize(360,480)
# root.iconbitmap('ressources/logo.ico')
root.config(background='#55aaee')

action_frame = tk.Frame(root, bg='#55aaee')

label_title = tk.Label(root, text="Welcome on LSB reader", font=("Arial", 20), bg='#55aaee', fg="#ffeedd")
label_title.pack(side='top', expand=True)

question_texte = tk.Label(root, text="Que veux tu faire ?", font=("Arial", 10), bg='#55aaee', fg="#ffeedd")
question_texte.pack(expand=True)

encode_button = tk.Button(action_frame, text = "Encoder une image", font=("Arial", 10), fg='#55aaee', bg="#ffeedd")
encode_button.pack(expand=True, pady=50)

decode_button = tk.Button(action_frame, text = "Décoder une image", font=("Arial", 10), fg='#55aaee', bg="#ffeedd")
decode_button.pack(expand=True, pady=50)

action_frame.pack(expand=True, pady=50)

# Encode Page


# Decode Page


root.mainloop()