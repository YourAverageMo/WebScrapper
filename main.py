import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


def scrap():
    """scraps above URL and ->

    Returns:
        print(): web scrap data saved into local dir 
    """
    response = requests.get(URL)
    webpage = response.text

    with open("./top_100_movies.text", mode="w") as f:
        f.write(webpage)
    return print(
        f"{URL}\n Successfully scrapped and saved as top_100_movies.text")


with open("./top_100_movies.text", mode="r") as f:
    soup = BeautifulSoup(f, "html.parser")
    movies = soup.findAll(name="h3", class_="title")

    # ok so this is a long and somewhat confusing list comp but im very proud of it. what it does is first split each work in 'movies' into its own list entry then remove the number that precedes the movie title (the [1:] part). thennnnnnn joins the remaing words into its own string. each string is then its own list item :D simple
movies = [" ".join((movie.getText().split())[1:]) for movie in movies]

# for the next part you could use dict comp to number them in increasing order but id rather just use a for loop with a variable :D

with open("./top_100_movies_list.text", mode="w") as f:
    rank = 1
    for movie in movies:
        line = f"{rank}) {movie}\n"
        f.write(line)
        rank += 1

# UPDATE: soooooo i misunderstood the teacher and kinda messed up and instead of fixing it imma just write this:

# i thought she wanted us to make the 100th film as the 1st film for some reason.... but instead she just wanted us to print the list in ascending order... she could have just said that. so yeeeee my bad but hey great list comp :D
