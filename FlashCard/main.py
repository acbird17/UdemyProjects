from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")



# ---------------------------- Flashcards ------------------------------- #
def random_word():
    global current_card, flip_timer
    current_card = random.choice(words)
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_body, image=front_card)
    flip_timer = window.after(3000, func=flip_card)
    
def flip_card():
    global current_card
    canvas.itemconfig(card_body, image=back_card)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"])
    
def is_known():
    words.remove(current_card)
    print(len(words))
    data = pandas.DataFrame(words)
    data.to_csv("data/words_to_learn.csv", index=False)
    random_word()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
card_body = canvas.create_image(400, 263, image=front_card)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

x_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=x_image, highlightthickness=0, command=random_word)
wrong_button.grid(column=0, row=1)

check_image = PhotoImage(file="./images/right.png")
right_button = Button(image=check_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

random_word()

window.mainloop()