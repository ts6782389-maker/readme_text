# expenses tracker 
while True:
    print("1 . add expenses")
    print("2   view expenses")
    print("3.  total")
    print("4.  total by category")
    print("5.  delete")
    print("6.  exit")

    choice = input("enter your choice :")

    if(choice == "1"):
        amount = input("enter the expenses value : ")
        category = input("enter the category : ")
        info = amount + "," + category + "\n"
        file = open("expenses.txt" , "a")
        data = file.write(info)
        print(data)
        file.close()

    elif(choice == "2"):
        file = open("expenses.txt" , "r")
        data = file.readlines()
        file.close()
        for line in data:
            result = line.split(",")
            print("amount :" , result[0] , "category :" , result[1])

    elif(choice == "3"):
        file = open("expenses.txt" , "r")
        data = file.readlines()
        file.close()
        total = 0
        for line in data:
            result = line.split(",")
            total += int(result[0])
            print("total :" , total)

    elif( choice == "4"):
        file = open("expenses.txt" , "r")
        data = file.readlines()
        file.close()
        total_categaory = 0

        word = input("enter the expense for total : ")
        for line in data:
            result = line.split(",")
            if word in result[1]:
                total_categaory += int(result[0])
                print("total expenses of the category" , total_categaory)

    elif(choice == "5"):
        file = open("expenses.txt" , "r")
        data = file.readlines()
        file.close()

        count = 1
        for line in data:
            print(count , line)
            count += 1

        num = int(input("enter your number line to delete : "))
        new_expenses = []
        count = 1

        for line in data:
            if(count != num):
                new_expenses.append(line)

        file = open("expenses.txt" , "w")
        for line in new_expenses:
            file.write(line)

    else:
        break
            

        



