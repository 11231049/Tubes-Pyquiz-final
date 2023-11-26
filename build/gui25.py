
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/hanshi/Tkinter-Designer/tkdesigner/build/assets/frame25")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("360x800")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 360,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    95.0,
    43.0,
    image=image_image_1
)

canvas.create_rectangle(
    26.0,
    158.0,
    340.0,
    425.0,
    fill="#FFF9F9",
    outline="")

canvas.create_text(
    26.0,
    91.0,
    anchor="nw",
    text="Pembahasan",
    fill="#FFFFFF",
    font=("GermaniaOne Regular", 24 * -1)
)

canvas.create_text(
    45.0,
    175.0,
    anchor="nw",
    text="C.Sebuah blok kode yang dapat dipanggil dengan sebuah nama\n\nFungsi pada python dapat digunakan berulang, cukup sekali mendefinisikan fungsi dan ditempat lain pun bisa menggunakannya selama dalam satu program.",
    fill="#000000",
    font=("GermaniaOne Regular", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=101.0,
    y=675.0,
    width=169.0,
    height=37.0
)
window.resizable(False, False)
window.mainloop()
