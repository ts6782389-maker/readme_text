all_students = []

while True:
    print("1. add student")
    print("2. view student")
    print("3. average of marks")
    print("4. topper of the class")
    print("5. delete student")
    
    choice = input("enter your choice :")

    if choice == "1":
        name = input('enter your name :')
        maths = int(input("enter your maths marks :"))
        science = int(input("enter your science marks :"))
        student = {"name": name,
                   "maths": maths,
                   "science": science}
        all_students.append(student)
    elif choice == "2":
        for info in all_students:
            print(info["name"])
            print(info["maths"])
            print(info["science"])
        
    elif choice == "3":
        student_name = input("enter the name of the student for avg : ")
        for info in all_students:
            if(info["name"] == student_name ):
                a = info["maths"]
                b = info["science"]
                sum = a+b
                average = sum/2
                print(average)
      
        print("radha radha")
    elif choice == "4":
        highest_avg = 0
        topper_name = ""
        for info in all_students:
            sum = info["maths"] + info["science"]
            average = sum/3
            if average > highest_avg:
                highest_avg = average
                topper_name = info["name"]

        print(topper_name , " is the topper with average" , highest_avg)

    elif(choice == "5"):
        student_info = input("enter the name of the student data to delete")
        new_students = []
        for info in all_students:
            if(info["name"] != student_info):
                new_students.append(info)
                all_students = new_students

    else:
        print("INVALID CHOICE")

        # The learning from this project is it's very exciting and also
        # the list in dictionary a very much new concept
        # the lsit in dictionary is like the list a big box and the 
        # small boxes are the seperate dictionary that are present their 
        # when i loop them it will only do one thing just took one small
        # boxe one at a time 





    

        


    


    










