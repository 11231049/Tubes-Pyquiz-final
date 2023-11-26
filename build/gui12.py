
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/hanshi/Tkinter-Designer/tkdesigner/build/assets/frame12")


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

canvas.create_text(
    106.0,
    86.0,
    anchor="nw",
    text="Evaluasi Quiz",
    fill="#FFFFFF",
    font=("GermaniaOne Regular", 32 * -1)
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
    x=96.0,
    y=477.0,
    width=202.0,
    height=40.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=96.0,
    y=532.0,
    width=243.0,
    height=41.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    177.5,
    318.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFF9F9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=146.0,
    y=237.0,
    width=63.0,
    height=161.0
)

canvas.create_text(
    52.0,
    129.0,
    anchor="nw",
    text="     Selamat (Username) !\n     kamu kompeten dalam \nQuiz Algoritma Pemograman :) \n",
    fill="#FFFFFF",
    font=("GermaniaOne Regular", 24 * -1)
)

canvas.create_text(
    19.0,
    137.0,
    anchor="nw",
    text="  ",
    fill="#FFFFFF",
    font=("GermaniaOne Regular", 24 * -1)
)
window.resizable(False, False)
window.mainloop()
