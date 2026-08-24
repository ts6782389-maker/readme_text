dict = {
    "name" : "anant panwar",
    "age"  : 18,
    "city" : "greater noida"
}

print(dict["name"])

info = [("apple" ,3) , ("banana",5)]

def search(fruits):
    for value in info:
        if fruits == value[0]:
            print("found_it")
            print("the quantity of",fruits,value[1])

search("banana")

#That "magic formula" that converts something (like a book title, or in our case, a key like "banana") into a number telling you exactly where to look, is roughly what a hash function does. It takes a key and converts it into a number very quickly, using math, and that number tells the dict exactly which "slot" to go check, instead of scanning everything.

print(hash("banana"))