from tkinter import *

# ------------------------- CONSTANT ---------------------------------- #
BLACK = "#2C333D"
YELLOW = "#FCD836"
WHITE = "#FFFFFF"
GRAY_WHITE = "#F4F4F4"
CARD_TITLE = "Bahnschrift"
CARD_WORD = "Calibri"


# -------------------------- NEXT CARD ------------------------------- #

def next_card(args):
    pass


# --------------------------- UI SETUP -------------------------------- #

# TODO: Creating Program window
# creating window object
window = Tk()

# add title to the program
window.title("Flashy Card")

# window size
window.config(padx=50, pady=50, bg=GRAY_WHITE)

# add custom favicon
window.iconbitmap(r'images/favicon.ico')

# TODO: Creating canvas

# creating a canvas
canvas = Canvas(width=800, height=526)

# front card image
front_card_image = PhotoImage(file="images/card_front.png")

# assigning the position for front card
canvas.create_image(400, 263, image=front_card_image)

# Canvas card title
canvas.create_text(400, 150, text="Title", font=(CARD_TITLE, 40, "italic"))

# canvas card word
canvas.create_text(400, 263, text="Word", font=(CARD_WORD, 60, "bold"))

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
cross_button = Button(image=check_icon, highlightthicknes=0, borderwidth=0)

# check button grid
cross_button.grid(row=1, column=1)

# run the window
window.mainloop()
