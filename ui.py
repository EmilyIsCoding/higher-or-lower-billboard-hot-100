import tkinter.messagebox
from tkinter import *
from game_brain import GameBrain
import billboard_hot_100_data

THEME_COLOR = "Black"

class GameInterface:

    def __init__(self, game_brain: GameBrain):
        """
        User interface for the game, displays the first two songs. Parameter: GameBrain class.
        """
        self.game = game_brain
        self.window = Tk()
        self.window.title("Higher or Lower: The Billboard Hot 100 Edition")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=2, row=0)

        self.canvas = Canvas(width=600, height=170, bg=THEME_COLOR, highlightthickness=0, bd=0)
        billboard_image = PhotoImage(file="./images/billboard_hot_100_template.png")
        self.canvas.create_image(300, 100, image=billboard_image)
        self.canvas.grid(column=0, row=1, columnspan=3)

        # Song1 Labels #
        self.song1_label = Label(
            text="Placeholder1",
            font=("Arial", 20, "italic"),
            fg="white",
            bg="black",
            wraplength=200,
            justify="left"
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
            font=("Arial", 20, "bold"),
            fg="white",
            bg="black",
            height=1
        )
        self.versus_label.grid(column=1, row=2, columnspan=1)

        # Song2 Labels #
        self.song2_label = Label(
            text="Placeholder2",
            font=("Arial", 20, "italic"),
            fg="white",
            bg="black",
            wraplength=200,
            justify="right"
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
            text="???",
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
            bd=0,
            command=self.higher_pressed
        )
        self.higher.grid(column=2, row=5)

        lower_image = PhotoImage(file="./images/lower_button.png")
        self.lower = Button(
            image=lower_image,
            highlightthickness=0,
            bd=0,
            command=self.lower_pressed
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

        self.next_song()

        self.window.mainloop()

    def next_song(self):
        self.window.config(bg=THEME_COLOR)
        self.versus_label.config(text="Vs.", bg=THEME_COLOR)
        self.song2_rank.config(text="???")
        self.score.config(text=f"Score: {self.game.score}")
        if self.game.still_has_songs():
            self.game.next_song()
            self.song1_label.config(text=self.game.song1)
            self.song1_rank.config(text=self.game.reveal_rank()[0])
            self.song2_label.config(text=self.game.song2)
        else:
            tkinter.messagebox.showinfo("Congratulations!", "You got all the songs right!")
            self.higher.config(state="disabled")
            self.lower.config(state="disabled")

    def higher_pressed(self):
        self.give_feedback(self.game.check_answer("B"))

    def lower_pressed(self):
        self.give_feedback(self.game.check_answer("A"))

    def give_feedback(self, is_right):
        self.song2_rank.config(text=f"{self.game.reveal_rank()[1]}")
        if is_right:
            self.versus_label.after(500, self.versus_label.config(text="✓", bg="green"))
        else:
            self.versus_label.after(500, self.versus_label.config(text="X", bg="red"))
        self.canvas.update()
        self.window.after(500, self.next_song())

# TODO: Find a way to make the buttons disappear and reveal a rank later? Can just modify by writing in the label.
# TODO: When pressing a button, give feedback colors
# TODO: When pressing a button, reveal the RAnk first
    # TODO: Change the Versus to a Check or Minus! In Green or Red!
# TODO: When getting the answer wrong, end the game and display a pop-up with the final score.