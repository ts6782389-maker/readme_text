# again notes app

while True:
    print("1. add notes")
    print("2. view notes")
    print("3. search notes")
    print("4. delete note")
    print("5. exit")

    choice = input("enter your choice : ")

    if(choice == "1"):
        note = input("enter note to add : ")
        file = open("notes.txt" , "a")
        file.write(note + "\n")
        file.close()

    elif(choice == "2"):
        file = open("notes.txt" , "r")
        print(file.read())

    elif(choice == "3"):
        file = open("notes.txt" , "r")
        data = file.readlines()
        file.close()

        word = input("enter the word to search :")
        for info in data:
                if word in info:
                    print("found it")
      
    elif(choice == "4"):
        file = open("notes.txt" , "r")
        data = file.readlines()
        file.close()

        count = 1
        for info in data:
            print(count , info)
            count += 1

        num = int(input("enter the number to delete : "))
        new_info = []

        count = 1
        for info in data:
            if(count != num):
                new_info.append(info)
                count += 1

        file = open("notes.txt" , "w")
        for info in new_info:
            file.write(info)
        file.close()

    elif(choice == "5"):
        break

    else:
        print("invalid choice")

            


       



        

        
