import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from graph import plot_functions
from math_engine import clean_expression, suggest_help

# =========================
# FENÊTRE
# =========================
root = tk.Tk()
root.iconbitmap("GraphX.ico")
root.title("GraphX")
root.geometry("1000x650")
root.configure(bg="#0E0E10")

BG = "#0E0E10"
FG = "#FFFFFF"
ACCENT = "#4C6FFF"
ENTRY_BG = "#1E1E1E"

# =========================
# GRAPHE (ZONE PRINCIPALE)
# =========================
fig, ax = plt.subplots()
fig.patch.set_facecolor(BG)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill="both", expand=True)

# =========================
# ASSISTANT
# =========================
assistant_frame = tk.Frame(root, bg="#15151A")
assistant_frame.pack(fill="x", padx=10, pady=5)

assistant_label = tk.Label(
    assistant_frame,
    text="Assistant : prêt à analyser vos fonctions",
    font=("Arial", 10),
    fg="#B0B0B0",
    bg="#15151A",
    anchor="w"
)
assistant_label.pack(fill="x", padx=10, pady=5)

# =========================
# BARRE BASSE
# =========================
bottom_frame = tk.Frame(root, bg=BG)
bottom_frame.pack(fill="x", pady=10)

entry = tk.Entry(
    bottom_frame,
    font=("Arial", 14),
    bg=ENTRY_BG,
    fg=FG,
    insertbackground=FG,
    width=45
)
entry.pack(side="left", padx=10)

# =========================
# TRACER
# =========================
def tracer():
    ax.clear()

    raw = entry.get()
    cleaned = clean_expression(raw)

    functions = cleaned.split(",")

    plot_functions(ax, functions)
    canvas.draw()

    tips = suggest_help(raw)

    if tips:
        assistant_label.config(
            text="Assistant : " + " | ".join(tips)
        )
    else:
        assistant_label.config(
            text="Assistant : fonction tracée avec succès ✔"
        )

# =========================
# BOUTON TRACER
# =========================
btn = tk.Button(
    bottom_frame,
    text="Tracer",
    font=("Arial", 12, "bold"),
    bg=ACCENT,
    fg="white",
    command=tracer
)
btn.pack(side="left", padx=5)

# =========================
# BOUTON PARAMÈTRES (placeholder)
# =========================
settings = tk.Button(
    bottom_frame,
    text="⚙️",
    font=("Arial", 14),
    bg=BG,
    fg=FG,
    relief="flat"
)
settings.pack(side="right", padx=10)

# =========================
# LANCEMENT
# =========================
root.mainloop()