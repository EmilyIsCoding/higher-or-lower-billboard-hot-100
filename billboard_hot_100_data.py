from bs4 import BeautifulSoup
import requests


class TimeMachine:

    def __init__(self, date):
        """
        Takes a date and returns an ordered list of the Hot 100 songs by their respective artist on that date.

        Parameters
        ----------
        date: in the format of YYYY-MM-DD

        Returns
        -------
        list: [(Song by Artist)]
        """
        self.date = date
        self.URL = f"https://www.billboard.com/charts/hot-100/" + date
        self.response = requests.get(self.URL)
        self.top_100_songs_page = self.response.text
        self.soup = BeautifulSoup(self.top_100_songs_page, "html.parser")

        self.scraped_songs = [song.get_text("|", strip=True) for song in self.soup.find_all(name="h3", class_="c-title", id="title-of-a-story")][5:]
        self.scraped_artists = [artist.get_text("|", strip=True) for artist in self.soup.find_all(name="span", class_="c-label")]

        self.song_list = [name for name in self.scraped_songs
                          if 'Songwriter(s):' not in name
                          if 'Producer(s):' not in name
                          if 'Imprint/Promotion Label:' not in name
                          if 'Additional Awards' not in name
                          ][:100]

        self.artist_list = [artist.split(" Featuring")[0].split(" Duet")[0] for artist in self.scraped_artists
                            if not artist.isnumeric()
                            if artist != "-"
                            if artist != "NEW"
                            if 'ENTRY' not in artist
                            ]

        self.top_100_songs = []
        assert len(self.song_list) == len(self.artist_list)
        for index in range(len(self.song_list)):
            self.top_100_songs.append(self.song_list[index] + " by " + self.artist_list[index])



# UI: Tkinter get() for date
# TimeMachine asks for date
# TimeMachine validates and loops if necessary
# If valid, time machine scrapes