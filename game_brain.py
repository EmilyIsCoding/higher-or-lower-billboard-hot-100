import random
songs_chosen = []


class GameBrain:

    def __init__(self, song_data):
        """
        Takes in a list to use for the Higher or Lower game.
        Randomly assigns song2 a song from the list.
        Has an initial Score of 0 for the game.
        """
        self.song_data = song_data
        self.song2 = random.choice(self.song_data)
        self.song1 = None
        self.answer = None
        self.score = 0

    def next_song(self):
        """
        Assigns song1 as the value of song2.
        Randomly assigns song 2.
            Makes sure song1 and song2 are different.
        Appends song2 to the list of songs_chosen so there are no repeats each time this function is called.
        """
        self.song1 = self.song2
        self.song2 = random.choice(self.song_data)
        while self.song1 == self.song2 or self.song2 in songs_chosen:
            self.song2 = random.choice(self.song_data)
        songs_chosen.append(self.song2)

    def check_answer(self, user_answer):
        """
        Compares user_answer for which song ranked higher in the data to the actual answer.
        If a song comes before another song in the list, it ranked higher.
        If the user is correct, their Score increases by 1.
        """
        if self.song_data.index(self.song1) < self.song_data.index(self.song2):
            self.answer = "A"
        else:
            self.answer = "B"

        if user_answer == self.answer:
            self.score += 1
            return True
        else:
            return False

