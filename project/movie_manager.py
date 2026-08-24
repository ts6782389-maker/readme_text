all_movies = []


import requests
api_key = "992f5089"

class Movie:
    def __init__(self,title , year , director , imdb_rating ,watched = False):
        self.title = title
        self.year = year
        self.director = director 
        self.imdb_rating = imdb_rating
        self.watched = watched

    def display(self):
        print(self.title)
        print(self.year)
        print(self.director)
        print(self.imdb_rating)
        print(self.watched)

file = open("watchlist.txt" , "r")
data = file.readlines()
file.close()

try:
    for line in data:
        
        parts = line.split(",")
        title = parts[0]
        year = parts[1]
        director = parts[2]
        imdb_rating = parts[3]
        watched = parts[4].strip() == "True"
        new_movie = Movie(title , year , director , imdb_rating , watched)
        all_movies.append(new_movie)
except:
    print("no data in the file")

while True:

    print("1. search for a movie to add to watchlist")
    print("2. view watchlist")
    print("3. mark  movie as watched")
    print("4. view average rating of watchlist")
    print("5. save/load watchlist to a file")
    print("6. sort by rating")
    print("7. exit")
    print("8. sort by title")
    print("9. sort by year")

    choice = input("enter yoour choice :")
    if choice == "1":
        movie_name = (input("enter movie name : "))
        respones = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&t={movie_name}")
        data = respones.json()
        if data["Response"] == "True":
            title = data["Title"]
            year = data["Year"]
            director = data["Director"]
            imdb_rating = data["imdbRating"]
            new_movie = Movie(title, year, director, imdb_rating)
            all_movies.append(new_movie)
            print("movie added to watchlist")

        file = open("watchlist.txt", "w")
        for info in all_movies:
            file.write(info.title + "," + info.year + "," + info.director + "," + info.imdb_rating + "," + str(info.watched) + "\n")
            file.close()

        else:
            print("movie not found")

    elif(choice == "2"):
        for info in all_movies:
            info.display()

    elif(choice == "3"):
        movie_title = input("Title of movie for mark as watched : ")
        for info in all_movies:
            if movie_title in info.title:
                info.watched = True
                print("movie mark as watched")

            file = open("watchlist.txt", "w")
        for movie in all_movies:
            file.write(movie.title + "," + movie.year + "," + movie.director + "," + movie.imdb_rating + "," + str(movie.watched) + "\n")
        file.close()     

    elif(choice == "4"):
        total_rating = 0
        for info in all_movies:
            total_rating += float(info.imdb_rating)
        average_rating = total_rating / len(all_movies)
        print("average rating of watchlist is : " , average_rating)

    elif(choice == "5"):
        file = open("watchlist.txt", "w")
        for info in all_movies:
            file.write(info.title + "," + info.year + "," + info.director + "," + info.imdb_rating + "," + str(info.watched) + "\n")
        file.close()
        print("watchlist saved to file")

    elif(choice == "6"):
        sorted_movies = sorted(all_movies , key=lambda m: float(m.imdb_rating) , reverse = True)
        for info in sorted_movies:
            print(info.title , info.imdb_rating)

    elif(choice == "7"):
        break

    elif(choice == "8"):
        sorted_movies1 = sorted(all_movies , key=lambda m: m.title , reverse =True)
        for info in sorted_movies1:
            print(info.title , info.imdb_rating)

    elif(choice == "9"):
        sorted_movies = sorted(all_movies , key=lambda m: m.year , reverse = True)
        for info in sorted_movies:
            print(info.title , info.year)

