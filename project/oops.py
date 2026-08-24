class students():
    def __init__(self , name , maths , science):
        self.name = name
        self.maths = maths
        self.science = science

    def average(self):
        return (self.maths + self.science)/2

all_students = []
try:
    file = open("students.txt", "r")
    data = file.readlines()
    file.close()

    for line in data:
        try:
            parts = line.split(",")
            name = parts[0]        
            maths = int(parts[1])
            science = int(parts[2])
        except:
            print("skipping the data")
            continue

        s = students(name, maths, science)
        all_students.append(s)

except:
    print("no saved data")

while True:                              # indent 0 — menu starts here, AFTER loading
    print("1. Add student")
    print("2. View students")
    print("3. Average of a student")
    print("4. Topper")
    print("5. Delete student")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        try:
            maths = int(input("Enter maths: "))
            science = int(input("Enter science: "))
        except:
            print("please enter in the format of integer not string")
            continue
        
        s = students(name, maths, science)
        all_students.append(s)

        file = open("students.txt", "w")
        for info in all_students:
            file.write(info.name + "," + str(info.maths) + "," + str(info.science) + "\n")
        file.close()

    elif choice == "2":
        for info in all_students:
            print(info.name, info.maths, info.science)

    elif choice == "3":
        student_name = input("Enter name for average: ")
        for info in all_students:
            if info.name == student_name:
                print(info.average())

    elif choice == "4":
        highest_avg = 0
        topper_name = ""
        for info in all_students:
            if info.average() > highest_avg:
                highest_avg = info.average()
                topper_name = info.name
        print("Topper:", topper_name)

    elif choice == "5":
        del_name = input("Enter name to delete: ")
        new_students = []
        for info in all_students:
            if info.name != del_name:
                new_students.append(info)
        all_students = new_students

        file = open("students.txt", "w")
        for info in all_students:
            file.write(info.name + "," + str(info.maths) + "," + str(info.science) + "\n")
        file.close()

    elif choice == "6":
        break

    else:
        print("Invalid choice")

        #explained the concept of error handling!!



