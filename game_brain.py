import random
songs_chosen = []


class GameBrain:

    def __init__(self, song_data):
        self.song_data = song_data
        self.song2 = random.choice(self.song_data)
        self.song1 = None
        self.answer = None
        self.score = 0
        self.game_continue = True

        # #Might have to separate this chunk elsewhere
        # while self.game_continue:
        #     self.song1 = self.song2
        #     self.song2 = random.choice(self.song_data)
        #     while self.song1 == self.song2 or self.song2 in songs_chosen:
        #         self.song2 = random.choice(self.song_data)
        #
        #     songs_chosen.append(self.song2)
        #
        #     # This just closes the loop so I can keep testing
        #     self.game_continue = False

    def loop_check(self, continue_check):
        while continue_check:
            self.song1 = self.song2
            self.song2 = random.choice(self.song_data)
            while self.song1 == self.song2 or self.song2 in songs_chosen:
                self.song2 = random.choice(self.song_data)

            songs_chosen.append(self.song2)

            # This just closes the loop so I can keep testing
            # continue_check = False