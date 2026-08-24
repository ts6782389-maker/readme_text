"""my_movies = {"Inception", "Interstellar", "Avengers", "Tenet"}
friend_movies = {"Avengers", "Tenet", "Joker"}

common = my_movies&friend_movies
print(common)

unioun = my_movies | friend_movies
print(unioun)

difference = my_movies - friend_movies
print(difference)"""

#generators
# for a big value like square of first 1 million numbers
#normally you will do.
squares = [x**2 for x in range(1000000)]

#this takes up every huge amount of memory and it can only be fixed by using genertaors cause it waste memory
# A generator is like a vending machine — it only makes/gives you the next item exactly when you ask for it (press the button), not before.

"""def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1"""

#The key difference: return gives back a value and the function ends completely. yield gives back a value but pauses the function — it remembers exactly where it left off, ready to continue from that exact spot the next time you ask for another value.
"""gen = count_up_to(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))"""

"""for number in count_up_to(5):
    print(number)"""

# even number generator shazaam! diy

"""def even_numbers(n):
    count = 2
    while count <= n :
        yield count
        count += 2

for num in even_numbers(2):
    print(num)"""


#fibonacci generators diy this generator bascially yields the first n fibonacci numbers.
"""def fibonacci_gen(n):
    a = 0 
    b = 1
    count = 0
    while count < n:
        yield a 
        a, b=b , a+b
        count += 1

# a new concept a and b"""

"""concept = "Let's trace through with real numbers. Say right now a = 1 and b = 1 (before this line runs).
         "Step 1: Python looks at the right side — b, a + b"
        It grabs the current/old value of b, which is 1
It calculates a + b using the current/old values: 1 + 1 = 2
So the right side becomes: 1, 2 (a pair of two values, calculated using the OLD a and b)
Step 2: Python assigns these to the left side, in order
a gets the first value → a = 1
b gets the second value → b = 2
So after this one line runs: a = 1 (was b's old value), b = 2 (was a + b using old values)."""

"""The rule: in ANY assignment statement, Python always fully evaluates everything on the right side of the = FIRST, and only afterward assigns the result(s) to the variable(s) on the left"""

#projects on tuples and generators concepts.. the text analyser on different page..

#ards and **kwargs
#args bascially fix the problm that if a fuction is defined for two arguments
#but if a function use arg function it can take as amny as arguments the user input
"""def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_all(1, 2, 3))        # 6
print(add_all(5, 10, 15, 20))  # 50"""

note = """*args collects whatever arguments get passed in and bundles them into a tuple automatically — that's why you can loop through args just like any list/tuple.
Try this yourself — type it, test with different numbers of arguments, and confirm it works with 2, 3, or 5 numbers passed in."""

#args bscially bundle ups the arguments into tuple thats why we can loop it 

example = """def all_sum(*args):
    total = 0
    for num in args:
        total += num
        print(total)

all_sum(2,3,5)"""

#kwargs** dont forget the two stars 
#bscially kwargs collects all the arguments in a key and value format ex name=anant or name : anant this makes all the bundles up int the dictionary format and it 
#can loop through just like dict. so args = tuple , kwargs = dictionary

example = """def print_info(**kwargs):
    for key in kwargs:
        print(key , ":" , kwargs[key])

print_info(name="sanu", age=14 , city="roorkee")"""

example = """def describe(name , *args , **kwargs):
    print("name:" , name)
    print("extra info:" , args)
    print("details:" , kwargs)

describe("Anant" , "roorkee" , "India", age=19 , hooby="coding")"""

#oop heritance is a very intersetung topic which take one calss attributes and fuction and whenwe worte it into another it takes up all the property of the previous class sucessfully.
#so be ready for this shit

example = """class Movies():
    def __init__(self,title , year):
        self.year = year
        self.title = title 

    def display(self):
        print(self.title , "-" , self.year)

class Series(Movies):
    def __init__(self,title , year , seasons):
        super().__init__(title,year)
        self.seasons = seasons

    def display(self):
        super().display()
        print("Seasons : ", self.seasons)

s1 = Series("breaking bad" , 2012 , 5)
s1.display()

m1 = Movies("obsession" , 2026)
m1.display()"""

#super it gives you acess to parent class it just used to acess the properites from the parnt class without writing name 
#example super().init(title , year)

class Vechile():
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

    def display(self):
        print(self.brand , "-" ,self.speed)

class Car(Vechile):
    def __init__(self,brand ,speed , doors):
        super().__init__(brand,speed)
        self.doors = doors

    def display(self):
        super().display()
        print(self.doors)

v = Vechile("generic" , 100)
v.display()

c = Car("tesla" , 250 , 4)
c.display()

    




    

