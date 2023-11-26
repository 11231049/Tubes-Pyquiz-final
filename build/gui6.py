
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/hanshi/Tkinter-Designer/tkdesigner/build/assets/frame6")


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
    11.0,
    212.0,
    anchor="nw",
    text=" Bagaimana  cara  mengawali  \n         komentar  pada  pyhton?",
    fill="#FFF8F8",
    font=("RubikBubbles Regular", 20 * -1)
)

canvas.create_text(
    11.0,
    95.0,
    anchor="nw",
    text="Jawab  quiz  berikut  dengan  mengisi  kolom  \njawaban  sesuai  opsi  yang  dipilih  (A,B,C)",
    fill="#FFF8F8",
    font=("RubikBubbles Regular", 15 * -1)
)

canvas.create_text(
    48.0,
    305.0,
    anchor="nw",
    text="A.   Tagar  ‘#’\n\nB.   Kurung  ()\n\nC.  Kurawal  {}",
    fill="#FFF8F8",
    font=("RubikBubbles Regular", 16 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    184.5,
    585.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFF9F9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=66.0,
    y=561.0,
    width=237.0,
    height=46.0
)

canvas.create_text(
    42.0,
    525.0,
    anchor="nw",
    text="Opsi Jawaban",
    fill="#FFFFFF",
    font=("GermaniaOne Regular", 24 * -1)
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
    x=106.0,
    y=654.0,
    width=169.0,
    height=37.0
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
    x=290.0,
    y=23.0,
    width=42.0,
    height=41.0
)
window.resizable(False, False)
window.mainloop()
