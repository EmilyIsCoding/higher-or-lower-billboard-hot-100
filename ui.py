from tkinter import *
from game_brain import GameBrain

THEME_COLOR = "Black"

class GameInterface:

    def __init__(self):
        """
        User interface for the game. Parameter: GameBrain class.
        """
        # self.game = game_brain
        self.window = Tk()
        self.window.title("Higher or Lower: The Billboard Hot 100 Edition")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=400, height=250, bg=THEME_COLOR, highlightthickness=0, bd=0)
        billboard_image = PhotoImage(file="./images/billboard_hot_100_template.png")
        self.canvas.create_image(200, 145, image=billboard_image)
        self.canvas.grid(column=0, row=0, columnspan=3, pady=50)

        self.song1_label = Label(
            text="Placeholder1",
            font=("Arial", 20, "italic"),
            fg="white",
            bg="black"
        )
        self.song1_label.grid(column=0, row=0)

        self.versus_label = Label(
            text="Vs.",
            font=("Arial", 15, "bold"),
            fg="white",
            bg="black"
        )
        self.versus_label.grid(column=1, row=0)

        self.song2_label = Label(
            text="Placeholder2",
            font=("Arial", 20, "italic"),
            fg="white",
            bg="black"
        )
        self.song2_label.grid(column=2, row=0)

        self.window.mainloop()


test = GameInterface()
