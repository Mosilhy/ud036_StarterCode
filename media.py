import fresh_tomatoes
import webbrowser


class Movie:
    """Movie Class That contain movie title , main story ,
   link to the picture and a link to the trailer """
    def __init__(self, titlee, storyy, poster, trailer):
        self.title = titlee
        self.story = storyy
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
