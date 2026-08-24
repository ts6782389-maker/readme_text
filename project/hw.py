import requests
class Movies:
    def __init__(self , title ,  year , director , imdb_rating , watched = False):
        self.title = title
        self.year = year
        self.director = director
        self.imdb_rating = imdb_rating
        self.watched = watched

all_movies = []
try:
    file = open("watchlist.txt" , "r")
    data = file.readlines()
    file.close()

    for info in data:
        parts = info.split(",")
        title = parts[0]
        year = parts[1]
        director = parts[2]
        imdb_rating = parts[3]
        watched = parts[4].strip() == "True"
        new_movie = Movies(title , year , director , imdb_rating , watched)
        all_movies.append(new_movie)
except:
    print("there is error . Please stand by!!!")

while True:
    print("1 . search for a movie to add to watchlist")
    print("2.  view watchlist")
    print("3.  mark movie as watched")
    print("4.  view average rating of watchlist")
    print("5.  sort by rating")
    print("6.  Exit")

    choice = input("enter your choice : ")
    if choice == "1":
        api_key = "992f5089"
        movie_name = input("enter the movie name :")
        responses = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&t={movie_name}")
        data = responses.json()

        if data.get("Response") == "True":
            movie = Movies(data["Title"], data["Year"], data["Director"], data["imdbRating"], watched=False)
            all_movies.append(movie)

            with open("watchlist.txt", "w") as file:
                for info in all_movies:
                    file.write(",".join([info.title, info.year, info.director, info.imdb_rating, str(info.watched)]) + "\n")

            print("movie added to watchlist")
        else:
            print("the movie was not found and please write movie name")

    elif choice == "2":
        for info in all_movies:
            print(info.title)
            print(info.year)
            print(info.director)
            print(info.imdb_rating)
            print(info.watched)



                



       

    

    


       
        


                             
