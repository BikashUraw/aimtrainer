import tkinter as tk
import random

score = 0
shots = 0


def fire(event=None):
    global score, shots

    shots += 1

    # वास्तविक click भएको position
    x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    y = canvas.winfo_pointery() - canvas.winfo_rooty()

    # Head को position
    hx1, hy1, hx2, hy2 = canvas.coords(head)

    if hx1 <= x <= hx2 and hy1 <= y <= hy2:
        score += 1
        result.config(text="HEADSHOT! 🎯")
    else:
        result.config(text="MISS ❌")

    accuracy = (score / shots) * 100
    stats.config(
        text=f"Score: {score} | Accuracy: {accuracy:.1f}%"
    )


def move_target():
    x = random.randint(50, 330)
    y = random.randint(80, 400)

    canvas.coords(head, x, y, x + 40, y + 40)
    canvas.coords(body, x - 15, y + 40, x + 55, y + 130)


root = tk.Tk()
root.title("Safe Headshot Trainer")
root.geometry("400x650")

stats = tk.Label(
    root,
    text="Score: 0 | Accuracy: 0%",
    font=("Arial", 16)
)
stats.pack()

result = tk.Label(
    root,
    text="Click the target head",
    font=("Arial", 18)
)
result.pack()

canvas = tk.Canvas(root, width=400, height=500)
canvas.pack()

head = canvas.create_oval(
    180, 120, 220, 160,
    fill="orange"
)

body = canvas.create_rectangle(
    165, 160, 235, 250,
    fill="blue"
)

fire_button = tk.Button(
    root,
    text="🔥 FIRE",
    font=("Arial", 22)
)
fire_button.pack(pady=10)

fire_button.bind("<Button-1>", fire)

move_button = tk.Button(
    root,
    text="Move Target",
    command=move_target
)
move_button.pack()

root.mainloop()
