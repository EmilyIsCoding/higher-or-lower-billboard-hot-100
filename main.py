from billboard_hot_100_data import TimeMachine

date = input("Which year do you want to travel to? Type in this format: YYYY-MM-DD: ")

data = TimeMachine(date)
print(data.top_100_songs)