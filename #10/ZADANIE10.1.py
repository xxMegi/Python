import tkinter as tk
import random

def roll_dice():
    result = random.randint(1, 6)
    result_label.config(text=f"WYNIK: {result}", fg="purple")
    dice_image_label.config(image=images[result - 1])

root = tk.Tk()
root.title("Symulator kostki do gry")
root.geometry("400x350")

result_label = tk.Label(root, text="Zagrajmy! Kliknij, aby rzucić kostką", font=("Comic Sans MS", 15), fg="purple")
result_label.pack(pady=20)

images = [
    tk.PhotoImage(file=f"kostka/kostka_{i}.png") for i in range(1, 7)
]

dice_image_label = tk.Label(root)
dice_image_label.pack(pady=20)
button = tk.Button(root, text="RZUĆ KOSTKĄ!", command=roll_dice, font=("Comic Sans MS", 17), bg="pink")
button.pack(pady=20)

root.mainloop()