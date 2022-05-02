from tkinter import *
from game_brain import GameBrain

THEME_COLOR = "Black"

class GameInterface:

    def __init__(self, game_brain: GameBrain):
        """
        User interface for the game. Parameter: GameBrain class.
        """
        self.game = game_brain
        self.window = Tk()
        self.window.title("Higher or Lower: The Billboard Hot 100 Edition")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=2, row=0)

        self.canvas = Canvas(width=400, height=170, bg=THEME_COLOR, highlightthickness=0, bd=0)
        billboard_image = PhotoImage(file="./images/billboard_hot_100_template.png")
        self.canvas.create_image(200, 100, image=billboard_image)
        self.canvas.grid(column=0, row=1, columnspan=3)

        # Song1 Labels #
        self.song1_label = Label(
            text="Placeholder1",
            font=("Arial", 20, "italic"),
            fg="white",
            bg="black"
        )
        self.song1_label.grid(column=0, row=2)

        self.song1_text = Label(
            text="ranked",
            font=("Arial", 15),
            fg="white",
            bg="black"
        )
        self.song1_text.grid(column=0, row=3)

        self.song1_rank = Label(
            text="#{Rank}",
            font=("Arial", 20),
            fg="white",
            bg="black"
        )
        self.song1_rank.grid(column=0, row=4)


        # Versus Label #
        self.versus_label = Label(
            text="Vs.",
            font=("Arial", 15, "bold"),
            fg="white",
            bg="black",
            height=1
        )
        self.versus_label.grid(column=1, row=2)

        # Song2 Labels #
        self.song2_label = Label(
            text="Placeholder2",
            font=("Arial", 20, "italic"),
            fg="white",
            bg="black",
        )
        self.song2_label.grid(column=2, row=2)

        self.song2_text = Label(
            text="ranked",
            font=("Arial", 15),
            fg="white",
            bg="black"
        )
        self.song2_text.grid(column=2, row=3)

        self.song2_rank = Label(
            text="#{Hidden-Rank}",
            font=("Arial", 20),
            fg="white",
            bg="black"
        )
        self.song2_rank.grid(column=2, row=4)

        # Higher or Lower Buttons #
        higher_image = PhotoImage(file="./images/higher_button.png")
        self.higher = Button(
            image=higher_image,
            highlightthickness=0,
            bd=0
        )
        self.higher.grid(column=2, row=5)

        lower_image = PhotoImage(file="./images/lower_button.png")
        self.lower = Button(
            image=lower_image,
            highlightthickness=0,
            bd=0
        )
        self.lower.grid(column=2, row=6)

        # Pocket Watch #
        self.time_machine_date = Label(
            text="{yyyy-mm-dd}",
            font=("Arial", 15),
            fg="white",
            bg="black"
        )
        self.time_machine_date.grid(column=0, row=5)

        pocket_watch_image = PhotoImage(file="./images/pocket_watch.png")
        self.pocket_watch = Label(
            image=pocket_watch_image,
            font=("Arial", 15),
            fg="white",
            bg="black"
        )
        self.pocket_watch.grid(column=0, row=6)

        # Area to get next song #
        self.next_song()

        self.window.mainloop()

    def next_song(self):
        self.canvas.config(bg="black")
        self.score.config(text=f"Score: {self.game.score}")
        if self.game.still_has_songs():
            self.game.next_song()
            self.song1_label.config(text=self.game.song1)
            self.song1_rank.config(text=self.game.reveal_rank()[0])
            self.song2_label.config(text=self.game.song2)

# TODO: Find a way to make the buttons disappear and reveal a rank later? Can just modify by writing in the label.
# TODO: Map functions to buttons (have them modify the labels)
# TODO: Find a placeholder image for the bottom left, maybe where you time travelled to?
# TODO: How to make text wrap/go into the next line...