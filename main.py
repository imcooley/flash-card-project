from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
words = pandas.read_csv("./data/french_words.csv")
records = words.DataFrame.to_dict(orient="records")

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ---------------------------- Canvas ---------------------------- #
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

# ---------------------------- Buttons ---------------------------- #
check_image = PhotoImage(file="./images/right.png")
unknown_button = Button(image=check_image, highlightthickness=0)
unknown_button.grid(row=1, column=1)
cross_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)


window.mainloop()

