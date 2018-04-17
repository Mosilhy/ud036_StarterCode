from media import *


movie1 = Movie(  # making an instance of Movie class
 "Toy story", "A story of toys geting alive",
 "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
 "https://www.youtube.com/watch?v=KYz2wyBy3kc")
movie2 = Movie(
 "Avatar", " humans have depleted Earth's natural resources,'\
 leading to a severe energy crisis",
 "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
 "https://www.youtube.com/watch?v=5PSNL1qE6VY")
movie3 = Movie(
 "Ratatouille", "Remy is an idealistic and ambitious young rat,'\
 gifted with highly developed senses of taste and smell.'\
 Inspired by his idol, the recently deceased chef Auguste Gusteau, '\
 Remy dreams of becoming a cook himself.",
 "https://upload.wikimedia.org/wikipedia/id/b/b9/RatatouillePoster2.jpg",
 "https://www.youtube.com/watch?v=c3sBBRxDAqk")

movie4 = Movie(
 "School of Rock", "No Vacancy, a rock band, performs at a'\
 nightclub three weeks before auditioning for the Battle of the Bands.'\
 Guitarist Dewey Finn creates on-stage antics,'\
 including a failed stage dive that abruptly ends the performance. ",
 "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
 "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
movie5 = Movie(
 "Midnight in Paris", "Gil Pender, a successful but creatively'\
 unfulfilled Hollywood screenwriter, and his fiancée Inez, '\
 are in Paris vacationing with Inez's wealthy, conservative parents.",
 "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
 "https://www.youtube.com/watch?v=FAfR8omt-CY")
movie6 = Movie(
 "The Hunger Games", "As punishment for a past rebellion,'\
 each of the 12 districts of Panem is forced by the Capitol to'\
 select two tributes, one boy and one girl between the ages of 12 and 18,'\
 to fight to the death in the annual Hunger'\
 Games until there is only one survivor. ",
 "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg",
 "https://www.youtube.com/watch?v=mfmrPu43DF8")
movies = [movie1, movie2, movie3, movie4, movie5, movie6]
fresh_tomatoes.open_movies_page(movies)  # send movies to be displayed
