from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)



my_image = PhotoImage(file="path/to/image_file.png")
button = Button(image=my_image, highlightthickness=0)

window.mainloop()

