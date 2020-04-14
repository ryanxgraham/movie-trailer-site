"""Create instances of movies, put them in a list, and builds the site."""

import media
import fresh_tomatoes

"""Create instances of movies for site."""
brazil = media.Movie(
    "Brazil",
    "(1985)",
    "A man loses his job in a boring dystopia",
    "https://images-na.ssl-images-amazon.com/images/I/51AtZzOydpL._AC_.jpg",
    "https://www.youtube.com/watch?v=ZKPFC8DA9_8")
paprika = media.Movie(
    "Paprika",
    "(2006)",
    "A psychatrist goes on a wild trip",
    "https://images-na.ssl-images-amazon.com/images/I/51K-UVQgMML._AC_.jpg",
    "https://www.youtube.com/watch?v=jJzEW_eE1G0")
young_frankenstein = media.Movie(
    "Young Frankenstein",
    "(1974)",
    "A man visits his ancestral home",
    "https://images-na.ssl-images-amazon.com/images/I/5112h20rBwL._AC_.jpg",
    "https://www.youtube.com/watch?v=mOPTriLG5cU")
mandy = media.Movie(
    "Mandy",
    "(2018)",
    "Nicolas Cage goes nuts",
    "https://images-na.ssl-images-amazon.com/images/I/41EAM6XmsXL._AC_.jpg",
    "https://www.youtube.com/watch?v=hRKVxT4-1wM")
ace_ventura = media.Movie(
    "Ace Venture: When Nature Calls",
    "(1995)",
    "In search of Shikaka",
    "https://images-na.ssl-images-amazon.com/images/I/51d4Nz21hNL._AC_.jpg",
    "https://www.youtube.com/watch?v=cXcH0f2B2vA")
airplane = media.Movie(
    "Airplane!",
    "(1980)",
    "Don't eat the fish!",
    "https://images-na.ssl-images-amazon.com/images/I/51zWRLrTz3L._AC_.jpg",
    "https://www.youtube.com/watch?v=IJJQ2-VORo0")

"""Create a list of movies"""
movies = [brazil, paprika, young_frankenstein, mandy, ace_ventura, airplane]

"""Makes the site"""
fresh_tomatoes.open_movies_page(movies)
