#quiz game code starts 
total_score = 0

import requests 
import random

while True:
    print("1. start the quiz")
    print("2. total_score")
    print("3. exit")
    print("4. View leaderboard")

    choice = input("enter your choice :")

    if(choice == "1"):
        responses = requests.get("https://opentdb.com/api.php?amount=5")
        data = responses.json()

        name_player = input("enter the player name : ")

        for question in data["results"]:
            print(question["question"])
            a = question["correct_answer"]
            b = question["incorrect_answers"]
            options = b +[a]
            random.shuffle(options)


            count = 1
            for test in options:
                print(count , "." + test)
                count += 1

            try:


                choice_num = int(input("enter your answer : "))
                selected_answer = options[choice_num - 1]

            except:
                print("an unexpected error has occured")

            if selected_answer == a:
                print("corrext answer u got +1 marks")
                total_score += 1 

            else:
                print("incorrect answer")

        file = open("leaderboard.txt" , "a")
        data = file.write(name_player + "," + str(total_score) + "\n")
        file.close()  

    elif(choice == "2"):
        print("the total_score of player 1 is :",total_score)

    elif(choice == "3"):
        break

    elif(choice == "4"):
        file = open("leaderboard.txt" , "r")
        data = file.readlines()
        file.close()
        all_players = []

        for line in data:
            parts = line.split(",")
            name = parts[0]
            score = int(parts[1])
            all_players.append([name , score])

        sorted_players = sorted(all_players , key=lambda entry : entry[1] , reverse = True)
        rank = 1
        for info in sorted_players:
            print(rank ,"name : " ,  info[0]  + "," + "score :" , info[1] )
            rank +=1 

    else:
        print("INVALID CHOICE")
