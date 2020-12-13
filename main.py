import random
import pandas
from tkinter import *

# ------------------------- CONSTANT ---------------------------------- #
BLACK = "#2C333D"
YELLOW = "#FCD836"
WHITE = "#FFFFFF"
GRAY_WHITE = "#F4F4F4"
BAHNSCHRIFT = "Bahnschrift"
CALIBRI = "Calibri"

# -------------------------- WORD DICT ------------------------------- #
# default card is empty
current_card = {}

# know word dictionary is empty
known_words = {}

# reading the data from know data
try:
    know_data = pandas.read_csv("data/know_word.csv")
except FileNotFoundError:
    # if know data not found then go to original data
    original_data = pandas.read_csv("data/Bangla_word_list.csv")
    learning = original_data.to_dict(orient="records")
else:
    # creating dictionary using pandas
    learning = know_data.to_dict(orient="records")


# -------------------------- NEXT CARD ------------------------------- #
# TODO: when cross button pressed show the next word in english and flip the image

def next_card():
    """Return next value randomly from the dictionary"""
    # global current cart
    global current_card, flip_timer
    # cancel the timer
    window.after_cancel(flip_timer)
    # randomly choose word from the dictionary
    current_card = random.choice(learning)
    # replace the title text in the UI
    canvas.itemconfig(card_title, text="English", fill=BLACK)
    # replace the word text in the UI
    canvas.itemconfig(card_word, text=current_card["English"], fill=BLACK)
    # change the background images if button pressed
    canvas.itemconfig(card_background, image=front_card_image)
    # flip timer
    flip_timer = window.after(3000, func=flip_card)


# ------------------------- FLIP CARD -------------------------------- #
# TODO: Flip card after 3 seconds and show the bangla value
def flip_card():
    """Flip the card after 3 seconds """
    canvas.itemconfig(card_title, text="Bangla", fill=WHITE)
    # show the equivalent meaning of the current word
    canvas.itemconfig(card_word, text=current_card["Bangla"], fill=WHITE)
    # changing the background images
    canvas.itemconfig(card_background, image=back_card_image)


# --------------------------- KNOWN WORD ------------------------------ #

# TODO: When know button pressed it save in the know dictionary
def know_word():
    """Save Know word into new file"""
    learning.remove(current_card)
    # remove data from current card
    new_data = pandas.DataFrame(learning)
    # create a new csv file using pandas without index
    new_data.to_csv("data/know_word.csv", index=False)
    # show the next word
    next_card()


# --------------------------- UI SETUP -------------------------------- #

# TODO: Creating Program window
# creating window object
window = Tk()

# add title to the program
window.title("Learn English to Bangla Vocabulary")

# window size
window.config(padx=50, pady=50, bg=GRAY_WHITE)

# add custom favicon
window.iconbitmap(r'images/favicon.ico')

# flip the card after 3 seconds
flip_timer = window.after(3000, func=flip_card)

# TODO: Creating canvas

# creating a canvas
canvas = Canvas(width=800, height=526)

# front card image
front_card_image = PhotoImage(file="images/card_front.png")

# back card image
back_card_image = PhotoImage(file="images/card_back.png")

# assigning the position for front card
card_background = canvas.create_image(400, 263, image=front_card_image)

# Canvas card title
card_title = canvas.create_text(400, 150, text="Title", font=(BAHNSCHRIFT, 40, "normal"))

# canvas card word
card_word = canvas.create_text(400, 263, text="Word", font=(CALIBRI, 60, "bold"))

# canvas config
canvas.config(bg=GRAY_WHITE, highlightthicknes=0)

# canvas grid
canvas.grid(row=0, column=0, columnspan=2)

# TODO: Buttons

# cross icon
cross_icon = PhotoImage(file="images/cancel.png")

# assign icon to the button without border or background thickness


cross_button = Button(image=cross_icon, highlightthicknes=0, borderwidth=0, command=next_card)

# cross button grid
cross_button.grid(row=1, column=0)

# check icon
check_icon = PhotoImage(file="images/checked.png")

# assign icon to the button without border or background thickness
cross_button = Button(image=check_icon, highlightthicknes=0, borderwidth=0, command=know_word)

# check button grid
cross_button.grid(row=1, column=1)

# calling the next card function
next_card()

# run the window
window.mainloop()
