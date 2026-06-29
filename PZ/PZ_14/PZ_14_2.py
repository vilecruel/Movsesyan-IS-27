import tkinter as tk
from tkinter import messagebox


def reverse_number():
    input_text = entry.get()

    if not input_text.isdigit() or len(input_text) != 3:
        messagebox.showerror(
            "Ошибка", "Пожалуйста, введите корректное трёхзначное число!"
        )
        return

    original_number = int(input_text)
    reversed_number = int(input_text[::-1])

    result_label.config(
        text=f"Исходное число: {original_number}\nРазвёрнутое число: {reversed_number}"
    )


root = tk.Tk()
root.title("Разворот числа")
root.geometry("350x200")
root.resizable(False, False)

instruction_label = tk.Label(
    root, text="Введите трёхзначное число:", font=("Arial", 11)
)
instruction_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), justify="center", width=10)
entry.pack(pady=5)

process_button = tk.Button(
    root, text="Развернуть", command=reverse_number, bg="#4CAF50", fg="white"
)
process_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11, "bold"), fg="#333333")
result_label.pack(pady=10)

root.mainloop()
