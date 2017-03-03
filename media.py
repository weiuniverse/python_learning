import webbrowser


class Movie:

    """this class define a Movie"""
    VALID_RATING = ["G","R"]
    def __init__(self,movie_title,movie_storyline,movie_post_image,movie_trailer_youtube):
        self.title=movie_title
        self.__storyline=movie_storyline
        self.post_image=movie_post_image
        self.__trailer_youtube=movie_trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.__trailer_youtube)

    def show_storyline(self):
        print(self.__storyline)

GAN=Movie("gan","IanGoodfellow's talk about GAN","https://www.youtube.com/watch?v=NKiwFF_zBu4","https://www.youtube.com/watch?v=NKiwFF_zBu4")
GAN.show_storyline()
#GAN.show_trailer()
print(GAN.__doc__,GAN.__module__)

