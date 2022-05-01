import random


class GameBrain:

    def __init__(self, song_data):
        self.song_data = song_data
        self.song2 = random.choice(self.song_data)
        self.game_continue = True
        while self.game_continue:
            self.song1 = self.song2
            self.song2 = random.choice(self.song_data)

            while self.song1 == self.song2:
                self.song2 = random.choice(self.song_data)

            # This just closes the loop so I can keep testing
            self.game_continue = False
