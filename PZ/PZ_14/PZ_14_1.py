#Практическая 14

import tkinter as tk
from tkinter import ttk

def run_task_1():
    root = tk.Tk()
    root.title("Testform")
    root.geometry("650x550")
    root.configure(bg="#1a1a1a")

    style = ttk.Style()
    style.theme_use('clam')

    main_frame = tk.Frame(root, bg="#ffffff", bd=1, relief="solid")
    main_frame.pack(pady=20, padx=20, fill="both", expand=True)

    header_frame = tk.Frame(main_frame, bg="#f0f0f0", bd=0)
    header_frame.pack(fill="x", side="top")

    header_line = tk.Frame(main_frame, bg="#b3b3b3", height=1)
    header_line.pack(fill="x", side="top")

    header_label = tk.Label(header_frame, text="Testform", bg="#f0f0f0", fg="#000000", font=("Arial", 12, "bold"), anchor="w")
    header_label.pack(fill="x", padx=20, pady=10)

    content_frame = tk.Frame(main_frame, bg="#ffffff")
    content_frame.pack(fill="both", expand=True, padx=20, pady=15)

    def create_label(text, row):
        lbl = tk.Label(content_frame, text=text, bg="#ffffff", fg="#000000", font=("Arial", 11), anchor="w", width=15)
        lbl.grid(row=row, column=0, sticky="nw", pady=8)

    create_label("Name", 0)
    name_entry = tk.Entry(content_frame, width=35, bd=1, relief="solid", highlightthickness=0)
    name_entry.grid(row=0, column=1, sticky="w", pady=8)

    create_label("Password", 1)
    pass_entry = tk.Entry(content_frame, width=35, show="*", bd=1, relief="solid", highlightthickness=0)
    pass_entry.grid(row=1, column=1, sticky="w", pady=8)

    create_label("Gender", 2)
    gender_var = tk.StringVar(value="None")
    gender_frame = tk.Frame(content_frame, bg="#ffffff")
    gender_frame.grid(row=2, column=1, sticky="w", pady=4)
    tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", bg="#ffffff", fg="#000000", activebackground="#ffffff").pack(anchor="w", pady=2)
    tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", bg="#ffffff", fg="#000000", activebackground="#ffffff").pack(anchor="w", pady=2)

    create_label("Continent", 3)
    continent_combo = ttk.Combobox(content_frame, values=["Please select...", "Asia", "Africa", "Europe", "North America", "South America", "Australia"], width=33, state="readonly")
    continent_combo.current(0)
    continent_combo.grid(row=3, column=1, sticky="w", pady=8)

    create_label("Meals", 4)
    meals_frame = tk.Frame(content_frame, bg="#ffffff")
    meals_frame.grid(row=4, column=1, sticky="w", pady=4)
    meal1 = tk.BooleanVar()
    meal2 = tk.BooleanVar()
    meal3 = tk.BooleanVar()
    tk.Checkbutton(meals_frame, text="breakfast", variable=meal1, bg="#ffffff", fg="#000000", activebackground="#ffffff").pack(anchor="w", pady=2)
    tk.Checkbutton(meals_frame, text="lunch", variable=meal2, bg="#ffffff", fg="#000000", activebackground="#ffffff").pack(anchor="w", pady=2)
    tk.Checkbutton(meals_frame, text="dinner", variable=meal3, bg="#ffffff", fg="#000000", activebackground="#ffffff").pack(anchor="w", pady=2)

    create_label("Remark", 5)
    remark_text = tk.Text(content_frame, width=45, height=5, bd=1, relief="solid", highlightthickness=0)
    remark_text.grid(row=5, column=1, sticky="w", pady=8)

    footer_line = tk.Frame(main_frame, bg="#b3b3b3", height=1)
    footer_line.pack(fill="x", side="bottom")

    footer_frame = tk.Frame(main_frame, bg="#f0f0f0", bd=0)
    footer_frame.pack(fill="x", side="bottom")

    cancel_btn = tk.Button(footer_frame, text="Cancel", width=10, bg="#ffffff", fg="#000000", bd=1, relief="solid", activebackground="#e6e6e6", command=root.destroy)
    cancel_btn.pack(side="right", padx=20, pady=10)

    send_btn = tk.Button(footer_frame, text="Send", width=10, bg="#ffffff", fg="#000000", bd=1, relief="solid", activebackground="#e6e6e6")
    send_btn.pack(side="right", pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_task_1()