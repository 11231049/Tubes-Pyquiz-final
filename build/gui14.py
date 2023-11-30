
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame14")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("360x800")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#252525",
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
    90.0,
    154.0,
    anchor="nw",
    text="Jawaban  Benar!",
    fill="#2AE531",
    font=("Grobold", 20 * -1)
)

canvas.create_text(
    25.0,
    193.0,
    anchor="nw",
    text="Yuk  masuk  ke  halaman  penjelasan  !",
    fill="#FFFFFF",
    font=("Grobold", 16 * -1)
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
    x=95.0,
    y=300.0,
    width=169.0,
    height=46.0
)
window.resizable(False, False)
window.mainloop()
