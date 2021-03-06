import datetime
from billboard_hot_100_data import TimeMachine
from game_brain import GameBrain
from ui import GameInterface


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        return "ValueError"


date = input("Which year do you want to travel to? Type in this format: YYYY-MM-DD: ")
while validate(date) == "ValueError":
    date = input("Which year do you want to travel to? Type in this format: YYYY-MM-DD: ")
try:
    song_data = TimeMachine(date)
    print(song_data.top_100_songs)

    game = GameBrain(song_data.top_100_songs, date)
    game_ui = GameInterface(game)

except AssertionError:
    print("Can't travel to this date, please choose another.")