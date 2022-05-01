import datetime
from billboard_hot_100_data import TimeMachine


def validate(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return False


date = input("Which year do you want to travel to? Type in this format: YYYY-MM-DD: ")
while validate(date) == False:
    date = input("Which year do you want to travel to? Type in this format: YYYY-MM-DD: ")
song_data = TimeMachine(date)
print(song_data.top_100_songs)