import fresh_tomatoes
import media

toy_story=media.Movie("Toy Story", 
                      "A story of a boy and his toys that come to loife", 
                      "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar=media.Movie("Avatar",
                   "A marine on an alien planet",
                   "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                   "https://www.youtube.com/watch?v=5PSNL1qE6VY")


school_of_rocks=media.Movie("School of Rocks",
                   "Using rock music to learn",
                   "https://en.wikipedia.org/wiki/School_of_Rock#/media/File:School_of_Rock_Poster.jpg",
                   "https://www.youtube.com/watch?v=3PsUJFEBC74")


bolt=media.Movie("Bolt",
                   "Dog thinking himself to be the superhero",
                   "https://en.wikipedia.org/wiki/Bolt_(2008_film)#/media/File:Bolt_ver2.jpg",
                   "https://www.youtube.com/watch?v=zm51H0dIzYQ")


social_network=media.Movie("Social Network",
                   "Mark Zukerberg story",
                   "https://en.wikipedia.org/wiki/The_Social_Network#/media/File:Social_network_film_poster.jpg",
                   "https://www.youtube.com/watch?v=lB95KLmpLR4")


the_fifth_estate=media.Movie("The Fifth estate",
                   "Story about the wikileaks",
                   "https://en.wikipedia.org/wiki/The_Fifth_Estate_(film)#/media/File:The_Fifth_Estate_poster.jpg",
                   "https://www.youtube.com/watch?v=ZT1wb8_tcYU")

movies=[toy_story, avatar, school_of_rocks, bolt, social_network, the_fifth_estate]
fresh_tomatoes.open_movies_page(movies)
